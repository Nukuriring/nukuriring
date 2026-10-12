---
title: "Great divergence 챕터별 심화 학습 자료"
uuid: 16280657-5ad5-4b91-97ea-f04a0696bfa1
created: 2026-09-22
updated: 2026-09-22
project: "Great divergance"
url: https://claude.ai/chat/16280657-5ad5-4b91-97ea-f04a0696bfa1
turns: 12
type: 원자료/대화
---

> 요약: **Conversation overview**  The person is engaged in a chapter-by-chapter reading project of Kenneth Pomeranz's *The Great Divergence* (Princeton University Press, 2000), and asked Claude to produce a Korean-language companion reading piece for each chapter—not a simple summary, but an extensive, detail-oriented piece approximately 30 minutes in reading length that faithfully conveys the chapter's core arguments while enriching them with related materials, background context, and interesting additional narratives. The person has the book file on their local computer (not Google Drive, as Claude initially assumed), and uploads it for Claude to read directly.  The conversation involved three main tasks. First, Claude produced an initial companion piece for the Introduction based on the publicly available PDF rather than the person's file, which contained several factual and page-reference errors. Second, after the person clarified the file was on their computer (not Google Drive), Claude read the actual uploaded file, identified specific errors in the first draft, and corrected them—fixing the title of Part II, the page location of the coal/colonies argument, the scope of the geographic coverage section (adding the "densely populated" vs. "fully populated" distinction and the three reasons for geographic focus), the Yangzi Delta population figure placement, removing unverifiable claims (e.g., the Austen comparison, the 55% GDP figure), and correcting the ghost acreage and Hartwell iron production details. Third, the person asked a substantive question about the relationship between the California School and institutional/cliometric economic historians, which Claude answered in flowing prose covering the New Institutional Economics tradition (North, Acemoglu-Johnson-Robinson), cliometric wage and GDP comparisons (Broadberry, Allen, Li Bozhong/van Zanden), persistence studies (AJR, Nunn, Dell), and points of convergence and tension with Pomeranz's framework. Finally, the person asked Claude to save the corrected artifact to Google Drive.  The person prefers writing that avoids "A가 아니라 B" (A rather than B) contrast constructions entirely, prioritizes sentence-level flow and natural prose over structural outlines, uses rich Sino-Korean vocabulary with full grammatical particles, avoids em-dashes, and does not use bullet points in body text. They want the companion pieces to be faithful to the source text's argumentative sequence, include page references for cross-checking, clearly distinguish between book content and supplementary material, and only include verified information with sources. The person also expects Claude to check in before beginning long tasks rather than proceeding on assumptions—a correction explicitly made when Claude assumed the file was in Google Drive.  **Tool knowledge**  Google Drive file creation worked using `mcp__Google_Drive__create_file` with `contentMimeType` set to `text/html` rather than `text/markdown`. The markdown approach caused rendering problems: tilde characters used for Korean page-range notation (e.g., "3~27쪽") were interpreted as strikethrough markup, and bold formatting was inconsistently applied. Switching to HTML with explicit `<b>`, `<h2>`, `<h3>`, `<table>`, and `<p>` tags resolved all formatting issues. The `trash_file` operation requires additional permissions and failed silently, so duplicate files from failed attempts must be flagged to the person for manual deletion rather than removed programmatically. Reading back a newly created file using `mcp__Google_Drive__read_file_content` with the returned `fileId` is a reliable way to verify that formatting was applied correctly before reporting success to the person. For this person's Drive, files are created in the root "My Drive" folder by default, which was the desired location.

## 영진 · 2026-09-22T02:18

폴더 안에 Great divergance 책이 있을 거야.  챕터 하나씩 읽어보려고 해. 그런데 그냥 정리하는게 아니라 관련된 자료와 더 많은 이야기 거리를 추가해서 챕터의 핵심 요지를 충실하고 디테일하게 전달하면서 더 많은 재미있는 이야기 거리들을 추가한 읽을 거리를 만들어줬으면 좋겠어. 꽤 Extensive하고 Detail oriented된 책에는 그렇지만 충실한 그리고 분량이 꽤 길어서 한 reading time을 30분 정도 잡아야 하는 읽을 거리를 만들어줘

## Claude · 2026-09-22T02:25

케네스 포메란츠(Kenneth Pomeranz)의 『대분기(The Great Divergence)』로 알고 진행하겠습니다. 첫 회차는 서론(Introduction)으로 시작하겠습니다. 서론은 책 전체의 문제의식과 방법론, 여섯 개 장의 논증 구도를 한꺼번에 제시하기 때문에 이후 챕터를 읽을 때 기준점이 됩니다.

