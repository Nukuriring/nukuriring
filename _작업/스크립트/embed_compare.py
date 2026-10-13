# 사용법: python3 -P _작업/스크립트/embed_compare.py . [--a BAAI/bge-m3] [--b nlpai-lab/KURE-v1] [--n 100] [--k 5]
# 두 임베딩 모델(embed.py로 각각 만든 것)의 최근접 이웃을 같은 카드 n장에 대해 나란히 보여 준다.
# 영진 님이 어느 모델의 이웃이 더 그럴듯한지 고르는 시험지이다(작업 계획 3단계, 결정 사항 5).
# 카드는 클러스터마다 고르게, 시드를 고정해 뽑는다. 본문 벡터 기준이고 상위·하위 번호 관계인 카드는 뺀다.
# 결과: `_작업/검색/모델 비교.md`. 카드마다 `- [ ] A 쪽이 낫다 / - [ ] B 쪽이 낫다 / - [ ] 비슷하다`에 표시합니다.
import argparse, glob, json, os, random, re

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('--a', default='BAAI/bge-m3')
ap.add_argument('--b', default='nlpai-lab/KURE-v1')
ap.add_argument('--n', type=int, default=100)
ap.add_argument('--k', type=int, default=5)
o = ap.parse_args()
V = o.vault


def load(model):
    D = os.path.join(V, '_작업', '검색', '임베딩', model.replace('/', '__'))
    ids = [r['id'] for r in json.load(open(os.path.join(D, 'ids.json'), encoding='utf-8'))]
    return ids, np.load(os.path.join(D, 'body.npy')).astype(np.float32)


ia, A = load(o.a)
ib, B = load(o.b)
common = sorted(set(ia) & set(ib))
title, cluster = {}, {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read()
    m = re.search(r'^# (\S+) (.+)$', x, re.M)
    c = re.search(r'^cluster:\s*(.+)$', x, re.M)
    if m:
        title[m.group(1)] = m.group(2)
        cluster[m.group(1)] = c.group(1).strip() if c else ''
common = [i for i in common if i in title]
rng = random.Random(20261013)
by = {}
for i in common:
    by.setdefault(cluster[i], []).append(i)
pick = []
while len(pick) < min(o.n, len(common)):
    for cl in sorted(by):
        if by[cl] and len(pick) < o.n:
            pick.append(by[cl].pop(rng.randrange(len(by[cl]))))


def nn(ids, M, cid):
    p = {i: n for n, i in enumerate(ids)}
    s = M @ M[p[cid]]
    out = []
    for n in np.argsort(-s):
        j = ids[n]
        if j == cid or j.startswith(cid) or cid.startswith(j) or j not in title:
            continue
        out.append((j, float(s[n])))
        if len(out) == o.k:
            break
    return out


L = ['---', 'type: 작업', '---', f'# 임베딩 모델 비교: A = `{o.a}`, B = `{o.b}`', '',
     f'카드 {len(pick)}장마다 두 모델이 고른 가까운 카드 {o.k}장입니다. 지문 소재를 찾을 때 더 쓸모 있는 이웃을 고른 쪽에 표시해 주세요. '
     '두 목록에 함께 나온 카드는 굵게 표시했습니다.', '']
for cid in pick:
    na, nb = nn(ia, A, cid), nn(ib, B, cid)
    both = {j for j, _ in na} & {j for j, _ in nb}
    fmt = lambda j, s: (f'**[[{j} {title[j]}|{j}]]**' if j in both else f'[[{j} {title[j]}|{j}]]') + f' {title[j][:50]} ({s:.2f})'
    L += [f'## {cid} {title[cid]}', f'({cluster[cid]})', '', 'A:'] + [f'- {fmt(j, s)}' for j, s in na]
    L += ['', 'B:'] + [f'- {fmt(j, s)}' for j, s in nb]
    L += ['', '- [ ] A 쪽이 낫다', '- [ ] B 쪽이 낫다', '- [ ] 비슷하다', '']
open(os.path.join(V, '_작업', '검색', '모델 비교.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
print(f'카드 {len(pick)}장 → _작업/검색/모델 비교.md')
