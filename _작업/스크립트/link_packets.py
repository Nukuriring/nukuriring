# 사용법: python3 -P _작업/스크립트/link_packets.py . [묶음당 쌍 수=100]
# `_작업/연결/후보.json`의 쌍을 제목만 담은 판정 꾸러미 `_작업/연결/꾸러미/lN.md`로 나눈다.
import json, os, re, sys, glob
V = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 100
P = json.load(open(os.path.join(V, '_작업', '연결', '후보.json'), encoding='utf-8'))
T = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    x = open(f, encoding='utf-8').read()
    m = re.search(r'^# (\S+) (.+)$', x, re.M)
    cl = (re.search(r'^cluster:\s*(.+)$', x, re.M) or [None, ''])[1].strip()
    vo = (re.search(r'^voice:\s*(.+)$', x, re.M) or [None, ''])[1].strip()
    if m: T[m.group(1)] = (m.group(2), cl, vo)
for bi in range(0, len(P), N):
    b = P[bi:bi + N]; name = f'l{bi // N + 1}'
    L = [f'# 연결 판정 꾸러미 {name}', '', '쌍마다 두 카드의 제목(한 문장 주장), 클러스터, voice, 후보로 뽑힌 신호가 있습니다.', '']
    for n, p in enumerate(b, 1):
        ta, tb = T[p['a']], T[p['b']]
        via = '; '.join(v[:60] for v in p['via'])
        L += [f"{n}. **{p['a']}** [{ta[1]}, {ta[2]}] {ta[0]}", f"   **{p['b']}** [{tb[1]}, {tb[2]}] {tb[0]}", f"   신호: {via}", '']
    open(os.path.join(V, '_작업', '연결', '꾸러미', name + '.md'), 'w', encoding='utf-8').write('\n'.join(L))
print((len(P) + N - 1) // N, 'packets')
