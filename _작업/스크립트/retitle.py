# 사용법: python3 _작업/스크립트/retitle.py . [--dry-run]
# 영구 노트의 H1 제목을 고친 뒤 실행한다. H1과 파일명이 다른 카드마다 파일명을 H1로 바꾸고(git mv),
# 보관함 전체(.md·.json·.base, `_원자료/`와 `.git` 제외)에서 옛 파일명을 새 파일명으로 바꾼다.
# H1에 파일명에 쓸 수 없는 글자(\ / : * ? " < > | # ^ [ ])가 있으면 그 카드는 건너뛰고 보고한다.
# 끝나면 struct.py → render_hub.py → merge_index.py → lint.py 순서로 마무리한다.
import os, re, subprocess, sys, unicodedata

V = sys.argv[1]
DRY = '--dry-run' in sys.argv
nfc = lambda s: unicodedata.normalize('NFC', s)
ren, bad = {}, []
for fn in os.listdir(os.path.join(V, '영구')):
    if not fn.endswith('.md'):
        continue
    stem = fn[:-3]
    t = open(os.path.join(V, '영구', fn), encoding='utf-8').read()
    m = re.search(r'^# (.+?)\s*$', t, re.M)
    if not m or nfc(m.group(1)) == nfc(stem):
        continue
    new = nfc(m.group(1))
    if re.search(r'[\\/:*?"<>|#^\[\]]', new) or new.split(' ')[0] != stem.split(' ')[0]:
        bad.append((stem, new)); continue
    ren[stem] = new
for old, new in ren.items():
    print(f'{old}\n  → {new}')
for b in bad:
    print('건너뜀(쓸 수 없는 글자나 번호 불일치):', b[0], '→', b[1])
if DRY or not ren:
    print(f'{"(시험) " if DRY else ""}이름 바꿀 카드 {len(ren)}장'); sys.exit()
for old, new in ren.items():
    subprocess.run(['git', 'mv', os.path.join('영구', old + '.md'), os.path.join('영구', new + '.md')], cwd=V, check=True)
n = 0
for dp, ds, fs in os.walk(V):
    rel = os.path.relpath(dp, V)
    if rel.startswith('.git') or rel.startswith('_원자료'):
        continue
    for f in fs:
        if not f.endswith(('.md', '.json', '.base')):
            continue
        p = os.path.join(dp, f)
        s = open(p, encoding='utf-8', newline='').read()
        s2 = s
        for old, new in ren.items():
            s2 = s2.replace('[[' + old + ']]', '[[' + new + ']]').replace('[[' + old + '|', '[[' + new + '|').replace('[[' + old + '#', '[[' + new + '#').replace('"' + old + '"', '"' + new + '"')
        if s2 != s:
            open(p, 'w', encoding='utf-8', newline='').write(s2); n += 1
print(f'이름 바꾼 카드 {len(ren)}장, 링크를 고친 파일 {n}개')
