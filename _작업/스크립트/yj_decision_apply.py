# 사용법: python3 _작업/스크립트/yj_decision_apply.py . <판정 페이지 db에서 내려받은 decisions 폴더> [--dry-run]
# 영진 voice 부분 판정 카드에 대한 영진 님 결정(판정 페이지 2026-10-13)을 verify 필드에 남긴다.
#  - '수정안 채택'(카드를 원문 강도에 맞게 고침)과 '그대로 둠'(영진 님이 지금 문장을 인정함) → verify: 지지됨, verify_by: 영진(판정 페이지)
#  - 'voice 변경' → verify를 지운다(카드가 문헌·종합이 되어 문헌·종합 판정 대상이 되었으므로 다음 판정 묶음에서 다시 본다).
#  - 그 밖의 결정과 status 검토됨·다시씀 카드는 건드리지 않는다.
import glob, json, os, re, sys
from datetime import date

V, D = sys.argv[1], sys.argv[2]
DRY = '--dry-run' in sys.argv
FIELDS = ('verify', 'verify_date', 'verify_by')
files = {os.path.basename(f).split(' ')[0]: f for f in glob.glob(os.path.join(V, '영구', '*.md'))}


def set_fields(text, values):
    nl = '\r\n' if '\r\n' in text[:200] else '\n'
    t = text.replace('\r\n', '\n')
    end = t.find('\n---', 4)
    fm, rest = t[4:end], t[end:]
    lines = [l for l in fm.split('\n') if not re.match(r'(%s):' % '|'.join(FIELDS), l)]
    if values:
        at = next((i + 1 for i, l in enumerate(lines) if l.startswith('created:')), len(lines))
        lines[at:at] = [f'{k}: {values[k]}' for k in FIELDS]
    return ('---\n' + '\n'.join(lines) + rest).replace('\n', nl)


n = {'지지됨': 0, '지움': 0, '건너뜀': 0}
for f in sorted(glob.glob(os.path.join(D, 'y_*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    cid, ch = d.get('ref'), d.get('choice')
    p = files.get(cid)
    if not p:
        n['건너뜀'] += 1; continue
    t = open(p, encoding='utf-8', newline='').read()
    if re.search(r'^status:\s*(검토됨|다시씀)', t, re.M):
        n['건너뜀'] += 1; continue
    if ch in ('수정안 채택', '그대로 둠'):
        new = set_fields(t, dict(verify='지지됨', verify_date=date.today().isoformat(), verify_by='영진(판정 페이지)')); k = '지지됨'
    elif ch == 'voice 변경':
        new = set_fields(t, None); k = '지움'
    else:
        n['건너뜀'] += 1; continue
    if not DRY and new != t:
        open(p, 'w', encoding='utf-8', newline='').write(new)
    n[k] += 1
print(('(시험) ' if DRY else '') + ', '.join(f'{k} {v}' for k, v in n.items()))
