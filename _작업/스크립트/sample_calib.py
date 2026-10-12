# 사용법: py -3 _작업/스크립트/sample_calib.py . [문헌 수] [종합 수] [시드]
# lint.json에서 오류가 없고 출처를 로컬에서 찾을 수 있는 문헌·종합 카드를 무작위로 뽑아
# `_작업/검증/02 판정자 보정 표본.md`(영진 님 판정용 표)와 `calib_ids.json`을 쓴다.
import json, os, random, sys
from datetime import date
V = sys.argv[1]
n_lit = int(sys.argv[2]) if len(sys.argv) > 2 else 35
n_syn = int(sys.argv[3]) if len(sys.argv) > 3 else 15
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 20261012
d = json.load(open(os.path.join(V, '_작업', '검증', 'lint.json'), encoding='utf-8'))['cards']

def ok(c):
    if c['errors'] or c.get('status') != '초안':
        return False
    ws = ' '.join(c['warnings'])
    return 'W-출처형식' not in ws and 'W-인용미확인' not in ws

rng = random.Random(seed)
pick = []
for voice, n in (('문헌', n_lit), ('종합', n_syn)):
    pool = sorted((c for c in d if c.get('voice') == voice and ok(c)), key=lambda c: c['file'])
    pick += rng.sample(pool, n)
out = os.path.join(V, '_작업', '검증')
json.dump([c['id'] for c in pick], open(os.path.join(out, 'calib_ids.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False)
L = ['---', 'type: 작업', f'updated: {date.today().isoformat()}', '---', '# 판정자 보정 표본',
     '',
     f'문헌 카드 {n_lit}장과 종합 카드 {n_syn}장을 무작위로 뽑았습니다(시드 {seed}). 출처를 로컬에서 찾을 수 있고 lint 오류가 없는 카드만 넣었습니다.',
     '',
     '카드를 열어 출처와 대조한 뒤 **판정** 칸에 `지지됨 · 부분 · 원문없음 · 모순 · 판단불가` 가운데 하나를 적어 주세요. 기준은 `_작업/카드 검증 지침.md` §4~5입니다. 메모 칸에는 문제가 된 문장을 짧게 적으시면 됩니다. Sonnet과 Opus 검증자의 판정은 이 표와 따로 기록하고, 영진 님 판정이 끝난 뒤에 대조합니다.',
     '',
     '| # | 카드 | voice | 판정 | 메모 |', '|---|---|---|---|---|']
for k, c in enumerate(pick, 1):
    stem = c['file'].rsplit('/', 1)[-1][:-3]
    L.append(f"| {k} | [[{stem}\\|{c['id']}]] | {c['voice']} |  |  |")
open(os.path.join(out, '02 판정자 보정 표본.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print(len(pick), 'cards →', '_작업/검증/02 판정자 보정 표본.md')
