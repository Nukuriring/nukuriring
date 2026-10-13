# 사용법: python3 _작업/스크립트/compress_apply.py . [--dry-run]
# 길이 처리 초안(`_작업/대기열/판정페이지/items.json`의 kind len) 가운데 권고나 결정이 '압축'인 카드의
# 본문(H1 다음부터 첫 '## ' 절 앞까지)을 초안의 '### 압축안' 문단으로 바꾼다. 다른 절과 frontmatter는 건드리지 않는다.
# 결정 파일(`--decisions <폴더>`, 판정 페이지 db에서 내려받은 JSON)이 있으면 그 결정이 권고보다 앞선다.
# status가 검토됨·다시씀인 카드는 건너뛴다. 결과는 `_작업/대기열/반영 기록.md`에 덧붙인다.
import glob, json, os, re, sys
from datetime import date

V = sys.argv[1]
DRY = '--dry-run' in sys.argv
dec = {}
if '--decisions' in sys.argv:
    for f in glob.glob(os.path.join(sys.argv[sys.argv.index('--decisions') + 1], '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        dec[os.path.basename(f)[:-5]] = d.get('choice') or ''
items = json.load(open(os.path.join(V, '_작업', '대기열', '판정페이지', 'items.json'), encoding='utf-8'))
files = {os.path.basename(f).split(' ')[0]: f for f in glob.glob(os.path.join(V, '영구', '*.md'))}
done, skip = [], []
for it in items:
    if it['kind'] != 'len':
        continue
    choice = dec.get(it['key']) or it['rec']
    if choice != '압축':
        continue
    m = re.search(r'### 압축안\s*\n(.*?)(?=\n- |\n###|\Z)', it['body'], re.S)
    new = m.group(1).strip() if m else ''
    p = files.get(it['id'])
    if not new or not p:
        skip.append((it['id'], '압축안 또는 카드 없음')); continue
    t = open(p, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in t[:300] else '\n'
    t = t.replace('\r\n', '\n')
    if re.search(r'^status:\s*(검토됨|다시씀)', t, re.M):
        skip.append((it['id'], 'status 잠금')); continue
    h = re.search(r'^# .+$', t, re.M)
    sec = t.find('\n## ', h.end())
    if sec < 0:
        skip.append((it['id'], '절 없음')); continue
    out = t[:h.end()] + '\n\n' + new + '\n' + t[sec:]
    if not DRY:
        open(p, 'w', encoding='utf-8', newline='').write(out.replace('\n', nl))
    done.append(it['id'])
print(('(시험) ' if DRY else '') + f'압축 반영 {len(done)}장, 건너뜀 {len(skip)}장')
for s in skip:
    print('  건너뜀', *s)
if not DRY:
    log = os.path.join(V, '_작업', '대기열', '반영 기록.md')
    head = '' if os.path.exists(log) else '---\ntype: 작업\n---\n# 대기열 반영 기록\n'
    with open(log, 'a', encoding='utf-8', newline='\n') as w:
        w.write(head + f'\n## {date.today().isoformat()} 압축 {len(done)}장\n' + ', '.join(done) + '\n')
