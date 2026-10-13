# 사용법: python3 _작업/스크립트/yj_verify_apply.py . [--dry-run]
# 영진 voice 카드 근거 대조 결과(`_작업/검증/영진카드_*.md`의 표)를 카드 frontmatter의
# verify, verify_date, verify_by에 옮긴다. Bases 대시보드에서 영진 카드 대기열을 보이게 하려는 것이다.
#  - 판정 '확인' → verify: 지지됨, '부분' → 부분, 'voice 변경 제안' → 부분(영진 님 판단 대상으로 남김).
#    이미 voice를 바꾼 카드('voice 부적합 → …', '영진 → …')는 지금 voice가 영진이 아니므로 건너뛴다.
#  - 같은 카드가 여러 표에 나오면 `영진카드_합치기후.md`(합치기 뒤 재대조)가 이긴다.
#  - verify_by는 `sonnet(근거대조)`, verify_date는 표 파일의 대조 날짜(합치기후는 2026-10-13, 나머지 2026-10-12).
#  - 지금 voice가 영진인 카드만, status가 검토됨·다시씀이 아닌 카드만 쓴다. 본문과 다른 필드는 건드리지 않는다.
import glob, os, re, sys

V = sys.argv[1]
DRY = '--dry-run' in sys.argv
FIELDS = ('verify', 'verify_date', 'verify_by')
files = sorted(glob.glob(os.path.join(V, '_작업', '검증', '영진카드_*.md')), key=lambda f: '합치기후' in f)
res = {}
for f in files:
    date = '2026-10-13' if '합치기후' in f else '2026-10-12'
    for l in open(f, encoding='utf-8'):
        c = [s.strip() for s in l.strip().strip('|').split('|')]
        if len(c) < 2 or not re.match(r'^[0-9][0-9a-z]*$', c[0]):
            continue
        j = c[1]
        if j.startswith('확인'):
            v = '지지됨'
        elif j.startswith('부분') or j.startswith('voice 변경 제안'):
            v = '부분'
        else:
            continue
        res[c[0]] = (v, date)

cards = {}
for fn in glob.glob(os.path.join(V, '영구', '*.md')):
    m = re.match(r'(\S+) ', os.path.basename(fn))
    if m:
        cards[m.group(1)] = fn


def set_fields(text, values):
    nl = '\r\n' if '\r\n' in text[:200] else '\n'
    t = text.replace('\r\n', '\n')
    end = t.find('\n---', 4)
    fm, rest = t[4:end], t[end:]
    lines = [l for l in fm.split('\n') if not re.match(r'(%s):' % '|'.join(FIELDS), l)]
    at = next((i + 1 for i, l in enumerate(lines) if l.startswith('created:')), len(lines))
    lines[at:at] = [f'{k}: {values[k]}' for k in FIELDS]
    return ('---\n' + '\n'.join(lines) + rest).replace('\n', nl)


done, skip, missing = {'지지됨': 0, '부분': 0}, [], []
for cid, (v, d) in sorted(res.items()):
    if cid not in cards:
        missing.append(cid); continue
    text = open(cards[cid], encoding='utf-8', newline='').read()
    voice = (re.search(r'^voice:\s*(\S+)', text, re.M) or [None, ''])[1]
    status = (re.search(r'^status:\s*(\S+)', text, re.M) or [None, ''])[1]
    if voice != '영진' or status in ('검토됨', '다시씀'):
        skip.append(f'{cid}({voice},{status})'); continue
    new = set_fields(text, dict(verify=v, verify_date=d, verify_by='sonnet(근거대조)'))
    if new != text and not DRY:
        open(cards[cid], 'w', encoding='utf-8', newline='').write(new)
    done[v] += 1
print(f"{'(시험) ' if DRY else ''}반영 지지됨 {done['지지됨']} · 부분 {done['부분']}, 건너뜀 {len(skip)}, 카드 없음 {len(missing)}")
if skip:
    print('건너뜀:', ', '.join(skip[:20]))
if missing:
    print('카드 없음:', ', '.join(missing[:20]))
