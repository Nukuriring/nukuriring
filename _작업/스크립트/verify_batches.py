# 사용법: py -3 _작업/스크립트/verify_batches.py . [묶음 크기]
# lint.json에서 voice 문헌·종합 카드를 골라, `_작업/검증/판정/<id>.json`이 아직 없는 카드만
# 클러스터·번호 순서로 묶어 `_작업/검증/판정 분담.json`에 쓴다. 다시 실행하면 남은 카드만 묶는다.
import json, os, re, sys

V = sys.argv[1]
size = int(sys.argv[2]) if len(sys.argv) > 2 else 40
cards = json.load(open(os.path.join(V, '_작업', '검증', 'lint.json'), encoding='utf-8'))['cards']
done_dir = os.path.join(V, '_작업', '검증', '판정')
done = {f[:-5] for f in os.listdir(done_dir) if f.endswith('.json')} if os.path.isdir(done_dir) else set()


def natkey(cid):
    return [int(t) if t.isdigit() else t for t in re.findall(r'\d+|\D+', cid)]


todo = [c for c in cards if c.get('voice') in ('문헌', '종합') and not c['errors'] and c['id'] not in done]
todo.sort(key=lambda c: (c.get('cluster') or '', natkey(c['id'])))
batches = []
for c in todo:
    if not batches or len(batches[-1]['ids']) >= size or batches[-1]['cluster'] != c.get('cluster'):
        # 클러스터가 바뀌면 새 묶음을 시작하되, 앞 묶음이 너무 작으면 이어 붙인다
        if batches and len(batches[-1]['ids']) < size // 2 and len(batches[-1]['ids']) < size:
            batches[-1]['ids'].append(c['id']); batches[-1]['cluster'] = c.get('cluster'); continue
        batches.append(dict(n=len(batches) + 1, cluster=c.get('cluster'), ids=[]))
    batches[-1]['ids'].append(c['id'])
out = dict(size=size, done=len(done), remaining=len(todo), batches=batches)
json.dump(out, open(os.path.join(V, '_작업', '검증', '판정 분담.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(f'판정 완료 {len(done)}장, 남은 카드 {len(todo)}장, 묶음 {len(batches)}개')
