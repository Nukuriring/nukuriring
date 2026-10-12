# Big data’s disparate impact

초록: 데이터 마이닝과 같은 알고리즘 기술의 옹호자들은 이 기술들이 의사 결정 과정에서의 인간 편향을 제거한다고 주장한다. 그러나 알고리즘은 그것이 작업하는 데이터 만큼만 잘 작동할 수 있을 뿐이다. 데이터는 많은 경우 알고리즘이 이전 의사 결정 자의 편견들을 내재하도록 허락하곤 한다. 다른 경우에는 데이타는 그저 사회에서 지속하고 있는 널리 퍼진 편견들을 반영하기도 한다. 또 다른 경우, 데이터 마이닝은 놀라울정도로 유용한 규칙성들은 발견할 수도 있는데, 이런 규칙성들이 사실 이전에 존재하던 배제의 패턴 혹은 불평등의 패턴일 뿐이다. 데이터 마이닝에 대한 의존을 생각하지 않는 것은 역사적으로 불이익을 받았거나 취약한 집단들의 사회에 대한 온전한 참여를 제한하게 될 수 있다. 더 심각하게, 이러한 결과적인 차별은 거의 언제나 알고리즘 사용에 있어 비의도적인 발생적 속성인 이다. 프로그래머의 의식적인 선택이 아니라. 그럼에도 불구하고 문제의 원인이 무엇이고, 그것을 법정에서 설명하는 것은 비정상적으로 어려운 일이다.

**이 논문은 고용에서의 차별을 금지하는 Title VII의 관점을 통해 이러한 우려들을 살펴본다. 차별할 의도를 입증할 수 없는 경우, 데이터 마이닝의 피해자들에게 가장 유망한 법적 수단은 ‘간접차별(disparate impact)’ 법리로 보인다. 그러나 판례와 미국 고용평등기회위원회(Equal Employment Opportunity Commission)의 통일 가이드라인(Uniform Guidelines)은, 어떤 관행의 결과가 미래의 고용성과를 예측하는 것으로 입증될 경우, 그것이 ‘사업상 필요성(business necessity)’으로 정당화될 수 있다고 본다. 그리고 데이터 마이닝은 본래 그런 통계적 상관관계를 찾아내기 위해 고안된 기술이다. 만약 이 발견들이 허위임을 입증할 수 있는 실질적 방법이 없다면, Title VII은 이러한 알고리즘의 사용을 허용하는 셈이 되며, 그 결과로 나타나는 상관관계는 흔히 역사적인 편견의 패턴, 보호 집단에 대한 타인의 차별, 혹은 기초 데이터의 결함을 반영하게 될 것이다.**

이러한 비의도적 차별의 원인을 해결하고, 그에 대응하는 법의 결함을 시정하는 일은 기술적으로도, 법적으로도, 정치적으로도 어려운 과제이다. 계산 기술적으로는 달성할 수 있는 한계가 존재한다. 예컨대 차별이 데이터 자체가 과거의 의도적 차별의 산물이라는 점에서 발생할 경우, 이 오염된 과거 데이터를 정화하기 위한 명확한 방법이 존재하지 않는 경우가 많다. 데이터 마이닝 결과를 사후적으로 수정하는 시정 조치는 법적, 정치적으로 논쟁적인 영역을 건드릴 수 있다. 이러한 개혁을 둘러싼 어려움은 반차별법을 구성하는 두 주요 이론, 즉 **범주금지주의(anticlassification)**와 종속방지주의(antisubordination) 사이의 긴장을 뚜렷하게 부각시킨다. 빅데이터가 야기하는 간접차별 문제를 해결하기 위해서는, 단지 편견과 선입견을 제거하기 위한 최선의 노력만으로는 부족하며, ‘차별’과 ‘공정성’이라는 개념 전반을 전면적으로 재검토하는 작업이 필요하다.**

- 개념

제도적 차별(Institutional discrimination): Unconscious, implicit biases and inertia within society's institutions, rather than intentional choices, account for a large part of the disparate effect observed

existing law largely fails to address the discrimination that can result from data mining.

1. **현행 법체계, 특히 Title VII는 데이터 마이닝으로 인한 차별을 효과적으로 규제하지 못한다.**
2. 이 논의는 Title VII에 집중되지만, **문제는 Title VII만의 한계가 아니라, 전체 반차별법(jurisprudence)의 구조적 문제이다.**
    - 즉, **절차적 공정성(procedural fairness)** 중심의 기존 법이 **실질적 불평등의 재생산**을 방치하고 있다.
3. 따라서 고용 외의 다른 영역 (예: **주거, 장애, 신용, 보험**)에서도 **유사한 문제**, 즉 **구조적 약자를 또다시 불리하게 만드는 결과**가 나타날 가능성이 크다.

| Part | 주요 내용 | 중심 질문 |
| --- | --- | --- |
| **I** | 데이터 마이닝 과정이 차별을 어떻게 초래하는가 | "기술적 절차는 정말 중립적인가?" |
| **II** | 현행 Title VII 법리가 이를 규제할 수 있는가 | "법은 이 문제를 감지하고 책임을 묻는가?" |
| **III** | 이 문제를 해결하려면 어떤 개혁이 필요한가 | "차별과 공정성을 다시 정의할 필요가 있는가?" |
- 5가지 데이터 마이닝 메커니즘 where disproportionately adverse outcomes might occur
    - Target variable과 Class label의 설정

| 항목 | 설명 |
| --- | --- |
| **데이터 분석** | 의미 있는 통계적 패턴을 자동 발견하여 예측·분류에 활용하는 작업 |
| **Target Variable** | 예측하려는 속성 또는 문제 정의 (예: 근속 기간, 생산성 등) |
| **Class Labels** | Target을 구분하는 분류 범주 (예: 3개월 이상 vs. 미만) |
| **과정** | 문제 정의 → 변수 설정 → 레이블링 → 모델 훈련 → 적용 |
| **내재 위험** | 문제 정의 자체의 주관성, 프록시 학습, 구조적 편향의 재생산 |
- 학습 데이터

| 구분 | 메커니즘 1 | 메커니즘 2 |
| --- | --- | --- |
| **이름** | **편견을 내포한 사례 학습** (Learning from prejudiced decisions) | **편향된 표본 학습** (Learning from a biased sample) |
| **핵심 구조** | 과거의 **차별적 결정**을 정당한 학습 자료로 수용 | 데이터셋 자체가 **특정 집단을 과소·과대표집** |
| **원인** | 예: 편향된 인간 판단이 포함된 과거 라벨링 | 예: 데이터가 일부 집단을 체계적으로 누락 |
| **위험 결과** | 알고리즘이 **차별 규칙을 그대로 재생산** | 특정 집단에 대한 **시스템적 불이익** 발생 |
| **유형** | **잘못된 라벨링** (Improper labeling) | **비대표적 표본 구성** (Sampling bias) |
| **예시** | - 여성 지원자가 과거 ‘적합하지 않다’는 평가를 받은 사례들을 그대로 학습에 사용 → 여성은 부적합하다는 규칙 학습- 판사의 인종 편견이 반영된 과거 판결 데이터를 모델이 학습 | - 고소득 백인 남성 위주의 금융 데이터만 학습 → 저소득층이나 소수 인종에 대해 정확히 예측 못하거나 과소평가- 장애인을 포함하지 않은 생산성 데이터셋 사용으로, 장애인을 과소평가 |
- **훈련 데이터의 라벨링은 본질적으로 주관적이다.**  분석가가 부여하는 class label은 해석과 판단을 수반하며, 객관적으로 결정되지 않는다. **과거의 편견이 반영된 결정이 라벨로 사용되면, 모델은 그 편견을 학습한다.** 과거의 차별적 판단이 ‘정답’으로 전제될 경우, 알고리즘은 이를 일반화된 규칙으로 내면화한다. **라벨링 기준이 애매하거나 경계가 자의적일 경우, 사례들이 부정확하게 분류된다.** 이는 라벨의 불일관성과 분류의 오류로 이어지고, 결국 판단의 왜곡을 낳는다. **훈련 데이터에 포함된 편향은 평가(validation) 단계에서도 그대로 유지된다.** 훈련 데이터의 문제는 평가 지표에 감춰져 감지되기 어렵다. **이로 인해 과거 개인들의 편견이 구조화된 판단 규칙으로 전화된다.** 차별은 더 이상 개인의 판단이 아니라, 시스템적 결과로 제도화된다.
- **사례: St. George’s 병원의 입학 결정 자동화**
    
    → 과거 여성과 유색인종에 불리했던 결정을 학습한 알고리즘이 동일한 차별을 재생산하였다.
    
- **현행 사용자 행동도 편향된 라벨링의 근거가 될 수 있다.**
    
    → 예: 흑인 이름 검색 시 체포 기록 광고가 더 자주 나타나는 현상은 사용자 클릭 패턴이 차별적이기 때문이다.
    

- Data set problem

### I. **전제: 데이터 수집은 중립적이지 않다**

- 데이터 마이닝의 효과는 전적으로 **수집된 데이터의 품질과 대표성**에 의존한다.
- 그러나 실제 데이터는 다음과 같은 문제를 안고 있다:
    - **개별 기록이 오류를 포함할 수 있음**
    - **특정 집단(보호집단)에 속한 사람들의 기록은 더 높은 비율로 오류를 포함**
    - **전체 데이터셋에서 보호집단이 과소대표될 수 있음**

→ 즉, **데이터의 품질과 대표성은 계층/집단에 따라 체계적으로 다를 수 있음**.

---

### II. **차별 발생 방식: 네 가지 구조적 메커니즘**

### 1. **불균등한 데이터 품질**

