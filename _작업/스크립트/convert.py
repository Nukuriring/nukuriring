import json, os, re, sys
src, outroot = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding='utf-8'))
def safe(s, n=60):
    s = re.sub(r'[\\/:*?"<>|\n\r\t]', ' ', s or 'untitled').strip()
    s = re.sub(r'\s+', ' ', s)
    return s[:n].rstrip(' .')
def main_branch(conv):
    msgs = conv['messages']
    by = {m['uuid']: m for m in msgs}
    leaf = conv.get('leaf')
    if leaf and leaf in by:
        chain = []; cur = leaf; seen=set()
        while cur and cur in by and cur not in seen:
            seen.add(cur); chain.append(by[cur]); cur = by[cur].get('parent')
        chain.reverse()
        if len(chain) >= max(1, len(msgs)//3): return chain
    return msgs
def write_conv(conv, folder, project):
    os.makedirs(folder, exist_ok=True)
    date = (conv.get('created_at') or '')[:10]
    fn = f"{date}_{safe(conv.get('name'))}.md"
    path = os.path.join(folder, fn); i = 2
    while os.path.exists(path):
        path = os.path.join(folder, fn[:-3] + f"_{i}.md"); i += 1
    chain = main_branch(conv)
    lines = ['---', f"title: \"{(conv.get('name') or '').replace(chr(34), chr(39))}\"", f"uuid: {conv['uuid']}",
             f"created: {date}", f"updated: {(conv.get('updated_at') or '')[:10]}", f"project: \"{project}\"",
             f"url: https://claude.ai/chat/{conv['uuid']}", f"turns: {len(chain)}", 'type: 원자료/대화', '---', '']
    if conv.get('summary'): lines += ['> 요약: ' + conv['summary'].replace('\n', ' '), '']
    for m in chain:
        who = '영진' if m.get('sender') == 'human' else 'Claude'
        lines.append(f"## {who} · {m.get('at','')}")
        for a in m.get('attachments') or []:
            lines.append(f"> 첨부: {a.get('name')} ({a.get('size')} bytes)")
        for f in m.get('files') or []:
            lines.append(f"> 파일: {f}")
        lines += ['', (m.get('text') or '').strip(), '']
    open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    return path
n = 0
for pname, p in d['projects'].items():
    base = os.path.join(outroot, 'projects', safe(pname))
    for doc in p['docs']:
        rel = doc['file_name']
        dpath = os.path.join(base, 'docs', *[safe(x, 120) for x in rel.split('/')])
        if not os.path.splitext(dpath)[1]: dpath += '.md'
        os.makedirs(os.path.dirname(dpath), exist_ok=True)
        open(dpath, 'w', encoding='utf-8').write(doc.get('content') or ''); n += 1
    for c in p['conversations']:
        write_conv(c, os.path.join(base, 'chats'), pname); n += 1
for c in d['non_project_conversations']:
    write_conv(c, os.path.join(outroot, 'chats'), ''); n += 1
print('written', n)
