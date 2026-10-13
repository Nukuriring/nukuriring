# 사용법: python3 _작업/스크립트/queue_report.py .   (먼저 lint.py를 돌려 `_작업/검증/lint.json`을 최신으로 둔다)
# 영진 님 판단 대기열(작업 계획 2단계) 가운데 frontmatter로 거를 수 없는 항목을 목록 노트로 만든다.
# frontmatter로 거를 수 있는 항목(verify, voice, cluster)은 `_작업/대기열/대기열.base`가 직접 보여 준다.
# 결과: `_작업/대기열/길이 초과.md`, `서지 확인.md`, `제안 연결.md`, `voice 변경.md`, `00 대기열.md`(입구)
import collections, glob, json, os, re, sys
from datetime import date

V = sys.argv[1]
Q = os.path.join(V, '_작업', '대기열')
os.makedirs(Q, exist_ok=True)
today = date.today().isoformat()
lint = json.load(open(os.path.join(V, '_작업', '검증', 'lint.json'), encoding='utf-8'))
stem = lambda p: os.path.basename(p)[:-3]
nat = lambda s: [int(t) if t.isdigit() else t for t in re.findall(r'\d+|\D+', s)]


def write(name, title, intro, lines):
    L = ['---', 'type: 작업', f'updated: {today}', '---', f'# {title}', '', intro, ''] + lines
    open(os.path.join(Q, name + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')


# 1. 길이 초과 (lint W-길이)
long = [c for c in lint['cards'] if any(w.startswith('W-길이') for w in c['warnings'])]
by = collections.defaultdict(list)
for c in sorted(long, key=lambda c: -c.get('sentences', 0)):
    by[c['cluster']].append(c)
L = []
for cl in sorted(by, key=lambda k: -len(by[k])):
    L += [f'## {cl} ({len(by[cl])}장)', '']
    L += [f"- [ ] [[{stem(c['file'])}|{c['id']}]] {c.get('sentences', '?')}문장 · {c['voice']}" for c in by[cl]] + ['']
write('길이 초과', f'본문 길이 점검 ({len(long)}장)',
      '`lint.py`가 종결 어미로 센 문장 수가 3~8문장 범위를 벗어난 카드입니다. 문장 수가 많은 순서입니다. '
      '분할, 유지, 압축 가운데 고르시면 됩니다. 처리한 줄은 체크해 주세요.', L)

# 2. 서지 확인 (문헌 노트의 '확인 필요')
lit = []
for f in sorted(glob.glob(os.path.join(V, '문헌', '*.md'))):
    t = open(f, encoding='utf-8').read()
    hits = [l.strip() for l in t.split('\n') if '확인 필요' in l]
    if hits:
        lit.append((stem(f), hits))
L = []
for s, hits in lit:
    L.append(f'- [ ] [[{s}]]')
    L += [f'    - {h[:160]}' for h in hits[:3]]
write('서지 확인', f'서지 확인 ({len(lit)}편)',
      "문헌 노트 가운데 '확인 필요' 표시가 남은 노트와 그 줄입니다. 저자, 연도, 판본을 확인해 주세요.", L)

# 3. Claude 제안 연결 (연결 절 끝 '(제안: Claude)')
sug = collections.Counter()
clus = {}
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    t = open(f, encoding='utf-8').read()
    n = t.count('(제안: Claude)')
    if n:
        sug[stem(f)] = n
        m = re.search(r'^cluster:\s*(.+)$', t, re.M)
        clus[stem(f)] = m.group(1).strip() if m else ''
bc = collections.defaultdict(list)
for s in sug:
    bc[clus[s]].append(s)
L = ['## 클러스터별 집계', '', '| 클러스터 | 카드 | 제안 줄 |', '|---|---|---|']
L += [f'| {cl} | {len(v)} | {sum(sug[s] for s in v)} |' for cl, v in sorted(bc.items(), key=lambda x: -len(x[1]))]
L += ['', '## 카드 목록 (제안 줄이 많은 순)', '']
L += [f'- [[{s}|{s.split(" ")[0]}]] {sug[s]}줄' for s in sorted(sug, key=lambda s: (-sug[s], nat(s)))]
write('제안 연결', f'Claude 제안 연결 검토 (카드 {len(sug)}장, {sum(sug.values())}줄)',
      "다른 묶음 카드 사이에 Claude가 넣은 연결 줄입니다. 줄 끝에 `(제안: Claude)`가 붙어 있습니다. "
      "확인한 줄은 표시를 지우고, 틀린 줄은 줄째 지우시면 됩니다. Obsidian 검색 `\"(제안: Claude)\"`로도 찾을 수 있습니다.", L)

# 4. voice 변경 카드 (원자료 대조로 바꾼 8장)
CH = {'47a2d': '영진 → 문헌', '47h10': '영진 → 문헌', '37d': '영진 → 문헌', '37d1': '영진 → 문헌',
      '37d1a': '영진 → 문헌', '35h': '영진 → 종합', '35h2': '영진 → 종합', '32l': '영진 → 종합'}
files = {os.path.basename(f).split(' ')[0]: stem(f) for f in glob.glob(os.path.join(V, '영구', '*.md'))}
L = [f'- [ ] [[{files[c]}|{c}]] {v}' if c in files else f'- [ ] {c} {v} (카드 없음: 합쳐졌거나 이름이 바뀜)' for c, v in CH.items()]
write('voice 변경', 'voice 변경 확인 (8장)',
      '영진 voice 대조(2026-10-12)에서 원자료를 근거로 voice를 바꾼 카드입니다. 사유는 `_작업/검증/00 요약.md`에 있습니다. '
      '승인하시면 체크하고, 되돌리실 카드는 voice를 직접 고쳐 주세요. `37d` 세 장은 지문 초고 안의 프리커 논증 요약이라 문헌으로 바꿨습니다.', L)

# 5. 입구 노트
vc = collections.Counter()
for f in glob.glob(os.path.join(V, '영구', '*.md')):
    t = open(f, encoding='utf-8').read(800)
    v = re.search(r'^verify:\s*(\S+)', t, re.M)
    vo = re.search(r'^voice:\s*(\S+)', t, re.M)
    vc[(vo.group(1) if vo else '?', v.group(1) if v else '없음')] += 1
L = ['## 한눈에', '', '| voice | 지지됨 | 부분 | 원문없음 | 모순 | 판단불가 | 없음 |', '|---|---|---|---|---|---|---|']
for vo in ('문헌', '종합', '영진'):
    L.append(f'| {vo} | ' + ' | '.join(str(vc[(vo, k)]) for k in ('지지됨', '부분', '원문없음', '모순', '판단불가', '없음')) + ' |')
L += ['', '`없음`은 표본에서 빠진 저위험 문헌 카드입니다. 영진 voice는 원자료 근거 대조 결과입니다(확인 → 지지됨).', '',
      '## frontmatter로 보는 대기열 (Bases)', '',
      '- ![[대기열.base#내용 오류(모순·원문없음)]]', '',
      '- ![[대기열.base#영진 카드 부분 판정]]', '',
      '- 그 밖의 보기: [[대기열.base]]의 `부분 판정(문헌·종합)`, `판단불가`, `미검증(클러스터별)`', '',
      '## 목록 노트', '',
      f'- [[voice 변경]]: 8장',
      f'- [[길이 초과]]: {len(long)}장',
      f'- [[서지 확인]]: 문헌 노트 {len(lit)}편',
      f'- [[제안 연결]]: 카드 {len(sug)}장, {sum(sug.values())}줄',
      '', '## 준비된 초안 (Claude가 만든 처리안)', '',
      '판정 페이지 https://claude.ai/artifact/PqirM4oJBAH15MzwzuH5b4 에서 클릭으로 고르시면 됩니다(결정은 페이지 db `decisions`에 저장, 원본은 `판정페이지/`, 자료는 `queue_items.py`가 만듦).', '',
      '- `분할초안/L1`~`L8`: 길이 경고가 났던 카드 289장의 분할·압축·유지 권고와 초안(10-13 기준, 이후 lint 수정으로 실제 경고는 줄었음)',
      '- `영진 부분/Y1`~`Y4`: 영진 voice 부분 판정 83장의 카드 문장·원문 대목·수정안·voice 변경안',
      '- `서지 후보/S1`~`S4`: 문헌 노트 112편의 서지 후보(웹 검색, 근거 URL·확신도)', '',
      '- 원서가 있어야 판정할 수 있는 카드(카벨 COH, 맥도웰 2008): `_작업/검증/05 영진 판정 대기열.md`의 C 갈래',
      '- 투자 대화 파일명(`2026-05-02_600만원 ISA…`) 변경 여부와 M7 카드 6장의 출처 링크: 결정 대기',
      '- 『Life and Action』 수록 여부(`20a`·`20b`, `@Thompson2004`): 확인 대기', '',
      'status를 `검토됨`으로 올리시면 그 카드는 이후 에이전트가 허락 없이 고치지 않습니다. '
      '이 노트는 `queue_report.py`가 다시 만듭니다. 목록 노트의 체크 표시는 다시 만들면 지워지므로, 처리 결과는 카드에 직접 반영해 주세요.']
write('00 대기열', '영진 님 판단 대기열', '작업 계획 2단계의 입구 노트입니다.', L)
print(f'길이 {len(long)}, 서지 {len(lit)}, 제안 연결 카드 {len(sug)}장 {sum(sug.values())}줄 → _작업/대기열/')