먼저 구글 드라이브에서 원문 파일을 찾아 서론을 직접 읽겠습니다. 그다음 서평과 후속 논쟁, 관련 일화를 조사해서 30분 분량의 읽을거리로 구성하겠습니다. 드라이브에서 파일을 찾지 못하면 공개된 원문 발췌와 연구 문헌을 근거로 작성하고, 그 사실을 글 첫머리에 밝혀 두겠습니다. 1장부터 시작하기를 원하시면 알려 주세요.

[tool_use: launch_extended_search_task]

포메란츠 『대분기』 서론 함께 읽기(제1회) 자료가 준비되었습니다. 프린스턴대 판본(2000) 서론 원문(pp. 3–25)을 저자가 전개한 순서대로 따라가며, 책의 방법론(비교·연결·서사, 상호적 비교, 다극적 세계), 유럽 중심 서사의 세 갈래와 두 무리(존스·하이날의 인구·생태·축적론, 브로델·월러스틴·노스·브레너의 시장·제도론), 그리고 석탄과 신대륙(유령 경지)이라는 핵심 논점을 정리했습니다. 아울러 '대분기'·'인볼루션'·'근면혁명' 용어의 계보, 캘리포니아 학파, 하트웰의 송대 철·석탄 연구, 황·브레너와의 논쟁, 브로드베리 등의 계량경제사, 한국 학계의 수용, 저자 소개 등을 곁가지로 담았고, 책 전체 구성 표와 참고 문헌, 다음 회차(1장) 예고까지 포함했습니다.

[tool_use: artifacts]

## 영진 · 2026-09-22T02:46
> 파일: The Great Divergence China, Europe, and the Making of the Modern World Economy (Kenneth Pomeranz) (z-library.sk, 1lib.sk, z-lib.sk).pdf

잠깐 드라이브 파일에 있는게 아니고 내 컴퓨터 있어

제발 중간에 확인해줘~

## Claude · 2026-09-22T02:49

[tool_use: view]

[tool_use: view]

[tool_use: bash_tool]

[tool_use: bash_tool]

[tool_use: bash_tool]

[tool_use: bash_tool]

파일 위치를 여쭤보지 않고 구글 드라이브에 있다고 가정한 채 조사를 시작했습니다. 먼저 확인드렸어야 했는데 죄송합니다. 앞으로는 긴 작업에 들어가기 전에 방향을 먼저 확인받겠습니다.

올려 주신 파일은 프린스턴대학출판부 2000년판(393쪽)입니다. 서론은 원서 3~27쪽에 걸쳐 있고, 일곱 개 절로 나뉩니다. 지난 읽을거리는 온라인에 공개된 같은 2000년판 원문을 근거로 작성되었습니다. 그래서 쪽수 체계와 전체 논지는 대체로 일치합니다. 다만 파일과 대조해 보니 바로잡아야 할 부분이 다섯 군데 있었습니다.

1. '지리적 범위에 관하여' 절(25~27쪽)의 내용을 잘못 전달했습니다. 이 절에서 포메란츠는 책이 세계 각 지역을 불균등하게 다룬다고 밝히고, 그 이유로 세 가지를 듭니다. 인구 밀도와 스미스적 분업의 관계, 인구가 '조밀한(densely populated)' 지역과 '포화된(fully populated)' 지역의 구분, 그리고 자신이 받은 학문적 훈련입니다. 특히 '포화된' 지역 개념은 3부의 생태 논의로 이어지는 중요한 개념인데 읽을거리에서 빠졌습니다. 그 절에 적어 둔 장강 삼각주 인구 수치(3,100만~3,700만 명)는 7쪽의 비교 단위 논의에 나오는 내용입니다. 핵심 지역 목록에 덧붙인 긴키(近畿) 지역은 원문에 없습니다.
2. 2부 제목을 잘못 번역했습니다. 원제는 "From New Ethos to New Economy? Consumption, Investment, and Capitalism"이므로 '새로운 에토스에서 새로운 경제로?'로 옮겨야 합니다.
3. 석탄과 식민지가 만든 '두 개의 결정적 단절'을 6쪽 각주에 나오는 것으로 표시했는데, 이 대목은 7쪽 본문에 있습니다.
4. 서론 분량을 '약 20쪽'으로 적었지만, 실제로는 약 25쪽입니다. '원래 아주 다른 책의 한 장으로 시작되었다'는 구절은 감사의 글(ix쪽)에 나오는데, 서론에 있는 것처럼 소개했습니다.
5. 도입부에서 첫 문장이 '『오만과 편견』의 첫 문장만큼 유명하다고 회자된다'고 썼는데, 이 서술은 근거를 찾지 못했습니다. 조사 과정에서 덧붙은 수사로 보이므로 삭제해야 합니다.

