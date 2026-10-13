# 사용법: py -3 _작업/스크립트/notion_map.py . [카드 번호…]
# 카드 `## 출처` 절의 Notion 표기(URL, 「제목」, 경로, 맨 제목)를 `_원자료/notion/` 내보내기 파일로 해석해
# `_작업/검증/notion_map.json`을 쓴다. 검증자는 이 표로 원자료 파일을 찾는다. 카드는 고치지 않는다.
# 카드 번호를 주면 그 카드만 해석해 화면에 출력하고 파일은 쓰지 않는다.
import json, os, re, sys, unicodedata, collections
from datetime import date

V = sys.argv[1]
ONLY = set(sys.argv[2:])
EXPORT = '_원자료/notion/Export-c8124db7-875f-40d8-b724-67e0c0e3200e'
HEX = re.compile(r'([0-9a-f]{32})')


def nfc(s):
    return unicodedata.normalize('NFC', s)


def norm(s):
    s = nfc(s).replace('\xad', '').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    # 내보내기 파일명은 : ? / 따옴표 같은 문장부호를 빼거나 바꾸므로 글자와 숫자만 남겨 비교한다
    return re.sub(r'[^0-9a-z가-힣ㄱ-ㅎα-ωά-ώ]+', '', s.casefold())


# ---------- 내보내기 색인 ----------
by_id = {}                      # hex → 상대 경로
by_title = collections.defaultdict(list)   # 정규화 제목 → [상대 경로]
records = []                    # (정규화 제목, 정규화 상위 폴더 목록, 상대 경로)
root = os.path.join(V, EXPORT)
for dp, dns, fns in os.walk(root):
    rel_dir = nfc(os.path.relpath(dp, V).replace('\\', '/'))
    parents = [norm(p) for p in nfc(os.path.relpath(dp, root).replace('\\', '/')).split('/') if p != '.']
    for fn in fns:
        fn = nfc(fn)
        m = re.match(r'(.*) ([0-9a-f]{32})(_all)?\.(md|csv)$', fn)
        if not m or m.group(3):
            continue
        rel = f'{rel_dir}/{fn}'
        by_id[m.group(2)] = rel
        t = norm(m.group(1))
        by_title[t].append(rel)
        records.append((t, parents, rel))


def pick(cands, context):
    """제목이 같은 후보가 여럿이면 줄의 나머지 말에 상위 폴더 이름이 나오는 후보를 고른다."""
    if len(cands) <= 1:
        return cands
    ctx = norm(context)
    scored = []
    for rel in cands:
        folders = [norm(p) for p in rel[len(EXPORT) + 1:].split('/')[:-1]]
        scored.append((sum(1 for f in folders if f and f in ctx), rel))
    best = max(s for s, _ in scored)
    top = [r for s, r in scored if s == best]
    return top


def by_name(title, context):
    t = norm(title)
    if not t:
        return [], ''
    if t in by_title:
        return pick(by_title[t], context), 'title'
    # 내보내기 파일명은 긴 제목을 잘라 둔다. 카드가 전체 제목을 적었거나 잘린 제목을 적은 경우
    pre = [rel for tt, _, rel in records if len(tt) >= 8 and (t.startswith(tt) or tt.startswith(t)) and len(t) >= 8]
    if pre:
        return pick(pre, context), 'prefix'
    return [], ''


def by_path(path, context):
    segs = [norm(s) for s in path.split('/') if s.strip()]
    last, ups = segs[-1], segs[:-1]
    cands = [rel for tt, parents, rel in records if tt == last and all(u in parents for u in ups)]
    if not cands:
        cands = [rel for tt, parents, rel in records if tt == last]
    if not cands:  # '3/20 Mon'처럼 제목 자체에 빗금이 든 경우
        return by_name(path, context)
    return pick(cands, context), 'path'


def lookup(key, context):
    key = re.sub(r'\s*[>›]\s*', '/', key).strip('/ ')  # 'A > B'와 'A › B'도 경로로 본다
    return by_path(key, context) if '/' in key else by_name(key, context)


def subdir(rel):
    """하위 페이지가 든 같은 이름의 폴더가 있으면 그 경로(목차 역할의 상위 페이지인 경우)."""
    d = re.sub(r' [0-9a-f]{32}\.md$', '', rel)
    return d if d != rel and os.path.isdir(os.path.join(V, d)) else None


