import os, re, sys, importlib.util
VAULT = os.path.expanduser('~/mnt/Projects/Zettelkasten')
D = os.path.join(VAULT, '영구')
W = os.path.expanduser('~/zkwork')
C = {}
for n in ['cards45_a', 'cards45_b', 'cards45_c']:
    spec = importlib.util.spec_from_file_location(n, os.path.join(W, n + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k in m.C:
        assert k not in C, k
    C.update(m.C)
stem = {}
for f in os.listdir(D):
    if f.endswith('.md'):
        i = f.split(' ', 1)[0]
        assert i not in stem, i
        stem[i] = f[:-3]
dry = '--dry' in sys.argv
BAD_TITLE = set('\\/:*?"<>|#^[]\'“”‘’')
problems = []
for i, c in C.items():
    t = c['title']
    if set(t) & BAD_TITLE: problems.append((i, 'bad char in title', set(t) & BAD_TITLE))
    if not t.endswith('다'): problems.append((i, 'title not ending in 다'))
    for txt in [c['body']] + [r for _, r in c['links']]:
        for bad in ['—', '아니라', '<!--']:
            if bad in txt: problems.append((i, 'forbidden', bad))
    for li, _ in c['links']:
        if li not in stem: problems.append((i, 'missing link target', li))
    nks = len(c['links'])
    if not (2 <= nks <= 5): problems.append((i, 'link count', nks))
    ns = len(re.findall(r'(?:다|이다)[.]\s|(?:다|이다)\.$|다\.\)', c['body'].strip()))
    print(f"{i:5s} title_len={len(t):3d} hangul={len(re.findall('[가-힣]', t)):3d} sents~{c['body'].strip().count('다. ')+1} links={nks} | {t}")
if problems:
    print('PROBLEMS', problems); sys.exit(1)
expected = sorted(k for k in stem if k[0] in '45')
assert sorted(C) == expected, (sorted(C), expected)
for i, c in C.items():
    p = os.path.join(D, stem[i] + '.md')
    s = open(p, encoding='utf-8').read()
    assert s.startswith('---\n')
    fm_end = s.index('\n---\n', 4) + 5
    fm = s[:fm_end]
    rest = s[fm_end:]
    a = rest.index('\n## 연결\n'); b = rest.index('\n## 출처\n')
    h1 = [l for l in rest[:a].splitlines() if l.startswith('# ')]
    assert len(h1) == 1 and h1[0].startswith('# ' + i + ' '), (i, h1)
    conn = rest[a + len('\n## 연결\n'):b].splitlines()
    nav = [l for l in conn if re.match(r'- (상위|다음|가지): \[\[', l)]
    com = [l for l in conn if l.strip().startswith('<!--')]
    other = [l for l in conn if l.strip() and l not in nav and l not in com]
    assert len(com) == 1 and com[0].strip().endswith('-->'), (i, com)
    assert not other, (i, other)
    navset = {re.search(r'\[\[([^\]]+)\]\]', l).group(1) for l in nav}
    xl = []
    for li, r in c['links']:
        target = stem[li]
        assert target not in navset, (i, 'link duplicates nav', li)
        xl.append(f'- [[{target}]]: {r}')
    new = (fm + '\n# ' + i + ' ' + c['title'] + '\n\n' + c['body'].strip() + '\n\n## 연결\n'
           + '\n'.join(nav + xl) + '\n\n## 출처\n' + c['sources'].strip() + '\n')
    if dry:
        if i in ('4', '5e1'):
            print('=' * 30, p); print(new)
    else:
        open(p, 'w', encoding='utf-8', newline='\n').write(new)
print('done', 'dry' if dry else 'written', len(C))
