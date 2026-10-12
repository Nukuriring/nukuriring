# 사용법: python3 _작업/스크립트/merge_index.py <보관함>
# `_작업/색인조각/*.md`의 `- 키워드: {번호}, {번호}` 줄을 모아 `01 색인.md`의 키워드 목록과 합치고,
# 구조 노트 목록을 `구조/` 폴더에서 다시 만든다. 같은 키워드는 카드를 합쳐 최대 4장까지 남긴다.
import glob, json, os, re, sys
V = sys.argv[1]
mp = json.load(open(os.path.join(V, '_작업', '번호표.json'), encoding='utf-8'))
file2id = {d['file']: i for i, d in mp.items()}
def segs(i): return re.findall(r'\d+|[a-z]+', i)
def key(i): return [(0, int(s), '') if s.isdigit() else (1, 0, s) for s in segs(i)]
kw = {}
def add(k, ids):
    cur = kw.setdefault(k, [])
    for i in ids:
        if i in mp and i not in cur: cur.append(i)
idx_path = os.path.join(V, '01 색인.md')
old = open(idx_path, encoding='utf-8').read()
for l in old.split('\n'):
    m = re.match(r'- (.+?): (\[\[.+)$', l)
    if m:
        add(m.group(1), [file2id[x] for x in re.findall(r'\[\[([^\]]+)\]\]', m.group(2)) if x in file2id])
bad = 0
for p in sorted(glob.glob(os.path.join(V, '_작업', '색인조각', '*.md'))):
    for l in open(p, encoding='utf-8').read().split('\n'):
        m = re.match(r'- (.+?): (.+)$', l)
        if not m: continue
        ids = re.findall(r'\{([0-9][0-9a-z]*)\}', m.group(2))
        miss = [i for i in ids if i not in mp]
        if miss: bad += 1; print('UNKNOWN ID', miss, os.path.basename(p), m.group(1))
        add(m.group(1).strip(), ids)
hubs = sorted(f[:-3] for f in os.listdir(os.path.join(V, '구조')) if f.endswith('.md'))
def sortkey(k): return re.sub(r'[^0-9A-Za-z가-힣]', '', k).lower()
rows = ['- ' + k + ': ' + ', '.join(f"[[{mp[i]['file']}]]" for i in sorted(kw[k], key=key)[:4]) for k in sorted(kw, key=sortkey) if kw[k]]
head = """---
type: 색인
updated: 2026-10-12
---
# 색인

키워드에서 진입 카드로 가는 목록입니다. 한 키워드에는 진입점이 되는 카드를 한두 장만 적고, 나머지는 그 카드의 연결을 따라갑니다. 주제 전체를 보려면 `구조/`의 구조 노트에서 시작합니다.

## 구조 노트
""" + '\n'.join(f'- [[{h}]]' for h in hubs) + '\n\n## 키워드\n'
open(idx_path, 'w', encoding='utf-8').write(head + '\n'.join(rows) + '\n')
print('keywords', len(rows), 'hubs', len(hubs), 'bad', bad)
