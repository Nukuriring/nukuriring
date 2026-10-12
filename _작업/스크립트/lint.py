"""보관함 결정적 점검(LLM 없음).

사용:
  py _작업/스크립트/lint.py                 보관함 전체 → _작업/검증/lint.json, 01 lint 요약.md
  py _작업/스크립트/lint.py --file <경로>…  지정 파일만 점검해 화면에 출력
  py _작업/스크립트/lint.py --hook          Claude Code PostToolUse 훅(stdin JSON). 오류가 있으면 종료 코드 2

오류(E)는 형식이 깨진 것이고, 경고(W)는 지침 위반 의심입니다. 훅은 오류만 막습니다.
카드는 고치지 않고 읽기만 합니다.
"""
import os, re, sys, json, unicodedata, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / '_작업' / '검증'

VOICES = {'문헌', '영진', '종합'}
STATUSES = {'초안', '검토됨', '다시씀'}
VERIFY = {'지지됨', '부분', '원문없음', '모순', '판단불가'}
REQUIRED = ['id', 'type', 'voice', 'status', 'tags', 'sources', 'cluster', 'created']
ENDINGS = set('다요까죠오네라자가지냐니')  # 종결 어미의 마지막 글자로 흔한 것

nfc = lambda s: unicodedata.normalize('NFC', s)


# ---------- 파일 색인 ----------
_index = None
def file_index():
    """링크 해석용: 경로(확장자 유무)와 파일명(확장자 유무) → 존재."""
    global _index
    if _index is not None:
        return _index
    paths, names = set(), set()
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in ('.git', '.obsidian', '.trash', '.claude')]
        rel_dir = os.path.relpath(dp, ROOT).replace('\\', '/')
        for fn in fns:
            fn = nfc(fn)
            stem = fn.rsplit('.', 1)[0] if '.' in fn else fn
            rel = fn if rel_dir == '.' else f'{nfc(rel_dir)}/{fn}'
            rel_stem = stem if rel_dir == '.' else f'{nfc(rel_dir)}/{stem}'
            for k in (rel, rel_stem):
                paths.add(k); paths.add(k.casefold())
            for k in (fn, stem):
                names.add(k); names.add(k.casefold())
    _index = (paths, names)
    return _index


def resolves(target):
    target = nfc(target.split('|', 1)[0].split('#', 1)[0].strip())
    if not target:
        return True  # [[#제목]] 같은 문서 내부 링크
    paths, names = file_index()
    if '/' in target:
        return target in paths or target.casefold() in paths
    return target in names or target.casefold() in names


# ---------- 파싱 ----------
def parse(text):
    text = text.replace('\r\n', '\n')
    fm, body = None, text
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end != -1:
            fm_text = text[4:end]
            body = text[end + 4:].lstrip('\n')
            fm = {}
            for m in re.finditer(r'^([A-Za-z_]+):\s*(.*)$', fm_text, flags=re.M):
                fm[m.group(1)] = m.group(2).strip()
    h1 = re.search(r'^# (.+)$', body, flags=re.M)
    sections = {}
    for m in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', body, flags=re.M | re.S):
        sections[m.group(1).strip()] = m.group(2)
    main = ''
    if h1:
        after = body[h1.end():]
        nxt = re.search(r'^## ', after, flags=re.M)
        main = after[:nxt.start()] if nxt else after
    return fm, (h1.group(1).strip() if h1 else None), main.strip(), sections


SENT_END = re.compile(r'([가-힣A-Za-z0-9)\]"\'”’」』])([.?!])(?=["\'”’)\]」』]*(\s|$))')
def sentences(main):
    """종결 부호 기준 문장 끝 목록: (부호 앞 글자, 위치). 목록 줄과 인용 블록은 뺀다."""
    lines = [l for l in main.split('\n') if l.strip() and not re.match(r'\s*([-*>]|\d+\.)\s', l)]
    txt = ' '.join(lines)
    out = []
    for m in SENT_END.finditer(txt):
        prev = m.group(1)
        before = txt[max(0, m.start() - 3):m.start() + 1]
        if re.search(r'(^|[^가-힣])(p|pp|cf|vs|ed|eds|vol|ch|no|Mr|Dr|St|e\.g|i\.e)$', txt[max(0, m.start() - 4):m.start() + 1]):
            continue
        if prev.isdigit() and re.search(r'§\s*\d+$|\d$', before) and m.group(2) == '.':
            continue  # 번호·절 표기
        out.append((prev, m.start()))
    return out, txt


