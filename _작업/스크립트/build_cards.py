import os, re, sys, json
V = sys.argv[1]
H = os.path.join(V, '_작업', '후보')
files = {'A': 'A_트래비스_침묵.md', 'B': 'B_트래비스_맥도웰_논쟁.md', 'C': 'C_맥도웰_개념주의.md', 'D': 'D_오스틴_지식과_지각.md'}
cands = {}
for g, fn in files.items():
    t = open(os.path.join(H, fn), encoding='utf-8').read()
    parts = re.split(r'^## (?:[A-D]-)?C(\d+) ', t, flags=re.M)
    for i in range(1, len(parts), 2):
        num, chunk = parts[i], parts[i+1]
        title = chunk.split('\n', 1)[0].strip()
        rest = chunk.split('\n', 1)[1] if '\n' in chunk else ''
        def field(name):
            m = re.search(r'^- ' + name + r':\s*(.*)$', rest, flags=re.M)
            return m.group(1).strip() if m else ''
        bm = re.search(r'^- 본문:\s*\n(.*)', rest, flags=re.M | re.S)
        body = bm.group(1) if bm else ''
        body = re.split(r'^---\s*$|^# ', body, flags=re.M)[0]
        body = '\n'.join(l.strip() for l in body.strip().split('\n'))
        cands[f'{g}-C{int(num):02d}'] = dict(title=title, voice=field('voice'), basis=field('근거'), rel=field('관계 제안'), body=body)
MAP = """
1 D-C01|1a D-C02|1a1 D-C03|1a2 D-C04|1a3 D-C05|1a4 D-C06|1a5 D-C07|1a6 D-C08|1b D-C09|1c D-C10|1c1 D-C11|1c2 D-C12|1c3 D-C13|1d D-C14|1d1 D-C15|1e D-C16
2 A-C01|2a A-C02|2a1 A-C03|2a2 A-C04|2b A-C05|2c A-C06|2c1 A-C07|2c1a A-C08|2c2 A-C09|2d A-C14
3 C-C01|3a C-C02|3a1 C-C03|3b C-C04|3c C-C05|3d C-C06|3d1 C-C07|3d2 C-C08|3d3 B-C01|3e C-C09|3e1 C-C10|3e2 C-C11|3e3 C-C12|3e4 C-C13|3e5 C-C14|3f C-C15|3f1 C-C16|3f2 C-C17|3f3 C-C18|3g B-C19|3g1 B-C20|3h C-C19|3h1 C-C20|3h2 C-C21|3h3 C-C22
4 B-C07|4a B-C02|4b B-C03|4b1 B-C04|4b2 B-C08|4b3 B-C17|4c B-C05|4d B-C06|4d1 B-C16|4e B-C09|4f B-C10|4g B-C11|4g1 B-C12|4h B-C13|4h1 B-C14|4i B-C15|4j B-C18
5 A-C11|5a A-C10|5b A-C12|5b1 A-C16|5c A-C13|5c1 A-C15|5d A-C18|5e A-C17|5e1 B-C21
"""
pairs = [p.split() for line in MAP.strip().split('\n') for p in line.split('|')]
assert len(pairs) == len(cands) == len({c for _, c in pairs}), (len(pairs), len(cands))
def fname(i, title):
    s = re.sub(r'[\\/:*?"<>|#^\[\]“”‘’\'`]', '', title)
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > 70: s = s[:70].rstrip(' ,.')
    return f'{i} {s}'
ids = [i for i, _ in pairs]
info = {i: dict(cands[c], cand=c, file=fname(i, cands[c]['title'])) for i, c in pairs}
def parent(i):
    return i[:-1] if len(i) > 1 and not (i[-1].isdigit() and i[-2].isdigit()) else None
def sibling_next(i):
    last = i[-1]
    nxt = i[:-1] + (chr(ord(last) + 1) if last.isalpha() else str(int(last) + 1))
    return nxt if nxt in info else None
def children(i):
    return [j for j in ids if parent(j) == i]
cite = re.compile(r'\[\[(@[^\]]+)\]\]')
os.makedirs(os.path.join(V, '영구'), exist_ok=True)
for i in ids:
    d = info[i]
    srcs = sorted(set(cite.findall(d['basis'])))
    tagmap = {'1': '오스틴', '2': '트래비스', '3': '맥도웰', '4': '트래비스-맥도웰-논쟁', '5': '욕구'}
    fm = ['---', f'id: {i}', 'type: 영구', f"voice: {d['voice'].split()[0] if d['voice'] else ''}", 'status: 초안',
          f"tags: [지각의철학, {tagmap[i[0]]}]", 'sources: [' + ', '.join(f'"[[{s}]]"' for s in srcs) + ']',
          'cluster: 지각의 철학', f"candidate: {d['cand']}", 'created: 2026-10-09', '---']
    links = []
    p = parent(i)
    if p: links.append(f"- 상위: [[{info[p]['file']}]]")
    n = sibling_next(i)
    if n: links.append(f"- 다음: [[{info[n]['file']}]]")
    for ch in children(i): links.append(f"- 가지: [[{info[ch]['file']}]]")
    basis = [b.strip() for b in re.split(r';\s*(?=\[|\()', d['basis']) if b.strip()]
    out = fm + ['', f"# {i} {d['title']}", '', d['body'], '', '## 연결'] + links + \
          ['<!-- 관계 제안(통합 시 링크로 바꾸고 이 주석을 지움): ' + d['rel'].replace('-->', '->') + ' -->', '', '## 출처'] + [f'- {b}' for b in basis] + ['']
    open(os.path.join(V, '영구', d['file'] + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
rows = ['---', 'type: 작업', 'updated: 2026-10-09', '---', '# 번호표 (지각의 철학 시범)', '', '| 번호 | 후보 | voice | 파일 |', '|---|---|---|---|']
for i in ids:
    d = info[i]; rows.append(f"| {i} | {d['cand']} | {d['voice']} | [[{d['file']}]] |")
open(os.path.join(V, '_작업', '번호표.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(rows) + '\n')
json.dump({i: dict(file=info[i]['file'], cand=info[i]['cand']) for i in ids}, open(os.path.join(V, '_작업', '번호표.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=0)
print(len(ids), 'cards written')
