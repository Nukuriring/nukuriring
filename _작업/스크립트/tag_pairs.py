# 사용법: python3 -P _작업/스크립트/tag_pairs.py . [카드당 상한=3]
# 개념 태그(`_작업/연결/태그/결과/t*.md`)를 공유하는 다른 클러스터 카드 쌍을 뽑는다.
# - 어휘(`_작업/연결/태그/어휘.md`)에 없는 태그는 버린다.
# - 점수: 공유 태그의 IDF 합. 공유 태그가 둘 이상이거나, 하나라도 40장 이하에 붙은 드문 태그여야 한다.
# - 같은 group, 이미 링크된 카드, 상위·하위 번호, 앞서 연결 판정한 쌍(`_작업/연결/판정/l*.md`)은 뺀다.
# 결과: `_작업/연결/후보_태그.json`
import re, glob, os, sys, json, math, collections, itertools
V = sys.argv[1]; K = int(sys.argv[2]) if len(sys.argv) > 2 else 3
vocab = {re.match(r'- (.+?):', l).group(1).strip() for l in open(os.path.join(V, '_작업/연결/태그/어휘.md'), encoding='utf-8') if re.match(r'- (.+?):', l)}
tags, bad = {}, collections.Counter()
for f in glob.glob(os.path.join(V, '_작업/연결/태그/결과/t*.md')):
    for l in open(f, encoding='utf-8'):
        m = re.match(r'\s*-?\s*(\S+?):\s*(.*)$', l.strip())
        if not m: continue
        ts = [t.strip() for t in m.group(2).split(';') if t.strip()]
        ok = [t for t in ts if t in vocab]; bad.update(t for t in ts if t not in vocab)
        tags[m.group(1)] = ok
C = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read()
    m = re.search(r'^# (\S+) ', x, re.M)
    if not m: continue
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', x, re.M) or [0, ''])[1].strip()
    C[m.group(1)] = dict(group=g('group'), cluster=g('cluster'), links=set(re.findall(r'\[\[(\S+?) ', x)))
judged = set()
for f in glob.glob(os.path.join(V, '_작업/연결/판정/[lm]*.md')):
    for l in open(f, encoding='utf-8'):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) >= 4 and c[0].isdigit(): judged.add(tuple(sorted((c[1], c[2]))))
users = collections.defaultdict(list)
for i, ts in tags.items():
    if i in C:
        for t in ts: users[t].append(i)
N = len(tags); idf = {t: math.log(N / len(u)) for t, u in users.items()}
P = collections.defaultdict(lambda: [0.0, []])
for t, us in users.items():
    if len(us) > 250: continue
    for a, b in itertools.combinations(sorted(us), 2):
        if C[a]['cluster'] == C[b]['cluster'] or C[a]['group'] == C[b]['group']: continue
        if a.startswith(b) or b.startswith(a) or b in C[a]['links'] or a in C[b]['links']: continue
        if (a, b) in judged: continue
        P[(a, b)][0] += idf[t]; P[(a, b)][1].append(t)
cand = [(k, s, ts) for k, (s, ts) in P.items() if len(ts) >= 2 or min(len(users[t]) for t in ts) <= 40]
cand.sort(key=lambda x: -x[1])
cnt = collections.Counter(); out = []
for (a, b), s, ts in cand:
    if cnt[a] >= K or cnt[b] >= K: continue
    cnt[a] += 1; cnt[b] += 1
    out.append(dict(a=a, b=b, rank=round(s, 2), via=['tag:' + '·'.join(ts)]))
json.dump(out, open(os.path.join(V, '_작업/연결/후보_태그.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('tagged', len(tags), 'with tags', sum(1 for v in tags.values() if v), 'unknown tags', sum(bad.values()), bad.most_common(5))
print('raw pairs', len(P), 'eligible', len(cand), 'kept', len(out), 'cards', len(cnt))
