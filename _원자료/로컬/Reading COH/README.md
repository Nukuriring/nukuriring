# Reading COH — Cavell, *Conditions Handsome and Unhandsome*

Stanley Cavell, *Conditions Handsome and Unhandsome: The Constitution of Emersonian Perfectionism* (The Carus Lectures, 1988). La Salle, Ill.: Open Court, 1990. © University of Chicago.

읽기·작업용 세팅. 원본은 스캔 PDF (189쪽, Acrobat OCR 레이어), 텍스트는 OCR 추출 후 **기계적 교정만** 적용 (원문 왜곡 위험이 없는 패턴만 수정).

## 파일 구조

| 파일 | 내용 | 원서 페이지 | 분량 |
|---|---|---|---|
| `text/01_preface.md` | Preface and Acknowledgments | xi–xxxix | ~12,800 단어 |
| `text/02_introduction.md` | Introduction: Staying the Course | 1–32 | ~14,200 |
| `text/03_lecture-1_aversive-thinking.md` | Aversive Thinking: Emersonian Representations in Heidegger and Nietzsche | 33–63 | ~13,500 |
| `text/04_lecture-2_argument-of-the-ordinary.md` | The Argument of the Ordinary: Scenes of Instruction in Wittgenstein and in Kripke | 64–100 | ~15,900 |
| `text/05_lecture-3_conversation-of-justice.md` | The Conversation of Justice: Rawls and the Drama of Consent | 101–126 | ~11,800 |
| `text/06_epilogue.md` | Epilogue | 127–128 | ~600 |
| `text/07_appendix-a_hope-against-hope.md` | Appendix A: Hope against Hope (Iona College 연설) | 129–138 | ~5,500 |
| `text/08_appendix-b_cover-letter.md` | Appendix B: A Cover Letter (예루살렘 워크숍) | 139–141 | ~1,400 |
| `text/09_bibliography.md` | Bibliography | 143–151 | ~3,100 |

보조 자료: `conditions-handsome-and-unhandsome.pdf` (원본), `_raw/full_raw_ocr.txt` (무교정 전체 OCR), `_scans/` (OCR 불량 페이지의 원본 이미지), `reading-log.md` (진행 기록).

## 페이지 참조 체계

- 본문 내 `[p. N]` = **원서 페이지 N의 시작**. 인용·출처 표기는 이 번호 기준.
- PDF 페이지 = 원서 페이지 + 38 (본문 arabic). 서문 roman: PDF = roman − 2.
- 원본 페이지 이미지가 필요하면: `pdftoppm -f <PDF쪽> -l <PDF쪽> -r 150 -gray -png conditions-handsome-and-unhandsome.pdf out`

## OCR 품질 주의사항

적용한 교정: 행말 하이픈 단어 재결합, 문단 리플로우, 러닝 헤더·페이지 번호 제거, 고유명사 소문자 j 복원 (John, Jerusalem 등), 연도 붙음 분리, 참고문헌 `).`→`J.` 등 확실한 패턴만.

남아 있는 오류 유형: 붙은 단어 (예: "literaturethat", "Nearthe"), 일부 em-dash 소실, 블록 인용 들여쓰기 소실 (인용문이 본문 문단에 합류), 이탤릭 정보 소실, 산발적 글자 오인식.

**OCR 불량 페이지** (스캔 여백 손상, 단어 누락 가능 — 정밀 독해·인용 시 `_scans/`의 원본 이미지로 대조할 것):
원서 p. 65, 68, 69, 72, 73, 76, 77, 79, 82 (강연 2) / p. 106, 107, 112, 122 (강연 3) / p. 130, 131 (부록 A). 파일명: `_scans/book-p<원서쪽>-<PDF쪽>.png`. 참고문헌 (p. 143–151)도 OCR 품질 낮음 — 서지 인용 시 원본 확인 권장.

## 읽기 세션 워크플로우 (v2)

**전체 기준은 `학습_프로토콜.md`** — 학습과학·LLM 정독 보고서 근거의 개정판. 요약 루프:

1. **P0 위치·목표** — `reading-log.md` 확인 + 지난 세션 24h 재현 항목 점검, 이번 착지 목표 1문장
2. **P1 정독·해설(진입로)** — explanation-first walkthrough, 불량 페이지는 `_scans/`로 대조, 어려운 전환점에서 정지
3. **P2 학습자 생성(반전)** — 사용자가 먼저 재구성 → Claude는 설명 말고 빈틈만 지적(파인먼)
4. **P3 적대적 검토** — 정독 도구(변증 지도·오독 탐지 등) 가동 + steelman-후-공격, 동의 유보
5. **P4 인출 검증(착지)** — 메커니즘 + 한 문장 정수를 무보조 재현
6. **P5 카드화·로그** — 원자 카드 선별 → `notes/`, `reading-log.md` 갱신 + 다음 세션 24h 재현 예약

상시 방어(아첨·설명깊이 착각·인용 날조·인지 오프로딩)와 붙여 쓰는 프롬프트 원형은 `학습_프로토콜.md` §2–§4 참조. 핵심 반전: **해설은 진입로, 인출은 목적지** — 세션은 Claude의 설명이 아니라 사용자의 무보조 재현으로 끝난다.
