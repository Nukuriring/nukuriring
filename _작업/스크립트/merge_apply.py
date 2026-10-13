# 사용법: python3 -P _작업/스크립트/merge_apply.py . [--dry-run]
# 중복 카드 합치기(`_작업/연결/합치기/목록.json`: [{keep, drop}])를 마무리한다.
# 작업자가 남는 카드(keep)에 내용·출처·연결을 옮긴 뒤 실행한다.
# - 합쳐질 카드(drop)에 하위 번호 카드가 있으면 파일과 번호를 남기고 본문을 안내 한 줄로 바꾼다(안내 카드).
#   하위 카드가 없으면 파일을 지운다.
# - 보관함 전체(원자료 제외)의 [[drop 파일명]] 링크를 최종 남는 카드로 바꾼다. 연쇄(a→b→c)는 끝까지 따라간다.
#   안내 카드를 가리키는 '상위:'·'다음:'·'가지:' 줄은 번호 체계를 위해 그대로 둔다.
# - `_작업/구조작성/`, `_작업/색인조각/`의 {drop} 자리표시자를 {최종 카드}로 바꾼다.
# - 남는 카드 frontmatter의 aliases에 합쳐진 카드의 제목을 넣고, 자기 자신·중복 연결 줄을 정리한다.
import json, os, re, sys, glob
V = sys.argv[1]; DRY = '--dry-run' in sys.argv
L = json.load(open(os.path.join(V, '_작업/연결/합치기/목록.json'), encoding='utf-8'))
F = {os.path.basename(f).split(' ')[0]: f for f in glob.glob(os.path.join(V, '영구', '*.md'))}
name = lambda i: os.path.basename(F[i])[:-3]
nxt = {p['drop']: p['keep'] for p in L}
def final(i):
    seen = set()
    while i in nxt and i not in seen: seen.add(i); i = nxt[i]
    return i
def has_children(d):
    for j in F:
        if j != d and j.startswith(d):
            c = j[len(d)]
            if (d[-1].isdigit() and c.isalpha()) or (d[-1].isalpha() and c.isdigit()): return True
    return False
title = {}
for i in F:
    m = re.search(r'^# \S+ (.+)$', open(F[i], encoding='utf-8').read(), re.M); title[i] = m.group(1) if m else ''
drops = {p['drop'] for p in L}
stubs = {d for d in drops if has_children(d)}
dead = drops - stubs
red = {name(d): name(final(d)) for d in drops}
log = []
# 1. aliases
aliases = {}
for d in drops: aliases.setdefault(final(d), []).append(title[d])
for k, al in aliases.items():
    t = open(F[k], encoding='utf-8').read()
    fm_end = t.find('\n---', 4)
    fm = t[:fm_end]
    m = re.search(r'^aliases:\s*\[(.*)\]\s*$', fm, re.M)
    old = [a.strip().strip('"') for a in m.group(1).split('",')] if m and m.group(1).strip() else []
    new = old + [a for a in al if a not in old]
    line = 'aliases: [' + ', '.join(json.dumps(a, ensure_ascii=False) for a in new) + ']'
    fm = re.sub(r'^aliases:.*$', line, fm, flags=re.M) if m else fm + '\n' + line
    t = fm + t[fm_end:]
    if not DRY: open(F[k], 'w', encoding='utf-8').write(t)
# 2. stubs and deletions
for d in sorted(stubs):
    t = open(F[d], encoding='utf-8').read()
    fm_end = t.find('\n---', 4) + 4
    head = t[:fm_end]
    rest = t[fm_end:]
    tl = re.search(r'^# .+$', rest, re.M).group(0)
    conn = rest.split('\n## 연결', 1)[1].split('\n## ')[0] if '\n## 연결' in rest else ''
    keep_lines = [l for l in conn.split('\n') if re.match(r'- (상위|다음|가지):', l.strip())]
    src = '\n## 출처' + rest.split('\n## 출처', 1)[1] if '\n## 출처' in rest else '\n## 출처\n- 합친 카드의 출처를 따른다.\n'
    body = f"{head}\n{tl}\n\n이 카드의 내용은 [[{name(final(d))}]]에 합쳤다. 하위 카드의 번호 체계를 잇기 위해 남겨 둔 안내 카드이다.\n\n## 연결\n" + '\n'.join(keep_lines + [f'- [[{name(final(d))}]] (합침): 이 카드의 내용을 옮긴 카드이다.']) + '\n' + src
    if not DRY: open(F[d], 'w', encoding='utf-8').write(body)
    log.append(f'안내 카드: {d} → {final(d)}')
for d in sorted(dead):
    if not DRY: os.remove(F[d])
    log.append(f'삭제: {d} → {final(d)}')
# 3. redirect links
changed = 0
stubnames = {name(d) for d in stubs}
for dp, ds, fs in os.walk(V):
    if '_원자료' in dp or '.git' in dp or '.obsidian' in dp: continue
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(dp, f)
        if not os.path.exists(p): continue
        t = open(p, encoding='utf-8').read(); o = t
        out = []
        for line in t.split('\n'):
            structural = re.match(r'\s*- (상위|다음|가지):', line)
            for a, b in red.items():
                if structural and a in stubnames: continue
                if f[:-3] == a: continue
                line = line.replace('[[' + a + ']]', '[[' + b + ']]').replace('[[' + a + '|', '[[' + b + '|')
            out.append(line)
        t = '\n'.join(out)
        if '구조작성' in dp or '색인조각' in dp:
            for d in drops: t = t.replace('{' + d + '}', '{' + final(d) + '}')
        # 남는 카드: 자기 링크·중복 링크 줄 정리
        me = f[:-3]
        if dp.endswith('영구') and '\n## 연결' in t:
            head, rest = t.split('\n## 연결', 1)
            sec, sep, tail = rest.partition('\n## ')
            seen, lines = set(), []
            for l in sec.split('\n'):
                m = re.match(r'\s*-\s*(?:(?:상위|다음|가지):\s*)?\[\[([^\]|]+)', l)
                if m and not re.match(r'\s*- (상위|다음|가지):', l):
                    tgt = m.group(1)
                    if tgt == me or tgt in seen: continue
                    seen.add(tgt)
                lines.append(l)
            t = head + '\n## 연결' + '\n'.join(lines) + (sep + tail if sep else '')
        if t != o:
            changed += 1
            if not DRY: open(p, 'w', encoding='utf-8').write(t)
print('\n'.join(log)); print('stubs', len(stubs), 'deleted', len(dead), 'files changed', changed)