- 사회적 약자일수록 **형식 경제(formal economy)에 덜 참여**, **온라인 기술 접근성 낮음**, **시장 대상에서 제외**.
- 결과적으로:
    - 이들의 기록은 더 **부정확하고 미완성**되어 있으며,
    - **관측 자체가 덜 이루어짐** (예: 신용기록, 고용 이력 등).

### 2. **체계적 과소대표 (Systematic Underrepresentation)**

- 보호집단의 삶은 덜 "데이터화(datafied)"됨.
- 데이터 기반 분석에서 이들은 **보이지 않게 되며**, **정책·자원·기회 분배에서 배제됨**.

### 3. **편향된 기록과 ‘잘못된 일반화’**

- 기업은 과거 데이터에서 유도된 패턴을 **일반화된 규칙**으로 사용함.
- 하지만 그 데이터가 **왜곡된 샘플에 기반**한다면, 생성된 규칙은 **특정 집단을 구조적으로 불이익**에 빠뜨림.
    - 예: 한 회사가 과거 직원 데이터를 기반으로 신입 지원자를 평가할 경우,
        - 기존 직원 구성 자체가 편향되어 있다면 → 미래 예측도 왜곡됨.

### 4. **과잉 감시와 과잉 기록**

- 보호집단이 **불균형적으로 더 많이 감시**될 경우, 이들의 실수나 위반도 더 많이 기록됨.
- 이후 관리자들은 이러한 **편향된 데이터에 기반해 더 많은 감시를 가함**.
- 결과: **편견을 강화하는 순환 구조** 형성.

---

### III. **구체적 사례**

### 📍 1. **Street Bump 사례 (보스턴)**

- 스마트폰 센서를 통해 도로 파손 자동 감지.
- 문제: **스마트폰 보급 불균형 → 저소득층 지역에서 데이터가 덜 수집됨**.
- 결과: 도시 자원이 보호집단 지역에 **덜 배정**, **차별적 서비스 격차** 발생.

### 📍 2. **온라인 채용 플랫폼**

- 고용주가 **영상 이력서, 디지털 플랫폼** 등 첨단 방식에 의존할 경우:
    - **디지털 접근성 낮은 보호집단은 지원조차 어려움**.
    - 데이터상 **관심 없음/부적격자**로 간주되어 **재배치, 추천에서 제외됨**.

### 📍 3. **직장 내 과도한 감시**

- 특정 인종/집단에 대해 더 많이 감시함 → **더 많은 잘못이 ‘기록’됨**.
- 다음 관리자는 이 데이터를 바탕으로 **해당 집단을 ‘리스크’로 간주**.
- 결과: 차별적 감시 → 더 많은 기록 → 편견 강화의 자기강화 구조.

---

### IV. **결론 및 함의**

- **데이터 수집의 대표성과 품질이 보호집단과 구조적으로 연결**되어 있을 경우,
    
    → 데이터 마이닝은 **편견과 차별을 학습, 재생산, 심화**한다.
    
- 이는 단지 과거를 반영하는 것이 아니라, **미래의 기회와 평가 구조까지 오염시킴**.
- 편향된 데이터를 통한 예측은:
    1. 보호집단을 시스템적으로 배제하며,
    2. 이후의 데이터마저도 더욱 편향되게 만드는 **구조적 순환 고리**를 형성한다.

- Feautre selction

### 정의: Feature Selection이란 무엇인가?

> “Through a process called ‘feature selection,’ organizations and the data miners that work for them make choices about what attributes they observe and subsequently fold into their analyses.” (p. 688)
> 
- 즉, **feature selection**은 데이터 마이닝 과정에서 **분석에 포함할 속성(변수)을 선택**하는 절차로,
    
    현실 세계의 복잡한 개체를 모델이 다룰 수 있는 **단순한 수치적 표현**으로 환원하는 방식이다.
    

그러나 이 선택은 중립적인 기술적 과정이 아니라, 특정 집단에 대해 **체계적으로 부정확한 판단을 초래할 수 있는 결정적인 관문**이 된다.

### 1. **속성 선택의 미비로 인한 정확도 격차**

> “Members of protected classes may find that they are subject to systematically less accurate classifications or predictions because the details necessary to achieve equally accurate determinations reside at a level of granularity and coverage that the selected features fail to achieve.” (p. 688)
> 
- 보호집단은 자신의 특성을 **정확히 표현해줄 수 있는 고해상도(high-resolution) 정보가 분석에서 누락**되거나 축약되어,
    
    → **일관되게 부정확한 판단을 받게 되는 구조적 불이익**을 겪는다.
    
1. **현실의 복잡성에 대한 표현 불가능성**

> “It is often impossible to collect all the attributes of a subject or take all the environmental factors into account with a model.”
> 
> 
> *(Calders & Zliobaite, p. 688)*
> 
- 데이터는 항상 **현실의 축소된 표현**일 뿐이며,
    
    모델이 **모든 인과적 요인을 포괄하기는 구조적으로 불가능하다.**
    

→ 하지만 이 **불가피한 정보 누락**은 일부 집단에게 **더 큰 부정확성과 불이익**을 야기한다는 점에서 차별과 연결된다.

### **3. 통계적 합리성과 윤리적 불공정성의 충돌**

> “Decision makers that rely on statistically sound but nonuniversal generalizations ‘are being simultaneously rational and unfair’ because certain individuals are ‘actuarially saddled’ by statistically sound inferences that are nevertheless inaccurate.”
> 
> 
> *(Schauer, p. 689)*
> 
- 즉, **통계적으로 유효하더라도**,
    
    그것이 개별적으로 부당한 결과를 낳는다면 → 그것은 **합리적이면서도 불공정한 판단**이 된다.
    

4. **정보 비용 회피를 통한 정당화**

> “Obtaining information that is sufficiently rich to permit precise distinctions can be expensive.... Even marginal improvements in accuracy may come at significant practical costs.” (p. 689)
> 
- 보호집단에 대한 더 정확한 분류를 위해 **더 정밀한 정보가 필요하지만**,
    
    조직은 **비용 효율성(cost-efficiency)**을 이유로 **부정확한 대체변수(coarse features)**를 선택하게 된다.
    

→ 이는 결과적으로 보호집단에 대해 **높은 오류율을 감수하면서도 정당화되는 구조적 차별**을 낳는다.

### III. 📚 구체적 사례들

### A. **출신 대학을 feature로 활용하는 고용 관행**

> “Hiring decisions that consider academic credentials tend to assign enormous weight to the reputation of the college or university... even though such reputations may communicate very little about the applicant’s job-related skills.” (p. 689)
> 
- 명문대 졸업자 선호는 **비용 없이 정보를 전달하는 수단**이지만,
    
    명문대 진입이 어려운 보호집단은 → **체계적으로 탈락**하게 된다.
    

---

### B. **Redlining (지역 기반 금융 차별)**

> “Decision makers can argue that they are willing to tolerate higher rates of erroneous determinations for certain groups because the benefits derived from more granular data... do not justify the costs.” (p. 690)
> 
- 금융기관이 **거주 지역 정보**로 위험도를 판단할 때,
    
    지역 내부의 실제 다양성을 무시하고 → **보호집단이 밀집된 지역 전체를 배제**하는 결과가 초래된다.
    

---

### C. **형사기록 접근 불가 시 인종을 proxy로 활용하는 사례**

> “When employers lack access to criminal records, they may consider race in assessing an applicant’s likelihood of having a criminal record because there are statistical differences...”
> 
> 
> *(Strahilevitz, p. 691)*
> 
- 명시적 인종 차별은 없어도, **정보 부족을 보완하려는 시도에서 인종이 부정확한 대체지표로 사용**될 수 있다.

### I. 📌 정의: Proxy란 무엇인가?

- **Proxy**란, 특정한 속성이 **표면상으로는 중립적**이지만, 실제로는 **보호집단에 대한 소속 정보를 우회적으로 암시하는 변수**를 말한다.
- 즉, **“합리적 기준처럼 보이는 요소들이 보호집단의 구성원 여부를 간접적으로 반영”**하는 경우이다.

> “The criteria that are genuinely relevant in making rational and well-informed decisions also happen to serve as reliable proxies for class membership.”
> 
> 
> (*p. 691*)
> 

---

### II. ⚠️ 문제 제기: 왜 프록시가 위험한가?

### 1. **차별적 의도가 없더라도, 불리한 결과를 반복한다**

- 결정자는 합리적이고 예측력 높은 속성을 사용하려 하지만,
    
    그 속성들이 우연히 보호집단과 **높은 상관관계(correlation)**를 가지면 →
    
    **예측력이 높아질수록 차별도 강화**됨.
    

> “Decision makers do not necessarily intend this disparate impact... [but] their reasonable priorities as profit seekers unintentionally recapitulate the inequality that happens to exist in society.”
> 
> 
> (*p. 691*)
> 

---

### 2. **불평등의 원인을 학습하게 되는 모델의 역설**

- 과거 데이터가 단지 차별을 담고 있는 것이 아니라,
    
    **실제로 성과 차이를 반영**하는 경우도 있음.
    

> “Data mining ‘may discover patterns of lower performances, skills or capacities of protected-by-law groups.’”
> 
> 
> (*Romei & Ruggieri, quoted p. 691*)
> 
- 이때, 데이터 마이닝은 **차별을 단순히 반영하는 것이 아니라,
정확도를 높이려 할수록 그 차별을 더 정확하게 재현**하게 된다.

> “Better data and more features will simply come closer to exposing the exact extent of inequality.”
> 
> 
> (*p. 692*)
> 

---

### III. 🧠 메커니즘: 왜 차별은 제거되지 않는가?

### A. **비차별적 변수도 보호집단 정보를 ‘중복 부호화’(redundant encoding)할 수 있다**

