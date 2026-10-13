# 사용법: python3 -P _작업/스크립트/link_signals.py . [카드당 상한=4]
# (-P: 이 폴더의 struct.py가 표준 모듈 struct를 가리지 않게 한다)
# 다른 묶음(group) 카드와 이을 연결 후보를 LLM 없이 뽑는다. Obsidian 플러그인 방식을 옮겼다.
#  1. 키워드 신호(Note Linker 방식): 카드의 '관련 주제(다른 묶음)' 키워드를 `_작업/색인조각/`의
#     키워드→카드 대응과 카드 제목에 맞춘다.
#  2. 공동 인용 신호(Graph Analysis의 Adamic-Adar 방식): 같은 문헌 노트·원자료를 출처로 쓰는
#     다른 묶음 카드. 출처를 쓰는 카드가 많을수록 가중치를 낮춘다(1/log 차수).
#  3. 유사도 신호(Smart Connections 대용): 제목·본문 문자 2~4그램 TF-IDF 코사인. 순위 보조로만 쓴다.
#  4. 중복 판정에서 논쟁 관계·일반화 관계로 나온 쌍(`_작업/검색/판정조각/*.md`)은 사유와 함께 그대로 넣는다.
# 같은 group, 이미 링크된 카드, 상위·하위 번호 관계는 뺀다.
# 결과: `_작업/연결/후보.json`
import re, glob, os, sys, json, math, collections
from sklearn.feature_extraction.text import TfidfVectorizer
V = sys.argv[1]; K = int(sys.argv[2]) if len(sys.argv) > 2 else 4
C = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read()
    if not x.startswith('---'): continue
    fm, body = x.split('---', 2)[1:]
    m = re.search(r'^# (\S+) (.+)$', body, re.M)
    if not m: continue
    i, title = m.group(1), m.group(2)
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', fm, re.M) or [None, ''])[1].strip()
    main = re.sub(r'^# .+$', '', body.split('\n## ')[0], flags=re.M)
    src = body.split('## 출처')[-1] if '## 출처' in body else ''
    srcs = set(re.findall(r'\[\[(@[^\]|]+|_원자료/[^\]|]+)', src + fm))
    kw = []
    for l in re.findall(r'관련 주제\(다른 묶음\):\s*(.+)', body):
        kw += [k.strip() for k in re.split(r'[,;·]', l) if len(k.strip()) >= 2]
    C[i] = dict(file=os.path.basename(f)[:-3], title=title, group=g('group'), cluster=g('cluster'), voice=g('voice'),
                text=title + ' ' + title + ' ' + main, links=set(re.findall(r'\[\[(\S+?) ', body)), kw=kw, srcs=srcs)
ids = list(C); pos = {i: n for n, i in enumerate(ids)}
def blocked(a, b):
    return a == b or a.startswith(b) or b.startswith(a) or b in C[a]['links'] or a in C[b]['links'] or C[a]['group'] == C[b]['group']
norm = lambda s: re.sub(r'\s+', '', re.sub(r'\(.*?\)', '', s)).lower()
# 색인 키워드 → 카드
IDX = collections.defaultdict(set)
for f in glob.glob(os.path.join(V, '_작업', '색인조각', '*.md')):
    for l in open(f, encoding='utf-8'):
        m = re.match(r'- (.+?):\s*(\{.+)$', l.strip())
        if not m: continue
        key = m.group(1); cards = re.findall(r'\{(\S+?)\}', m.group(2))
        for k in {norm(key)} | {norm(p) for p in re.findall(r'\((.+?)\)', key)}:
            if len(k) >= 2: IDX[k] |= {c for c in cards if c in C}
P = collections.defaultdict(lambda: dict(score=0.0, via=[]))
def add(a, b, s, via):
    if blocked(a, b): return
    k = tuple(sorted((a, b))); P[k]['score'] += s
    if via not in P[k]['via']: P[k]['via'].append(via)
# 1. 키워드
titles_norm = {i: norm(C[i]['title']) for i in ids}
for a in ids:
    for kw in C[a]['kw']:
        nk = norm(kw); hits = set(IDX.get(nk, set()))
        for p in re.findall(r'\((.+?)\)', kw): hits |= IDX.get(norm(p), set())
        if len(nk) >= 3 and len(hits) < 3:
            hits |= {b for b in ids if nk in titles_norm[b]}
        hits = {b for b in hits if not blocked(a, b)}
        if not hits or len(hits) > 12: continue
        for b in hits: add(a, b, 1.0 / math.sqrt(len(hits)), 'kw:' + kw)
# 2. 공동 인용
users = collections.defaultdict(list)
for i in ids:
    for s in C[i]['srcs']: users[s].append(i)
for s, us in users.items():
    if len(us) < 2 or len(us) > 60: continue
    w = 1.0 / math.log(len(us) + 1)
    groups = collections.defaultdict(list)
    for u in us: groups[C[u]['group']].append(u)
    if len(groups) < 2: continue
    for a in us:
        for b in us:
            if a < b: add(a, b, w * 0.5, 'src:' + s.split('/')[-1][:40])
# 4. 중복 판정 결과
for f in glob.glob(os.path.join(V, '_작업', '검색', '판정조각', '*.md')):
    for l in open(f, encoding='utf-8'):
        c = [x.strip() for x in l.split('|')[1:-1]]
        if len(c) >= 5 and c[2] in ('논쟁 관계', '일반화 관계') and c[0] in C and c[1] in C:
            k = tuple(sorted((c[0], c[1])))
            if C[c[0]]['links'] & {c[1]} or C[c[1]]['links'] & {c[0]}: continue
            P[k]['score'] += 2.0; P[k]['via'].append(f'dup:{c[2]}:{c[4]}')
# 3. 유사도로 순위 보정
vec = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4), min_df=2, max_df=0.3, sublinear_tf=True)
X = vec.fit_transform([C[i]['text'] for i in ids])
for k, p in P.items():
    s = float(X[pos[k[0]]].multiply(X[pos[k[1]]]).sum())
    p['sim'] = round(s, 3); p['rank'] = p['score'] * (0.5 + s)
cnt = collections.Counter(); out = []
for k, p in sorted(P.items(), key=lambda kv: -kv[1]['rank']):
    a, b = k
    if p['sim'] < 0.05 and not any(v.startswith('dup') for v in p['via']): continue
    if cnt[a] >= K or cnt[b] >= K: continue
    cnt[a] += 1; cnt[b] += 1
    out.append(dict(a=a, b=b, rank=round(p['rank'], 3), sim=p['sim'], via=p['via'][:3]))
os.makedirs(os.path.join(V, '_작업', '연결'), exist_ok=True)
json.dump(out, open(os.path.join(V, '_작업', '연결', '후보.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
src = collections.Counter(v.split(':')[0] for p in out for v in p['via'])
cross = sum(1 for p in out if C[p['a']]['cluster'] != C[p['b']]['cluster'])
print('raw', len(P), 'kept', len(out), 'cross-cluster', cross, 'cards', len(cnt), 'signals', dict(src))
for p in out[::max(1, len(out)//12)][:12]:
    print(p['rank'], p['via'][0][:28], '|', C[p['a']]['title'][:40], '||', C[p['b']]['title'][:40])