앞으로의 진행 방식도 제안드립니다. 챕터마다 원문 파일을 먼저 읽고 세 가지를 짧게 정리해서 보여 드리겠습니다. 원서의 절 구성을 따르는 논증 지도, 덧붙일 이야깃거리 후보, 그리고 예상 분량입니다. 확인해 주시면 그 구성대로 본문을 쓰겠습니다. 완성본의 쪽수와 인용은 파일과 대조해서 검증하겠습니다.

[tool_use: ask_user_input_v0]

## 영진 · 2026-09-22T02:50

질문: 지금은 어떻게 진행할까요?
답변: 서론 읽을거리 오류만 수정

## Claude · 2026-09-22T03:06

[tool_use: bash_tool]

[tool_use: bash_tool]

[tool_use: bash_tool]

[tool_use: bash_tool]

[tool_use: web_search]

[tool_use: web_search]

[tool_use: web_search]

[tool_use: bash_tool]

[tool_use: create_file]

## 영진 · 2026-09-22T03:20

계속

## Claude · 2026-09-22T03:25

[tool_use: create_file]

[tool_use: bash_tool]

[tool_use: bash_tool]

[tool_use: Artifact]

수정본을 올렸습니다. 앞서 말씀드린 다섯 군데를 고쳤고, 원서 파일과 서론 전체를 다시 대조하는 과정에서 네 군데를 더 찾아 바로잡았습니다.

첫째, 은 재화폐화 사례 뒤에 붙어 있던 "유럽 중심의 세계 체제가 아메리카를 착취한 것이 아니라…"라는 문장은 포메란츠의 논지를 왜곡하고 있었습니다. 이 문장은 원문(5쪽) 내용으로 바꾸었습니다. 전염병이 스페인 제국 성립에 결정적이었다는 점과, 헤게모니적 유럽 핵심부는 19세기 산업화가 상당히 진행된 뒤에야 말할 수 있다는 정리입니다. 둘째, 포메란츠가 양방향 비교로 "두 질문을 분리한다"고 쓴 대목은 방향이 반대였습니다. 원문(9쪽)에서 그는 두 질문을 서로 잇습니다. 셋째, 유령 경지의 900만·2,300만 에이커는 신대륙 면화로 만든 실을 양모로 대체할 때 필요한 목양지 면적이고, 석탄의 1,500만 에이커는 리글리의 추정치입니다(276쪽). 넷째, 생태 논의와 스기하라 논의의 순서를 원문 순서로 되돌렸습니다. 세부 표현도 원문에 맞췄습니다. 예를 들어 "기술을 창출한"은 "숙련을 쌓아 올린"으로, 브레너 요약의 "쫓겨난 농민이"는 "쫓겨난 농민 가운데 적어도 일부가"로 고쳤습니다.

곁가지 가운데 의심스러운 두 곳도 확인했습니다. 브로드베리 등이 말한 1700년은 양쪽 선도 지역을 견준 결과입니다. 이들에 따르면 중국 전체는 15세기 초에 이미 유럽의 가장 발전한 지역보다 상당히 가난했지만, 장강 삼각주는 1700년 무렵에야 뒤처졌고, 2021년의 재정리에서도 대분기가 1700년 무렵 시작되었다는 결론을 유지했습니다. 그래서 출처를 확인할 수 없던 "1700년에 유럽 선도국의 55%" 수치를 이 내용으로 바꾸었습니다. 하트웰은 1962년 논문에서 1078년의 철 생산량을 7만 5천 톤으로 추정했습니다. 흔히 인용되는 12만 5천 톤을 그 논문의 추정치로 소개한 부분을 고쳤고, 근거를 찾지 못한 1인당 소비 비교는 뺐습니다. 그 밖에 "페어뱅크 상을 두 번 받은 유일한 학자"라는 최상급 서술과, 「10년 후」에 관한 불분명한 서술도 확인 가능한 범위로 줄였습니다.

