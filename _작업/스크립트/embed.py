# 사용법: py -3 -P _작업/스크립트/embed.py . [--model BAAI/bge-m3] [--batch 16] [--max-len 1024] [--device auto|cuda|cpu] [--int8] [--chunk 200] [--force]
# (-P: 이 폴더의 struct.py가 표준 모듈 struct를 가리지 않게 한다)
# 영구 노트를 임베딩해 `_작업/검색/임베딩/<모델 이름>/`에 쓴다. PC의 GPU에서 돌리는 스크립트이다.
#  - title.npy: 제목(명제 한 문장) 벡터. 중복 탐지(dupes.py)에 쓴다.
#  - body.npy: 제목 + 본문(연결·출처 절 제외) 벡터. 연결 후보와 검색(search.py)에 쓴다.
#  - ids.json: 행 순서대로 [{"id", "file", "hash"}]. hash는 제목+본문의 sha1 앞 12자.
#  - meta.json: 모델 이름, 차원, 만든 날짜, 장치.
# 벡터는 L2 정규화한 float16으로 저장한다(내적 = 코사인). 저장소에 함께 올려 클라우드 세션도 쓰게 한다.
# 다시 실행하면 hash가 같은 카드는 기존 벡터를 그대로 쓰고, 바뀐 카드와 새 카드만 계산한다(--force는 전부 다시).
# --chunk장마다 중간 저장하므로, 멈춘 뒤 다시 실행하면 이어서 계산한다. meta.json의 complete가 true여야 완성이다.
# --int8: CPU에서 선형층을 int8로 양자화해 2배 안팎 빠르게 한다(유사도 값이 조금 달라짐).
#
# 준비(PC, 한 번만):
#   py -3 -m pip install torch --index-url https://download.pytorch.org/whl/cu124
#   py -3 -m pip install sentence-transformers numpy
#   py -3 -c "import torch; print(torch.cuda.is_available())"   ← True가 나와야 GPU를 씁니다
# GPU 메모리가 4GB보다 작으면(BGE-M3는 반정밀도로도 약 1.1GB) --device auto가 CPU를 고른다. CPU는 수십 분 걸린다.
# 대조 모델: --model nlpai-lab/KURE-v1 (embed_compare.py로 두 모델의 이웃을 비교)
import argparse, datetime, glob, hashlib, json, os, re, sys, time

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('--model', default='BAAI/bge-m3')
ap.add_argument('--batch', type=int, default=16)
ap.add_argument('--max-len', type=int, default=1024)
ap.add_argument('--device', default='auto', choices=['auto', 'cuda', 'cpu'])
ap.add_argument('--chunk', type=int, default=200)
ap.add_argument('--int8', action='store_true')
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

new, dev = {}, 'none'


def save(final=False):
    done = [c for c in cards if c['id'] in new or (c['id'] in old and old[c['id']][0] == c['hash'])]
    if not done:
        return 0
    T = np.asarray([new[c['id']][0] if c['id'] in new else old[c['id']][1] for c in done], dtype=np.float16)
    B = np.asarray([new[c['id']][1] if c['id'] in new else old[c['id']][2] for c in done], dtype=np.float16)
    np.save(os.path.join(D, 'title.npy'), T)
    np.save(os.path.join(D, 'body.npy'), B)
    json.dump([dict(id=c['id'], file=c['file'], hash=c['hash']) for c in done],
              open(os.path.join(D, 'ids.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
    json.dump(dict(model=a.model, dim=int(T.shape[1]), cards=len(done), total=len(cards), complete=len(done) == len(cards),
                   recomputed=len(new), device=dev, int8=a.int8, date=datetime.date.today().isoformat()),
              open(os.path.join(D, 'meta.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    return len(done)


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
        print(f'CPU로 계산합니다. {a.chunk}장마다 저장하므로 멈춰도 다시 실행하면 이어서 계산합니다.', file=sys.stderr)
        torch.set_num_threads(max(1, os.cpu_count() or 1))
    m = SentenceTransformer(a.model, device=dev)
    m.max_seq_length = a.max_len
    if dev == 'cuda':
        m.half()
    elif a.int8:
        # CPU 동적 양자화: 선형층을 int8로 바꿔 2배 안팎 빨라진다. 유사도 값은 조금 달라진다.
        m[0].auto_model = torch.quantization.quantize_dynamic(m[0].auto_model, {torch.nn.Linear}, dtype=torch.qint8)
    kw = dict(batch_size=a.batch, normalize_embeddings=True, show_progress_bar=False, convert_to_numpy=True)
    t0 = time.time()
    for k in range(0, len(todo), a.chunk):
        part = todo[k:k + a.chunk]
        tv = m.encode([c['title'] for c in part], **kw)
        bv = m.encode([c['title'] + '\n' + c['main'] for c in part], **kw)
        for n, c in enumerate(part):
            new[c['id']] = (tv[n], bv[n])
        n_done = save()
        el = time.time() - t0
        left = el / len(new) * (len(todo) - len(new))
        print(f'{len(new)}/{len(todo)}장 계산, 저장된 카드 {n_done}/{len(cards)}장, '
              f'경과 {el / 60:.0f}분, 남은 시간 약 {left / 60:.0f}분', flush=True)
n_done = save()
print(f'저장 완료: 카드 {n_done}/{len(cards)}장, 이번에 계산 {len(new)}장' + ('' if n_done == len(cards) else ' (미완성, 다시 실행하면 이어서 계산)'))
