# 사용법: python3 -P _작업/스크립트/link_apply.py . [--dry-run] [판정 파일 ...]
# 판정 파일을 주면 그 파일만 반영한다. 주지 않으면 l*.md·m*.md 전부를 다시 읽는데, 그러면 합치기·이름 변경으로
# 정리된 옛 쌍이 다시 들어갈 수 있으므로 새 판정만 반영할 때는 파일을 지정한다(2026-10-13).
# 연결 판정(`_작업/연결/판정/l*.md`)에서 `채택`된 쌍을 두 카드의 `## 연결` 절에 넣는다.
# - 줄 형식: `- [[상대 파일명]] (관계): 근거 (제안: Claude)`
# - '관련 주제(다른 묶음)' 줄이 있으면 그 앞에, 없으면 연결 절 끝에 넣는다. 이미 링크가 있으면 넣지 않는다.
# - status가 검토됨·다시씀인 카드는 건너뛰고 보고한다.
# - `중복 의심`은 `_작업/연결/중복 의심.md`에 모은다.
import re, glob, os, sys, collections
V = sys.argv[1]; DRY = '--dry-run' in sys.argv
F = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    F[os.path.basename(f).split(' ')[0]] = f
rows = []
_only = [a for a in sys.argv[2:] if not a.startswith('--')]
for f in (_only or sorted(glob.glob(os.path.join(V, '_작업', '연결', '판정', 'l*.md')) + glob.glob(os.path.join(V, '_작업', '연결', '판정', 'm*.md')))):
    for l in open(f, encoding='utf-8'):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) >= 6 and c[0].isdigit(): rows.append((os.path.basename(f)[:-3], *c[1:6]))
add = collections.defaultdict(list); dup = []; cnt = collections.Counter()
for b, a, bb, verdict, rel, why in rows:
    cnt[verdict] += 1
    if a not in F or bb not in F: continue
    if verdict == '채택' and why:
        why = why.rstrip('.') + '.'
        rel = rel or '관련'
        add[a].append((bb, rel, why)); add[bb].append((a, rel, why))
    elif verdict in ('중복 의심', '중복'):
        dup.append((b, a, bb, why))
name = lambda i: os.path.basename(F[i])[:-3]
changed = skipped = lines = 0; locked = []
for i, items in add.items():
    t = open(F[i], encoding='utf-8').read()
    if re.search(r'^status:\s*(검토됨|다시씀)', t, re.M): locked.append(i); continue
    if '\n## 연결' not in t: skipped += 1; continue
    head, rest = t.split('\n## 연결', 1)
    sec, sep, tail = (rest.partition('\n## ') if '\n## ' in rest else (rest, '', ''))
    sl = sec.rstrip('\n').split('\n')
    new = []
    for o, rel, why in items:
        if f'[[{name(o)}]]' in t or f'[[{name(o)}|' in t: continue
        new.append(f'- [[{name(o)}]] ({rel}): {why} (제안: Claude)')
    if not new: continue
    k = next((n for n, l in enumerate(sl) if l.startswith('- 관련 주제')), len(sl))
    sl[k:k] = new; lines += len(new)
    out = head + '\n## 연결' + '\n'.join(sl) + '\n' + (('\n## ' + tail) if sep else '')
    if not out.endswith('\n'): out += '\n'
    if not DRY: open(F[i], 'w', encoding='utf-8').write(out)
    changed += 1
L = ['---', 'type: 작업', 'updated: 2026-10-13', '---', '# 중복 의심 (연결 판정에서)', '',
     '묶음이 다른데 같은 주장을 거의 같은 범위로 말한다고 판정된 쌍입니다. 합칠지는 영진 님이 정합니다.', '']
L += [f'- [[{name(a)}]] · [[{name(b)}]] ({bt}): {why}' for bt, a, b, why in dup if a in F and b in F]
if not DRY and not _only: open(os.path.join(V, '_작업', '연결', '중복 의심.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(dict(cnt), 'cards changed', changed, 'lines', lines, 'locked', locked, 'no-section', skipped, 'dup', len(dup))