글 곳곳에 남아 있던 'A가 아니라 B' 구문은 명제를 그대로 두고 구문만 고쳤습니다. 나머지 곁가지는 이번에 하나씩 다시 검증하지 않았습니다. 캘리포니아 학파라는 명칭의 유래, 내권 유행어의 세부, 한국 학계의 수용 같은 부분입니다.

1장으로 넘어가실 때 말씀해 주세요. 원서를 먼저 읽고 논증 지도와 이야깃거리 후보, 예상 분량부터 정리해서 보여 드리겠습니다.

## 영진 · 2026-09-22T04:34

궁금한것 - 제도경제학 혹은 수량 경제학 부류의 장기 지속 연구 하는 계량 경제사학자들과 이들의 관계는 어떻게 되는거야?

## Claude · 2026-09-22T04:39

[tool_use: web_search]

여기서는 "장기 지속 연구"를, 먼 과거의 조건이 오늘날의 경제적 결과를 얼마나 규정하는지 계량적으로 추적하는 지속성(persistence) 연구까지 포함하는 넓은 뜻으로 받아들여 답하겠습니다. 요약하면 캘리포니아 학파는 질문과 가설을 던졌고, 제도경제학자와 계량경제사학자들은 자기 분과의 증거 기준으로 그 가설을 검증하면서 경쟁하는 설명을 내놓았습니다. 두 진영은 서로 논적이면서, 상대의 방법을 꾸준히 흡수해 온 협업자이기도 합니다.

먼저 출신 분과가 다릅니다. 캘리포니아 학파의 핵심 인물은 대부분 역사학자나 사회학자이고, 비교사적 서술과 1차 사료, 지역 연구의 축적을 주된 도구로 씁니다. 제도경제학과 계량경제사 쪽은 경제학과에서 훈련받은 연구자가 중심이며, 국민계정 추계, 실질임금 비교, 가격 이론, 회귀 분석을 증거의 기준으로 삼습니다. 그럼에도 『대분기』가 곧바로 경제학자들의 논쟁 상대가 된 데에는 이유가 있습니다. 포메란츠는 스미스적 성장이나 신고전파적 시장 같은 경제학의 어휘로 논지를 짰고, 유령 경지 같은 수량 추정까지 제시했습니다.

제도경제학과의 관계는 서론에서 이미 드러납니다. 포메란츠는 더글러스 노스를 명시적인 논적으로 지목합니다(원서 14~15쪽). 2장에서는 18세기 중국의 토지·노동·상품 시장이 서유럽보다 오히려 완전 경쟁에 더 가까웠다고 주장합니다(원서 17쪽). 효율적 시장과 재산권이 성장을 낳았다는 신제도주의의 잣대를 그대로 가져와서, 그 잣대로 재도 중국이 뒤지지 않는다는 것을 보이는 전략입니다.

이후 제도 쪽의 응답은 두 방향으로 전개되었습니다. 첫째는 대런 애쓰모글루, 사이먼 존슨, 제임스 로빈슨의 「유럽의 부상(The Rise of Europe)」(2005)입니다. 이 논문도 대서양 무역을 결정적 요인으로 꼽지만, 그 효과는 상인 세력을 키워 군주 권력을 제약하는 제도 변화를 거쳐 나타났다고 봅니다. 같은 대서양을 두고 포메란츠는 자원을, 이들은 제도를 매개로 지목한 셈입니다. 둘째는 국가와 정치 구조로 초점을 옮긴 연구들입니다. 캘리포니아 학파의 빈 웡은 경제학자 장로랑 로젠탈과 함께 『Before and Beyond Divergence』(2011)를 썼습니다. 이 책에 따르면 유럽의 정치적 분열과 잦은 전쟁이 제조업을 성벽 안의 도시로 몰아넣었습니다. 도시에서는 자본이 싸고 노동이 비쌌기 때문에 자본 집약적 기술이 촉진되었다는 것입니다. 학파 내부에서 정치경제학적 제도 설명이 나온 셈입니다. 존슨과 코야마의 「국가와 경제 성장: 역량과 제약」(2017) 같은 국가 역량 연구는 이 방향을 더 밀고 나갑니다. 캘리포니아 학파는 청조의 가벼운 과세를 민생을 중시한 농업 제국의 특징으로 조명했습니다. 국가 역량 연구는 같은 사실을 재정·행정 역량의 한계로 읽습니다.

