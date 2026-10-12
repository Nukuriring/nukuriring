import os, re, json, sys
V = sys.argv[1]; D = os.path.join(V, '영구')
def segs(i): return re.findall(r'\d+|[a-z]+', i)
def key(i): return [(0, int(s), '') if s.isdigit() else (1, 0, s) for s in segs(i)]
def parent(i):
    s = segs(i); return ''.join(s[:-1]) if len(s) > 1 else None
def nxt(i):
    s = segs(i)
    if len(s) < 2: return None
    l = s[-1]
    if l.isdigit(): l = str(int(l) + 1)
    else: l = l[:-1] + chr(ord(l[-1]) + 1) if l[-1] != 'z' else l + 'a'
    return ''.join(s[:-1] + [l])
cards = {}
for f in os.listdir(D):
    if not f.endswith('.md'): continue
    t = open(os.path.join(D, f), encoding='utf-8').read()
    m = re.search(r'^id:\s*(\S+)\s*$', t, flags=re.M)
    if not m or not t.startswith('---'): continue
    i = m.group(1)
    if i in cards: print('DUPLICATE ID', i, f, cards[i]['file']); continue
    fm = t.split('---')[1]
    g = lambda k: (re.search(r'^' + k + r':\s*(.*)$', fm, flags=re.M) or [None, ''])[1].strip()
    h1 = re.search(r'^# \S+ (.+)$', t, flags=re.M)
    cards[i] = dict(file=f[:-3], title=h1.group(1).strip() if h1 else '', voice=g('voice'), cluster=g('cluster'), group=g('group') or g('candidate'))
ids = sorted(cards, key=key)
kids = {}
for i in ids:
    p = parent(i)
    if p in cards: kids.setdefault(p, []).append(i)
    elif p: print('ORPHAN (parent missing)', i)
for i in ids:
    p = os.path.join(D, cards[i]['file'] + '.md'); t = open(p, encoding='utf-8').read()
    if '## 연결' not in t:
        t = t.replace('\n## 출처', '\n## 연결\n\n## 출처', 1) if '\n## 출처' in t else t + '\n## 연결\n'
    head, rest = t.split('## 연결', 1)
    m = re.match(r'(.*?)(\n## |\Z)', rest, flags=re.S)
    sec, tail = rest[:m.end(1)], rest[m.end(1):]
    lines = [l for l in sec.split('\n') if not re.match(r'- (상위|다음|가지):', l)]
    body = [l for l in lines if l.strip()]
    st = []
    pp = parent(i)
    if pp in cards: st.append(f"- 상위: [[{cards[pp]['file']}]]")
    n = nxt(i)
    if n in cards: st.append(f"- 다음: [[{cards[n]['file']}]]")
    for k in kids.get(i, []): st.append(f"- 가지: [[{cards[k]['file']}]]")
    new = head + '## 연결\n' + '\n'.join(st + body) + '\n' + tail
    if new != t: open(p, 'w', encoding='utf-8', newline='\n').write(new)
json.dump(cards, open(os.path.join(V, '_작업', '번호표.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
rows = ['---', 'type: 작업', 'updated: 2026-10-09', '---', '# 번호표', '', '영구 노트 전체 목록입니다. 스크립트가 자동으로 만듭니다.', '', '| 번호 | voice | 클러스터 | 파일 |', '|---|---|---|---|']
rows += [f"| {i} | {cards[i]['voice']} | {cards[i]['cluster']} | [[{cards[i]['file']}]] |" for i in ids]
open(os.path.join(V, '_작업', '번호표.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(rows) + '\n')
names = {f[:-3] for dp, _, fs in os.walk(V) for f in fs if f.endswith('.md')}
paths = {os.path.relpath(os.path.join(dp, f), V)[:-3].replace(os.sep, '/') for dp, _, fs in os.walk(V) for f in fs if f.endswith('.md')}
bad = []
skip_raw = not os.path.isdir(os.path.join(V, '_원자료'))  # 원자료 없는 사본(클라우드)에서는 원자료 링크를 검사하지 않는다
for d in ['영구', '문헌', '구조']:
    for f in os.listdir(os.path.join(V, d)):
        if not f.endswith('.md'): continue
        for l in re.findall(r'\[\[([^\]|#]+)', open(os.path.join(V, d, f), encoding='utf-8').read()):
            l = l.strip().rstrip('\\')
            if skip_raw and l.startswith('_원자료/'): continue
            if l and l not in names and l not in paths: bad.append((d, f[:25], l))
print('cards', len(cards), 'dangling', len(bad))
for b in bad[:60]: print('  ', b)