QUOTE = re.compile(r'["“]([^"“”]{8,}?)["”]')
def norm_q(s):
    s = nfc(s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().casefold()


_cache = {}
def read_norm(rel):
    if rel in _cache:
        return _cache[rel]
    p = None
    cand = ROOT / rel
    if cand.is_file():
        p = cand
    else:
        parent = cand.parent
        if parent.is_dir():
            stem = nfc(cand.name)
            for f in parent.iterdir():
                if nfc(f.stem) == stem or nfc(f.name) == stem:
                    p = f; break
    txt = None
    if p:
        try:
            txt = norm_q(p.read_text(encoding='utf-8', errors='replace'))
        except OSError:
            pass
    _cache[rel] = txt
    return txt


PRIVACY = [
    (re.compile(r'(?<!\d)(19|20)\d{2}-\d{5}(?!\d)'), '학번 형태'),
    (re.compile(r'\d[\d,]*\s?만\s?원'), '금액'),
    (re.compile(r'\b(sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|AIza[0-9A-Za-z_-]{30,})'), 'API 키 형태'),
]


# ---------- 점검 ----------
def check_card(path):
    rel = path.relative_to(ROOT).as_posix()
    stem = nfc(path.stem)
    E, W = [], []
    text = path.read_text(encoding='utf-8', errors='replace')
    fm, h1, main, sec = parse(text)

    if fm is None:
        return dict(file=rel, id=None, errors=['E-fm: frontmatter가 없음'], warnings=[])
    cid = fm.get('id', '')
    for k in REQUIRED:
        if k not in fm or fm[k] == '':
            E.append(f'E-fm: {k} 필드가 없음')
    if not (fm.get('group') or fm.get('candidate')):
        E.append('E-fm: group 필드가 없음')
    if fm.get('type') and fm['type'] != '영구':
        E.append(f"E-fm: type 값 '{fm['type']}'")
    if fm.get('voice') and fm['voice'] not in VOICES:
        E.append(f"E-fm: voice 값 '{fm['voice']}'")
    if fm.get('status') and fm['status'] not in STATUSES:
        E.append(f"E-fm: status 값 '{fm['status']}'")
    if fm.get('created') and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', fm['created']):
        E.append(f"E-fm: created 값 '{fm['created']}'")
    if fm.get('verify') and fm['verify'] not in VERIFY:
        E.append(f"E-fm: verify 값 '{fm['verify']}'")
    if cid and not stem.startswith(cid + ' '):
        E.append(f"E-id: 파일명 접두어와 id '{cid}'가 다름")
    if h1 is None:
        E.append('E-h1: H1 제목이 없음')
    elif nfc(h1) != stem:
        E.append('E-h1: H1과 파일명이 다름')

    for m in re.finditer(r'!?\[\[([^\]]+)\]\]', text):
        if not resolves(m.group(1)):
            E.append(f'E-link: [[{m.group(1)}]] 대상 없음')

    src = sec.get('출처', '').strip()
    if not src:
        E.append('E-출처: 출처 절이 없거나 비어 있음')

    # 본문 길이와 문체
    ends, flat = sentences(main)
    n = len(ends)
    if n < 3 or n > 8:
        W.append(f'W-길이: 본문 {n}문장(기준 3~8)')
    bad_end = [flat[max(0, i - 8):i + 2] for c, i in ends if re.match(r'[가-힣]', c) and c not in ENDINGS]
    if bad_end:
        W.append(f"W-종결: 종결어미가 아닌 끝 {len(bad_end)}곳 (예: '…{bad_end[0]}')")
    title_body = (h1 or '') + '\n' + main
    if '—' in title_body:
        W.append('W-엠대시: 제목이나 본문에 엠대시')
    m = re.search(r'\S+[이가] 아니라 ', title_body)
    if m:
        W.append(f"W-아니라: 'A가 아니라 B' 구문 ('{m.group(0).strip()}')")
    if re.search(r'Claude[가는의]', main):
        W.append('W-대화서술: 본문에 Claude 발화 경과 서술')

    # 연결 절
    links_sec = sec.get('연결', '')
    link_lines = [l for l in links_sec.split('\n') if '[[' in l]
    if len(link_lines) < 2:
        W.append(f'W-연결수: 연결 절 링크 {len(link_lines)}개')
    no_reason = [l for l in link_lines
                 if not re.match(r'- (상위|다음|가지):', l.strip())
                 and re.fullmatch(r'-\s*\[\[[^\]]+\]\]\s*[:：]?\s*', l.strip())]
    if no_reason:
        W.append(f'W-연결근거: 근거 없는 링크 {len(no_reason)}개')

    # voice 정합
    if fm.get('voice') == '영진' and '_원자료/' not in src and 'Notion' not in src and 'notion' not in src:
        W.append('W-voice: 영진 카드인데 출처에 원자료(대화·Notion)가 없음')

    # 출처 해석 가능성
    raw_links = re.findall(r'\[\[(_원자료/[^\]|#]+)', src)
    lit_links = re.findall(r'\[\[(@[^\]|#]+)', src)
    if src and not raw_links and not lit_links and 'notion' not in src.casefold():
        W.append('W-출처형식: 문헌 노트·원자료·Notion 어느 것으로도 해석되지 않음')
    if src and not raw_links and 'notion' in src.casefold():
        W.append('W-출처Notion: 로컬 원자료 링크 없이 Notion 표기만 있음')

    # 인용 대조
    # 원어(라틴 문자 위주) 인용은 문헌 노트·원자료 모두와, 한국어 인용은 원자료와만 대조한다.
    # 한국어 인용은 대개 영어 원문의 번역이라 문헌 노트와 글자 대조가 되지 않는다.
    quotes = [q for q in QUOTE.findall(main) if re.search(r'[A-Za-z가-힣]{3}', q)]
    latin = lambda q: len(re.findall(r'[A-Za-z]', q)) >= len(re.findall(r'[가-힣]', q))
    if quotes:
        raw_hay = [h for h in (read_norm(r.strip()) for r in raw_links) if h]
        lit_hay = [h for h in (read_norm('문헌/' + l.strip()) for l in lit_links) if h]
        hay = raw_hay + lit_hay
        if hay:
            miss = [q for q in quotes
                    if not any(norm_q(q) in h for h in (hay if latin(q) else raw_hay))
                    and (latin(q) or raw_hay)]
            if miss:
                W.append(f"W-인용: 출처에서 찾지 못한 인용 {len(miss)}개 (예: \"{miss[0][:40]}\")")
        else:
            W.append(f'W-인용미확인: 인용 {len(quotes)}개, 대조할 로컬 출처 없음')

    for rx, label in PRIVACY:
        if rx.search(text):
            W.append(f'W-개인정보: {label} 문자열')

    if '\r\n' in text:
        W.append('W-줄바꿈: CRLF')
    return dict(file=rel, id=cid, voice=fm.get('voice'), cluster=fm.get('cluster'),
                status=fm.get('status'), sentences=n, errors=E, warnings=W)


def check_lit(path):
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding='utf-8', errors='replace')
    E, W = [], []
    for m in re.finditer(r'!?\[\[([^\]]+)\]\]', text):
        if not resolves(m.group(1)):
            E.append(f'E-link: [[{m.group(1)}]] 대상 없음')
    if '확인 필요' in text:
        W.append('W-서지: 확인 필요 표시')
    if '—' in text:
        W.append('W-엠대시')
    return dict(file=rel, id=None, errors=E, warnings=W)


