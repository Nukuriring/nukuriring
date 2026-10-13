# 사용법: python3 -P _작업/스크립트/dupes.py . [--model BAAI/bge-m3] [--title 0.85] [--body 0.88] [--batch 50] [--packets]
# (-P: 이 폴더의 struct.py가 표준 모듈 struct를 가리지 않게 한다)
# embed.py가 만든 임베딩으로 중복·유사 카드 후보 쌍을 뽑는다. 모델을 다시 부르지 않으므로 GPU 없이 돌아간다.
#  1. 제목 벡터 코사인이 --title 이상인 쌍
#  2. 본문 벡터 코사인이 --body 이상이고 서로 상위 5위 안에 드는 쌍
#  3. `_작업/정리 후보.md`에서 나온 쌍(`_작업/검색/쌍.json`) 가운데 아직 판정하지 않은 쌍. 유사도를 붙여 순위만 다시 매긴다.
# 뺄 것: 이미 판정한 쌍(`_작업/검색/판정조각/*.md`, `_작업/연결/판정/*.md`), 상위·하위 번호 관계(한쪽 id가 다른 쪽의 접두어).
# 같은 group 안의 쌍과 다른 group 사이의 쌍을 표시한다(같은 묶음 안의 겹침은 작업자가 일부러 나눈 줄기일 수 있다).
# 결과: `_작업/검색/후보쌍.json`(점수 순). --packets를 주면 중복판정자용 꾸러미 `_작업/검색/꾸러미/eN.md`도 쓴다.
import argparse, glob, json, os, re

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('--model', default='BAAI/bge-m3')
ap.add_argument('--title', type=float, default=0.85)
ap.add_argument('--body', type=float, default=0.88)
ap.add_argument('--batch', type=int, default=50)
ap.add_argument('--packets', action='store_true')
a = ap.parse_args()
V = a.vault
D = os.path.join(V, '_작업', '검색', '임베딩', a.model.replace('/', '__'))
rows = json.load(open(os.path.join(D, 'ids.json'), encoding='utf-8'))
meta = json.load(open(os.path.join(D, 'meta.json'), encoding='utf-8'))
if not meta.get('complete', True):
    print(f"경고: 임베딩이 미완성입니다({meta.get('cards')}/{meta.get('total')}장). PC에서 embed.py를 다시 돌려 마저 계산하세요.")
T = np.load(os.path.join(D, 'title.npy')).astype(np.float32)
B = np.load(os.path.join(D, 'body.npy')).astype(np.float32)
ids = [r['id'] for r in rows]
pos = {i: n for n, i in enumerate(ids)}

# 카드 정보(현재 파일 기준). 임베딩 뒤에 지워진 카드는 뺀다.
info = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read().replace('\r\n', '\n')
    if not x.startswith('---'):
        continue
    fm, body = x.split('---', 2)[1:]
    m = re.search(r'^# (\S+) (.+)$', body, re.M)
    if not m:
        continue
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', fm, re.M) or [None, ''])[1].strip()
    info[m.group(1)] = dict(file=os.path.basename(f)[:-3], title=m.group(2), group=g('group'),
                            cluster=g('cluster'), voice=g('voice'), path=f)
stale = [i for i in ids if i not in info]
if stale:
    print(f'임베딩에 있으나 지금은 없는 카드 {len(stale)}장(합치기·이름 변경). embed.py를 다시 돌리면 정리됩니다.')

# 이미 판정한 쌍
judged = set()
for f in glob.glob(os.path.join(V, '_작업', '검색', '판정조각', '*.md')):
    for l in open(f, encoding='utf-8'):
        c = [s.strip() for s in l.strip().strip('|').split('|')]
        if len(c) >= 3 and (c[0] in info or c[1] in info):
            judged.add(tuple(sorted(c[:2])))
for f in glob.glob(os.path.join(V, '_작업', '연결', '판정', '*.md')):
    for l in open(f, encoding='utf-8'):
        c = [s.strip() for s in l.strip().strip('|').split('|')]
        if len(c) >= 4 and c[0].isdigit():
            judged.add(tuple(sorted(c[1:3])))


