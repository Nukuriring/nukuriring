# 사용법: py -3 _작업/스크립트/verify_batches.py . [묶음 크기] [--sample 비율]
# lint.json에서 voice 문헌·종합 카드를 골라, `_작업/검증/판정/<id>.json`이 아직 없는 카드만
# 클러스터·번호 순서로 묶어 `_작업/검증/판정 분담.json`에 쓴다. 다시 실행하면 남은 카드만 묶는다.
# --sample 0.25: 위험 카드(종합 voice이거나 W-출처Notion 밖의 lint 경고가 있는 카드)는 모두,
#   저위험 카드는 클러스터마다 그 비율만 무작위로 뽑는다(시드 고정, 다시 실행해도 같은 표본).
#   뽑히지 않은 저위험 카드는 분담표의 `deferred`에 남긴다.
import json, os, random, re, sys

V = sys.argv[1]
argv = sys.argv[2:]
sample = None
if '--sample' in argv:
    i = argv.index('--sample'); sample = float(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
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
for c in todo:
    if not batches or len(batches[-1]['ids']) >= size or batches[-1]['cluster'] != c.get('cluster'):
        # 클러스터가 바뀌면 새 묶음을 시작하되, 앞 묶음이 너무 작으면 이어 붙인다
        if batches and len(batches[-1]['ids']) < size // 2 and len(batches[-1]['ids']) < size:
            batches[-1]['ids'].append(c['id']); batches[-1]['cluster'] = c.get('cluster'); continue
        batches.append(dict(n=len(batches) + 1, cluster=c.get('cluster'), ids=[]))
    batches[-1]['ids'].append(c['id'])
out = dict(size=size, sample=sample, done=len(done), remaining=len(todo), deferred=deferred, batches=batches)
json.dump(out, open(os.path.join(V, '_작업', '검증', '판정 분담.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(f'판정 완료 {len(done)}장, 남은 카드 {len(todo)}장, 묶음 {len(batches)}개' + (f', 보류(저위험 표본 밖) {len(deferred)}장' if sample is not None else ''))
