# 사용법: python3 -P _작업/스크립트/search.py . "질의" [--k 10] [--bm25-only] [--model BAAI/bge-m3] [--cluster 이름] [--voice 문헌]
#         python3 -P _작업/스크립트/search.py . --like <카드 id> [--k 10]
#         python3 -P _작업/스크립트/search.py . --rebuild
# (-P: 이 폴더의 struct.py가 표준 모듈 struct를 가리지 않게 한다. PC에서는 py -3 -P)
# 영구 노트를 찾는 하이브리드 검색이다(작업 계획 4단계 2안). 결과는 카드 id와 제목만 돌려준다. 본문은 직접 읽는다.
#  - BM25: kiwipiepy 형태소 분석 토큰(체언·용언 어간·어근·외국어·한자·숫자). 조사가 붙은 어절도 같은 토큰이 된다.
#    kiwipiepy가 없으면 글자 2그램으로 대신한다(품질이 떨어짐). 설치: pip install kiwipiepy
#  - 벡터: embed.py가 만든 본문 벡터. 질의를 벡터로 바꾸려면 같은 모델이 로컬에 있어야 하므로(PC), 없으면 BM25만 쓴다.
#    --like는 저장된 카드 벡터끼리 비교하므로 모델 없이도 된다.
#  - 두 순위를 RRF(k=60)로 합친다.
# 원자료(`_원자료/`)는 검색하지 않는다. 출처는 카드의 `## 출처`를 따라가 확인한다.
# 토큰 캐시: `_작업/검색/bm25_cache.json`(git 제외). 카드가 바뀌면 그 카드만 다시 분석한다.
import argparse, collections, glob, hashlib, json, math, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument('vault')
ap.add_argument('query', nargs='?', default='')
ap.add_argument('--k', type=int, default=10)
ap.add_argument('--like')
ap.add_argument('--bm25-only', action='store_true')
ap.add_argument('--model', default='BAAI/bge-m3')
ap.add_argument('--cluster')
ap.add_argument('--voice')
ap.add_argument('--rebuild', action='store_true')
a = ap.parse_args()
V = a.vault
SD = os.path.join(V, '_작업', '검색')
os.makedirs(SD, exist_ok=True)

# ---------- 카드 ----------
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
    al = g('aliases')
    text = m.group(2) + '\n' + m.group(2) + '\n' + al + '\n' + g('tags') + '\n' + main  # 제목은 두 번 넣어 가중
    cards[m.group(1)] = dict(title=m.group(2), cluster=g('cluster'), voice=g('voice'), text=text,
                             hash=hashlib.sha1(text.encode('utf-8')).hexdigest()[:12])

# ---------- 토큰화 ----------
try:
    from kiwipiepy import Kiwi
    _kiwi = Kiwi()
    KEEP = ('NNG', 'NNP', 'NNB', 'NR', 'VV', 'VA', 'XR', 'SL', 'SH', 'SN', 'MAG')

    def tok(s):
        return [t.form.lower() for t in _kiwi.tokenize(s) if t.tag.startswith(KEEP) and (len(t.form) > 1 or t.tag in ('SH', 'NNG', 'NNP'))]
    TOK = 'kiwi'
except ImportError:
    def tok(s):
        s = re.sub(r'\s+', ' ', s.lower())
        out = []
        for w in re.findall(r'[0-9a-z]+|[^\s0-9a-z\W]+', s):
            out += [w] if w.isascii() else ([w] if len(w) == 1 else [w[i:i + 2] for i in range(len(w) - 1)])
        return out
    TOK = 'bigram'
    print('알림: kiwipiepy가 없어 글자 2그램으로 검색합니다(pip install kiwipiepy).', file=sys.stderr)

cp = os.path.join(SD, 'bm25_cache.json')
cache = {}
if os.path.exists(cp) and not a.rebuild:
    try:
        cache = json.load(open(cp, encoding='utf-8'))
        if cache.get('tokenizer') != TOK:
            cache = {}
    except ValueError:
        cache = {}
