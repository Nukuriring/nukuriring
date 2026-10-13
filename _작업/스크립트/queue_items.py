# 사용법: python3 _작업/스크립트/queue_items.py .
# 대기열 준비 초안(`_작업/대기열/영진 부분/Y*.md`, `분할초안/L*.md`, `서지 후보/S*.md`)을 읽어
# 판정 페이지가 쓰는 `_작업/대기열/판정페이지/items.json`을 만든다.
# 항목 key는 판정 db 문서 id로 쓴다: y_<카드 id>, l_<카드 id>, b_<문헌 노트 이름 sha1 앞 10자>.
import glob, hashlib, json, os, re, sys

V = sys.argv[1]
Q = os.path.join(V, '_작업', '대기열')
nat = lambda s: [int(t) if t.isdigit() else t for t in re.findall(r'\d+|\D+', s)]
lint = {c['id']: c for c in json.load(open(os.path.join(V, '_작업', '검증', 'lint.json'), encoding='utf-8'))['cards']}
long_now = {i for i, c in lint.items() if any(w.startswith('W-길이') for w in c['warnings'])}


def unlink(s):
    s = re.sub(r'\[\[[^\]|]+\|([^\]]+)\]\]', r'\1', s)
    return re.sub(r'\[\[([^\]]+)\]\]', r'\1', s)


def sections(path):
    t = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    parts = re.split(r'^## (?!#)', t, flags=re.M)[1:]
    for p in parts:
        head, _, body = p.partition('\n')
        body = '\n'.join(l for l in body.split('\n') if not re.match(r'\s*- \[[ x]\]', l)).strip()
        yield head.strip(), body


items = []
for f in sorted(glob.glob(os.path.join(Q, '영진 부분', 'Y*.md')), key=nat):
    for head, body in sections(f):
        m = re.match(r'\[\[([^\]|]+)\|([^\]]+)\]\]\s*·?\s*(.*)', head)
        if not m:
            continue
        cid = m.group(2).strip()
        rec = re.search(r'^- 권고:\s*\**([^\n*]+)', body, re.M)
        items.append(dict(key='y_' + cid, kind='yj', id=cid, title=m.group(1)[len(cid):].strip(), tag=m.group(3).strip(),
                          rec=(rec.group(1).strip() if rec else ''), body=unlink(body), batch=os.path.basename(f)[:-3]))
for f in sorted(glob.glob(os.path.join(Q, '분할초안', 'L*.md')), key=nat):
    for head, body in sections(f):
        m = re.match(r'\[\[([^\]|]+)\|([^\]]+)\]\]\s*(.*)', head)
        if not m:
            continue
        cid = m.group(2).strip()
        rest = m.group(3)
        rec = re.search(r'권고:\s*\**\s*([가-힣]+)', rest)
        n = re.search(r'\((\d+)문장', rest)
        items.append(dict(key='l_' + cid, kind='len', id=cid, title=m.group(1)[len(cid):].strip(),
                          tag=(n.group(1) + '문장' if n else ''), rec=(rec.group(1) if rec else ''),
                          lint=lint.get(cid, {}).get('sentences'), flagged=cid in long_now,
                          body=unlink(body), batch=os.path.basename(f)[:-3]))
for f in sorted(glob.glob(os.path.join(Q, '서지 후보', 'S*.md')), key=nat):
    for head, body in sections(f):
        m = re.match(r'\[\[([^\]|]+)\]\]', head)
        if not m:
            continue
        name = m.group(1).strip()
        high = len(re.findall(r'\|\s*높음\s*\|', body))
        items.append(dict(key='b_' + hashlib.sha1(name.encode()).hexdigest()[:10], kind='bib', id=name, title=name, tag=f'높음 {high}' if high else '',
                          rec='', body=unlink(body), batch=os.path.basename(f)[:-3]))
out = os.path.join(Q, '판정페이지')
os.makedirs(out, exist_ok=True)
json.dump(items, open(os.path.join(out, 'items.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False)
from collections import Counter
print(Counter(i['kind'] for i in items), 'dup keys', len(items) - len({i['key'] for i in items}))
print(Counter((i['kind'], i['rec']) for i in items))
