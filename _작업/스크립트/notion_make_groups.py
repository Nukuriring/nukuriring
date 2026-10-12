import json,os,re,collections,math
V=os.path.expanduser("~/mnt/Projects/Zettelkasten")
REL="_원자료/notion/Export-c8124db7-875f-40d8-b724-67e0c0e3200e"
items=json.load(open(f"{V}/_작업/후보/notion_최종분류.json"))
CAP=560000
cluster={"자기지식투명":("자기지식과 투명성","자기지식"),"합리성규범":("행위와 실천이성","합리성과-행위"),"윤리책임":("윤리와 가치","윤리와-책임"),
 "고대철학":("고대철학","고대철학"),"사회정치":("정치·사회·역사·법","사회철학"),"영문학":("영문학과 문학비평","영문학"),"카벨":("카벨과 일상언어철학","카벨노트"),
 "양상형이상":("형이상학과 양상","형이상학"),"언어분석":("언어와 의미","언어분석"),"인식론":("인식론","인식론노트"),"근세철학":("근세철학","근세철학"),
 "한국철학":("한국철학","한국철학"),"현상학":("현상학과 대륙철학","현상학"),"과학철학":("과학철학","과학철학노트"),"AI철학":("AI와 윤리","AI철학"),
 "민법":("법학","민법"),"실무":("실용 지식","실무지식"),"고전어":("고전어","고전어")}
combo=[("NJ",["자기지식투명"]),("NR",["합리성규범"]),("NE",["윤리책임"]),("NA",["고대철학"]),("NP",["사회정치"]),("NL",["영문학"]),("NC",["카벨"]),("NM",["양상형이상"]),
 ("NK",["언어분석","인식론"]),("NX",["근세철학","한국철학"]),("NH",["현상학","과학철학","AI철학"]),("NZ",["민법","실무","고전어"])]
by=collections.defaultdict(list)
for bk,s,r,t,vg,note in items:
    if bk=="EXCL": continue
    by[bk].append((r,s,t,vg,note))
def netsizes(lst):
    mx={}
    for r,s,t,vg,n in lst:
        if vg: mx[vg]=max(mx.get(vg,0),s)
    out=[]
    for r,s,t,vg,n in lst:
        out.append(s if (not vg or s==mx[vg]) else 0)
    return out
num=41
groups=[]
for pref,bks in combo:
    chunks=[]  # (bucket, files)
    for bk in bks:
        lst=sorted(by[bk],key=lambda x:x[0])
        ns=netsizes(lst)
        tot=sum(ns)
        k=max(1,math.ceil(tot/CAP))
        target=tot/k
        cur=[];cs=0;parts=[]
        for f,n in zip(lst,ns):
            if cs+n>target*1.15 and cur and len(parts)<k-1:
                parts.append((cur,cs));cur=[];cs=0
            cur.append(f);cs+=n
        parts.append((cur,cs))
        for p,cs in parts: chunks.append((bk,p,cs))
    # chunk -> group number: combo with only one bucket may have several groups
    if len(bks)==1:
        for i,(bk,p,cs) in enumerate(chunks,1):
            groups.append((f"{pref}{i}",[(bk,p,cs)]))
    else:
        groups.append((f"{pref}1",chunks))
os.makedirs(f"{V}/_작업/그룹",exist_ok=True)
index=[]
for code,chs in groups:
    lines=["---","type: 작업",f"group: {code}","---"]
    desc=" + ".join(f"{bk}" for bk,_,_ in chs)
    lines.append(f"# 그룹 {code}: Notion 공부 노트 ({desc})\n")
    nums=[]
    for bk,p,cs in chs:
        nums.append((num,bk));num+=1
    for (n,bk),(bk2,p,cs) in zip(nums,chs):
        cl,tag=cluster[bk]
        lines.append(f"- 최상위 번호: {n} ({bk})")
        lines.append(f"  - 클러스터: {cl} (태그 `{tag}`), 원자료 실질 분량 약 {cs//1000}KB, 파일 {len(p)}개")
    lines.append("")
    lines.append("## 범위와 유의점")
    lines.append("- 원자료는 Notion 내보내기 파일입니다. 경로의 기준은 `"+REL+"`이고, 아래 목록의 상대 경로 앞에 이 기준을 붙입니다. 파일명 끝의 32자 해시는 Notion ID입니다.")
    lines.append("- 이 자료는 영진 님의 수업 필기, 강독 요약, 논평문(response), 발제문, 기말 논문입니다. 직접 쓴 논평문·발제문·논문에서 영진 님 본인의 주장은 voice `영진`으로 두고, 강의록과 읽은 글의 요약은 `문헌`으로 둡니다. 본인 주장인지 구별되지 않으면 `종합`으로 둡니다. 출처 절에는 Notion 파일명(해시 제외)과 수업명이나 날짜를 적습니다.")
    lines.append("- 같은 문서의 여러 버전(초안, 최종, 수정본)은 `버전 묶음`으로 표시했습니다. 가장 완성된 하나를 기준으로 삼고 나머지는 보조 자료로만 씁니다.")
    lines.append("- 이미 보관함에 있는 카드와 주제가 겹칠 수 있습니다(특히 자기지식, 카벨, 합리성, 증언, 지각). `번호표.md`와 `문헌/`을 먼저 확인하고, 같은 내용을 새 카드로 중복해서 만들지 않습니다. 겹치면 기존 카드로 링크하고, 새 정보나 다른 독해만 새 카드로 만듭니다.")
    lines.append("- 학번이나 수강 신청 정보 같은 개인 식별 정보와 성적, 제출 형식 지시는 카드에 옮기지 않습니다. 파일명에 학번이 있어도 출처 표기에서는 학번을 뺍니다.")
    lines.append("- 업무(출제·검토 등)와 개인 재정, 일정 정보는 옮기지 않습니다. 학술 내용이 없는 파일(목차만 있는 페이지, 빈 템플릿)은 건너뛰고 마무리 보고에 적습니다.")
    lines.append("- 한 파일이 100KB를 넘으면 구간으로 나누어 읽습니다. 책을 번역하거나 인용한 대목은 원문 인용으로 오해되지 않게 출처 절에 '필기'라고 표시합니다.")
    lines.append("")
    lines.append("## 원자료")
    for (n,bk),(bk2,p,cs) in zip(nums,chs):
        lines.append(f"### 번호 {n} ({bk})")
        for r,s,t,vg,note in p:
            tag=f" [버전 묶음: {vg}]" if vg else ""
            nt=f" ({note})" if note else ""
            lines.append(f"- `{r}` {s//1000}KB{tag}{nt}")
    open(f"{V}/_작업/그룹/{code}.md","w",encoding="utf-8").write("\n".join(lines)+"\n")
    index.append((code,[(n,bk) for n,bk in nums],sum(cs for _,_,cs in chs),sum(len(p) for _,p,_ in chs)))
for i in index: print(i)
print("last number",num-1)