> “The problem stems from what researchers call ‘redundant encodings,’ cases in which membership in a protected class happens to be encoded in other data.”
> 
> 
> (*p. 691*)
> 
- 예: 범죄기록은 인종을 삭제하더라도,
    
    **거주지역, 소득, 교육 수준** 등과 연동되어 여전히 **인종 정보를 암시**함.
    

---

### B. **모든 차별적 효과가 '나쁜 데이터'에서 기인하지 않는다**

- 심지어 다음 조건이 모두 충족되더라도 차별은 발생할 수 있다:
    1. 데이터셋에 편견 없음
    2. 금지된 변수 제거됨
    3. 피처가 정교하고 다양함
    4. 목적은 순수하게 정확도 극대화임

> “This may occur even if proscribed criteria have been removed... and the only goal is to maximize classificatory or predictive accuracy.”
> 
> 
> (*p. 691*)
> 

→ 즉, **정확하고 공정한 모델일수록 오히려 사회적 불평등을 더 정확히 재현**해버리는 구조.

---

### IV. 📚 예시적 정식화 (암시적 사례)

- 고용주가 성과 예측을 위해 생산성, 이직률, 근무 시간 등을 고려할 경우,
    
    이 요소들이 **보호집단의 구성원들이 체계적으로 덜 보유한 특성**이라면:
    
    → 해당 집단에 **일관되게 불리한 예측**이 발생.
    

> “Employers may find that they subject members of protected groups to consistently disadvantageous treatment because the criteria that determine the attractiveness of employees happen to be held at systematically lower rates by members of these groups.”
> 
> 
> (*p. 691*)
> 

### I. 📌 정의: Masking이란 무엇인가?

- **Masking**은 **의도적 차별(intentional discrimination)**을 기술적으로 은폐할 수 있게 해주는 메커니즘이다.
- 즉, 데이터 마이닝이 외관상 합리적이고 중립적인 판단처럼 보이지만,
    
    실제로는 **편향된 입력·분석 방식을 고의로 설계하여 차별을 유도**할 수 있다.
    

> “Any form of discrimination that happens unintentionally can also be orchestrated intentionally.”
> 
> 
> (*p. 692*)
> 

---

### II. ⚙️ 작동 방식: 의도적 차별을 은폐하는 방법들

저자는 기존 네 가지 메커니즘(Target Variable, Labeling, Data Collection, Feature Selection, Proxies)을 **차별을 의도적으로 설계하는 수단**으로 전환시킬 수 있다고 본다:

### 1. **데이터 수집의 편향을 의도적으로 조작**

> “Decision makers could knowingly and purposefully bias the collection of data to ensure that mining suggests rules that are less favorable to members of protected classes.”
> 
> 
> (*p. 692*)
> 

### 2. **과거 편향된 결정들을 정당한 훈련 데이터로 간주**

> “They could... preserve the known effects of prejudice in prior decision making by insisting that such decisions constitute a reliable and impartial set of examples.”
> 
> 
> (*p. 692*)
> 

### 3. **의도적으로 정보의 해상도를 낮춰 보호집단 배제**

> “Decision makers could intentionally rely on features that only permit coarse-grained distinction making... and justify writing off entire groups composed disproportionately of members of protected classes.”
> 
> 
> (*p. 692*)
> 

이러한 방식은, 저자가 말하듯 "**디지털 레드라이닝(digital redlining)**"을 정교하게 가능하게 한다.

---

### III. ⚠️ 구조적 위험: 왜 마스킹은 더 위험한가?

### A. **보호집단 정보를 직접 알지 않아도 차별 가능**

> “Data mining could grant decision makers the ability to distinguish and disadvantage members of protected classes even if those decision makers do not have access to explicit information about individuals’ class membership.”
> 
> 
> (*p. 693*)
> 
- 즉, 명시적 인종이나 성별 정보 없이도, 데이터 마이닝은 **프록시(proxy)**를 통해 **소속 집단을 우회적으로 식별**하고 차별할 수 있다.

---

### B. **불법적 동기를 감추는 기술적 정당화**

> “Data mining could provide cover for intentional discrimination... because the process conceals the fact that decision makers determined and considered the individual's class membership.”
> 
> 
> (*p. 693*)
> 
- 이처럼 **데이터 마이닝은 동기의 흔적을 지우기 때문에**,
    
    실제로 의도적 차별이 있어도 **법적 입증이 어려워짐**.
    

---

### IV. 🧠 법적・정치적 함의

- 마스킹은 단지 기술 문제를 넘어, **법적 책임 회피 수단**으로 악용될 수 있다.
- 특히, **Title VII 하에서 의도적 차별(intent)**이 법적 판단의 핵심일 때,
    
    → 마스킹은 **입증 불가능한 차별**을 가능하게 만든다.
    

> “Most cases of employment discrimination are already sufficiently difficult to prove; employers motivated by conscious prejudice would have little to gain by pursuing these complex and costly mechanisms to further mask their intentions.”
> 
> 
> (*p. 693*)
> 
- 그러나 저자는 **의도적 차별보다 더 심각하고 빈번한 문제는 오히려 ‘비의도적 차별’**이라고 결론지으며,
    
    마스킹은 그 중 하나의 국면에 불과하다고 지적한다.
    

> “Unintentional discrimination is the more pressing concern because it is likely to be far more common and easier to overlook.”
> 
> 
> (*p. 693*)
> 

- 법리적 책임

### I. 📌 Title VII 책임 구조 개관

고용주(employer)는 Title VII 위반 혐의로 **두 가지 법리적 경로**에서 책임을 질 수 있다:

1. **Disparate Treatment** (차별적 취급)
2. **Disparate Impact** (차별적 결과)

---

### II. 🧷 Disparate Treatment (의도적 차별)

### 1. 구성요소 (두 갈래):

> “Disparate treatment comprises two different strains of discrimination: (1) formal disparate treatment of similarly situated people and (2) intent to discriminate.”
> 
- **(1) 형식적 차별**: 동일한 상황에 있는 사람들을 다르게 대우한 경우
- **(2) 의도적 차별**: 차별적 대우를 하려는 고의(intent 또는 motive)를 입증해야 함

### 2. 특징:

- **중심 쟁점**: **의도(intent)** 여부
- 원고는 **고의적 차별의 증거**를 제시해야 하며, 이는 종종 간접적 정황증거로 판단됨

---

### III. ⚠️ Disparate Impact (의도와 무관한 결과 중심 차별)

> “Disparate impact refers to policies or practices that are facially neutral but have a disproportionately adverse impact on protected classes.”
> 

### 1. 구성요소 (3단계 테스트):

> “The doctrine first asks whether there is a disparate impact on members of a protected class, then whether there is some business justification for that impact, and finally, whether there were less discriminatory means of achieving the same result.”
> 
- **(1) Disparate Impact**: 외관상 중립적인 정책이 **보호집단에 불균형적으로 불리한 영향을 주는지**를 판단
- **(2) Business Necessity**: 피고(고용주)가 해당 정책의 **합리적 업무상 필요성**을 증명할 기회가 주어짐
- **(3) Less Discriminatory Alternative**: 원고가 **동등한 목적을 달성할 수 있는 덜 차별적인 대안**이 있었음을 보여주면 → 고용주는 책임을 지게 됨

### 2. 특징:

- **의도(intent)는 불문**함 — 차별의 목적이 없어도, **결과가 문제**이면 책임 발생 가능
- **정책 자체가 차별적으로 보일 필요 없음** (외형상 중립 가능)

### 1. Formal Disparate Treatment: “Protected Class as Input”

**가능한 경우:**

데이터 마이닝 시스템이 보호된 클래스(예: 인종, 성별)를 **직접적인 입력 변수(feature)** 로 포함한 경우, 결과와 무관하게 **법적으로 금지된 분류 행위**가 발생하므로 책임이 성립됩니다.

- 저자는 이 경우를 “formal discrimination”이라 부르며, 그 자체로 법적 해악을 구성한다고 주장합니다:
    
    > “Considering membership in a protected class as a potential proxy is a legal classificatory harm in itself.” (p. 695)
    > 
- 심지어 그 특성이 **결과에 아무런 영향을 주지 않아도**, 분류 행위 자체가 위법입니다:
    
    > “Because classification itself can be a legal harm, irrespective of the effect, the same should be true of using protected class as an input.” (p. 695)
    > 

**제한점:** 그러나, 보호된 클래스가 직접 feature로 포함되는 경우는 실제 데이터 마이닝에서 드뭅니다. 실질적 쟁점은 대부분 **비의도적 차별**이나 **프록시를 통한 간접 차별**입니다. 여기서부터 법리는 취약해집니다.

---

### 2. Masking: **의도적 차별의 은폐**

**책임이 성립하는 경우:**

의도적인 차별을 위장한 형태로, 예컨대 데이터 수집이나 feature selection을 의도적으로 조작하여 보호된 클래스를 불이익 처리하는 규칙을 유도하는 경우입니다.

- 이 경우는 **Disparate Treatment**의 전형적인 사례이며, masking은 본질적으로 "pretext"로 간주됩니다:
    
    > “The fact that it is accomplished algorithmically does not make it less of a disparate treatment violation, as the entire idea of masking is pretextual.” (p. 697)
    > 

**어려움:**

다만, **의도를 입증하는 것이 매우 어렵다**는 점이 핵심 장애입니다. 저자는 이렇게 지적합니다:

> “Like in any disparate treatment case, however, proof will be difficult to come by, something even truer for masking.” (p. 697)
> 

---

### 3. Labeling Examples / Data Collection / Feature Selection / Proxies:

→ **비의도적 차별 메커니즘 (Unintentional Discrimination)**

**Disparate Treatment의 한계:**

위의 네 가지 메커니즘은 모두 의도하지 않은 구조적 차별을 만들어낼 수 있지만, Disparate Treatment 법리는 이들을 다룰 수 없습니다. 왜냐하면 현행 법리는 **의도(intent)** 또는 **동기(motive)**를 중심으로 구성되어 있기 때문입니다.

