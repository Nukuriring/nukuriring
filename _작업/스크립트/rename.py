import os, re, json, sys
V = sys.argv[1]
mp = json.load(open(os.path.join(V, '_작업', '번호표.json'), encoding='utf-8'))
def fname(i, title):
    s = re.sub(r'[\\/:*?"<>|#^\[\]“”‘’\'`]', '', title)
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > 80: s = s[:80].rstrip(' ,.')
    return f'{i} {s}'
old2new = {}; cand2new = {}; titles = {}
for i, d in mp.items():
    old = d['file']; p = os.path.join(V, '영구', old + '.md')
    t = open(p, encoding='utf-8').read()
    m = re.search(r'^# (\S+) (.+)$', t, flags=re.M)
    assert m and m.group(1) == i, (i, old)
    new = fname(i, m.group(2).strip()); titles[i] = m.group(2).strip()
    old2new[old] = new; cand2new[d['cand']] = new
    if new != old:
        np_ = os.path.join(V, '영구', new + '.md'); assert not os.path.exists(np_), np_
        os.rename(p, np_)
changed = 0; dangling = set()
allnames = set(old2new.values())
for dp, dirs, fs in os.walk(V):
    if '_원자료' in dp or '.obsidian' in dp: continue
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(dp, f); t = open(p, encoding='utf-8').read(); o = t
        for old, new in sorted(old2new.items(), key=lambda x: -len(x[0])):
            t = t.replace('[[' + old + ']]', '[[' + new + ']]').replace('[[' + old + '|', '[[' + new + '|')
        t = re.sub(r'후보\s*([A-D])-C(\d+)', lambda m: '[[' + cand2new.get(f'{m.group(1)}-C{int(m.group(2)):02d}', m.group(0)) + ']]', t)
        if t != o: open(p, 'w', encoding='utf-8', newline='\n').write(t); changed += 1
for i in mp: mp[i]['file'] = old2new[mp[i]['file']]; mp[i]['title'] = titles[i]
json.dump(mp, open(os.path.join(V, '_작업', '번호표.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
rows = ['---', 'type: 작업', 'updated: 2026-10-09', '---', '# 번호표 (지각의 철학 시범)', '', '| 번호 | 후보 | 파일 |', '|---|---|---|']
rows += [f"| {i} | {d['cand']} | [[{d['file']}]] |" for i, d in mp.items()]
open(os.path.join(V, '_작업', '번호표.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(rows) + '\n')
# link check
names = {f[:-3] for dp, _, fs in os.walk(V) for f in fs if f.endswith('.md')}
paths = {os.path.relpath(os.path.join(dp, f), V)[:-3].replace(os.sep, '/') for dp, _, fs in os.walk(V) for f in fs if f.endswith('.md')}
for dp, _, fs in os.walk(V):
    if '_원자료' in dp or '.obsidian' in dp: continue
    for f in fs:
        if not f.endswith('.md'): continue
        for l in re.findall(r'\[\[([^\]|#]+)', open(os.path.join(dp, f), encoding='utf-8').read()):
            l = l.strip()
            if l not in names and l not in paths and l.replace('\\', '') not in names: dangling.add((f, l))
print('files changed', changed); print('dangling', len(dangling))
for x in sorted(dangling)[:40]: print(x)
