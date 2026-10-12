import os, re, collections, sys
root = sys.argv[1]  # vault root
C = {
 '지각의 철학': ['Travis','트래비스','McDowell','맥도웰','Sellars','셀러스','지각','perception','Given','소여','개념주의','선언주의','Brewer','Ginsborg','Gauker'],
 '언어와 의미': ['Frege','프레게','Wittgenstein','비트겐슈타인','occasion','상황 민감','지표사','indexical','허구적 이름','고유명','단칭 명제','Kripke','크립키','의미론','semantic','Recanati','르카나티','Bivalence','바칸','Grice','그라이스'],
 '증언 인식론': ['증언','testimony','Coady','코디','Reid','리드','Hume','흄','환원주의','reductionis','Fricker','프리커','Lackey'],
 '모호성과 논리': ['Williamson','윌리엄슨','모호','vague','소리테스','sorites','초평가','supervaluation','MFE','margin','safety','세이프티','degrees of truth'],
 '인식론 일반': ['DeRose','Nozick','노직','Goldman','골드만','Sosa','소사','Gettier','게티어','맥락주의','contextualism','회의주의','skeptic','신빙론','reliabilis'],
 '과학철학': ['Kuhn','쿤','Laudan','라우든','Hempel','헴펠','Railton','Woodward','Kitcher','Longino','McMullin','설명','explanation','패러다임'],
 '카벨과 일상언어철학': ['Cavell','카벨','COH','Emerson','에머슨','완전주의','perfectionism','Bauer','바우어','Must We'],
 '자기지식과 투명성': ['Moran','모런','모란','transparency','투명성','self-knowledge','자기지식','apperception','통각'],
 '행위와 실천이성': ['Anscombe','앤스컴','Thompson','톰슨','intention','의도','desire','욕구','action','행위','Millgram','Velleman'],
 '윤리와 가치': ['Parfit','파핏','비동일성','non-identity','harm','해악','aggregation','집계','mortality','필멸','불멸','enhancement','Kass','Socrates','소크라테스','부활'],
 '정치·사회철학': ['시민 불복종','civil disobedience','Rawls','롤스','MacIntyre','매킨타이어','파레지아','parrhesia','Foucault','푸코','좁은 회랑','Acemoglu','Shevardnadze','셰바르드나제','헌법','정의관'],
 '미학과 매체': ['Walton','월튼','Neely','음악','music','매체','medium','사진','photograph','바르트','Barthes','Bazin','영화','허구','fiction','햄릿'],
 '경제학과 경제사': ['Backhouse','Mokyr','모키어','Keynes','케인스','macro','거시','경매','auction','투자','ISA','커버드콜','economics','경제학','Great Divergence','성장','네트워크'],
 '법학': ['명의신탁','소유권','민법','판례','청구권','헌법 개정','헌법 창조'],
 '역사': ['아우구스투스','Augustus','울프 홀','Wolf Hall','튜더','Tudor','Cromwell','크롬웰'],
}
def classify(text):
    sc = {k: sum(len(re.findall(re.escape(w), text, re.I)) for w in ws) for k, ws in C.items()}
    best = sorted(sc.items(), key=lambda x: -x[1])
    return best[0][0] if best[0][1] >= 5 else '미분류', best[:3]
rows = collections.defaultdict(list)
base = os.path.join(root, '_원자료', 'claude.ai')
for dp, _, fs in os.walk(base):
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(dp, f); t = open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, root).replace(os.sep, '/')
        proj = rel.split('/')[3] if '/projects/' in rel else ''
        kind = '문서' if '/docs/' in rel else '대화'
        cl, top = classify(t[:200000])
        # project-level overrides
        override = {'논자시': None, 'Keyens on probability': '경제학과 경제사', 'Macro': '경제학과 경제사', 'Great divergance': '경제학과 경제사', '투자의사결정': '경제학과 경제사', '집필': '창작·에세이', '크립키의 위악성': '카벨과 일상언어철학', 'Cavell': '카벨과 일상언어철학'}
        if proj in override and override[proj]: cl = override[proj]
        if proj == '논자시':
            if 'A-2' in rel or 'A2-' in f: cl = '인식론 일반'
            elif 'B-1' in rel or 'B1' in f: cl = '언어와 의미'
            elif 'C-1' in rel or 'C1' in f: cl = '과학철학'
        title = f[:-3]
        rows[cl].append((rel, title, kind, proj, len(t)//1000, ', '.join(f"{k}:{v}" for k, v in top if v)))
order = list(C.keys()) + ['창작·에세이', '미분류']
out = ['---', 'type: 작업', 'updated: 2026-10-09', '---', '# 원자료 인벤토리 (claude.ai)', '',
       '> 키워드 빈도로 자동 분류한 잠정 지도입니다. 분류가 틀린 항목은 카드를 만들 때 바로잡습니다.', '']
for cl in order:
    if cl not in rows: continue
    rs = sorted(rows[cl], key=lambda r: r[0])
    out += [f'## {cl} ({len(rs)})', '', '| 자료 | 종류 | 프로젝트 | 크기 |', '|---|---|---|---|']
    for rel, title, kind, proj, kb, top in rs:
        out.append(f'| [[{rel[:-3]}\\|{title}]] | {kind} | {proj} | {kb}KB |')
    out.append('')
os.makedirs(os.path.join(root, '_작업'), exist_ok=True)
open(os.path.join(root, '_작업', '원자료 인벤토리.md'), 'w', encoding='utf-8').write('\n'.join(out))
print({k: len(v) for k, v in rows.items()})
