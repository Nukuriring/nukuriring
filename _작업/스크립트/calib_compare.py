# 사용법:
#   py -3 _작업/스크립트/calib_compare.py . agree <폴더A> <폴더B>
#       두 판정 폴더(예: _작업/검증/보정/sonnet, …/opus)의 카드 판정을 맞대어 일치율과 엇갈린 카드를 출력한다.
#   py -3 _작업/스크립트/calib_compare.py . planted <정답표.json> <판정 폴더>…
#       오류를 넣은 시험 카드의 정답표와 판정 폴더를 대조해 유형별 탐지율과 대조군 오탐을 출력한다.
# 출력은 화면과 `--out <파일>`(선택)에 쓴다. 카드는 고치지 않는다.
import json, os, sys, collections

V = sys.argv[1]
mode = sys.argv[2]
args = sys.argv[3:]
out_path = None
if '--out' in args:
    i = args.index('--out'); out_path = args[i + 1]; args = args[:i] + args[i + 2:]
SEVERITY = {'지지됨': 0, '판단불가': 1, '부분': 2, '원문없음': 3, '모순': 4}


def load(d):
    d = os.path.join(V, d) if not os.path.isabs(d) else d
    res = {}
    for f in sorted(os.listdir(d)):
        if f.endswith('.json'):
            try:
                j = json.load(open(os.path.join(d, f), encoding='utf-8'))
                res[str(j.get('id', f[:-5]))] = j
            except ValueError:
                res[f[:-5]] = None
    return res


L = []
if mode == 'agree':
    A, B = load(args[0]), load(args[1])
    na, nb = os.path.basename(args[0].rstrip('/\\')), os.path.basename(args[1].rstrip('/\\'))
    ids = sorted(set(A) | set(B))
    both = [i for i in ids if A.get(i) and B.get(i)]
    same = [i for i in both if A[i]['verdict'] == B[i]['verdict']]
    L.append(f'{na} {sum(1 for i in A if A[i])}장, {nb} {sum(1 for i in B if B[i])}장, 둘 다 {len(both)}장, 카드 판정 일치 {len(same)}장')
    m = collections.Counter((A[i]['verdict'], B[i]['verdict']) for i in both)
    L.append('')
    L.append(f'| {na} \\ {nb} | ' + ' | '.join(SEVERITY) + ' |')
    L.append('|---|' + '---|' * len(SEVERITY))
    for a in SEVERITY:
        L.append(f'| {a} | ' + ' | '.join(str(m[(a, b)] or '') for b in SEVERITY) + ' |')
    for name, X in ((na, A), (nb, B)):
        c = collections.Counter(X[i]['verdict'] for i in X if X[i])
        L.append(f'- {name}: ' + ' · '.join(f'{v} {c[v]}' for v in SEVERITY))
    L.append('')
    L.append('엇갈린 카드: ' + ', '.join(f'{i}({A[i]["verdict"]}/{B[i]["verdict"]})' for i in both if i not in same))
    missing = [i for i in ids if not (A.get(i) and B.get(i))]
    if missing:
        L.append('한쪽이 없거나 읽기 실패: ' + ', '.join(missing))

elif mode == 'planted':
    key = json.load(open(args[0], encoding='utf-8'))
    for d in args[1:]:
        R = load(d)
        name = os.path.basename(d.rstrip('/\\'))
        by_type = collections.defaultdict(lambda: [0, 0, 0])  # 정확, 다른 비지지 판정으로라도 잡음, 전체
        fp, ctrl, rows = 0, 0, []
        for k in key:
            r = R.get(k['id'])
            v = r['verdict'] if r else '(없음)'
            if k['type'] == '대조군':
                ctrl += 1
                if v != '지지됨':
                    fp += 1
                rows.append(f"  {k['id']:>7} 대조군 → {v}")
                continue
            exp = {'모순': '모순', '원문에 없음': '원문없음', '부분 지지': '부분'}.get(k['expected'], k['expected'])
            # 바꾼 문장을 판정자가 지지됨이 아닌 명제로 잡았는지: 바꾼 문장의 일부가 그 명제 text에 들어 있는가
            hit_claim = None
            if r:
                frag = k['mutated'][:25]
                for c in r.get('claims', []):
                    t = c.get('text', '')
                    if c.get('label') not in ('지지됨', '연결') and (frag[:12] in t or t[:12] in k['mutated']):
                        hit_claim = c.get('label'); break
            t = by_type[k['type']]
            t[2] += 1
            if v == exp:
                t[0] += 1
            if v not in ('지지됨', '판단불가', '(없음)'):
                t[1] += 1
            rows.append(f"  {k['id']:>7} {k['type']} 기대 {exp} → 카드 {v}, 해당 명제 {hit_claim or '못 짚음'}")
        L.append(f'## {name}')
        tot = [sum(x[i] for x in by_type.values()) for i in range(3)]
        L.append(f'오류 카드 {tot[2]}장: 기대 판정과 정확히 일치 {tot[0]}, 지지됨이 아닌 판정으로 잡음 {tot[1]}. 대조군 {ctrl}장 중 지지됨이 아닌 판정 {fp}')
        for ty, (a, b, n) in sorted(by_type.items()):
            L.append(f'- {ty}: 일치 {a}/{n}, 잡음 {b}/{n}')
        L += rows
        L.append('')

text = '\n'.join(L)
print(text)
if out_path:
    open(os.path.join(V, out_path), 'w', encoding='utf-8', newline='\n').write(text + '\n')