docs = cache.get('docs', {})
changed = False
for i, c in cards.items():
    if i not in docs or docs[i]['hash'] != c['hash']:
        docs[i] = dict(hash=c['hash'], toks=tok(c['text'])); changed = True
for i in [i for i in docs if i not in cards]:
    del docs[i]; changed = True
if changed or a.rebuild:
    json.dump(dict(tokenizer=TOK, docs=docs), open(cp, 'w', encoding='utf-8'), ensure_ascii=False)
if a.rebuild:
    print(f'토큰 캐시 재작성: 카드 {len(docs)}장 ({TOK})'); sys.exit()

# ---------- BM25 ----------
ids = sorted(cards)
tf = {i: collections.Counter(docs[i]['toks']) for i in ids}
dl = {i: len(docs[i]['toks']) for i in ids}
avg = sum(dl.values()) / max(1, len(ids))
df = collections.Counter(t for i in ids for t in tf[i])
N = len(ids)


def bm25(q_toks, k1=1.5, b=0.75):
    s = {}
    for t in set(q_toks):
        if t not in df:
            continue
        idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
        for i in ids:
            f = tf[i].get(t)
            if f:
                s[i] = s.get(i, 0) + idf * f * (k1 + 1) / (f + k1 * (1 - b + b * dl[i] / avg))
    return [i for i, _ in sorted(s.items(), key=lambda x: -x[1])]


# ---------- 벡터 ----------
def vec_rank(qv=None, like=None):
    import numpy as np
    D = os.path.join(SD, '임베딩', a.model.replace('/', '__'))
    if not os.path.exists(os.path.join(D, 'body.npy')):
        return None
    vids = [r['id'] for r in json.load(open(os.path.join(D, 'ids.json'), encoding='utf-8'))]
    M = np.load(os.path.join(D, 'body.npy')).astype(np.float32)
    if like is not None:
        if like not in vids:
            return None
        qv = M[vids.index(like)]
    s = M @ qv
    return [vids[n] for n in np.argsort(-s)[:200] if vids[n] in cards]


def query_vec(q):
    try:
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer(a.model)
        return m.encode([q], normalize_embeddings=True)[0]
    except Exception as e:  # 모델이 없는 환경(클라우드)에서는 BM25만 쓴다
        print(f'알림: 질의 벡터를 만들 수 없어 BM25만 씁니다({type(e).__name__}).', file=sys.stderr)
        return None


def rrf(lists, k=60):
    s = collections.defaultdict(float)
    for L in lists:
        for r, i in enumerate(L[:200]):
            s[i] += 1 / (k + r + 1)
    return [i for i, _ in sorted(s.items(), key=lambda x: -x[1])]


lists, via = [], []
if a.like:
    if a.like not in cards:
        sys.exit(f'카드 {a.like}이(가) 없습니다.')
    lists.append(bm25(tok(cards[a.like]['title']))); via.append('bm25(제목)')
    v = vec_rank(like=a.like)
    if v:
        lists.append(v); via.append('벡터')
    exclude = lambda i: i == a.like or i.startswith(a.like) or a.like.startswith(i)
else:
    if not a.query:
        sys.exit('질의를 주거나 --like <id>를 씁니다.')
    lists.append(bm25(tok(a.query))); via.append('bm25')
    if not a.bm25_only:
        qv = query_vec(a.query)
        v = vec_rank(qv=qv) if qv is not None else None
        if v:
            lists.append(v); via.append('벡터')
    exclude = lambda i: False
res = [i for i in (rrf(lists) if len(lists) > 1 else lists[0]) if not exclude(i)
       and (not a.cluster or cards[i]['cluster'] == a.cluster) and (not a.voice or cards[i]['voice'] == a.voice)]
print(f"# 검색: {a.query or a.like} ({' + '.join(via)}, 토큰 {TOK})")
for n, i in enumerate(res[:a.k], 1):
    c = cards[i]
    print(f"{n}. [[{i} {c['title']}]] ({c['voice']} · {c['cluster']})")
