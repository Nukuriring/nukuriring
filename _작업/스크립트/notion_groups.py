import json,os,re,collections,sys
V=os.path.expanduser("~/mnt/Projects/Zettelkasten")
REL="_원자료/notion/Export-c8124db7-875f-40d8-b724-67e0c0e3200e"
b=json.load(open(f"{V}/_작업/후보/notion_bucket_초안.json"))
cl={x["rel"]:x for x in json.load(open(f"{V}/_작업/후보/notion_분류.json"))}
items=[]  # (bucket, size, rel, title, vg, note)
for bk,v in b.items():
    for s,r,t in v:
        if bk=="미분류":
            c=cl.get(r)
            nb=c["bucket"] if c else "EXCL"; vg=c.get("version_group","") if c else ""; note=c.get("note","") if c else ""
        else:
            nb=bk; vg=""; note=""
        items.append([nb,s,r,t,vg,note])
folder_rules=[("2023-2/서양 근대 철학","근세철학"),("2023-2/라틴어","고전어"),("그리스어 문법과 작문","고전어"),("2023-2/독일어","고전어"),("Plautus","고전어"),
 ("2025-1/심리철학연습","자기지식투명"),("2025-1/도덕적 책임 세미나","윤리책임"),("2025-1/사회철학연습","사회정치"),("2025-1/과학철학 과제 연구","과학철학"),("2025-1/개인공부","언어분석")]
for it in items:
    for k,nb in folder_rules:
        if k in it[2]:
            it[0]=nb;break
    if it[0].startswith("신규:"): it[0]="AI철학"
    if it[0]=="심리철학": it[0]="자기지식투명"
tot=collections.Counter(); 
for it in items: tot[it[0]]+=it[1]
print({k:v for k,v in tot.items()})
json.dump(items,open(f"{V}/_작업/후보/notion_최종분류.json","w"),ensure_ascii=False)
# 영문학 하위 구조
eng=collections.Counter()
for it in items:
    if it[0]=="영문학":
        parts=it[2].split("/")
        eng["/".join(parts[:3])[:60]]+=it[1]
print(sorted(eng.items(),key=lambda x:-x[1])[:20])
