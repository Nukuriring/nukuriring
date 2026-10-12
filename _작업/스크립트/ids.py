# 사용법: python3 _작업/스크립트/ids.py <보관함> <묶음코드 또는 번호 접두사> ...
# 묶음 코드(예: NP2)이면 그 묶음의 카드를, 숫자로 시작하면 해당 최상위 번호 줄기의 카드를 `번호<TAB>voice<TAB>제목` 형식으로 번호 순서대로 출력한다.
import json, os, re, sys
V = sys.argv[1]
mp = json.load(open(os.path.join(V, '_작업', '번호표.json'), encoding='utf-8'))
def segs(i): return re.findall(r'\d+|[a-z]+', i)
def key(i): return [(0, int(s), '') if s.isdigit() else (1, 0, s) for s in segs(i)]
for q in sys.argv[2:]:
    for i in sorted(mp, key=key):
        d = mp[i]
        if (q[0].isdigit() and segs(i)[0] == q) or (not q[0].isdigit() and d['group'] == q):
            print(f"{i}\t{d['voice']}\t{d['title']}")
