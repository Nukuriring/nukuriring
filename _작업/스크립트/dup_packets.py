# 사용법: python3 _작업/스크립트/dup_packets.py . [묶음당 쌍 수=50]
# `_작업/정리 후보.md`의 항목에서 중복 판정할 카드 쌍을 뽑고, 쌍과 카드 본문을 묶음 파일로 꾸린다.
# 결과: `_작업/검색/꾸러미/dN.md`(작업자가 읽을 파일), `_작업/검색/쌍.json`
# - 항목의 첫 콜론 앞에 나온 카드들끼리 모든 쌍을 만든다. '길이 점검' 항목은 뺀다.
# - 카드 본문은 frontmatter와 연결 절을 빼고 제목·voice·group·본문만 싣는다.
import re, itertools, glob, os, json, sys
V = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 50
t = open(os.path.join(V, '_작업', '정리 후보.md'), encoding='utf-8').read()
files = {os.path.basename(f).split(' ')[0]: f for f in glob.glob(os.path.join(V, '영구', '*.md'))}
pairs, sec = {}, ''
for l in t.split('\n'):
    if l.startswith('## '): sec = l[3:].strip('[] '); continue
    if not l.startswith('- ') or '길이' in l[:200]: continue
    head = re.split(r'\]\]\s*:', l, maxsplit=1)[0] + ']]'
    ids = [i for i in dict.fromkeys(re.findall(r'\[\[(\S+?) ', head)) if i in files]
    for a, b in itertools.combinations(ids, 2):
        k = tuple(sorted((a, b)))
        pairs.setdefault(k, sec)
def card(i):
    x = open(files[i], encoding='utf-8').read()
    fm = x.split('---', 2)[1]
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', fm, re.M) or [None, ''])[1].strip()
    body = x.split('---', 2)[2]
    title = re.search(r'^# (.+)$', body, re.M).group(1)
    body = re.sub(r'^# .+$', '', body, count=1, flags=re.M).split('\n## ')[0].strip()
    return f'### {title}\n(voice {g("voice")} · group {g("group")} · cluster {g("cluster")})\n\n{body}\n'
order = sorted(pairs, key=lambda k: (pairs[k], k))
batches = [order[i:i + N] for i in range(0, len(order), N)]
out = []
for bi, b in enumerate(batches, 1):
    ids = list(dict.fromkeys(i for p in b for i in p))
    L = [f'# 중복 판정 꾸러미 d{bi}', '', f'쌍 {len(b)}개, 카드 {len(ids)}장. 아래 쌍 목록의 두 카드를 카드 본문 절에서 찾아 판정합니다.', '', '## 쌍 목록', '']
    L += [f'{n}. {a} · {c}' for n, (a, c) in enumerate(b, 1)]
    L += ['', '## 카드 본문', ''] + [card(i) for i in ids]
    open(os.path.join(V, '_작업', '검색', '꾸러미', f'd{bi}.md'), 'w', encoding='utf-8').write('\n'.join(L))
    out.append({'batch': f'd{bi}', 'pairs': [list(p) for p in b], 'section': sorted({pairs[p] for p in b})})
json.dump(out, open(os.path.join(V, '_작업', '검색', '쌍.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(pairs), 'pairs', len(batches), 'batches')
for o in out[:3]: print(o['batch'], len(o['pairs']), o['section'][:3])
