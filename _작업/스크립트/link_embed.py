# 사용법: python3 -P _작업/스크립트/link_embed.py . [--model BAAI/bge-m3] [--k 8] [--min 0.70] [--per 3] [--same-cluster]
# 임베딩(본문 벡터)으로 다른 클러스터 카드 사이의 연결 후보를 뽑는다(작업 계획 5단계, 영역 간 연결 우선).
#  - 카드마다 다른 클러스터 카드 가운데 코사인 상위 k장을 보고, 유사도 --min 이상인 쌍을 후보로 삼는다.
#  - 서로의 상위 k 안에 드는 쌍(상호 이웃)을 먼저 두고, 카드 한 장이 후보에 나오는 횟수를 --per로 제한한다.
#  - 뺄 것: 이미 링크된 쌍, 같은 group, 상위·하위 번호 관계, 합치기 안내 카드, 이미 판정한 쌍
#    (`_작업/연결/판정/*.md`, `_작업/검색/판정조각/*.md`).
#  - --same-cluster를 주면 같은 클러스터 안의 쌍만 뽑는다(다른 group끼리).
# 결과: `_작업/연결/후보_임베딩.json` ({a, b, via, sim}). 꾸러미는 link_packets.py . 100 후보_임베딩.json v 로 만든다.
import argparse, collections, glob, json, os, re

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('--model', default='BAAI/bge-m3')
ap.add_argument('--k', type=int, default=8)
ap.add_argument('--min', type=float, default=0.70)
ap.add_argument('--per', type=int, default=3)
ap.add_argument('--same-cluster', action='store_true')
a = ap.parse_args()
V = a.vault
D = os.path.join(V, '_작업', '검색', '임베딩', a.model.replace('/', '__'))
vids = [r['id'] for r in json.load(open(os.path.join(D, 'ids.json'), encoding='utf-8'))]
M = np.load(os.path.join(D, 'body.npy')).astype(np.float32)

C = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read()
    if not x.startswith('---'):
        continue
    fm, body = x.split('---', 2)[1:]
    m = re.search(r'^# (\S+) (.+)$', body, re.M)
    if not m:
        continue
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', fm, re.M) or [None, ''])[1].strip()
    C[m.group(1)] = dict(cluster=g('cluster'), group=g('group'), links=set(re.findall(r'\[\[(\S+?) ', body)),
                         stub='남겨 둔 안내 카드' in body)
judged = set()
for f in glob.glob(os.path.join(V, '_작업', '연결', '판정', '*.md')) + glob.glob(os.path.join(V, '_작업', '검색', '판정조각', '*.md')):
    for l in open(f, encoding='utf-8'):
        c = [s.strip() for s in l.strip().strip('|').split('|')]
        if len(c) >= 4:
            pair = c[1:3] if c[0].isdigit() else c[0:2]
            judged.add(tuple(sorted(pair)))

rows = [n for n, i in enumerate(vids) if i in C and not C[i]['stub']]
ids = [vids[n] for n in rows]
X = M[rows]
S = X @ X.T
np.fill_diagonal(S, -1)
cl = np.array([C[i]['cluster'] for i in ids])
same = cl[:, None] == cl[None, :]
S_masked = np.where(same if not a.same_cluster else ~same, -1, S)
top = np.argsort(-S_masked, axis=1)[:, :a.k]
topset = [set(r) for r in top]


def ok(x, y):
    if x == y or x.startswith(y) or y.startswith(x):
        return False
    if C[x]['group'] == C[y]['group'] or y in C[x]['links'] or x in C[y]['links']:
        return False
    return tuple(sorted((x, y))) not in judged


P = {}
for n in range(len(ids)):
    for m in top[n]:
        s = float(S[n, m])
        if s < a.min:
            continue
        x, y = ids[n], ids[m]
        if not ok(x, y):
            continue
        k = tuple(sorted((x, y)))
        mutual = n in topset[m]
        if k not in P or s > P[k]['sim']:
            P[k] = dict(a=k[0], b=k[1], sim=round(s, 3), mutual=mutual)
order = sorted(P.values(), key=lambda p: (not p['mutual'], -p['sim']))
cnt, out = collections.Counter(), []
for p in order:
    if cnt[p['a']] >= a.per or cnt[p['b']] >= a.per:
        continue
    cnt[p['a']] += 1; cnt[p['b']] += 1
    p['via'] = [f"임베딩 {p['sim']}" + (' 상호 이웃' if p['mutual'] else '') + f" ({C[p['a']]['cluster']} / {C[p['b']]['cluster']})"]
    out.append(p)
json.dump(out, open(os.path.join(V, '_작업', '연결', '후보_임베딩.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
pairs = collections.Counter(tuple(sorted((C[p['a']]['cluster'], C[p['b']]['cluster']))) for p in out)
print(f"후보 {len(out)}쌍(상호 이웃 {sum(p['mutual'] for p in out)}), 이미 판정한 쌍 {len(judged)} 제외")
for (x, y), n in pairs.most_common(12):
    print(f'  {x} ↔ {y}: {n}')
