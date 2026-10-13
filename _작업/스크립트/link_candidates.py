# 사용법: python3 _작업/스크립트/link_candidates.py . [유사도 하한=0.18] [카드당 상한=3]
# 다른 묶음(group) 카드와 이을 연결 후보를 LLM 없이 뽑는다.
# - 질의: 카드마다 '관련 주제(다른 묶음)' 줄의 키워드 각각, 그리고 카드 제목 자체.
# - 색인: 모든 카드의 제목(두 번)과 본문에 대한 문자 2~4그램 TF-IDF.
# - 같은 group, 이미 링크된 카드, 상위·하위 번호 관계는 뺀다. 쌍은 대칭으로 한 번만 센다.
# 결과: `_작업/연결/후보.json` [{a, b, score, via}]
import re, glob, os, sys, json, collections
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
V = sys.argv[1]; TH = float(sys.argv[2]) if len(sys.argv) > 2 else 0.18; K = int(sys.argv[3]) if len(sys.argv) > 3 else 3
C = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read()
    if '---' not in x[:5]: continue
    fm, body = x.split('---', 2)[1:]
    m = re.search(r'^# (\S+) (.+)$', body, re.M)
    if not m: continue
    i, title = m.group(1), m.group(2)
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', fm, re.M) or [None, ''])[1].strip()
    main = body.split('\n## ')[0]
    links = set(re.findall(r'\[\[(\S+?) ', body))
    kw = []
    for l in re.findall(r'관련 주제\(다른 묶음\):\s*(.+)', body):
        kw += [k.strip() for k in re.split(r',|;|·', l) if len(k.strip()) >= 2]
    C[i] = dict(file=os.path.basename(f)[:-3], title=title, group=g('group'), cluster=g('cluster'), voice=g('voice'),
                text=title + ' ' + title + ' ' + re.sub(r'^# .+$', '', main, flags=re.M), links=links, kw=kw)
ids = list(C)
vec = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4), min_df=2, max_df=0.3, sublinear_tf=True)
X = vec.fit_transform([C[i]['text'] for i in ids])
pos = {i: n for n, i in enumerate(ids)}
def related(a, b):
    return a.startswith(b) or b.startswith(a) or b in C[a]['links'] or a in C[b]['links'] or C[a]['group'] == C[b]['group']
best = {}
def consider(a, sims, via):
    order = sims.argsort()[::-1]
    got = 0
    for n in order[:40]:
        b = ids[n]; s = float(sims[n])
        if s < TH: break
        if b == a or related(a, b): continue
        k = tuple(sorted((a, b)))
        if k not in best or best[k]['score'] < s: best[k] = dict(a=k[0], b=k[1], score=round(s, 3), via=via)
        got += 1
        if got >= 1: break
# 키워드 질의
for a in ids:
    for kw in C[a]['kw'][:6]:
        q = vec.transform([kw + ' ' + C[a]['title']])
        consider(a, linear_kernel(q, X).ravel(), 'kw:' + kw)
# 제목·본문 유사도 (다른 클러스터 우선)
S = linear_kernel(X, X)
for a in ids:
    row = S[pos[a]].copy()
    for n, b in enumerate(ids):
        if C[b]['cluster'] == C[a]['cluster']: row[n] *= 0.8
    consider(a, row, 'sim')
# 카드당 상한
cnt = collections.Counter(); out = []
for p in sorted(best.values(), key=lambda p: -p['score']):
    if cnt[p['a']] >= K or cnt[p['b']] >= K: continue
    cnt[p['a']] += 1; cnt[p['b']] += 1; out.append(p)
os.makedirs(os.path.join(V, '_작업', '연결'), exist_ok=True)
json.dump(out, open(os.path.join(V, '_작업', '연결', '후보.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
cross = sum(1 for p in out if C[p['a']]['cluster'] != C[p['b']]['cluster'])
print('cards', len(ids), 'with kw', sum(1 for i in ids if C[i]['kw']), 'pairs', len(out), 'cross-cluster', cross, 'cards touched', len(cnt))
for p in out[:5] + out[len(out)//2:len(out)//2+5] + out[-5:]:
    print(p['score'], p['via'][:30], '|', C[p['a']]['title'][:45], '||', C[p['b']]['title'][:45])
