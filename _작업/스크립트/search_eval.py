# 사용법: py -3.12 -P _작업/스크립트/search_eval.py . [--model BAAI/bge-m3] [--k 10]
# 검색 품질 시험(작업 계획 4단계). `_작업/검색/시험 질의.txt`의 질의마다 BM25만 쓴 결과와
# BM25+벡터(RRF) 결과를 상위 k장씩 나란히 `_작업/검색/검색 시험 결과.md`에 쓴다.
# 질의 벡터를 만들려면 임베딩 모델이 있어야 하므로 PC에서 돌린다. 모델은 한 번만 불러온다.
# 채점은 클라우드 세션이 결과 파일을 읽어 한다.
import argparse, collections, glob, json, math, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('--model', default='BAAI/bge-m3')
ap.add_argument('--k', type=int, default=10)
a = ap.parse_args()
V = a.vault
import numpy as np
from kiwipiepy import Kiwi

cards = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read().replace('\r\n', '\n')
    if not x.startswith('---'):
        continue
    fm, body = x.split('---', 2)[1:]
    m = re.search(r'^# (\S+) (.+)$', body, re.M)
    if not m:
        continue
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', fm, re.M) or [None, ''])[1].strip()
    main = body[m.end():].split('\n## ')[0].strip()
    cards[m.group(1)] = dict(title=m.group(2), cluster=g('cluster'), voice=g('voice'),
                             text=m.group(2) + '\n' + m.group(2) + '\n' + g('aliases') + '\n' + g('tags') + '\n' + main)
kiwi = Kiwi()
KEEP = ('NNG', 'NNP', 'NNB', 'NR', 'VV', 'VA', 'XR', 'SL', 'SH', 'SN', 'MAG')
tok = lambda s: [t.form.lower() for t in kiwi.tokenize(s) if t.tag.startswith(KEEP) and (len(t.form) > 1 or t.tag in ('SH', 'NNG', 'NNP'))]
print(f'카드 {len(cards)}장 형태소 분석 중(1분 안팎)...', flush=True)
ids = sorted(cards)
tf = {i: collections.Counter(tok(cards[i]['text'])) for i in ids}
dl = {i: sum(tf[i].values()) for i in ids}
avg = sum(dl.values()) / len(ids)
df = collections.Counter(t for i in ids for t in tf[i])
N = len(ids)


def bm25(q, k1=1.5, b=0.75):
    s = {}
    for t in set(tok(q)):
        if t not in df:
            continue
        idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
        for i in ids:
            f = tf[i].get(t)
            if f:
                s[i] = s.get(i, 0) + idf * f * (k1 + 1) / (f + k1 * (1 - b + b * dl[i] / avg))
    return [i for i, _ in sorted(s.items(), key=lambda x: -x[1])]


D = os.path.join(V, '_작업', '검색', '임베딩', a.model.replace('/', '__'))
vids = [r['id'] for r in json.load(open(os.path.join(D, 'ids.json'), encoding='utf-8'))]
M = np.load(os.path.join(D, 'body.npy')).astype(np.float32)
qs = [l.strip() for l in open(os.path.join(V, '_작업', '검색', '시험 질의.txt'), encoding='utf-8') if l.strip()]
print(f'모델을 불러와 질의 {len(qs)}개를 벡터로 바꿉니다...', flush=True)
from sentence_transformers import SentenceTransformer
QV = SentenceTransformer(a.model, device='cpu').encode(qs, normalize_embeddings=True)


def rrf(lists, k=60):
    s = collections.defaultdict(float)
    for L in lists:
        for r, i in enumerate(L[:200]):
            s[i] += 1 / (k + r + 1)
    return [i for i, _ in sorted(s.items(), key=lambda x: -x[1])]


out = ['---', 'type: 작업', '---', f'# 검색 시험 결과 ({a.model}, 상위 {a.k}장)', '',
       '질의마다 왼쪽은 BM25만, 오른쪽은 BM25+벡터(RRF)입니다. 양쪽에 다 나온 카드는 굵게 표시했습니다.', '']
for q, qv in zip(qs, QV):
    b = [i for i in bm25(q) if i in cards][:a.k]
    v = [vids[n] for n in np.argsort(-(M @ qv))[:200] if vids[n] in cards]
    h = [i for i in rrf([bm25(q), v]) if i in cards][:a.k]
    both = set(b) & set(h)
    fmt = lambda i: (f'**{i}**' if i in both else i) + f" {cards[i]['title'][:60]} ({cards[i]['voice']}·{cards[i]['cluster']})"
    out += [f'## {q}', '', '| 순위 | BM25 | 하이브리드 |', '|---|---|---|']
    for r in range(a.k):
        out.append(f"| {r + 1} | {fmt(b[r]) if r < len(b) else ''} | {fmt(h[r]) if r < len(h) else ''} |")
    out.append('')
p = os.path.join(V, '_작업', '검색', '검색 시험 결과.md')
open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('저장:', p)
