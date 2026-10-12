# 사용법: py -3 _작업/스크립트/verify_apply.py . [--dir <판정 폴더>] [--dry-run]
# 검증자가 쓴 판정 JSON(`_작업/검증/판정/<id>.json`)을 읽어 카드 frontmatter의
# verify, verify_date, verify_by 세 필드를 쓴다. 본문과 다른 필드는 건드리지 않는다.
# - status가 `검토됨`·`다시씀`인 카드는 영진 님이 고친 카드이므로 쓰지 않고 보고만 한다.
# - 판정 JSON이 형식에 맞지 않으면 그 카드는 건너뛰고 보고한다.
# - 결과를 `_작업/검증/03 판정 반영.md`에 요약하고, 판정이 지지됨이 아닌 카드를 대기열로 모은다.
import json, os, re, sys, collections
from datetime import date

V = sys.argv[1]
args = sys.argv[2:]
DRY = '--dry-run' in args
JDIR = os.path.join(V, '_작업', '검증', '판정')
if '--dir' in args:
    JDIR = os.path.join(V, args[args.index('--dir') + 1])

VERDICTS = ['지지됨', '부분', '원문없음', '모순', '판단불가']
LABELS = {'지지됨', '부분 지지', '원문에 없음', '모순', '판단 불가', '연결'}
LOCKED = {'검토됨', '다시씀'}
FIELDS = ('verify', 'verify_date', 'verify_by')


def card_verdict(claims):
    """카드 검증 지침 §5의 순서로 명제 판정에서 카드 판정을 다시 계산한다."""
    ls = [c.get('label') for c in claims if c.get('label') != '연결']
    if '모순' in ls:
        return '모순'
    if '원문에 없음' in ls:
        return '원문없음'
    if '부분 지지' in ls:
        return '부분'
    if ls and sum(1 for l in ls if l == '판단 불가') * 2 >= len(ls):
        return '판단불가'
    return '지지됨'


# 카드 번호 → 파일
cards = {}
for fn in os.listdir(os.path.join(V, '영구')):
    if fn.endswith('.md'):
        m = re.match(r'(\S+) ', fn)
        if m:
            cards[m.group(1)] = os.path.join(V, '영구', fn)


def set_fields(text, values):
    """frontmatter에서 세 필드를 지우고 created 다음(없으면 끝)에 다시 넣는다."""
    nl = '\r\n' if '\r\n' in text[:200] else '\n'
    t = text.replace('\r\n', '\n')
    end = t.find('\n---', 4)
    fm, rest = t[4:end], t[end:]
    lines = [l for l in fm.split('\n') if not re.match(r'(%s):' % '|'.join(FIELDS), l)]
    new = [f'{k}: {values[k]}' for k in FIELDS]
    at = next((i + 1 for i, l in enumerate(lines) if l.startswith('created:')), len(lines))
    lines[at:at] = new
    return ('---\n' + '\n'.join(lines) + rest).replace('\n', nl)


applied, same, skipped, bad, queue = [], [], [], [], []
count = collections.Counter()
files = sorted(f for f in os.listdir(JDIR) if f.endswith('.json')) if os.path.isdir(JDIR) else []
for f in files:
    try:
        j = json.load(open(os.path.join(JDIR, f), encoding='utf-8'))
    except (OSError, ValueError) as e:
        bad.append((f, f'JSON 읽기 실패: {e}')); continue
    cid = str(j.get('id', ''))
    claims = j.get('claims') or []
    problems = []
    if cid != f[:-5]:
        problems.append('id와 파일명이 다름')
    if cid not in cards:
        problems.append('카드 없음')
    if j.get('verdict') not in VERDICTS:
        problems.append(f"verdict 값 '{j.get('verdict')}'")
    if not claims or any(c.get('label') not in LABELS for c in claims):
        problems.append('명제 판정이 없거나 label 값이 틀림')
    if problems:
        bad.append((f, ', '.join(problems))); continue
    calc = card_verdict(claims)
    if calc != j['verdict']:
        bad.append((f, f"verdict '{j['verdict']}'가 명제 판정으로 계산한 '{calc}'와 다름")); continue

    path = cards[cid]
    text = open(path, encoding='utf-8', newline='').read()
    status = (re.search(r'^status:\s*(\S+)', text, flags=re.M) or [None, ''])[1]
    vals = dict(verify=j['verdict'], verify_date=j.get('date') or date.today().isoformat(),
                verify_by=j.get('model') or '미상')
    count[j['verdict']] += 1
    if j['verdict'] != '지지됨':
        bad_claims = [c for c in claims if c['label'] not in ('지지됨', '연결')]
        queue.append((cid, j['verdict'], bad_claims))
    if status in LOCKED:
        skipped.append((cid, status, j['verdict'])); continue
    new = set_fields(text, vals)
    if new == text:
        same.append(cid); continue
    if not DRY:
        open(path, 'w', encoding='utf-8', newline='').write(new)
    applied.append(cid)

# ---------- 보고 ----------
L = ['---', 'type: 작업', f'updated: {date.today().isoformat()}', '---', '# 판정 반영',
     '', f'`verify_apply.py`가 `{os.path.relpath(JDIR, V).replace(chr(92), "/")}`의 판정 {len(files)}건을 읽었습니다.' + (' (시험 실행, 카드는 쓰지 않음)' if DRY else ''),
     '', f"- 반영 {len(applied)}장, 이미 같음 {len(same)}장, 영진 님이 고친 카드라 건너뜀 {len(skipped)}장, 형식 오류 {len(bad)}건",
     '- 카드 판정: ' + ' · '.join(f'{v} {count[v]}' for v in VERDICTS)]
if skipped:
    L += ['', '## 건너뛴 카드 (status 검토됨·다시씀)', ''] + [f'- `{c}` ({s}): 판정 {v}' for c, s, v in skipped]
if bad:
    L += ['', '## 형식 오류 (반영하지 않음)', ''] + [f'- `{f}`: {why}' for f, why in bad]
if queue:
    L += ['', '## 대기열 (지지됨이 아닌 카드)', '', '판정 순서는 모순, 원문없음, 부분, 판단불가입니다.', '']
    order = ['모순', '원문없음', '부분', '판단불가']
    for cid, v, bcs in sorted(queue, key=lambda q: order.index(q[1])):
        stem = os.path.basename(cards[cid])[:-3]
        L.append(f'- [[{stem}|{cid}]] **{v}**')
        for c in bcs:
            note = f" — {c.get('note')}" if c.get('note') else ''
            L.append(f"  - ({c['label']}) {c.get('text', '')[:80]}{note[:120]}")
out = os.path.join(V, '_작업', '검증', '03 판정 반영.md')
if not DRY:
    open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('\n'.join(L[5:9]))