- 예컨대 McDonnell-Douglas 체계는 “프리텍스트(pretext)”의 존재를 밝혀야 하며, 이는 **의도적 차별**이 있어야만 성립합니다:
    
    > “Under the McDonnell-Douglas framework, a court must find either that the employer intended to discriminate or did not discriminate at all. Thus, unintentional discrimination will not lead to liability.” (p. 699)
    > 
- 설령 데이터 마이닝 알고리즘이 구조적으로 차별적인 결과를 산출하더라도, **의도나 동기를 입증할 수 없다면 책임 없음**:
    
    > “The doctrine focuses on human decision makers as discriminators… Even if disparate treatment doctrine could capture unintentional discrimination, it would only address such discrimination stemming from human bias.” (p. 700)
    > 

---

### 4. 지식 기반의 결정(intention vs. knowledge)

흥미로운 회색지대는, 알고리즘이 **차별적 결과를 낳을 것을 알면서도 사용하는 경우**입니다.

- 이 경우를 두고 저자는 다음과 같이 문제를 제기합니다:
    
    > “If an employer intends to employ the model, but knows it will produce a disparate impact, does she intend to discriminate?” (p. 701)
    > 
- 하지만 **지식(knowledge)**과 **의도(intent)**는 구별되며, 현재 법리는 **지식만으로는 책임을 묻기 어렵다**고 봅니다:
    
    > “Neither pretext nor motive exists here, and throughout civil and criminal law, ‘knowledge’ and ‘intent’ are considered distinct states of mind.” (p. 701)
    > 

---

### 결론: Disparate Treatment 법리의 포착 한계

- 유효하게 포착하는 메커니즘:
    - Formal Discrimination (클래스 변수 사용)
    - Masking (의도적 차별의 위장)
- 포착하지 못하는 메커니즘:
    - Labeling Examples
    - Data Collection
    - Feature Selection
    - Proxy 사용

이는 현행 법리의 **의도 중심 패러다임**이 데이터 기반 차별의 새로운 양태—특히 비의도적이고 구조적인 차별—을 감지하고 규율하는 데 **근본적 한계**를 드러냅니다.

## I. Business Necessity Defense

### 1. 법적 구조

“Business necessity”는 고용주의 차별적 효과를 낳는 고용 관행에 대해 **정당화 논거를 제시할 수 있는 유일한 방어 수단**이다:

> “This defense is, in a very real sense, the crux of disparate impact analysis, weighing Title VII's competing goals of limiting the effects of discrimination while allowing employers discretion to advance important business goals.” (p. 703)
> 

### 2. 판례 발전사와 기준의 형성

### ⮕ **Griggs v. Duke Power Co., 401 U.S. 424 (1971)**

- 원고는 고졸 학력과 지능검사가 흑인에게 불리하게 작용한다고 주장
- 대법원은 그 관행이 직무 성과와 직접적 관련이 없다는 이유로 이를 차별로 판단

> “The touchstone is business necessity. If an employment practice which operates to exclude Negroes cannot be shown to be related to job performance, the practice is prohibited.” (Griggs, at 431; p. 703)
> 

⟶ 이 판례에서 법원은 **“manifest relationship to job performance”**라는 기준을 최초 제시

---

### ⮕ **NYC Transit Auth. v. Beazer, 440 U.S. 568 (1979)**

- 회복 중인 약물 사용자 전체를 제외하는 규칙을 허용
- 법원은 “규칙이 고용의 안전성과 효율성을 *significantly serves*” 한다면 정당화된다고 판단

> “A 'narcotics rule,' which 'significantly serves' the 'legitimate employment goals of safety and efficiency,' was 'assuredly job related.’” (Beazer, at 587 n.31; p. 703)
> 

⟶ **기준이 “직무 수행 능력의 예측”에서 “일반적 조직 목적에 봉사”하는 것으로 완화됨**

---

### ⮕ **Wards Cove Packing Co. v. Atonio, 490 U.S. 642 (1989)**

- 고용주의 입증 책임을 축소하고, “business necessity”를 “business justification” 수준으로 하향시킴

> “There is no requirement that the challenged practice be ‘essential’ or ‘indispensable’ to the employer’s business.” (Wards Cove, at 659; p. 704)
> 

⟶ 이는 고용주의 부담을 경감하고, **합리적 정당화만 제시해도 족하다는 입장**을 강화함

---

### ⮕ **입법 개입: Civil Rights Act of 1991**

- Wards Cove 이후 **의도적으로 기준을 Griggs 이전으로 복귀시킴**
- 그러나 **“business necessity”의 실질 내용은 여전히 불확정적**:

> “Because the substantive standards for job-relatedness or business necessity were uncertain before Wards Cove, however, the confusion persisted even after the 1991 Act was passed.” (p. 704)
> 

---

### 3. 오늘날의 판단 기준

- 현재는 Griggs와 Wards Cove 사이 어딘가에 위치한 **“중간 수준의 정당성”**이 요구됨
- 일부 판례는 “manifest relationship”이나 “significantly correlated” 기준을 유지함:

> “[Courts] require that the hiring criteria bear a ‘manifest relationship’ to the employment in question or that they be ‘significantly correlated’ to job performance.” (p. 705)
> 

---

## II. Job-Relatedness

“Business necessity”와 긴밀히 연결되지만, *“job-relatedness”*는 특히 **측정 항목(target variable)이 직무 성과와 얼마나 관련되어 있는지를 평가하는 기준**이다.

### 1. 정의와 법리

Griggs에서는 두 개념이 구분 없이 사용되었지만, 이후 **“job-relatedness” = 직무 성과 예측 가능성**이라는 해석이 일반화됨:

> “The focus of the Court was clearly on future job performance, and the term 'job-related' has come to mean a practice that is predictive of job performance.” (p. 703)
> 

---

### 2. 데이터 마이닝에서의 적용

- **target variable**(예: tenure, performance rating 등)이 직무와 관련 없는 경우 → *직무 관련성 없음*
- 예: 검색 결과에 범죄 전과 관련 광고가 뜨는 경우
    
    → “이 변수는 직무와 무관하므로 정당화 불가”:
    

> “It would be difficult for an employer to justify an adverse determination based on the appearance of an advertisement suggesting a criminal record.” (p. 707)
> 

---

### 3. Validation 기준

EEOC Guidelines에서는 세 가지 검증 방식 요구:

- **Criterion-related validity**: 통계적으로 직무성과와 상관관계
- **Content validity**: 직무 자체의 과업을 측정
- **Construct validity**: 예: 정직성처럼 내재된 특성을 측정

> “As a statistical predictive measure, a data mining model could be validated by either criterion-related or construct validity.” (p. 709)
> 

하지만 대법원은 **이 가이드라인을 Ricci에서 무시**한 바 있다:

> “The Court found no genuine dispute that the tests at issue met the job-related and business necessity standards despite not having been validated under the Guidelines.” (p. 710)
> 

⟶ **실질적 validation 요건은 낮고, 법원은 흔히 ‘상식(common sense)’으로 판단한다.**

---

## III. Alternative Employment Practice

이 요건은 1991년 법에서 **고용 관행이 정당화된다 해도, 덜 차별적인 대안이 있다면 고용주는 그것을 채택했어야 한다는 추가 요건**이다.

### 1. 기준 설정: **Albemarle Paper Co. v. Moody, 422 U.S. 405 (1975)**

> “If an employer does... prove that its tests are ‘job related,’ it remains open to the complaining party to show that other tests or selection devices, without a similarly undesirable racial effect, would also serve the employer’s legitimate interest.” (Albemarle, at 425; p. 705)
> 

⟶ 이 판례는 **“대체 수단 제시”를 통해 최종적으로 차별적 실천을 금지할 수 있는 길을 열어줌**

---

### 2. 법리적 위치: “Surrebuttal” 구조

- 피고가 job-relatedness를 입증해도, 원고가 다시 대안적 수단을 제시하면 책임을 입증 가능
- 이 구조는 1991년 법에 의해 **명시적으로 채택됨**:
    
    42 U.S.C. § 2000e-2(k)(1)(A)(ii)
    

---

## 요약

| 요건 | 기준 형성 판례 | 현재 해석 | 데이터 마이닝 적용상 쟁점 |
| --- | --- | --- | --- |
| **Business Necessity** | *Griggs*, *Beazer*, *Wards Cove*, *Ricci* | 중간 수준 정당화 허용, validation 없이도 가능 | 예측성만 확보되면 통과 가능, 고용주에 유리 |
| **Job-Relatedness** | *Griggs*, EEOC Guidelines | 직무성과 예측 여부로 판단 | target variable의 정당화 여부가 핵심 |
| **Alternative Practice** | *Albemarle*, 1991 Act | 원고가 덜 차별적인 수단을 입증 | 고용주의 통제 부족, 비용 문제, 입증 곤란 |

Return to data mining

(1) 타겟 베리어블이 정말로 직종과 관련되어 있나? —> 만약 충분히 관련 없다면, Business necessity 변호 자체가 실패한다. 

그러므로 Disparate impact liability는 타겟 베리어블을 정의할 때 제대로 된 주의가 이루어지지 않았을 때 발견될 수 있다. → 그러나 실무에 있어서 어떤 사업 상 practice가 직무 관련한지를 결정하는 것은 결국 해당 practice가 실제로 차별적인지를 결정하는 규범적 판단을 요구하기 때문에 법원은 상식적 business practices for which an employer has a pluasilbe story를 받아들이고는 한다.

(2) 만약 타겟 베리어블이 직무 관련 있는 것이라면?

(2-1) 모델이 그 trait에 대해서 예측적인가? 