def related(x, y):
    return x == y or x.startswith(y) or y.startswith(x)


P = {}


def add(x, y, via, ts=None, bs=None):
    if x not in info or y not in info or related(x, y):
        return
    k = tuple(sorted((x, y)))
    if k in judged:
        return
    p = P.setdefault(k, dict(a=k[0], b=k[1], via=[]))
    if via not in p['via']:
        p['via'].append(via)


# 1. 제목 유사
ST = T @ T.T
np.fill_diagonal(ST, -1)
for n, m in zip(*np.where(np.triu(ST) >= a.title)):
    add(ids[n], ids[m], 'title')
# 2. 본문 상호 상위 5
SB = B @ B.T
np.fill_diagonal(SB, -1)
top = np.argsort(-SB, axis=1)[:, :5]
topset = [set(r) for r in top]
for n in range(len(ids)):
    for m in top[n]:
        if SB[n, m] >= a.body and n in topset[m]:
            add(ids[n], ids[m], 'body')
# 3. 정리 후보에서 온 쌍
qp = os.path.join(V, '_작업', '검색', '쌍.json')
if os.path.exists(qp):
    for b in json.load(open(qp, encoding='utf-8')):
        for x, y in b['pairs']:
            add(x, y, '정리후보')

for k, p in P.items():
    x, y = pos.get(k[0]), pos.get(k[1])
    p['title_sim'] = round(float(ST[x, y]), 3) if x is not None and y is not None else None
    p['body_sim'] = round(float(SB[x, y]), 3) if x is not None and y is not None else None
    p['same_group'] = info[k[0]]['group'] == info[k[1]]['group']
    p['score'] = max(p['title_sim'] or 0, p['body_sim'] or 0)
out = sorted(P.values(), key=lambda p: -p['score'])
json.dump(out, open(os.path.join(V, '_작업', '검색', '후보쌍.json'), 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=0)
cnt = lambda f: sum(1 for p in out if f(p))
print(f"후보 {len(out)}쌍 (제목 {cnt(lambda p: 'title' in p['via'])}, 본문 {cnt(lambda p: 'body' in p['via'])}, "
      f"정리 후보 {cnt(lambda p: '정리후보' in p['via'])}; 같은 group {cnt(lambda p: p['same_group'])}), "
      f"이미 판정해 뺀 쌍 {len(judged)}")


def card(i):
    x = open(info[i]['path'], encoding='utf-8').read().replace('\r\n', '\n')
    body = x.split('---', 2)[2]
    body = re.sub(r'^# .+$', '', body, count=1, flags=re.M).split('\n## ')[0].strip()
    c = info[i]
    return f"### {i} {c['title']}\n(voice {c['voice']} · group {c['group']} · cluster {c['cluster']})\n\n{body}\n"


if a.packets:
    PD = os.path.join(V, '_작업', '검색', '꾸러미')
    os.makedirs(PD, exist_ok=True)
    for old in glob.glob(os.path.join(PD, 'e*.md')):
        os.remove(old)
    for bi in range(0, len(out), a.batch):
        b = out[bi:bi + a.batch]
        name = f'e{bi // a.batch + 1}'
        cs = list(dict.fromkeys(i for p in b for i in (p['a'], p['b'])))
        L = [f'# 중복 판정 꾸러미 {name}', '',
             f'쌍 {len(b)}개, 카드 {len(cs)}장. 아래 쌍 목록의 두 카드를 카드 본문 절에서 찾아 판정합니다. '
             '유사도는 순위를 매기려고 붙인 값이며 판정 근거가 아닙니다.', '', '## 쌍 목록', '']
        L += [f"{n}. {p['a']} · {p['b']} (제목 {p['title_sim']}, 본문 {p['body_sim']}"
              f"{', 같은 묶음' if p['same_group'] else ''})" for n, p in enumerate(b, 1)]
        L += ['', '## 카드 본문', ''] + [card(i) for i in cs]
        open(os.path.join(PD, name + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
    print(f'꾸러미 {(len(out) + a.batch - 1) // a.batch}개 → _작업/검색/꾸러미/e*.md')
