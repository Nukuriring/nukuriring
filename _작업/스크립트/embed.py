# 사용법: py -3 -P _작업/스크립트/embed.py . [--model BAAI/bge-m3] [--batch 16] [--max-len 1024] [--device auto|cuda|cpu] [--force]
# (-P: 이 폴더의 struct.py가 표준 모듈 struct를 가리지 않게 한다)
# 영구 노트를 임베딩해 `_작업/검색/임베딩/<모델 이름>/`에 쓴다. PC의 GPU에서 돌리는 스크립트이다.
#  - title.npy: 제목(명제 한 문장) 벡터. 중복 탐지(dupes.py)에 쓴다.
#  - body.npy: 제목 + 본문(연결·출처 절 제외) 벡터. 연결 후보와 검색(search.py)에 쓴다.
#  - ids.json: 행 순서대로 [{"id", "file", "hash"}]. hash는 제목+본문의 sha1 앞 12자.
#  - meta.json: 모델 이름, 차원, 만든 날짜, 장치.
# 벡터는 L2 정규화한 float16으로 저장한다(내적 = 코사인). 저장소에 함께 올려 클라우드 세션도 쓰게 한다.
# 다시 실행하면 hash가 같은 카드는 기존 벡터를 그대로 쓰고, 바뀐 카드와 새 카드만 계산한다(--force는 전부 다시).
#
# 준비(PC, 한 번만):
#   py -3 -m pip install torch --index-url https://download.pytorch.org/whl/cu124
#   py -3 -m pip install sentence-transformers numpy
#   py -3 -c "import torch; print(torch.cuda.is_available())"   ← True가 나와야 GPU를 씁니다
# GPU 메모리가 4GB보다 작으면(BGE-M3는 반정밀도로도 약 1.1GB) --device auto가 CPU를 고른다. CPU는 수십 분 걸린다.
# 대조 모델: --model nlpai-lab/KURE-v1 (embed_compare.py로 두 모델의 이웃을 비교)
import argparse, datetime, glob, hashlib, json, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('--model', default='BAAI/bge-m3')
ap.add_argument('--batch', type=int, default=16)
ap.add_argument('--max-len', type=int, default=1024)
ap.add_argument('--device', default='auto', choices=['auto', 'cuda', 'cpu'])
ap.add_argument('--force', action='store_true')
a = ap.parse_args()
V = a.vault

import numpy as np


def read_cards(vault):
    out = []
    for f in sorted(glob.glob(os.path.join(vault, '영구', '*.md'))):
        x = open(f, encoding='utf-8').read().replace('\r\n', '\n')
        if not x.startswith('---'):
            continue
        body = x.split('---', 2)[2]
        m = re.search(r'^# (\S+) (.+)$', body, re.M)
        if not m:
            continue
        main = body[m.end():].split('\n## ')[0].strip()
        out.append(dict(id=m.group(1), file=os.path.basename(f)[:-3], title=m.group(2).strip(), main=main))
    return out


cards = read_cards(V)
slug = a.model.replace('/', '__')
D = os.path.join(V, '_작업', '검색', '임베딩', slug)
os.makedirs(D, exist_ok=True)
for c in cards:
    c['hash'] = hashlib.sha1((c['title'] + '\n' + c['main']).encode('utf-8')).hexdigest()[:12]

# 기존 벡터 재사용
old = {}
if not a.force and os.path.exists(os.path.join(D, 'ids.json')):
    try:
        oids = json.load(open(os.path.join(D, 'ids.json'), encoding='utf-8'))
        ot, ob = np.load(os.path.join(D, 'title.npy')), np.load(os.path.join(D, 'body.npy'))
        old = {r['id']: (r['hash'], ot[n], ob[n]) for n, r in enumerate(oids)}
    except (OSError, ValueError, KeyError) as e:
        print('기존 임베딩을 읽지 못해 전부 다시 계산합니다:', e)
todo = [c for c in cards if c['id'] not in old or old[c['id']][0] != c['hash']]
print(f'카드 {len(cards)}장, 다시 계산할 카드 {len(todo)}장 → {os.path.relpath(D, V)}')

dim = None
if todo:
    import torch
    from sentence_transformers import SentenceTransformer
    dev = a.device
    if dev == 'auto':
        dev = 'cpu'
        if torch.cuda.is_available():
            mem = torch.cuda.get_device_properties(0).total_memory / 2**30
            if mem >= 4:
                dev = 'cuda'
            else:
                print(f'알림: GPU 메모리가 {mem:.1f}GB라 모델이 올라가지 않으므로 CPU로 계산합니다.', file=sys.stderr)
    if dev == 'cpu':
        print(f'CPU로 계산합니다(카드 {len(todo)}장, 수십 분 걸릴 수 있음). 중간에 멈춰도 다시 실행하면 처음부터 계산합니다.', file=sys.stderr)
        torch.set_num_threads(max(1, os.cpu_count() or 1))
    m = SentenceTransformer(a.model, device=dev)
    m.max_seq_length = a.max_len
    kw = dict(batch_size=a.batch, normalize_embeddings=True, show_progress_bar=True, convert_to_numpy=True)
    if dev == 'cuda':
        m.half()
    tv = m.encode([c['title'] for c in todo], **kw)
    bv = m.encode([c['title'] + '\n' + c['main'] for c in todo], **kw)
    new = {c['id']: (tv[n], bv[n]) for n, c in enumerate(todo)}
    dim = tv.shape[1]
else:
    new, dev = {}, 'none'

T, B = [], []
for c in cards:
    t, b = new[c['id']] if c['id'] in new else old[c['id']][1:]
    T.append(t); B.append(b)
T = np.asarray(T, dtype=np.float16); B = np.asarray(B, dtype=np.float16)
np.save(os.path.join(D, 'title.npy'), T)
np.save(os.path.join(D, 'body.npy'), B)
json.dump([dict(id=c['id'], file=c['file'], hash=c['hash']) for c in cards],
          open(os.path.join(D, 'ids.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
json.dump(dict(model=a.model, dim=int(T.shape[1]), cards=len(cards), recomputed=len(todo), device=dev,
               date=datetime.date.today().isoformat()),
          open(os.path.join(D, 'meta.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(f'저장: title.npy·body.npy {T.shape}, 다시 계산 {len(todo)}장')