A. 데이터 마이닝은 그 정의상 이 조건을 만족시킨다. (타겟 베리어블이 정말로 직무 관련적이라면) 그러므로 강건한 데이터 마이닝은 Griggs 기준마저 만족시킬 수 있을 것이다.

(2-2) 모델이 예측하려고 했던 것을 적절하게 예측하는가?

Proxy 문제: Proxy 차별은 correct(올바르게) 최적화 한다. 차별적인 효과를 가질 때, 그것은 유관한 특성들이 실제 세계에서 분포되어 있는 방식을 반영한다.  —> O

biased sample 과 Mislabeled examples data mining: 적절한 예측을 내놓지 못한다. 

Dataset 문제가 있는 Datamining 역시 같은 문제를 겪는다. 

이러한 모델들은 직무와 관련 있을 수도 있고, 아닐 수도 있다. 모델의 오류가 결과값을 충분히 왜곡해서 모델이 직무 성과의 좋은 예측으로 기능하지 못하게 되는지의 여부에 그 관련성 판단은 달려 있을 것이다.

직무 관련 Standard guidelines

| 유형 | 정의 | 요건 | 주요 예시 |
| --- | --- | --- | --- |
| **Criterion-related** | 테스트 점수와 직무 성과 간의 통계적 상관관계 | p < 0.05 수준의 유의성 | 시험 점수 vs. 생산성 |
| **Content** | 테스트 내용이 실제 직무에서 필요한 능력 반영 | 직무 수행에 해당 능력이 실제로 사용되는가?  | 수작업 기술 테스트 |
| **Construct** | 측정된 심리적 특성과 직무 성과 간의 연관성 | 고용 절차가 특성과 유관한가?  특성은 직무 성과와 유관한가? | 정직성 vs. 신용관리 업무 |

Data mining은 Criterion과 Construct vaildity test를 통과할 수 있을 것. 이 테스트를 통과하는 것은 Datamining에게 굉장히 쉬운 일이다. 

결과적으로 Business necessity defense는 결국 측정 특성이 직무 수행에 중요한지 아닌지에만 그 성패가 달려 있게 될 것. 

결론 1: 결국 정당하게 직무 관련된 특성들을 예측하는 모든 데이터 마이닝 모델들은 Business necessity model 변호에 따라 liability가 발생하지 않을 것. 

그렇지만 Biased Samples, Mislabeld examples, litmied features —> 이 케이스들은 대안 법리에 따라 liability가 생길 수 있다.

BUt

### 1. **“모델 수정(fixing the model)”은 기술적으로 간단하지 않다**

- **예: LinkedIn 추천 알고리즘**
    
    특정 직종에 대해 LinkedIn이 제시하는 후보군이 사용자 선호(고용주의 편향)에 따라 차별적인 결과를 낳을 경우, 실제로 **차별을 만들어내는 알고리즘의 설계자는 LinkedIn**이다.
    
    > “Thus, it could not really be said that the employer ‘refuses’ to use an alternative employment practice.”
    > 
    > 
    > 고용주는 단지 그 도구를 사용할지 말지만 결정할 수 있으며, 알고리즘을 ‘수정’할 수 있는 권한이나 역량은 없음.
    > 
- **Street Bump 사례**
    
    유사하게, 시민 신고 기반 앱의 **보고 편향(reporting bias)**이 시스템에 내재되어 있으면, 이를 고치려면 원자료(raw input data)에 접근해야 하지만 이는 기술적, 법적 제약이 존재.
    
- **부족한 데이터(feature sparsity)의 문제**
    
    모델이 충분히 정교하거나 다양한 변수를 포함하지 못할 경우, 고용주는 **새로운 데이터를 수집해야 하며** 이는
    
    > “time consuming and costly, if not impossible for legal or technical reasons.”
    > 

---

### 2. **데이터 불균형의 인식 및 수정은 매우 어렵다**

- 데이터에 특정 집단이 과소/과대표집되었는지를 확인하려면, 분석가는
    
    > “some independent mechanism for determining these proportions”
    > 
    > 
    > 즉, 현실 인구 분포에 대한 신뢰 가능한 외부 기준이 필요하다.
    > 
- 하지만 현실적으로 어떤 특징(feature)이 **모델의 차별성을 유발하는지조차 식별하기 어렵ek.**
    
    > “data miners do not operate with causal relationships in mind.”
    > 

---

### 3. **법적 기준: ‘refuse to use’의 해석 불분명**

- 현재 **Title VII**이나 판례에서
    
    > “what it means for an employer to ‘refuse’ to adopt the less discriminatory procedure”
    > 
    > 
    > 는 명확히 정의되어 있지 않다.
    > 
- 학자들에 따르면, 이는 단순한 무지(unawareness)를 넘어서 **고용주가 실제로 대안을 검토하고도 거절했을 때에만 책임이 성립**할 수 있다.
    
    (Sullivan, Zimmer 인용)
    
- 예컨대, 고용주가 막대한 자원을 들여 데이터 수집·모델 설계를 이미 완료했고, 이후 차별 효과를 인지하지 못했으며, **재설계 비용이 너무 높다면**,
    
    > “is the employer ‘refusing’ to use a less discriminatory alternative, or does one simply not exist?”
    > 
- 비용 문제와 관련해 일부 법원은 **수정 비용이 과도할 경우 책임을 묻기 어렵다**고 인정한 바 있다. (Lidge, 200)

---

### 결론:

이러한 모든 기술적, 법적, 인식적 장애로 인해 저자는 **“the prospect of winning a data mining discrimination case on alternative employment practice grounds seems slim”** 이라고 결론짓는다. 즉, **형식적으로 대안이 “존재”하더라도**,

- 그것이 현실적으로 **식별 가능하지 않거나**,
- 법적으로 **“거절(refusal)” 요건을 충족하기 어렵기 때문에**,
    
    **disparate impact 법리가 데이터 마이닝에 대해서는 실질적으로 무력해질 수 있다.**
    

Liability 생성의 다른 방식? BN(business necessity) 기준 강화.

## 1. **Strict BN 기준이 작동 가능한 경우: 단일 특성(target trait) 예측 모델**

- 예: **고용 유지 기간(job tenure)** 예측 모델
    
    → 법원은 이를 "legitimate, non-discriminatory business objective"라고 간주할 수 있음
    
    → 하지만 여전히 **직무 수행의 ‘필수 조건’은 아님**
    
    > "But it is clearly not necessary to the job."
    > 
- Griggs식 strict BN에 따르면,
    
    고용주가 **cut score 이하의 지원자는 실제로 직무 수행이 불가능**하다는 점을 입증하지 못하면, BN 방어는 실패한다.
    
    > “Unless the employer can show that below the cut score, employees cannot do the work, then the strict business necessity defense will fail.”
    > 

⇒ **결론:** 데이터 마이닝이 단일 특성을 목표로 하고, 그 특성이 필수적이지 않다면, strict BN 기준 아래에서는 책임이 성립할 수 있다.

---

## 2. **Strict BN 기준이 무력화되는 경우: ‘총체적 적합도(general job performance)’ 예측 모델**

- 현실에서는 많은 고용주가 단일 특성 대신, 다수의 특성을 포괄하는 **총체적 적합성 모델**을 사용함.
    
    예: 8,000개 특성 기반의 “좋은 직원(good employee)” 모델
    
    > “Taken to an extreme, an 8,000-feature holistic determination of a ‘good employee’ would still not be strictly ‘necessary.’”
    > 
- 이 경우엔 **어떤 개별 특성도 ‘필수적’이라고 말하기 어렵고**, 따라서 strict BN 기준을 적용할 수 없음.
    
    > “Holding a business to such a standard, however, would simply be forbidding that business from ranking candidates if any disparate impact results.”
    > 

⇒ **결론:** strict BN 기준은 **단일 기술 요건을 중심으로 설계된 모델에는 작용할 여지가 있으나**,

현대의 **다변량적 데이터 마이닝 실무**에는 **구조적으로 부적합**함.

### Masking and problems of proof

Masking이 liable한 case인 것은 당연. 

그러나 어떻게 증명할 것인가?

어떻게 Masking을 탐지하고 증명할 것인가? 

### ⟡ I. **Masking된 차별의 구조: 어떻게 의도적 차별이 은폐되는가?**

### ▸ Premise 1. **고용주는 직접적으로 보호 집단(protected class)을 참조하지 않고도 차별 가능**

- 예: 인종 대신 **주소(neighborhood)**를 이용한 redlining.
    
    > “Due to housing segregation, neighborhood is a good proxy for race and can be used to redline candidates without reference to race.”
    > 
- 더 정교한 proxy: 음악 취향, 페이스북 ‘좋아요’, 친구 네트워크 등.
    
    > “Some combination of musical tastes, stored ‘likes’ on Facebook, and network of friends will reliably predict membership in protected classes.”
    > 

### ▸ Premise 2. **데이터 수집, 라벨링, 특성 선택의 왜곡을 통해 의도적 편향을 설계할 수 있음**

- 이는 겉보기에 **우연적 또는 기술적 오류처럼 보이므로**, 고의성이 감춰짐.
    
    > “These methods of intentional discrimination will look, for all intents and purposes, identical to the unintentional discrimination that can result from data mining.”
    > 

---

### ⟡ II. **Masking의 탐지: 왜 어렵고 애매한가?**

### ▸ 문제 1: **Disparate Treatment vs Disparate Impact 구분의 붕괴**

- Masking된 intentional discrimination은 실질적으로 **disparate impact 분석**으로 탐지됨.
    
    > “Detecting discrimination in the first instance will require the same techniques as detecting unintentional discrimination, namely a disparate impact analysis.”
    > 
- 하지만 intent가 없다는 전제를 가진 disparate impact 이론은 **의도적 차별에 대한 적절한 처벌 수단이 아님**.
- **양 법리의 증거 구조가 동일해지면서 개념적, 법적 혼란이 초래됨**
    
    > “Disparate treatment and disparate impact become essentially the same thing from an evidentiary perspective.”
    > 