계량경제사와의 관계는 가장 활발하고, 그만큼 긴장도 큽니다. "1750년까지 놀라운 유사성"이라는 명제는 검증 가능한 수량 가설로 받아들여졌고, 이후 실질임금 비교와 역사적 국민계정 추계가 쏟아졌습니다. 그 결과는 대체로 분기 시점을 1800년보다 앞당겼습니다. 브로드베리 등은 중국 전체가 15세기 초에 이미 유럽의 가장 발전한 지역보다 상당히 가난했고, 중국의 선도 지역인 장강 삼각주는 1700년 무렵에야 뒤처졌다고 봅니다. 그런데 이 결론을 얻어 낸 방법에는 캘리포니아 학파의 문제 제기가 흡수되어 있습니다. 양쪽의 선도 지역끼리 견주는 방식 자체가 포메란츠의 제안이었습니다. 브로드베리는 가드너와 함께 아프리카와 유럽을 비교한 2016년 논문의 제목에 아예 "상호적 비교"라는 말을 넣었습니다. 협업도 있었습니다. 리보중은 강남 경제사 연구로 포메란츠의 논지를 뒷받침했던 학자인데, 얀 라위턴 반 잔덴과 함께 장강 삼각주와 네덜란드의 국민계정을 직접 비교했습니다. 그 결과는 1820년대 네덜란드의 1인당 소득이 장강 삼각주보다 상당히 높았다는 것이었습니다. 학파와 가까운 연구자가 참여한 계량 연구가 학파의 강한 주장을 약화시킨 셈입니다.

역사학자 쪽의 반론도 이어졌습니다. 포메란츠는 「The Data We Have vs. the Data We Need」라는 글에서, 제목 그대로 지금 가진 자료와 결론에 필요한 자료 사이의 간극을 따졌습니다. 덩강(Kent Deng)과 패트릭 오브라이언은 명청 시대의 상대 임금 수준을 구성하는 데 쓰인 1차 사료를 검토해 그 통계적 기반을 비판했습니다. 『Seven Centuries of Unreal Wages』처럼, 과거 생활 수준을 재는 데 쓰여 온 임금 자료와 방법의 신뢰성을 겨냥한 논문집도 나왔습니다.

여기에는 서론과 이어지는 작은 반전이 있습니다. 서론에서 오브라이언은 "주변부는 주변적이었다"는 문장으로 포메란츠의 과녁이 되었던 인물입니다. 그런데 그는 2010년에 이 책이 촉발한 10년간의 논쟁을 정리하는 서평 논문을 썼습니다. 2020년에는 20년에 걸친 논쟁이 대체로 쿠즈네츠식 근대 경제사 패러다임 안에서 진행되었고, 바로 그 과정이 전근대의 대륙 간 상호적 비교에서 그 패러다임이 지닌 한계를 드러냈다고 평가했습니다. 이제는 계량 추계의 방법론 자체가 논쟁의 대상이 된 것입니다.

계량경제사학자라고 모두 캘리포니아 학파의 반대편에 서 있지는 않습니다. 로버트 앨런의 임금 자료는 "놀라운 유사성" 명제를 약화시켰습니다. 하지만 브리튼의 고임금과 값싼 석탄이 노동 절약 기술을 낳았다는 그의 설명은 석탄을 핵심 변수로 본다는 점에서 포메란츠와 겹칩니다. 유럽 안에서 북서유럽이 남유럽을 앞지른 과정을 다루는 "소분기(Little Divergence)" 연구도 비슷합니다. 흑사병을 유럽 내부 분기의 기원으로 보는 셰브케트 파무크의 연구(2007) 같은 작업은, "유럽의 기적"이라는 단위를 경계했던 포메란츠의 문제의식과 방향이 같습니다. 다만 분기의 기원을 훨씬 이른 시기로 잡는다는 점에서 포메란츠와 갈라집니다.

지속성 연구와의 관계는 가장 멀고, 문제의식의 방향도 거의 반대입니다. 이 계열에는 애쓰모글루·존슨·로빈슨의 식민지 제도 연구, 네이선 넌의 노예무역 연구, 멜리사 델의 페루 미타 연구, 코민·이스털리·공의 「국부는 기원전 1000년에 결정되었는가?」 같은 작업이 속합니다. 이들은 먼 과거의 조건이 수백 년 뒤의 경제적 결과로 이어지는 인과의 사슬을 회귀 분석으로 추적합니다. 이 계열은 대체로 분기가 일찍, 깊은 구조적 원인에서 비롯되었다는 그림을 그립니다. 캘리포니아 학파는 분기가 늦게, 우연적 국면에서 비롯되었다는 그림을 그립니다.

