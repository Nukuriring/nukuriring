# -*- coding: utf-8 -*-
"""카드·문헌 노트 일괄 생성기. 사용법: py mkbatch.py <보관함> <배치파일> [--force]

배치 파일 형식
  #GROUP NL3
  #CLUSTER 영문학과 문학비평
  #DATE 2026-10-12

  카드:   @@ 56b | 영진 | 태그1,태그2 | @McEwan2001; @King1981
          T: 제목 한 줄
          (본문, ## 연결, ## 출처 절을 마크다운으로 그대로 씀)

  문헌:   @@@ @Powers2021 Bewilderment | Richard Powers | 2021 | Bewilderment | 연도 출처 설명 | 읽은 원자료1; 원자료2
          (한 줄 요지부터 원자료까지 본문 절을 마크다운으로 그대로 씀)

본문 안의 [[56b1]] 같은 번호 링크는 실제 카드 파일명으로, [[@McEwan2001]] 같은 citekey 링크는
문헌 폴더의 실제 파일명으로 풀어 씁니다. 풀리지 않는 링크는 경고로 출력합니다.
문헌 노트가 이미 있으면 건너뜁니다(내용을 보태려면 직접 편집).
"""
import os, re, sys

V = sys.argv[1]
BATCH = sys.argv[2]
FORCE = '--force' in sys.argv
meta = {'GROUP': '', 'CLUSTER': '', 'DATE': '2026-10-12'}
cards, lits = [], []
cur = None
for line in open(BATCH, encoding='utf-8').read().split('\n'):
    m = re.match(r'^#(GROUP|CLUSTER|DATE)\s+(.*)$', line)
    if m:
        meta[m.group(1)] = m.group(2).strip()
        continue
    l = re.match(r'^@@@\s*(.*)$', line)
    if l:
        p = [x.strip() for x in l.group(1).split('|')]
        cur = dict(kind='lit', name=p[0], author=p[1], year=p[2], title=p[3], published=p[4] if len(p) > 4 else '',
                   read_via=p[5] if len(p) > 5 else '', body=[])
        lits.append(cur)
        continue
    h = re.match(r'^@@\s*(.*)$', line)
    if h:
        parts = [p.strip() for p in h.group(1).split('|')]
        cur = dict(kind='card', id=parts[0], voice=parts[1], tags=parts[2], sources=parts[3] if len(parts) > 3 else '', title='', body=[])
        cards.append(cur)
        continue
    if cur is None:
        continue
    if cur['kind'] == 'card' and line.startswith('T: ') and not cur['title']:
        cur['title'] = line[3:].strip()
        continue
    cur['body'].append(line)

BAD = re.compile(r'[\\/:*?"<>|#^\[\]“”‘’\'`]')
def clean(t):
    return re.sub(r'\s+', ' ', BAD.sub('', t)).strip()

fn = {}
for f in os.listdir(os.path.join(V, '영구')):
    if f.endswith('.md'):
        fn[f.split(' ')[0]] = f[:-3]
for c in cards:
    c['file'] = f"{c['id']} {clean(c['title'])}"
    if len(c['file']) > 120:
        print('경고: 파일명이 긴 카드', c['id'], len(c['file']))
    if c['id'] in fn and fn[c['id']] != c['file']:
        print('경고: 같은 번호의 다른 파일이 이미 있음', c['id'], fn[c['id']])
    fn[c['id']] = c['file']
lit = {}
for f in os.listdir(os.path.join(V, '문헌')):
    if f.endswith('.md') and f.startswith('@'):
        lit[f.split(' ')[0]] = f[:-3]
for t in lits:
    t['file'] = clean(t['name'])
    lit[t['file'].split(' ')[0]] = t['file']

warn = []
def resolve(text, cid):
    def rep(m):
        k = m.group(1).strip()
        if k.startswith('@'):
            key = k.split(' ')[0]
            if key in lit:
                return '[[' + lit[key] + ']]'
            warn.append((cid, k)); return m.group(0)
        if re.fullmatch(r'[0-9][0-9a-z]*', k) and k in fn:
            return '[[' + fn[k] + ']]'
        if k in fn.values() or k.startswith('_원자료') or os.path.exists(os.path.join(V, k)):
            return m.group(0)
        warn.append((cid, k)); return m.group(0)
    return re.sub(r'\[\[([^\]\|]+)\]\]', rep, text)

written = 0
for t in lits:
    path = os.path.join(V, '문헌', t['file'] + '.md')
    if os.path.exists(path):
        print('건너뜀(문헌 노트가 이미 있음, 내용을 보태려면 직접 편집):', t['file']); continue
    rv = [x.strip() for x in t['read_via'].split(';') if x.strip()]
    fm = ['---', 'type: 문헌', 'citekey: ' + t['file'].split(' ')[0][1:], 'author: ' + t['author'], 'year: ' + t['year'],
          'title: "' + t['title'].replace('"', "'") + '"',
          'published: "' + t['published'].replace('"', "'") + '"', 'status: 초안', 'read_via:']
    fm += ['  - "' + r.replace('"', "'") + '"' for r in rv]
    fm += ['created: ' + meta['DATE'], '---']
    body = resolve('\n'.join(t['body']).strip('\n'), t['file'])
    open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(fm) + '\n# ' + t['title'] + '\n\n' + body + '\n')
    written += 1
print('쓴 문헌 노트', written, '/', len(lits))

written = 0
for c in cards:
    path = os.path.join(V, '영구', c['file'] + '.md')
    if os.path.exists(path) and not FORCE:
        print('건너뜀(이미 있음):', c['file']); continue
    srcs = [s.strip() for s in c['sources'].split(';') if s.strip()]
    srcs_res = []
    for s in srcs:
        key = s.split(' ')[0]
        if key in lit: srcs_res.append('"[[' + lit[key] + ']]"')
        else: warn.append((c['id'], s)); srcs_res.append('"[[' + s + ']]"')
    fm = ['---', 'id: ' + c['id'], 'type: 영구', 'voice: ' + c['voice'], 'status: 초안',
          'tags: [' + ', '.join(t.strip() for t in c['tags'].split(',') if t.strip()) + ']',
          'sources: [' + ', '.join(srcs_res) + ']',
          'cluster: ' + meta['CLUSTER'], 'group: ' + meta['GROUP'], 'created: ' + meta['DATE'], '---']
    body = resolve('\n'.join(c['body']).strip('\n'), c['id'])
    out = '\n'.join(fm) + '\n# ' + c['file'] + '\n\n' + body + '\n'
    open(path, 'w', encoding='utf-8', newline='\n').write(out)
    written += 1
print('쓴 카드', written, '/', len(cards))
for w in warn:
    print('해결되지 않은 링크:', w)