---

### ⟡ III. **입증 전략의 어려움: 대안의 존재를 근거로 의도를 주장해야 함**

- 원고는 다음을 입증해야 함:
    - (a) 고용주가 더 정밀한 데이터, 더 정확한 라벨, 더 적절한 특성들을 사용하지 않았고
    - (b) 이는 합리적인 설명이 어려우며, 결과적으로 **pretext**로 보일 수 있음
        
        > “One could show that the neutral employment practice is a pretext by demonstrating that there is a more predictive alternative.”
        > 
- 그러나 이는 원래 **disparate impact의 대안 고용 관행(alternative employment practice)** 기준이지,
    
    **intent가 필요한 disparate treatment**의 요소가 아님.
    
- 따라서 **법적 이론 구조상 충돌 발생**
    
    > “The business necessity defense [is] not available in a disparate treatment case, so alternative employment practice is not the appropriate analysis.”
    > 

---

### ⟡ IV. **실무적 현실: 차별을 감추려는 고용주의 전략과 제도적 한계**

- 고용주는 법 위반을 피하기 위해 **의도적으로 민감정보 수집을 피함**
    
    > “Employers who do not want to discriminate go to great lengths to avoid raising the prospect….”
    > 
- 제3자에게 위탁하여 **종교·인종 등의 민감 정보를 제거한 보고서**만 받음
    
    → 실제 차별 의도가 있어도 **직접 본 적이 없다는 항변 가능**
    
- 그러나 데이터 마이닝으로는 **간접적으로 보호 집단 특성을 추론 가능**
    
    > “Employers can honestly disclaim any knowledge of the protected information. Nonetheless… she would be able to infer class membership from the data.”
    > 

⇒ **“I didn’t know”라는 항변은 더 이상 의도 부재를 보장하지 않음.**

---

### ⟡ V. **결론: 법이 요구하는 ‘의도’는 탐지 불가능에 가까워지고 있음**

- *의도(discriminatory animus)**는 점점 더 **기술적 조건에 의해 은폐될 수 있음**
- 하지만 현행 법제는 **이러한 의도 은폐를 탐지·처벌할 구조적 장치가 부족**
- 따라서 저자는, 데이터 마이닝 시대에 기존의 disparate treatment/treatment 구분이 **도식적으로는 유지되지만, 사실상 붕괴하고 있음**을 강조함

### 개혁의 어려움

두 가지 종류의 어려움 

1. 데이터 마이닝 자체의 속성이 개혁을 어렵게 만든다. 예를 들어 좋은 직원을 정의함에 있어서 주관성은 피할 수 없지만 동시에 그럼에도 불구하고 어떤 답변들은 명백하게 차별적일 수 있다. 어떻게 선을 그을 것인가?  

How does one draw that line? Can employers
gain access to the additional data necessary to correct for collection bias? How
much will it cost them to find it? How do we identify the "correct" baseline
historical data to avoid reproducing past prejudice or the "correct" level of
detail and granularity in a dataset? Before laws can be reformed, policy-level
answers to these basic technical, philosophical, and economic questions need to
be addressed at least to some degree.

2.

### ⟡ *(Step 1)* 모든 데이터 마이닝 기반 차별이 **절차적 대응 가능하지 않음**

> 일부 차별 메커니즘은 구조적으로 사전 예방이 불가능하거나 지나치게 복잡하며, **절차적 수단(procedural remedy)**으로는 충분하지 않음.
> 
> 
> 예: 불균형한 feature space, proxy discrimination, labeling bias 등.
> 

---

### ⟡ *(Step 2)* 그렇다면 **유일한 대응책은 결과 기반의 수정**일 수 있음

> 즉, “after-the-fact reweighting of outcomes” 또는 결과의 보정(reallocation)이 사후적 수단으로 남게 됨.
> 
> 
> 이 방식은 *de facto*로 **affirmative action**에 가까운 구조를 가짐.
> 

---

### ⟡ *(Step 3)* 그러나 이 보정 방식은 **현 정치·법적 환경에서 불가능하거나 위헌적일 수 있음**

> 우대조치의 냄새만 풍겨도 정치적으로 수용되기 어려움, 그리고 헌법적 정당성 자체도 위협받음.
> 
> 
> 따라서 이 대안마저 **실질적으로 차단됨**.
> 

---

### ⟡ ⟨Conclusion⟩ → 결과적으로,

**절차적 대응은 기술적으로 실패하고, 결과적 보정은 정치적으로 봉쇄된다.**

→ 이는 데이터 마이닝 기반 차별에 대해 **법적·제도적 개입 여지가 거의 사라진 상태**를 의미함.

타겟 변수 설정

### ⟡ 구조적 논증 분석:

### **Premise 1. 타겟 변수 설정은 ‘주관적’ 선택을 수반한다.**

- “Settling on a target variable is a necessarily subjective exercise.” (p.716)
- 이는 통계적 기준이 아니라, 해석적·정치적 기준에 따라 **문제의 정의(problem formulation)**가 결정된다는 점을 의미.

### **Premise 2. 경쟁적인 정의 간의 우열 판단은 불가능하거나 무의미하다.**

- 이유: "target variables are themselves incommensurable"
- 이는 **서로 다른 고용 목표**(e.g., 이직률 감소, 매출 증대, 혁신성 증가)가 지닌 **규범적 우선순위의 기준 자체가 서로 양립 불가능함**을 뜻함.

### **Premise 3. 따라서, 어떤 정의가 '더 옳다'거나 '더 공정하다'는 판단은 타당한 기준 없이 순환된다.**

- 저자는 Oscar Gandy의 말을 인용하여, “certain kinds of biases are inherent in the selection of goals”라 주장함.
- 곧, 차별은 “편향된 데이터”가 아니라 “편향된 목표 선택”에서부터 시작됨.

### **Premise 4. 현실적으로는 실용적 제약(비용, 기술력 등) 때문에 실제 직무 기술과 타겟 변수 사이에 긴밀한 대응조차 어려움.**

- “there should be a tight nexus... but this may not be possible for practical and economic reasons.”
- 이는 현실 속 **비이상적(nonideal)** 변수 설정의 불가피성과 함께, **현실적 차별 회피 수단이 무력해질 수 있음**을 시사.

### **Premise 5. 그러나 바로 이 점에서 개혁의 창구도 존재함: 설계 선택의 다양성**

- “this also offers an opportunity for creative thinking...”
- 예시: *Hayden v. County of Nassau* 판례
    - 문제 정의를 다양하게 조합함으로써 동일한 검사의 여러 scoring 구성 중 **통계적으로 유효하면서도 소수자에 유리한 조합 선택 가능**

---

### ⟡ 귀결 (Conclusion):

타겟 변수 설정은 **정의 자체가 차별 가능성을 포함한 정치적 행위**이기 때문에, 단순한 절차적 개입(예: validation standard)으로는 충분히 통제되지 않는다. 하지만, **다양한 설계 가능성**을 제도적으로 열어두는 방식은 **부분적이지만 실천 가능한 개혁 공간**을 제공한다.

훈련 데이터

## 1) **Labeling Examples: 과거의 차별이 레이블에 이미 내재되어 있는 문제**

### ⟡ 핵심 구조

### **Premise 1. 머신러닝은 과거의 사례에서 '좋은 직원'을 학습한다.**

- 하지만 이 ‘좋은 직원들’은 **과거 차별이 작동한 결과물**이다.
- 따라서 학습된 기준은 그 차별을 되풀이하게 된다:
    
    > "if the only examples an employer has to draw on are those of past employees who had been subject to discrimination, all learned rules will recapitulate this discrimination."
    > 

### **Premise 2. Title VII는 차별 금지와 고용주 재량을 균형 있게 보장해야 한다.**

- 전통적으로도 seniority 시스템 등은 차별을 고착화했으나, "bona fide seniority system" 예외가 존재해 합법으로 인정됨.
- 이처럼 과거의 편향된 기준을 제거하는 시도는 법적으로도 한계가 있다. (cf. *Trans World Airlines v. Hardison*, 432 U.S. 63 (1977))

### **Premise 3. 레이블을 ‘정정’하는 것은 실질적으로 불가능에 가깝다.**

- 이유: 고용 판단은 "주관적이며 모호한 기준"에 근거하므로 “what is the correct label is fuzzy.” (Calders & Zliobaite 인용)
- 차별 없는 결정이 **무엇이었을지를 복원(reconstruct)** 하는 작업은 통계적으로도, 규범적으로도 불가능에 가깝다.

### ⟡ 결론

→ **기계가 학습한 과거 판단이 편향되어 있다면**, 그 편향을 제거하려는 시도는 단순한 보정이나 재레이블링이 아닌, **전체적 재구성(rerendering)**을 요구하며, 이는 실질적으로 수행 불가능하거나 해석적 논란을 초래할 수 있다.

---

## (2) **Data Collection: 대표성 부족과 편향을 감지하고 수정하는 것의 한계**

### ⟡ 핵심 구조

### **Premise 1. 데이터 수집 과정에서의 편향은 자주 존재하며, 쉽게 드러나지 않는다.**

- **예외적 사례**: Street Bump 앱은 시각화(map plotting)를 통해 편향이 드러났음. (상류층 지역 위주로 pothole 리포트가 몰림)
- **일반적 현실**: 대부분의 편향은 **보고(reporting), 샘플링, 선택(selection) 편향**의 형태로 숨겨져 있으며, 이를 판별하려면 **외부 기준 정보**가 필요.

### **Premise 2. 편향을 수정하려면 고용주가 원시 데이터(raw data)에 접근 가능해야 한다.**