def check_path(p):
    p = Path(p).resolve()
    try:
        rel = p.relative_to(ROOT).as_posix()
    except ValueError:
        return None
    if p.suffix != '.md' or not p.is_file() or '.excalidraw' in p.name:
        return None
    if rel.startswith('영구/'):
        return check_card(p)
    if rel.startswith('문헌/'):
        return check_lit(p)
    return None


# ---------- 실행 ----------
def code(msg):
    return msg.split(':', 1)[0]


def run_all():
    cards = [check_path(p) for p in sorted((ROOT / '영구').glob('*.md'))]
    lits = [check_path(p) for p in sorted((ROOT / '문헌').glob('*.md'))]
    cards = [c for c in cards if c]; lits = [c for c in lits if c]
    ids = collections.defaultdict(list)
    for c in cards:
        if c['id']:
            ids[c['id']].append(c['file'])
    for c in cards:
        if c['id'] and len(ids[c['id']]) > 1:
            c['errors'].append(f"E-id중복: {', '.join(f for f in ids[c['id']] if f != c['file'])}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / 'lint.json', 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'cards': cards, 'literature': lits}, f, ensure_ascii=False, indent=0)
    write_summary(cards, lits)
    ne = sum(1 for c in cards + lits if c['errors'])
    print(f'카드 {len(cards)}장, 문헌 노트 {len(lits)}편 점검. 오류가 있는 파일 {ne}개.')
    print(f'→ {(OUT_DIR / "lint.json").relative_to(ROOT).as_posix()}, {(OUT_DIR / "01 lint 요약.md").relative_to(ROOT).as_posix()}')


def write_summary(cards, lits):
    from datetime import date
    ec, wc = collections.Counter(), collections.Counter()
    ec_files, wc_files = collections.defaultdict(list), collections.defaultdict(list)
    for c in cards:
        for m in set(map(code, c['errors'])):
            ec[m] += 1; ec_files[m].append(c['id'] or c['file'])
        for m in set(map(code, c['warnings'])):
            wc[m] += 1; wc_files[m].append(c['id'] or c['file'])
    by_voice = collections.Counter(c.get('voice') for c in cards)
    clean = sum(1 for c in cards if not c['errors'] and not c['warnings'])
    no_err = sum(1 for c in cards if not c['errors'])
    lit_err = sum(1 for c in lits if c['errors'])
    lit_bib = sum(1 for c in lits if any(w.startswith('W-서지') for w in c['warnings']))
    L = ['---', 'type: 작업', f'updated: {date.today().isoformat()}', '---',
         '# lint 요약', '',
         f'`_작업/스크립트/lint.py`가 만든 요약입니다. 카드별 상세는 `_작업/검증/lint.json`에 있습니다. 카드는 고치지 않았습니다.', '',
         f'- 카드 {len(cards)}장 (문헌 {by_voice["문헌"]}, 종합 {by_voice["종합"]}, 영진 {by_voice["영진"]})',
         f'- 오류 없는 카드 {no_err}장, 오류·경고 모두 없는 카드 {clean}장',
         f'- 문헌 노트 {len(lits)}편: 끊긴 링크가 있는 노트 {lit_err}편, 서지 확인 필요 {lit_bib}편', '',
         '## 오류 (형식이 깨짐)', '', '| 항목 | 카드 수 | 예 |', '|---|---|---|']
    for k, v in ec.most_common():
        L.append(f'| {k} | {v} | {", ".join(ec_files[k][:8])} |')
    L += ['', '## 경고 (지침 위반 의심)', '', '| 항목 | 카드 수 | 예 |', '|---|---|---|']
    for k, v in wc.most_common():
        L.append(f'| {k} | {v} | {", ".join(wc_files[k][:8])} |')
    dist = collections.Counter(min(c.get('sentences', 0), 15) for c in cards)
    L += ['', '## 본문 문장 수 분포 (종결 부호 기준 추정)', '',
          ' · '.join(f'{k}{"+" if k == 15 else ""}문장 {dist[k]}' for k in sorted(dist)), '']
    with open(OUT_DIR / '01 lint 요약.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L))


def run_files(files):
    worst = 0
    for f in files:
        r = check_path(f)
        if not r:
            continue
        for m in r['errors'] + r['warnings']:
            print(f"{r['file']}: {m}")
        if r['errors']:
            worst = 1
    return worst


def run_hook():
    try:
        data = json.loads(sys.stdin.buffer.read().decode('utf-8', errors='replace'))
    except Exception:
        return 0
    fp = (data.get('tool_input') or {}).get('file_path')
    if not fp:
        return 0
    r = check_path(fp)
    if not r or not r['errors']:
        return 0
    sys.stderr.write(f"lint: {r['file']}\n" + '\n'.join(r['errors']) +
                     '\n위 형식 오류를 고치세요(지침: _작업/작성 지침.md, _작업/그룹 작업 지침.md §3).\n')
    return 2


if __name__ == '__main__':
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding='utf-8')
        except Exception:
            pass
    a = sys.argv[1:]
    if '--hook' in a:
        sys.exit(run_hook())
    if '--file' in a:
        sys.exit(run_files(a[a.index('--file') + 1:]))
    run_all()
