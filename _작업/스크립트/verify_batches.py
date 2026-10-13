# 사용법: py -3 _작업/스크립트/verify_batches.py . [묶음 크기] [--sample 비율]
# lint.json에서 voice 문헌·종합 카드를 골라, `_작업/검증/판정/<id>.json`이 아직 없는 카드만
# 클러스터·번호 순서로 묶어 `_작업/검증/판정 분담.json`에 쓴다. 다시 실행하면 남은 카드만 묶는다.
# --sample 0.25: 위험 카드(종합 voice이거나 W-출처Notion 밖의 lint 경고가 있는 카드)는 모두,
#   저위험 카드는 클러스터마다 그 비율만 무작위로 뽑는다(시드 고정, 다시 실행해도 같은 표본).
#   뽑히지 않은 저위험 카드는 분담표의 `deferred`에 남긴다.
# --by-source: 클러스터·번호 순서 대신 주 출처 파일(notion_map의 첫 파일, 없으면 카드 `## 출처`의 첫 줄)이
#   같은 카드끼리 모아 묶는다. 큰 출처를 묶음마다 다시 읽지 않게 하려는 것이다. 묶음마다 `sources`(출처별 카드 수)를 남긴다.
import json, os, random, re, sys

V = sys.argv[1]
argv = sys.argv[2:]
sample = None
if '--sample' in argv:
    i = argv.index('--sample'); sample = float(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
by_source = '--by-source' in argv
argv = [a for a in argv if a != '--by-source']
size = int(argv[0]) if argv else 40
cards = json.load(open(os.path.join(V, '_작업', '검증', 'lint.json'), encoding='utf-8'))['cards']
done_dir = os.path.join(V, '_작업', '검증', '판정')
done = {f[:-5] for f in os.listdir(done_dir) if f.endswith('.json')} if os.path.isdir(done_dir) else set()


def natkey(cid):
    return [int(t) if t.isdigit() else t for t in re.findall(r'\d+|\D+', cid)]


todo = [c for c in cards if c.get('voice') in ('문헌', '종합') and not c['errors'] and c['id'] not in done]
deferred = []


def risky(c):
    return c.get('voice') == '종합' or any(not w.startswith('W-출처Notion') for w in c['warnings'])


if sample is not None:
    rng = random.Random(20261013)
    by_cluster = {}
    for c in sorted(cards, key=lambda c: c['id']):  # 표본은 전체 카드 기준으로 고정한다
        if c.get('voice') == '문헌' and not risky(c):
            by_cluster.setdefault(c.get('cluster'), []).append(c['id'])
    chosen = set()
    for cl, ids in by_cluster.items():
        chosen |= set(rng.sample(ids, max(1, round(len(ids) * sample))))
    deferred = [c['id'] for c in todo if not risky(c) and c['id'] not in chosen]
    todo = [c for c in todo if risky(c) or c['id'] in chosen]
todo.sort(key=lambda c: (c.get('cluster') or '', natkey(c['id'])))
batches = []


def source_key(c):
    nm = NOTION.get(c['id']) or []
    for x in nm:
        if x.get('files'):
            return x['files'][0]
    try:
        text = open(os.path.join(V, c['file']), encoding='utf-8').read()
    except OSError:
        return 'card:' + c['id']
    m = re.search(r'^## 출처\s*\n-?\s*(.+)', text, re.M)
    return re.sub(r'\s*\(.*$', '', m.group(1)).strip() if m else 'card:' + c['id']


if by_source:
    NOTION = json.load(open(os.path.join(V, '_작업', '검증', 'notion_map.json'), encoding='utf-8'))['cards']
    groups = {}
    for c in todo:
        groups.setdefault(source_key(c), []).append(c)
    # 큰 출처 묶음부터 채우고(20장 넘으면 나눔), 남는 자리는 같은 클러스터의 작은 묶음으로 채운다
    order = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[1][0].get('cluster') or '', kv[0]))
    for key, cs in order:
        for i in range(0, len(cs), size):
            part = cs[i:i + size]
            tgt = next((b for b in batches if len(b['ids']) + len(part) <= size and b['cluster'] == part[0].get('cluster')), None) \
                or next((b for b in batches if len(b['ids']) + len(part) <= size), None) if len(part) < size // 2 else None
            if tgt is None:
                tgt = dict(n=len(batches) + 1, cluster=part[0].get('cluster'), ids=[], sources={})
                batches.append(tgt)
            tgt['ids'] += [c['id'] for c in part]
            tgt['sources'][key] = tgt['sources'].get(key, 0) + len(part)
    todo_iter = []
else:
    todo_iter = todo
for c in todo_iter:
    if not batches or len(batches[-1]['ids']) >= size or batches[-1]['cluster'] != c.get('cluster'):
        # 클러스터가 바뀌면 새 묶음을 시작하되, 앞 묶음이 너무 작으면 이어 붙인다
        if batches and len(batches[-1]['ids']) < size // 2 and len(batches[-1]['ids']) < size:
            batches[-1]['ids'].append(c['id']); batches[-1]['cluster'] = c.get('cluster'); continue
        batches.append(dict(n=len(batches) + 1, cluster=c.get('cluster'), ids=[]))
    batches[-1]['ids'].append(c['id'])
out = dict(size=size, sample=sample, done=len(done), remaining=len(todo), deferred=deferred, batches=batches)
json.dump(out, open(os.path.join(V, '_작업', '검증', '판정 분담.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(f'판정 완료 {len(done)}장, 남은 카드 {len(todo)}장, 묶음 {len(batches)}개' + (f', 보류(저위험 표본 밖) {len(deferred)}장' if sample is not None else ''))