- 하지만:
    - (i) 많은 고용주는 **자체 데이터를 수집하지 않음**.
    - (ii) 제3자 데이터 제공자는 **데이터 독점 및 영업비밀 보호**를 이유로 공개를 꺼림.
    - (iii) 데이터 확장이나 보완은 **비용이 많이 들거나 법적으로 불가능**할 수 있음.

### **Premise 3. 그럼에도 불구하고, 유일하게 실현 가능한 수단은 '능동적 oversampling'이다.**

- 소수집단을 의도적으로 많이 포함시켜 학습시키는 것.
- 그러나 이것 역시 정확히 어떤 집단이 과소대표되고 있는지를 알아야 가능.

### ⟡ 결론

→ 수집 편향을 수정하려면 **심도 있는 데이터 접근성과 모델 수정 권한**이 필수인데, 이는 현재의 데이터 생태계 구조(특히 제3자 알고리즘 제공 모델)에서는 **제도적으로 보장되지 않음**. 이 때문에 **실질적인 책임 추궁 및 교정이 어렵다.**

---

## 종합 정리

| 문제 영역 | 핵심 어려움 | 예시 혹은 인용 출처 |
| --- | --- | --- |
| **Labeling** | 차별 없는 기준을 정하고 레이블링하는 것이 불가능함 | “the notion of what is the correct label is fuzzy” (p.717) |
| **Data Collection** | 편향 탐지와 수정 위해서는 원시 데이터 접근 및 수정 권한 필요 | Street Bump, 3rd-party vendor 문제 등 |

결론적으로, 저자는 훈련 데이터 단계의 개혁은 단순한 기술적 개선의 문제가 아니라, **법적, 경제적, 인식론적 제약**에 얽혀 있는 복합적 문제이며, **데이터 마이닝의 편향은 구조적으로 반복되기 쉬운 방식**으로 발생한다고 본다.

특징 선택

## ⟡ 논증 구조

### **Premise 1. Feature selection은 차별 의도가 없어도 오류를 만든다.**

- 고전적 disparate treatment와 달리, **차별적 의도가 없는 개인화/세분화된 분류**는 **어디까지가 정당한 통계적 차별인지** 판단이 모호함.
- 이 판단은 보통 다음 요소들에 따라 이뤄짐:
    - (1) 오류가 피할 수 있는 것이었는가?
    - (2) 더 정밀한 데이터를 얻는 것이 쉬웠는가?
    - (3) 그 데이터는 비용이 많이 들었는가?
    - (4) 비용 대비 편익이 낮은가?

> 이로부터 생기는 경향: 기업은 더 많은 데이터를 수집해야 할 의무가 있음 (단, 비용이 이득을 초과할 때까지만).
> 

---

### **Premise 2. 그러나 cost-benefit 기준은 도덕적/정치적 문제를 무시한다.**

- 저자는 이 기준이 **"누가 피해를 보는가"에 대한 윤리적 고려를 결여**한다고 지적함.

### ① 피해자의 관점 결여:

- 전체 정확도가 향상되더라도, 그 과정에서 **일방적인 피해자 집단**(예: 저소득층, 인종 소수자)이 **반복적으로 손해를 본다면** 이는 정당화될 수 없음.
- Gandy 인용: 기업이 이득을 계속 낼 수 있는 한, 특정 집단에 오류가 집중되어도 수정할 유인이 없음.

### ② 차별적 오류 분포:

- protected class에 속한 사람들이 **체계적으로 더 많은 오류에 노출**되면, 이는 **제도적 불평등을 강화**함.
- 이는 단순한 확률적 오차 문제가 아닌, **정의(distributive justice)**의 문제임.

---

### **Premise 3. 해법조차도 딜레마를 낳는다.**

- 가령, 데이터 해상도를 높이거나 feature를 추가해 오류를 줄이려 해도:
    - (a) **인과적 관계(causal mechanism)**가 파악되지 않는 한, 오류는 여전할 수 있음.
    - (b) 따라서 대안은 **집단 간 오류 비율의 균형(equalizing error rates)**을 맞추는 것.

> 하지만 이 경우, 전체 오류율이 증가할 수 있다. 즉, “모두에게 공평하게 부정확한” 결과를 내는 모델이 생김.
> 

---

## ⟡ 결론: Feature selection은 구조적 tradeoff 문제다

| 차원 | 문제 요약 |
| --- | --- |
| 기술적 | 어떤 feature가 정당한 기준인지를 **명확히 판단하기 어렵다** |
| 윤리적 | **누가 피해를 보는지**에 대한 고려 없이 정확도만 추구할 경우 정당성 상실 |
| 제도적 | 규범적 문제(정의, 공정성)를 반영한 **정책 가이드라인 부재** |

결국, feature selection은 단순한 **정밀화**의 문제라기보다는, **정당한 구별의 기준이 무엇인가**라는 본질적 윤리적/정치적 문제와 결부되어 있으며, 이로 인해 데이터 마이닝 시스템의 공정성은 쉽게 확보되지 않는다.

## ⟡ 논증 구조: Proxy Variables가 공정성을 훼손하는 구조적 이유

### **Premise 1. Proxy 제거는 기계적으로 어렵고 개념적으로도 모호하다.**

- 어떤 feature가 단지 class membership(예: 인종, 성별)을 예측하는 proxy인지, 아니면 실제로 job performance와 관련 있는 ‘정당한’ feature인지 **판별 기준이 명확하지 않음**.
    - Calders & Žliobaitė (2011): “[Highly correlated attribute]를 제거하는 것은 문제가 된다, 왜냐하면 그것이 label에 대해 실제로 정보력을 갖는 경우도 있기 때문이다.”
    - Pope & Sydnor (2011): 실제 feature들은 보통 “pure predictor도 pure proxy도 아니다.” → **혼합적 특성**.

---

### **Premise 2. Proxy를 제거해도 동일한 차별 효과가 대체적으로 지속된다.**

- 이유: **class membership 정보는 dataset의 여러 feature들에 걸쳐 분산되어 encode되어 있기 때문**.
    - 한 가지 proxy를 제거해도 **다른 경로를 통해 동일한 집단 구분이 재현됨**.
    - 예: 거리(distance to work)는 성과 예측에 중요하지만, 인종별 거주지 분포와 상관되므로 사용 시 법적 위험 발생.
    - → **다차원적, 중복적인 encoding**이 존재함.

---

### **Premise 3. Proxy 제거는 정확도를 저해하며, 이로 인해 fairness와 utility 간 trade-off 발생.**

- Calders & Verwer (2010): “모든 correlated attribute를 제거하면 차별은 줄어드나, **정확도(classifier accuracy)**가 크게 하락함.”
- Dwork et al. (2012): “이 결과들은 **fairness와 utility 사이의 정량적 trade-off**를 보여준다.”

→ 예측 정확도를 유지하려면 민감 특성과 상관된 feature를 사용할 수밖에 없으며, 이것은 다시 차별로 이어짐.

---

### **Premise 4. 민감 feature와 ‘정당한’ feature의 구분은 법적으로도 정치적으로도 매우 논쟁적이다.**

- “Feature가 proscribed한 특성과 관련이 있더라도, 그것이 객관적으로 정당한 정보인가?”라는 질문은 해결불가능하거나 **법적/도덕적으로 분열된 입장들에 부딪힘**.
- “현실의 사회적 불평등이 feature 자체에 스며들어 있기에, 그 어떤 정당한 예측 feature도 불평등을 반영할 가능성 높음” (즉, **class-conditioned relevance**의 문제).

---

## ⟡ 결론: Proxy 문제는 공정성-정확성 양립 불가능성을 드러낸다.

| 문제 영역 | 핵심 진단 |
| --- | --- |
| 기술적 | Proxy를 제거해도 class membership 정보는 feature 전반에 걸쳐 encode됨. |
| 통계적 | Proxy 제거는 분류 정확도 저하를 초래하며, 이로 인해 성능-공정성 trade-off 발생. |
| 윤리적 | 어떤 feature가 정당한 기준인지 판단하려면 사회적 불평등의 해석이 필요함. |
| 법적/정치적 | 민감 특성과 feature의 경계는 **제도적으로 명확히 구분 불가**, 법적 기준 부재. |
|  |  |

### ❖ 요점 정리: 외재적 어려움의 1차 구조 (정치적·헌법적 제약과 이론적 긴장)

### 1. **핵심 문제 제기**

- 데이터 마이닝에서 발생하는 차별은 **기존 Title VII 체계**로는 다루기 어렵다.
- 그 이유는 해결책이 **antisubordination 원칙**에 기반해야 하는데, 이는 미국 반차별법의 지배 원칙인 **anticlassification**과 충돌하기 때문이다.

### 2. **두 반차별 원칙의 대비**

- **Anticlassification**: 차별적 분류 자체를 금지. 법은 개인을 집단 속성이 아닌 “개인”으로 취급해야 한다.
- **Antisubordination**: 사회적 열위의 지위 자체를 개선하는 것이 법의 목적. 형식이 아니라 실질에 초점.

### 3. **법 교리와의 연결**

- **Disparate Treatment**: 고의적 차별을 금지 → anticlassification과 일치.
- **Disparate Impact**: 결과 중심의 차별 효과를 다룸 → antisubordination적 성격이 있으나,
    - 실제로는 **anticlassification 도구로 기능**(예: 고의 차별을 “evidentiary dragnet”으로 탐지).
    - 이중성 때문에 이론적으로 불투명.

### 4. **역사적 경향과 법적 귀결**

- 1970년대 중반부터 **antisubordination은 약화**, **anticlassification은 우세**:
    - *Washington v. Davis* (1976): 헌법상 평등 보호는 의도(intent) 차별만 금지.
    - 이후 소수자 보호 논리보다 **형식적 중립성**이 우선시됨.
- 결과적으로 백인 남성도 **disparate treatment 청구 가능** → 반차별법의 **소수자 보호 기능 약화**.