def bare_keys(line):
    """'Notion 페이지 제목 (…)'에서 제목 후보를 긴 것부터 낸다."""
    m = re.search(r'Notion\s+(?:내보내기\s+|원자료\s+)?(?:페이지\s+|파일명:\s*)?(.+?)(?:\s+\(|\s*$|;\s|\.\s)', line)
    if not m or m.group(1).startswith(('노트', '필기 전체')):
        return []
    full = m.group(1).strip().strip('`')
    keys = [full]
    if ', ' in full:
        keys.append(full.split(', ')[0])
    return keys


def resolve_line(line):
    out = []
    ids = HEX.findall(line) if re.search(r'notion\.(com|so)/', line) else []
    for h in ids:
        out.append(dict(key=h, method='url', files=[by_id[h]] if h in by_id else []))
    if ids:
        return out
    brackets = re.findall(r'「([^」]+)」', line)
    # 「페이지」 「절 이름」처럼 여럿이면 처음 해석되는 것이 페이지이고 나머지는 절 이름이다
    first = None
    for b in brackets:
        files, how = lookup(b, line)
        if files:
            return [dict(key=b, method=how, files=files)]
        first = first or dict(key=b, method='bracket', files=[])
    if first:
        return [first]
    keys = bare_keys(line)
    for key in keys:
        # 'A와 B'처럼 두 페이지를 함께 적은 경우
        parts = [key] + [p for p in re.split(r'(?<=\S)(?:와|과| 및) (?=\S)', key) if p != key]
        found = []
        for part in parts:
            files, how = lookup(part, line)
            if files:
                found.append(dict(key=part, method=how, files=files))
                if part == key:
                    break
        if found:
            return found
    if keys:
        # 괄호 앞까지가 길면 앞부분 단어를 줄여 가며 찾되, 두 단어·여섯 글자 아래로는 줄이지 않는다
        words = keys[-1].split()
        for k in range(len(words) - 1, 1, -1):
            cand = ' '.join(words[:k])
            if len(norm(cand)) < 6:
                break
            files, how = by_name(cand, line)
            if files:
                return [dict(key=cand, method=how, files=files)]
        out.append(dict(key=keys[0], method='bare', files=[]))
    return out


# ---------- 카드 ----------
cards = {}
stat = collections.Counter()
unresolved = []
for fn in sorted(os.listdir(os.path.join(V, '영구'))):
    if not fn.endswith('.md'):
        continue
    text = open(os.path.join(V, '영구', fn), encoding='utf-8').read().replace('\r\n', '\n')
    m = re.search(r'^id:\s*(\S+)', text, flags=re.M)
    if not m:
        continue
    cid = m.group(1).strip('"\'')
    if ONLY and cid not in ONLY:
        continue
    sec = text.split('\n## 출처', 1)
    if len(sec) < 2:
        continue
    src = sec[1].split('\n## ', 1)[0]
    refs = []
    for line in src.splitlines():
        if 'notion' not in line.casefold():
            continue
        for r in resolve_line(line):
            r['line'] = line.strip('- ').strip()
            subs = [d for d in (subdir(f) for f in r['files']) if d]
            if subs:
                r['subdir'] = subs[0]
            refs.append(r)
            stat[('해석' if r['files'] else '미해석', r['method'])] += 1
            if not r['files']:
                unresolved.append((cid, r['key']))
            elif len(r['files']) > 1:
                stat[('후보 여럿', r['method'])] += 1
    if refs:
        cards[cid] = refs

if ONLY:
    print(json.dumps(cards, ensure_ascii=False, indent=1))
    sys.exit()

out = dict(updated=date.today().isoformat(), export=EXPORT,
           note='카드 번호 → Notion 표기별 해석 결과. files가 여럿이면 후보이고, 비어 있으면 제목 일부로 Glob한다.',
           cards=cards)
p = os.path.join(V, '_작업', '검증', 'notion_map.json')
json.dump(out, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
n = sum(len(v) for v in cards.values())
ok = sum(1 for v in cards.values() for r in v if r['files'])
print(f'카드 {len(cards)}장, Notion 표기 {n}건, 해석 {ok}건({ok * 100 // max(n, 1)}%)')
for k, v in sorted(stat.items()):
    print(' ', k[0], k[1], v)
print('미해석 예:', unresolved[:15])
