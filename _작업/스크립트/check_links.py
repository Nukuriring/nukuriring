# 사용법: python3 _작업/스크립트/check_links.py <보관함> <파일 또는 접두사> ...
# 인자가 `영구/56`처럼 접두사이면 그 접두사로 시작하는 파일을, 파일 경로이면 그 파일을 검사한다.
# [[링크]]가 실제 .md 파일(이름 또는 보관함 상대 경로)이나 `_원자료/` 아래 실제 파일로 이어지는지 보고한다.
import glob, os, re, sys
V = sys.argv[1]
names = {f[:-3] for dp, _, fs in os.walk(V) if '.git' not in dp.split(os.sep) for f in fs if f.endswith('.md')}
rel = {os.path.relpath(os.path.join(dp, f), V)[:-3].replace(os.sep, '/') for dp, _, fs in os.walk(V) if '.git' not in dp.split(os.sep) for f in fs if f.endswith('.md')}
files = []
for a in sys.argv[2:]:
    files += [f for f in glob.glob(os.path.join(V, a + '*')) if f.endswith('.md')] if not os.path.isfile(os.path.join(V, a)) else [os.path.join(V, a)]
bad = 0
for p in sorted(set(files)):
    for l in re.findall(r'\[\[([^\]|#]+)', open(p, encoding='utf-8').read()):
        l = l.strip().rstrip('\\')
        if l in names or l in rel: continue
        if l.startswith('_원자료/') and any(os.path.exists(os.path.join(V, l + e)) for e in ('', '.md', '.txt')): continue
        bad += 1; print('DANGLING', os.path.basename(p)[:40], '->', l[:90])
print('files', len(set(files)), 'dangling', bad)