## ❖ 요점 정리: Ricci 판례와 헌법적 외재적 어려움

### 1. **헌법상 antisubordination 원칙의 부재**

- *헌법의 평등보호조항(Equal Protection Clause)**은 오직 **의도된 차별(intentional discrimination)**만 금지한다 (*Washington v. Davis* 참조).
- 따라서 **antisubordination 원칙은 헌법적 원칙이 아님**.
- 하지만 **법률적 차별금지법(예: Title VII)**은 이 원칙에 따라 구성될 가능성은 여전히 있음.

### 2. **Ricci v. DeStefano (2009)**의 핵심 판단

- 뉴헤이븐 시가 승진시험의 *disparate impact*를 우려해 결과 인증 거부 → 백인 소방관들이 *disparate treatment* 위반으로 소송.
- **대법원 판단**: 시험 결과가 *race-neutral*이지만, 결과 인증 거부는 **"race-conscious" 조치**로 간주됨 → **disparate treatment** 성립.
- 따라서, *disparate impact*를 피하려는 시도 자체가 **헌법상 차별이 될 수 있음**.

### 3. **Ricci의 기준: “strong basis in evidence”**

- *"실질적 증거에 근거(strong basis in evidence)"**가 없는 한, *disparate impact*를 교정하려는 조치는 불법적인 *disparate treatment*가 됨.
- 이 기준은 **사후 조치의 합법성을 제한**하고, 실제로는 **사전 조정만 허용**:
    - 예: 시험을 설계하는 단계에서는 조정이 허용됨 (test-design stage).
    - 하지만 **데이터 마이닝은 사후 발견이 일반적**이므로, 사전 수정이 현실적으로 불가능에 가까움.

### 4. **데이터 마이닝에의 귀결**

- 데이터 마이닝 편향을 교정하려면 **보호집단(class membership)** 정보를 고려해야 하므로, 본질적으로 **race-conscious remedy**가 필요.
- 이는 Ricci 판례의 기준에 의해 **헌법적 위험**을 동반하게 됨.

### 결과적 귀결:

- 데이터 마이닝에서의 차별을 해결하기 위한 **실질적 개입은 위헌 소지가 있음**.
- 특히, 보호집단 정보를 고려한 모델 수정은 **disparate treatment로 간주될 가능성**.
- **사후적 편향 수정은 법적으로 매우 제한됨**, 실질적으로 **불가능에 가까움**.

## 요점 정리: 절차적 정의의 붕괴와 antisubordination의 필요성

### 1. **해결 불가능한 상황: 결과 중심 조정의 헌법적 위험**

- **Premise 1**: 어떤 경우에는 차별적 결과를 해결하려면 **결과 기반 재조정(results-focused rebalancing)**이 불가피하다.
- **Premise 2**: 하지만 이는 형식적으로 race-conscious하므로 **헌법적으로 위헌 소지**가 있다.
- ▶︎ **귀결**: 절차적 편향 제거만으로는 충분치 않으며, 실질적 조정은 법적으로 제약된다.

### 2. **예시: 이직률 기반 예측 모델**

- 여성은 통계적으로 더 빨리 퇴사함 → 이 데이터를 기반으로 모델을 학습시키면 여성 지원자 전체가 불이익을 받음.
- 이는 **합리적인 비차별적 기준처럼 보이지만**, 결과적으로는 **구조적 성차별을 재현**한다.

> ✅ “가장 예측력이 높은 모델이 가장 차별적인 모델일 수 있다.”
> 
- ▶︎ **결론**: 예측 정확성(technocratic rationality)이 **공정성(fairness)의 기준이 될 수 없음**을 드러냄.

---

### 3. **형식적 공정성의 실패: 왜 단순히 편견 제거가 해법이 아닌가?**

- **단지 편견·고의차별을 제거한다고 해도**:
    - 구조적 불평등은 **데이터의 재현 메커니즘** 속에 잠복함.
    - 문제는 의도가 아니라 **결과(result)**임.
- ▶︎ 따라서, 데이터를 통한 차별 방지를 정당화하려면:
    - 더는 **정확성, 중립성, 예측 가능성** 같은 가치가 아니라,
    - **평등한 대표성과 실질적 지위 개선**이라는 **antisubordination 원칙**이 기준이 되어야 함.

---

### 4. **정보 억제의 역설: 데이터를 지워도 불평등은 남는다**

- 보호집단 정보 사용 금지 →
    - (a) 이미 인코딩된 경우엔 **무의미**
    - (b) 실제 예측에 기여하는 경우엔 **정확도 감소**
- ▶︎ 데이터 삭제는 본질적으로 **zero-sum 재분배 효과**를 발생시킴:
    - 어떤 집단이 더 불리해지거나 유리해짐.

---

### 5. **종합 결론: 쟁점은 결국 “어느 정도의 불평등이 허용 가능한가?”**

- **법적 프레임워크는 현재까지 절차적 정의에 매몰되어 있음**:
    - → 실제 쟁점은 **허용 가능한 차별 수준의 윤리적 판단**임.
- 그러나:
    - 이 문제는 **헌법적으로도 불안정하고**, **정치적으로도 회피됨**.
    - 그 결과, **데이터 마이닝은 구조적 불평등을 강화하는 경로가 된다.**

---

## ❖ 핵심 귀결

| 구조 | 설명 |
| --- | --- |
| 문제 진단 | 예측의 합리성(tenure, retention)을 근거로 한 결정이 구조적 차별을 정당화할 수 있음 |
| 제도적 한계 | 결과 기반의 재조정은 위헌 위험이 있고, 정보 삭제는 무력하거나 왜곡됨 |
| 정당화 전환 | 기존의 절차적 공정성(fair procedures) 대신, 실질적 평등(substantive equality)이 기준이 되어야 |
| 최종 결론 | 데이터 마이닝 시대에 반차별법은 **“어떤 수준의 불평등을 법이 허용할 수 있는가”**라는 새로운 윤리적 판단 체계를 요구함 |

## ❖ 요점 정리: 결론부 핵심 내용

### 1. **데이터 마이닝의 차별: 두 가지 유형**

- **(1) 오류 기반 차별 (When data mining goes "wrong")**
    - 선택된 변수, 편향된 훈련데이터, 부정확한 feature 선택 등에서 발생.
    - 전형적인 **기술적 오류** → **무고한 실수**로 인해 차별이 생김.
- **(2) 정확 기반 차별 (When data mining goes "right")**
    - 높은 정확도 자체가 **불평등한 현실을 반영** → 예측력이 곧 차별성.
    - 이 경우, 모델을 덜 정확하게 만들어야만 차별이 줄어듦.

> ✅ 정확하면 할수록 차별이 강화되는 역설이 발생
> 

---

### 2. **제도적·법적 대응의 한계**

- **오류 기반 차별조차도 ex ante 판단이 어렵다**
    - 문제적 변수, 편향의 기여도, 대표성 부족을 사전적으로 판단하기 어려움.
    - 모든 기업에게 이상적 모델을 요구하면 **과도한 책임부담** 발생 → **절차적 정당성 위배 가능성** (due process concern).
- **정확 기반 차별은 더욱 대응이 어려움**
    - 이 경우 차별은 구조적 현실(예: 자산격차, 교육격차) 반영의 결과이므로,
        - → **Title VII의 개별 청구 체계로는 해결 불가**
        - → 제도적·구조적 불평등의 치유는 **개별 기업에게 맡겨질 수 없음**

---

### 3. **정책적·법리적 재구성의 방향**

- **Disparate impact**는 **장애인 차별법의 ‘합리적 조정’(reasonable accommodation)**처럼,
    - 순수한 시장 합리성에서 벗어나 **일정 수준의 비용 부담을 요구**하는 체계로 해석 가능 (Jolls).
- 하지만 **비용의 한계는 존재**:
    - Title VII은 *least discriminatory means*를 요구하지 않으며,
    - **구조적 보상 책임 전체를 개별 기업에 부과하지도 않음.**
    - → **“방어 가능한 수준의 차별(disparate impact)”**만을 금지하는 것으로 이해되어야.

---

### 4. **대안적 해결 전략**

- **(1) negligent discrimination 이론**
    - *고의(intent)**가 아닌 **부주의(carelessness)**에 대한 책임 구조 도입.
    - 정밀한 데이터 분석 및 검토의무를 다하지 않은 기업에 책임.
- **(2) status quo에 대한 재검토**
    - 데이터 마이닝은 현실의 상태(status quo)를 그대로 전제 → **그 자체가 문제**.
    - 예: 더 친화적인 직장 문화, 양육친화 정책, 장기근속 유인을 통해 **현실 조건 자체를 변화시켜야** 함.
- **(3) 데이터의 비판적 활용**
    - 비교 데이터와 메타 분석을 통해 **제도적 차별의 조건**을 드러냄.
    - **교육과 인식 제고**: 기업이 문제의 존재를 인식할수록 자발적 수정 가능성 증가.
- **(4) 기술·법·정책 간 협력**
    - 데이터 과학자, 기업, 정책가, 법률가의 **다분야적 협업**이 필요.
    - **윤리적 설계와 규범적 감독이 병행**되어야.

---

## ❖ 최종 귀결

> 이 글은 데이터 마이닝 자체를 포기하라는 경고가 아니라,
> 
> 
> **“무비판적 채택이야말로 차별을 재생산할 위험”**이라는 점을 지적한다.
> 
- **데이터 마이닝은 공정성과 효율성을 동시에 증진시킬 수 있는 잠재력이 있으나**,
- **무비판적 적용은 기존 차별의 재생산**을 초래할 수 있다.
- 따라서 **정보 기술의 윤리적 설계, 실질 평등의 법적 수용, 그리고 제도적 상상력의 확장**이 요청된다.