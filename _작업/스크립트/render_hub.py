# 사용법: python3 _작업/스크립트/render_hub.py <보관함> <구조작성 파일> ...
# `_작업/구조작성/<이름>.md`의 {번호}를 [[실제 파일명]]으로 바꿔 `구조/<이름>.md`에 쓰고, 없는 번호와 없는 [[링크]]를 보고한다.
# `_작업/색인조각/<이름>.md`도 같은 방식으로 검사한다(쓰지는 않는다).
import json, os, re, sys
V = sys.argv[1]
mp = json.load(open(os.path.join(V, '_작업', '번호표.json'), encoding='utf-8'))
names = {f[:-3] for dp, _, fs in os.walk(V) if '.git' not in dp for f in fs if f.endswith('.md')}
bad = 0
def render(s, where):
    global bad
    def L(m):
        global bad
        i = m.group(1)
        if i not in mp: bad += 1; print('UNKNOWN ID', i, where); return m.group(0)
        return f"[[{mp[i]['file']}]]"
    return re.sub(r'\{([0-9][0-9a-z]*)\}', L, s)
for p in sys.argv[2:]:
    t = open(p, encoding='utf-8').read(); out = render(t, p)
    if '/색인조각/' in p.replace(os.sep, '/'):
        target = None
    else:
        target = os.path.join(V, '구조', os.path.basename(p)); open(target, 'w', encoding='utf-8').write(out)
    for l in re.findall(r'\[\[([^\]|#]+)', out):
        l = l.strip()
        if l.startswith('_원자료/') or l in names: continue
        print('MISSING LINK', l[:80], '←', os.path.basename(p)); bad += 1
    print('OK' if not bad else 'CHECK', os.path.basename(p), '→', target or '(검사만)')
