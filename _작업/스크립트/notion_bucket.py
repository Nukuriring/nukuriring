import os,re,json,hashlib,collections,sys
ROOT=os.path.expanduser("~/mnt/Projects/Zettelkasten/_원자료/notion/Export-c8124db7-875f-40d8-b724-67e0c0e3200e")
REL="_원자료/notion/Export-c8124db7-875f-40d8-b724-67e0c0e3200e"
inc=["📚 철학 자료 아카이브/철학 자료 마스터","Untill 2025","스터디 트래커/대학생 시험 대비 공부 트래커","민법","부동산학개론","회계원리","컴퓨터 활용 능력"]
excl_dirs=["Music Tracker","Belinda","Frankfurt_Love","2024 - 산티아고"]  # placeholder decisions; Belinda/Frankfurt are lit? handled below
files=[]
for top in inc:
    for r,d,f in os.walk(os.path.join(ROOT,top)):
        for x in f:
            if x.endswith(".md"):
                p=os.path.join(r,x)
                files.append(p)
def clean(x): return re.sub(r"\s[0-9a-f]{32}","",x)
rules=[
 ("EXCL","Music Tracker|국민연금|종소세|옷살|LEET 출제|Untitled$|^새 |^Exercises|^OT$|^1단원|기출$|초고 작성|최종 제출|^수업$|Overview"),
 ("민법","^민법/"),
 ("실무","부동산학개론|회계원리|컴퓨터 활용"),
 ("영문학","미문개|현대 영미문학|문철대|영문학 특강|Plautus|Belinda|History of RockH|Alain de botton|Annotated Bib|Deutch|Frankfurt_Love/|문학과 철학의 대화|Thomas Dekker|매미신화|동 주앙|conditions handsome|겨울방학|그리스어 문법|독후감|독단론|2023-2/|2025-1/|산티아고"),
 ("한국철학","이황|이이|조광조|정도전|한국 ?철학사|조선|붕당|율곡"),
 ("양상형이상","핸드아웃\\d|양상|Fine|본질|형이상학|Metaphys|Disposition|powerful|power$|세계|상대주의|분철세미나|서근철연|Chance vs|separating|자연학|질료|형상|들창코|‘분리’|Time, rationality"),
 ("자기지식투명","Boyle|Self-kn|Aarnio|핸드아웃_ ?0|Moran|Μoran|Boghossian|Blind reasoning|투명성|transparency|Understanding and|Understanding and Inference|실행 투명|Quotation|^인용|Self-knowledge|special self|Response to Boghossian|Richard Moran|Anscombe|FTT|Williamson_Assertion|인트로덕션|Introduction$"),
 ("카벨","Cavell|CAvell|KAK|Must we mean|Knowing and Acknowledging|Now you know|Companionable|Claim of Reason|world viewed|Skepticism|Sckepticism|Ryle|비트겐슈타인|길들여진|Stanley|silence of the senses|Mcdowell|Macdowell|Mc_|Mind and World|Lecture 1"),
 ("합리성규범","Normativity|합리성|Rational|RTR|IBR|Kolodny|Kiesewetter|Southwood|Setiya|TNR|Why be|Bratman|Korsgard|instrumental|Fogal|Primacy|Dab -|Desir|desir|Authority of desire|What desires|Weakness of Will|Davidson|Dretske|Dreskte|Nozick|Quine|Importance of being|Unifying"),
 ("윤리책임","윤리학|Williams|윌리엄스|Singer|싱어|Hope|railton|Railton|Responsib|Blame|Trust, anger|Evil|월러스|도덕적|moral|Moral|도덕|보상이론|Bernard|Hegel|헤겔|Frankfurt|Love|Velleman|Comparing Theories|LVR|Metaphysics of Moral|Kant"),
 ("고대철학","국가|플라톤|Phaedrus|파이드로스|고르기아스|칼리클레스|트라시마코스|아리스토텔레스|Everyone by nature|서양 고중세|266d|티마이오스|메논|카르미데스|프로타고라스|동굴|선분|앎과 믿음|376d|377b|378b|379c|380d8|386a|좋음과 아름다움|자유$|고대철학|경험에 의한|2회차|^d$|Chapter 8|^Chapter|^chapter|3,4|정치학 1권|정치학 3권|4권 11|^2장|^3장|칼리클레스의 오도|GTP|266d"),
 ("사회정치","Iris|낸시|Ahmed|SEP_On|Veena|Sheth|kong|Kong|Algorithmic|Big data|Robots|Moral Standing|Creativity, Art|Intelligib|홉스|로크|루소|영원한 평화|알고리즘|사회철학|Orsi|정체성|intersection|Coalition|Khader|Betcher|Feminism|SIsterhood|Playfulness|interpretive account|유동적|유지 보수|Non-ideal|성평등|op-ed|ethics of Generative|여성|환경위기|미합중국|인간의 시작|정치학|정치|국가가|저자는 유럽|Kirby|커비|신도현|베넷|라투르|메이야수|유한성|데란다|푸코|바르트|벤야민|갤럽|신유물론|도맞손|도둑맞은|벨만|Bryson"),
 ("현상학","현상학|후설|후세르|하이데거|phenomenological|Phenomen"),
 ("과학철학","과학 ?철학|Hempel|Kitcher|Woodward|Kuhn|Explanation|Carnap|Criteria of Confirmation|Structural Identity|Ruben|레일턴 헴펠"),
 ("언어분석","Frege|Russell|스트로슨|Strawson|분석성|Analytic|analytic|Semantic|분석철학|Williamson on|윈랤슨|윈리엄슨|Williamson|명제|문장"),
 ("인식론","인식론|Gettier|김태우|게티어|신빙|지식귀속|Epistemic norms|Harman|evidence|Knowing|Let people merely|Sckep|SEP 정리"),
]
bucket=collections.defaultdict(list)
seen={}
for p in files:
    rel=os.path.relpath(p,ROOT)
    title=clean(os.path.basename(p))[:-3]
    key=clean(rel)
    sz=os.path.getsize(p)
    b=None
    for name,rx in rules:
        if re.search(rx,key) or (name!="EXCL" and re.search(rx,title)):
            b=name;break
    if b is None: b="미분류"
    bucket[b].append((sz,rel,title))
out={}
for b,v in bucket.items():
    print(b,len(v),sum(s for s,_,_ in v))
json.dump({b:[(s,r,t) for s,r,t in v] for b,v in bucket.items()},open(os.path.expanduser("~/scratch/bucket.json"),"w"),ensure_ascii=False)
print("미분류:", " | ".join(f"{t}({s//1000}k)" for s,_,t in bucket["미분류"]))
