# 사용법: py -3 _작업/스크립트/verify_packets.py . <카드 번호…>
#        py -3 _작업/스크립트/verify_packets.py . --batches <시작 번호> <끝 번호>   (판정 분담.json의 묶음 번호)
# 검증자가 큰 출처 파일을 오가지 않도록, 카드마다 `_작업/검증/꾸러미/<id>.md`에
# 카드 본문과 출처별 관련 대목(카드의 핵심 어구가 많이 나오는 문단)을 미리 모아 둔다.
# 발췌는 길잡이일 뿐이다. 검증자는 발췌에 없는 명제를 '원문에 없음'으로 두기 전에 원본을 검색한다.
import json, os, re, sys, unicodedata

V = sys.argv[1]
args = sys.argv[2:]
OUT = os.path.join(V, '_작업', '검증', '꾸러미')
CARD_CAP = 9000      # 카드 하나의 발췌 총량(글자)
WHOLE = 2500         # 이보다 짧은 출처는 통째로 넣는다
WIN = 700            # 맞는 문단 앞뒤로 붙일 글자 수

nfc = lambda s: unicodedata.normalize('NFC', s)
JOSA = re.compile(r'(으로써|으로서|에서는|에게서|이라는|라는|이라고|라고|으로|에서|에게|까지|부터|처럼|보다|이다|하는|하고|하며|한다|된다|에는|에도|와는|과는|은|는|이|가|을|를|의|에|도|와|과|로|만)$')
STOP = set('그리고 그러나 하지만 또한 따라서 이것 그것 이는 그는 그녀 우리 있다 없다 한다 된다 것이다 때문 경우 대한 위한 통해 같은 다른 이런 그런 이를 이에 수업 필기 노트 카드 출처 본문 the and that this with from which their there what into have been were'.split())

cards = {}
for fn in os.listdir(os.path.join(V, '영구')):
    m = re.match(r'(\S+) .*\.md$', fn)
    if m:
        cards[nfc(m.group(1))] = os.path.join(V, '영구', fn)
nmap = json.load(open(os.path.join(V, '_작업', '검증', 'notion_map.json'), encoding='utf-8'))['cards']


def resolve(rel):
    """[[링크]] 대상 → 실제 파일 경로(확장자 생략 허용)."""
    rel = rel.split('|')[0].split('#')[0].strip()
    for cand in (rel, rel + '.md', rel + '.txt'):
        p = os.path.join(V, cand)
        if os.path.isfile(p):
            return cand
    return None


def terms(text):
    """카드 본문에서 출처와 맞춰 볼 어구: 라틴 문자 낱말, 숫자, 조사를 뗀 한국어 낱말, 인용문 조각."""
    out = set()
    for q in re.findall(r'["“]([^"”]{6,80})["”]', text):
        out.add(q.strip().casefold()[:40])
    for w in re.findall(r'[A-Za-z][A-Za-z\'-]{3,}', text):
        if w.casefold() not in STOP:
            out.add(w.casefold())
    for w in re.findall(r'\d{2,}(?:[.,]\d+)?', text):
        out.add(w)
    for w in re.findall(r'[가-힣]{2,}', text):
        w = JOSA.sub('', w)
        if len(w) >= 2 and w not in STOP:
            out.add(w)
    return out


def excerpt(src_text, ts, cap):
    if len(src_text) <= max(WHOLE, 0):
        return src_text.strip()
    paras = [p for p in re.split(r'\n\s*\n', src_text) if p.strip()]
    pos, scored, at = [], [], 0
    for p in paras:
        i = src_text.find(p, at); at = i + len(p)
        low = p.casefold()
        s = sum(1 for t in ts if t in low)
        scored.append((s, i, i + len(p)))
    scored.sort(key=lambda x: -x[0])
    spans, total = [], 0
    for s, a, b in scored:
        if s < 2 or total >= cap:
            break
        a, b = max(0, a - WIN), min(len(src_text), b + WIN)
        if b - a > 2500:  # 아주 긴 문단은 가운데를 잘라 낸다
            b = a + 2500
        spans.append((a, b)); total += b - a
    spans.sort()
    merged = []
    for a, b in spans:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    return '\n\n[…]\n\n'.join(src_text[a:b].strip() for a, b in merged)


def build(cid):
    path = cards.get(cid)
    if not path:
        return None
    text = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    body = text.split('\n---', 1)[1] if text.startswith('---') else text
    main = body.split('\n## 연결', 1)[0]
    src = text.split('\n## 출처', 1)[1].split('\n## ', 1)[0] if '\n## 출처' in text else ''
    ts = terms(main)
    sources = []
    for l in re.findall(r'\[\[(@[^\]]+)\]\]', src):
        r = resolve('문헌/' + l)
        sources.append(r or ('문헌/' + l.split('|')[0] + ' (파일 없음)'))
    for l in re.findall(r'\[\[(_원자료/[^\]]+)\]\]', src):
        r = resolve(l)
        sources.append(r or (l.split('|')[0] + ' (파일 없음)'))
    subdirs = []
    for ref in nmap.get(cid, []):
        sources += ref['files'][:2]
        if ref.get('subdir'):
            subdirs.append(ref['subdir'])
    sources = list(dict.fromkeys(sources))
    L = [f'# 꾸러미 {cid}', '', f'카드 파일: `{os.path.relpath(path, V).replace(os.sep, "/")}`', '',
         '## 카드', '', main.strip(), '', '## 출처 절', '', src.strip(), '']
    if subdirs:
        L += ['하위 페이지 폴더(상위 페이지 내용이 얕으면 여기서 찾음): ' + ', '.join(f'`{d}`' for d in dict.fromkeys(subdirs)), '']
    real = [s for s in sources if not s.endswith('(파일 없음)')]
    per = CARD_CAP // max(1, len(real))
    for s in sources:
        L.append(f'## 발췌: `{s}`')
        L.append('')
        if s.endswith('(파일 없음)'):
            L += ['(파일을 찾지 못함)', '']; continue
        try:
            st = open(os.path.join(V, s), encoding='utf-8', errors='replace').read().replace('\r\n', '\n')
        except OSError:
            L += ['(읽기 실패)', '']; continue
        ex = excerpt(st, ts, per)
        L += [f'(원본 {len(st):,}자 중 발췌. 발췌에 없는 명제는 원본을 검색한 뒤 판정)' if len(st) > WHOLE else '(원본 전체)', '',
              ex if ex else '(카드 어구와 맞는 대목을 찾지 못함. 원본을 직접 검색)', '']
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, f'{cid}.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    return sum(len(x) for x in L)


if args and args[0] == '--batches':
    d = json.load(open(os.path.join(V, '_작업', '검증', '판정 분담.json'), encoding='utf-8'))
    lo, hi = int(args[1]), int(args[2])
    ids = [i for b in d['batches'] if lo <= b['n'] <= hi for i in b['ids']]
else:
    ids = args
sizes = [s for s in (build(nfc(i)) for i in ids) if s]
if sizes:
    print(f'꾸러미 {len(sizes)}개, 평균 {sum(sizes) // len(sizes):,}자, 최대 {max(sizes):,}자 → _작업/검증/꾸러미/')
