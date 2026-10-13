# 사용법: py -3 _작업/스크립트/verify_split.py .
# 검증자가 묶음 하나의 판정을 한 파일로 쓴 `_작업/검증/판정/_묶음/<이름>.json`
# ({"model", "date", "cards": [카드 판정, …]})을 카드별 `_작업/검증/판정/<id>.json`으로 나눈다.
# 카드 판정 형식은 `카드 검증 지침.md` §6과 같다. 이미 있는 카드 파일은 덮어쓰지 않고 보고한다.
import json, os, sys

V = sys.argv[1]
SRC = os.path.join(V, '_작업', '검증', '판정', '_묶음')
DST = os.path.join(V, '_작업', '검증', '판정')
import glob
existing = {os.path.basename(f).split(' ')[0] for f in glob.glob(os.path.join(V, '영구', '*.md'))}
made, kept, bad, gone = 0, [], [], []
for f in sorted(os.listdir(SRC)) if os.path.isdir(SRC) else []:
    if not f.endswith('.json'):
        continue
    try:
        b = json.load(open(os.path.join(SRC, f), encoding='utf-8'))
    except ValueError as e:
        bad.append(f'{f}: {e}'); continue
    for c in b.get('cards', []):
        cid = str(c.get('id', ''))
        if not cid:
            bad.append(f'{f}: id 없는 항목'); continue
        c.setdefault('model', b.get('model'))
        c.setdefault('date', b.get('date'))
        if cid not in existing:
            gone.append(cid); continue  # 합치기·삭제로 없어진 카드의 옛 판정은 되살리지 않는다
        p = os.path.join(DST, f'{cid}.json')
        if os.path.exists(p):
            kept.append(cid); continue
        json.dump(c, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
        made += 1
print(f'(없어진 카드 {len(gone)}장 건너뜀) ' + f'카드 판정 파일 {made}개 생성, 이미 있어 둔 것 {len(kept)}개' + (f' ({", ".join(kept[:10])})' if kept else ''))
for x in bad:
    print('오류:', x)