접점도 있습니다. 애쓰모글루 등의 「운명의 역전(Reversal of Fortune)」(2002)은 1500년에 인구가 조밀하고 도시화된 지역이 오늘날 오히려 가난해졌음을 보였습니다. 1500년의 비유럽 핵심부가 부유했다는 사실 인식은 캘리포니아 학파와 같습니다. 해석은 역전의 원인을 식민지 제도에서 찾는다는 점에서 갈립니다. 역사학자들은 이 계열에 두 가지 비판을 제기해 왔습니다. 하나는 수 세기에 걸친 과정을 두 시점 사이의 상관관계로 압축한다는 "역사의 압축" 비판(개러스 오스틴, 2008)입니다. 다른 하나는 공간적 자기상관 때문에 지속성 추정치가 부풀려질 수 있다는 통계적 비판(모건 켈리, 2019)입니다. 우연과 국면을 강조하는 캘리포니아 학파의 태도는 이 비판들과 같은 편에 있습니다.

그레고리 클라크의 『A Farewell to Alms』(2007)도 이 반대편 극에 속합니다. 클라크는 잉글랜드 사회에서 수백 년에 걸쳐 진행된 선택 과정으로 산업혁명을 설명합니다. 그가 캘리포니아대학 데이비스 캠퍼스의 경제학자라는 점은 작은 아이러니입니다. 이 캠퍼스는 캘리포니아 학파의 잭 골드스톤이 몸담았던 곳이기도 합니다.

최근 흐름은 수렴 쪽입니다. 빅토르 쿠르(2020)처럼 서로 달라 보이는 결정 요인들을 화해시키려는 재평가가 나왔고, 포메란츠 자신도 파르타사라티와 함께 대분기 논쟁을 정리하는 글(2019)을 썼습니다. 경제사학계의 다수 견해를 요약하면 두 가지입니다. 선도 지역 사이의 분기는 1800년보다 이른 18세기 무렵 시작되었고, 그 원인은 에너지, 국가와 제도, 지식 문화가 얽힌 복합적인 것이라는 정도입니다. 물론 그 추계의 자료가 얼마나 믿을 만한지는 여전히 다투어지고 있습니다.

캘리포니아 학파는 분기 시점에 관한 강한 주장에서는 밀렸습니다. 하지만 선도 지역끼리 견주고, 비교의 양쪽을 모두 설명 대상으로 삼고, 세계적 연결을 고려하라는 방법론적 요구는 계량경제사의 표준 절차 안으로 들어갔습니다. 질문의 틀은 캘리포니아 학파가 짰고 증거의 기준은 경제학자들이 정했으며, 오늘의 대분기 논쟁은 그 둘이 협상해 온 결과라고 보시면 됩니다.

이 대립은 1장과 2장의 인구·임금·시장 논의에서 구체적으로 드러납니다. 해당 회차 구성안을 짤 때 이야깃거리 후보로 올려 두겠습니다.

## 영진 · 2026-09-22T04:39

save the artifact 구글 드라이브에

## Claude · 2026-09-22T04:50

[tool_use: tool_search]

[tool_use: Google Drive:create_file]

[tool_use: tool_search]

[tool_use: Google Drive:read_file_content]

[tool_use: Google Drive:create_file]

[tool_use: Google Drive:read_file_content]

[tool_use: tool_search]

[tool_use: Google Drive:trash_file]

구글 드라이브의 내 드라이브 최상위 폴더에 구글 문서로 저장했습니다.

[『대분기』 서론 함께 읽기 (제1회, 수정본)](https://docs.google.com/document/d/1zILRHkYBJzNyvSq7KtUdklEu3E3F_Il1HC3Mk0XGeEw/edit)

처음에는 마크다운 파일을 그대로 올렸습니다. 그런데 변환 과정에서 쪽수 범위에 쓴 물결표(~)가 취소선 기호로 처리되어 몇몇 문단에 취소선이 그어졌고, 일부 굵은 글씨도 적용되지 않았습니다. 그래서 같은 내용을 HTML 형식으로 다시 올렸습니다. 저장된 문서를 다시 읽어서 물결표, 굵은 글씨, 표, 제목 서식이 제대로 들어갔는지도 확인했습니다.

다만 서식이 깨진 첫 번째 사본이 같은 제목으로 드라이브에 남아 있습니다([링크](https://docs.google.com/document/d/1DiNyDdNbfiPDBD0MFLEtkf_io6eKCU8PfhE0jtOwc0A/edit)). 휴지통으로 옮기려 했지만 승인을 받지 못해서 그대로 두었습니다. 제가 휴지통으로 옮길까요?
