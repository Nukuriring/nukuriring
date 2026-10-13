# 사용법: py -3 _작업/스크립트/adjudicate_apply.py . [--dry-run]
# 영진 님 판정(`_작업/검증/영진 판정 queue83.json`, 판정 페이지 db에서 받은 카드별 선택)을
# 판정 파일(`_작업/검증/판정/<id>.json`)에 반영한다. 카드는 고치지 않는다.
# 반영 후 verify_apply.py를 다시 돌리면 frontmatter의 verify가 갱신된다.
# - 카드를 고침, 카드의 교정을 인정, 판정이 틀림: 문제 명제를 지지됨으로
# - 해석임을 밝힘: 문제 명제를 연결로 (카드 문장 끝에 해석 표시가 붙었다는 전제)
# - 문장을 지움, 제목을 고침: 문제 명제를 claims에서 빼 removed_claims로 옮김
# - 원서를 넣고 다시 판정, 그대로 둠, 보류: 판정은 그대로 두고 표시만 남김
# - 결정 값은 문자열이거나 {choice, skip_n(판정을 바꾸지 않을 명제 번호), pending(남은 일이 있으면 보류로 처리)}
import json, os, sys
V = sys.argv[1]
DRY = '--dry-run' in sys.argv
DEC = json.load(open(os.path.join(V, '_작업', '검증', '영진 판정 queue83.json'), encoding='utf-8'))
JDIR = os.path.join(V, '_작업', '검증', '판정')
DATE = '2026-10-13'
BAD = ('원문에 없음', '모순')


def card_verdict(claims):
    ls = [c.get('label') for c in claims if c.get('label') != '연결']
    if '모순' in ls: return '모순'
    if '원문에 없음' in ls: return '원문없음'
    if '부분 지지' in ls: return '부분'
    if ls and sum(1 for l in ls if l == '판단 불가') * 2 >= len(ls): return '판단불가'
    return '지지됨'


out = []
for cid, dec in sorted(DEC.items()):
    if isinstance(dec, str): dec = {'choice': dec}
    choice, skip = dec['choice'], set(dec.get('skip_n', []))
    if dec.get('pending'): choice = '보류'
    p = os.path.join(JDIR, cid + '.json')
    j = json.load(open(p, encoding='utf-8'))
    if j.get('adjudication') and not dec.get('redo'):
        out.append(f'{cid}: 이미 반영됨'); continue
    before = j['verdict']
    tag = f'영진 판정({DATE}): {choice}'
    keep, removed = [], []
    for c in j['claims']:
        if c.get('label') in BAD and c.get('n') not in skip and choice in ('카드를 고침', '카드의 교정을 인정', '판정이 틀림', '해석임을 밝힘', '문장을 지움', '제목을 고침'):
            c = dict(c, sonnet_label=c['label'])
            if choice in ('문장을 지움', '제목을 고침'):
                removed.append(c); continue
            c['label'] = '연결' if choice == '해석임을 밝힘' else '지지됨'
            c['note'] = (tag + '. ' + c.get('note', '')).strip()
        keep.append(c)
    j['claims'] = keep
    if removed: j['removed_claims'] = removed
    j['adjudication'] = {'choice': choice, 'date': DATE, 'sonnet_verdict': before, **{k: v for k, v in dec.items() if k != 'choice'}}
    j['verdict'] = card_verdict(keep)
    if j['verdict'] != before: j['model'] = (j.get('model') or 'sonnet') + '·영진'
    out.append(f'{cid}: {choice} / {before} → {j["verdict"]}')
    if not DRY:
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(out))
