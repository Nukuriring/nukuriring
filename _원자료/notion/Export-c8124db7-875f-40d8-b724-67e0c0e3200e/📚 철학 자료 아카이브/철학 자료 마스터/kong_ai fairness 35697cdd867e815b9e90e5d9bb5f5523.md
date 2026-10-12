# kong_ai fairness

검토 필요: No
문서유형: 에세이
본문 추출됨: Yes
분야: 심리철학, 윤리학·메타윤리, 정치·사회철학
수정일: April 8, 2025
원본경로: C:UsersuserDesktop2025-1심철연kong_ai fairness.docx
주제: 알고리즘 공정성
크기KB: 24.1
파일명: kong_ai fairness.docx
학기: 2025-1
확장자: .docx

ABSTRACT A growing number of studies on fairness in artificial intelligence (AI) use the notion of intersectionality to measure AI fairness. Most of these studies take intersectional fairness to be a matter of statistical parity among intersectional subgroups: an AI algorithm is “intersectionally fair” if the probability of the outcome is roughly the same across all subgroups defined by different combinations of the protected attributes. This paper identifies and examines three fundamental problems with this dominant interpretation of intersectional fairness in AI. First, the dominant approach is so preoccupied with the intersection of attributes/categories (e.g., race, gender) that it fails to address the intersection of oppression (e.g., racism, sexism), which is more central to intersectionality as a critical framework. Second, the dominant approach faces a dilemma between infinite regress and fairness gerrymandering: it either keeps splitting groups into smaller subgroups or arbitrarily selects protected groups. Lastly, the dominant view fails to capture what it really means for AI algorithms to be fair, in terms of both distributive and non-distributive fairness. I distinguish a strong sense of AI fairness from a weak sense that is prevalent in the literature, and conclude by envisioning paths towards strong intersectional fairness in AI.

Two types of group fairness: statistical fariness and parity of error rates

The AI fairness literature has advanced multiple definitions of fairness that are often categorized as group fairness. 3 According to the group fairness notion (also known as statistical fairness), fairness is defined as the equality of a statistical measure between “protected” (marginalized) and “unprotected” (privileged) groups. For example, a recidivism prediction algorithm is “fair” with respect to race, if the probability for Black defendants to be classified as future criminals is approximately the same as that for white defendants Another group fairness standard seeks parity of error rates (such as false positive rates) between groups. If the rate of Black defendants to be mistaken as future criminals is the same as that of white defendants, the algorithm is “fair.” In both standards, the key idea of group fairness is to “treat different groups equally.”

One problem of the group fairness notion is that it is “only suited to a limited number of coarse-grained, prescribed protected groups”

Fairness garymandering

Kearns and colleagues [32] coined the term “fairness gerrymandering” to explain this kind of intersectional unfairness in AI. The term refers to cases where the algorithm meets the fairness standard on each individual group but is unfair on their intersectional subgroups. Insofar as AI fairness research analyzes bias only along the axis of race or that of gender, it cannot adequately address intersectional bias experienced by Black women and other women of color

Consider a classifier that labels an example positive if and only if it corresponds to a black man, or a white woman. Then the classifier will appear to be equitable when one considers either protected attribute alone, in the sense that it labels both men and women as positive 50% of the time, and labels both black and white individuals as positive 50% of the time. But if one looks at any conjunction of the two attributes (such as black women), then it is apparent that the classifier maximally violates the statistical parity fairness constraint.

Aim

Although the gradual move away from single-axis approaches towards intersectional approaches is a positive development, the current ways that AI fairness research uses the notion of intersectionality entails problems. This paper critically analyzes the dominant interpretation of intersectional fairness in AI, and thereby aims to contribute to the efforts to build fairer AI algorithms

DOMINANT INTERPRETATION OF INTERSECTIONAL FAIRNESS: PARITY AMONG SUBGROUPS

take “intersectional fairness” to be a matter of ensuring statistical equality across subgroups.

Dominant approach

Definition 1. (intersectional fairness - PA). An AI algorithm is intersectionally fair if it achieves parity of a statistical measure (e.g., 1.1, 1.2) among intersectional subgroups that are defined by different combinations of the protected attributes

1.1 (statistical parity). if the probability of getting a loan is roughly the same across all subgroups defined by cross-cutting categories (e.g., women/men × Black/white × non-US/US = 8 subgroups); or

1.2 (equal false negative rates). if the rate for, e.g., Black women with non-US citizenship who have the ability to repay their loan are falsely denied a loan is roughly the same as the rate for other intersectional groups, such as white men with non-US citizenship and Black women with the US citizenship.

Problems

In this section, I identify and analyze three problems with PA: (1) an overemphasis on intersections of protected attributes, (2) an infinite regress and a reinscription of fairness gerrymandering, and (3) a narrow understanding of fairness as equal distribution

Splitting subgroups along the line of identity categories

First, PA is so preoccupied with the intersection of identity categories (e.g., race, gender, and disability) that it fails to address the intersection of oppression (e.g., racism, sexism, and ableism),

In PA, intersectionality is seen a matter of splitting a group into finer subgroups along the lines of identity categories, or as AI researchers call them, “protected attributes.

In other words, the path to intersectional fairness starts with combining multiple categories to define smaller subgroups so that one can apply fairness measures to all of the subgroups.

Intersectionality pertains not merely to identity categories but also and more to structural oppression. feminist philosophers and theorists widely agree that “intersectionality’s raison d’être lies in its attentiveness to power relations and social inequalities.”

This is to say that identity should be examined in its relationship to power, rather than as an independent, self-sufficient unit of analysis in a vacuum. Black women are oppressed not because they have intersecting identities of “Black” and “women” per se, but because these identities are shaped by and lived in the intersecting structure of racism and sexism.

Then what is the reason that datasets are so white- and maledominated? (기존 접근법과 구별되는 핵심 질문 – asking why!)

Images for datasets are often collected by crowdworkers, and it is possible that these crowdworkers are biased. Like many other people living in the system of white supremacist patriarchy, they may have inadvertently identified “humans” with whites and/or males, or at least, regarded them as the representative sample of humans.

The unintentional bias is also prevalent among AI engineers. The problem is rather that they are simply doing their jobs but their actions contribute to reproducing oppression. In the case of crowdworkers in particular, it is important to note that these workers are at the bottom end of the technical labor market

At the core of intersectionality is the idea that multiple forms of oppression intersect to constitute such a structure In other words, efforts to create intersectionally fair strategies should start from examining how structural oppressions—i.e., class, gender, race, and language oppressions that are normalized as everyday life conditions of US society—intersect in women’s experiences of domestic violence [15, pp. 1245-1251]. Without such examination, merely splitting women into finer groups along the lines of identity categories (e.g., poor, Asian, immigrant, less-English-proficient women) does not help

Q. 여기서 사실 우리가 관심 있는 것은 algo를 fair하게 만드는 것. – 그저 그룹을 더 finer 하게 나누는 것만으로는 algo-fariness가 성취가 안될 수 있다는 point는 인정. 그렇지만 그렇다고 해서 algo 자체의 fariness를 개선시키는 방법이 finer group spiltting이 아니라고 하는 것은 약간 부족한 근거다. 예를 들어 이런걸 생각해보자. 언어를 능숙하게 쓰려면 단순히 통사론적 지식과 의미론적 지식뿐만 아니라 사회적 관습, 맥락, 분위기에 따라 각 어휘가 가지는 미묘한 뉘앙스 역시 포착할 수 있어야만 한다. 그런데 이런 지식은 사실 명료화 되기 어렵다. 화용론적 지식은 고정화된 추론 규칙으로 환원되지 않기 때문이다. – 그렇다면 LLM, 혹은 어떤 system에게 언어를 잘하게 만들려면 이런 화용론적 지식을 최대한 명료화 시켜서 먹여줘야 하는 걸까?  아니다, 그저 통계적 학습을 시키면 된다.  언어와 학습에 대한 개인의 입장마다 다르겠지만, 이런 그림에 대해 다음과 같은 해석을 제공할 수 있다. 우리의 화용론적 지식들이 사실상 그런 어휘와 문장의 통계적 구조 속에 녹아 있다. AI에게 화용론적 지식을 학습시킬 필요는 없고, 그 통계를 바탕으로 결정을 내릴 수 있게하면, 자연스럽게 그 화용론적 지식이 따라 나온다.  그렇다면 fairness 그리고 insectionality를 이해하려면 – 우리 사회의 구체적인 억압의 구조와 권력 작동을 알아야만 한다는 주장이 옳다고 하더라도, AI algo에게 이를 학습시키는 방식은 그 억압의 구조와 작동 방식을 고려하는게 아니라 그저 그런 작동이 sediment로 쌓인 category들 간의 fairness를 고려하게 만드는 방식으로 이루어질 수 있는 것 아닌가?

결국: PA falsely suggests that intersectional bias in AI can be removed by simply generating more fine-grained combinations of identity categories or attributes. By doing so, PA diverts attention from what is more to the point: using intersectionality as a framework for analyzing and challenging complex systems of oppression.  이 주장의 충분한 supprot는 AI algo의 fariness 획득 방식에 대한 근거가 더 추가되어야 이루어지는 것이 아닌가?

Falling into either regress or gerrymandering

PA either faces an unwanted challenge of infinite regress, or it reinscribes the problem it claims to solve, namely, fairness gerrymandering.5

Ex) The task of this algorithm is to predict which applicants are most likely to be successful when hired. (Here, success is defined as working at this company for at least four years and being promoted at least once.) To best predict it, the algorithm has been trained through the past 25 years of applications to the company. After a trial run, the company notices that the algorithm is biased in favor of white men and against Asian women. It is because white men have constituted the majority of the “successful” employees at the company. In contrast, Asian women employees were hardly ever promoted, which led many of them to leave the company. Trained with these data, the hiring algorithm has taught itself that white men are more likely to be successful employees and thus white male applicants are preferable to Asian female applicants

How can this intersectional bias be corrected? PA’s solution is to divide applicants along racial and gender lines and ensure that all racial-gender groups have an approximately equal chance of getting hired.

In other words, all of these may be attributes that need protection. And there is an endless list of potential “protected attributes.”6 In addition to traditional identity categories, more concrete factors may have historically affected employee success at the company. Consider these two groups: • AM1. Asian men who are work visa holders and graduates of US East Coast universities • AM2. Asian men who are US citizens and graduates of US West Coast universities

To put it another way, is it sufficient to designate race and gender as protected attributes, or should racial-gender groups be split into even finer subgroups along the lines of visa status, location of alma mater, and so on?

On the one hand, if PA seeks parity among all possible subgroups, it would need to keep splitting groups into finer subgroups, until the point where there is no group and the individual is the only available unit of analysis

While the infinite regress problem is often raised by philosopher critics, it is not a hypothetical problem that arises only on the theoretical level. Infinite regress poses actual challenges to engineers. If AI attempts to assess bias in all the exponentially many subgroups, it confronts at least two computational problems

The number increases when protected features have more than two possible values (e.g., race: Black, White, Latinx, Native American/Indigenous, Asian, and so on). This way, the proposal to consider every possible subgroup becomes computationally impractical

Second, the size of subgroups would be too small. If subgroups are defined with combinations of 30 binary attributes, each of the 2 30 groups may have only a couple of members, and sometimes no member at all. This raises a data scarcity issue [40, 56]. How does an algorithm seek parity among subgroups if there are too little data available for most of the groups? It also risks overfitting

However, the attempt to consider all subgroups defined by intersecting combinations of protected attributes leaves algorithms with too many and too small subgroups—or, more precisely, individuals. If what PA fundamentally seeks is statistical parity between individuals (e.g., all individual job applicants have an equal probability of getting hired), it is unclear how this raceblind/gender-blind fairness measure specifically tackles intersectional race and gender bias against women of color (이건 맞다. Individual 간의 평등)

Reasonable point of stop?

“relevant” subgroups into consideration. Their line of argument proceeds as follows: In order to resolve both the problem of intersectional bias in AI (i.e., considering too few groups) and that of infinite regress (i.e., considering too many groups), we should split protected groups more finely but stop splitting at a “reasonable” point—somewhere between too few and too many. The question then is: What is a reasonable point and how do we know it? In short, according to these researchers, PA is to consider only statistically meaningful subgroups that can be identified by computers, as opposed to every possible subset.

This would lead to failure to protect minority subgroups [23]. Subgroups that are severely underrepresented in the dataset due to the very intersectional oppression they suffer are likely to be dismissed as “statistically meaningless.”

I argue that PA’s presupposition that it is okay to exclude statistically less important subgroups from the fairness consideration is another form of fairness gerrymandering, namely, an arbitrary selection of protected attributes

As explained earlier, fairness gerrymandering refers to an algorithm being fair with respect to one attribute (e.g., statistical parity between Blacks and whites) but unfair with respect to multiple attributes

statistically meaningful subgroups. Just as algorithms that require fairness only among racial groups can be criticized for being arbitrary from the perspective of intersectional racial and gender injustice, algorithms that designate race and gender as protected attributes can also be criticized for being arbitrary from the perspective of intersectional race, gender, class, and disability injustice

Q. 통계적으로 유의미하다는 것을 너무 약하게 보고 있는 것은 아닌가?  통계적 유의미성이 만능 키는 아닐지더라도, 최소한 임의성의 혐의에서는 어느 정도 벗어나게 해주는 것일지도? – 그러니까 통계적으로 유의미하다면, 그것이 dataset에서 marked될 수 있는 feautre를 가지고 있다는 것.  그리고 언제나 opression은 marked difference를 중심으로 일어나지 않나?  datset에서 포착될 수 있는 통계적 유의미성은 그렇다면 완전 임의적이라고 볼 수는 없지 않나?

As such, any decision to delineate between relevant and irrelevant subgroups is susceptible to criticism that it is arbitrary. The response that “we protect only such-and-such attributes because they are statistically meaningful while others are not” is inadequate to resolve the arbitrariness/gerrymandering concern, since the question of what is “relevant” is itself a political battleground, not merely a statistical problem

Q. 이게 결국 data enginner들과의 가장 큰 의견 차이일 듯하다. Relevancy가 political battleground의 영역이라고 해도!  당장 실제로 포착되고 deal될 수 있는 fainness problem은 통계적 유의미함으로 판단되어야 하는 것이라고 데이터 엔지니어들은 push할 듯. 결국 what is relevant?  can be decided by 통계적 유의미함.  That is the only (objective, scientific) criterion we have.

PA would suggest enforcing parity of false alarm rates between intersectional subgroups defined by combinations of gender = {nonbinary, female, male} and race = {Black, white, other races}. The algorithm is “intersectionally fair” if the rate for Black nonbinary people to be falsely marked as risky is roughly the same as, for example, the rate for white females

This fairness definition misses the point

To divide people into gender-racial subgroups and assess the false positive rate for Black nonbinary people, “nonbinary” must exist as one of the types of gender (and “Black” as a type of race). However, as Costanza-Chock’s experience shows, the problem is that there is no such thing as “nonbinary gender” in the algorithm in the first place. “Nonbinary” has not even been considered as a type of gender whose (statistical) relevance can be measured. It is an “unobserved characteristic,” in Tomasev et al’s [51] terminology

These issues of relevance—or more precisely, what can be assessed as more or less relevant, and what remains unobserved from the consideration of relevance—are political problems, not purely statistical ones that computers can identify and measure

Parity does not equal fairness

So far, this paper has focused on PA’s misinterpretation of intersectionality. The current section draws attention to PA’s misinterpretation of fairness. I argue that PA fails to capture what it really means for AI algorithms to be “fair,” in terms of both distributive justice and non-distributive justice.

PA takes a distributive approach to fairness. Suppose that a philosophy graduate program uses an AI algorithm to make admissions decisions. According to PA, this algorithm is intersectionally fair if it achieves parity of a statistical measure (e.g., the probability of being admitted) among intersectional subgroups of applicants (e.g., Black women, Black men, white women, and white men). That is, PA holds the view that equal distribution is a proper way of distributing benefits: the algorithm is fair if it distributes admissions rates equally across racial-gender groups.

. In order to undo the effects of structural oppression, I argue, AI-driven decision-making process may require more active interventions that allow a higher probability of preferable outcomes for marginalized subgroups than for privileged subgroups (적극적 우대조치의 필요성을 고려할 수 없는 algo)

The equalization of admissions rates does not ensure fairness, as it reflects and reproduces the status quo underrepresentation of Black women in philosophy Without attending to the structural pattern that privileges certain groups while marginalizing others, a mere equal probability distribution does not achieve fairness.

. I argue that AI fairness should be examined through this lens of non-distributive justice. The notion of fairness as a matter of challenging and subverting oppression, as opposed to a matter of achieving statistical parity, better captures what it means for algorithms to be “fair” and provides better directions for developing “fairer” algorithms.

PA seeks to mitigate these biases by equally distributing some number (e.g., approval rates or false denial rates) across groups defined by combinations of race and sexuality. However, the mortgage denial gap is not just a matter of numbers; it has been caused by social, institutional, and historical contexts, including the stereotype of homeowners as white married heterosexual men, the credit score system working in favor of landlords, and socioeconomic inequality between races that stem from the history of slavery and Jim Crow [38, 39]. It is these non-distributive contexts that shapes the uneven, unfair distributive pattern of denial rates.

Although seeking a more evenly distributed pattern is desirable, it is misleading to say that an algorithm’s fairness depends only on how it distributes the number.

Another problem with the distributive paradigm it overextends the concept of distribution to non-material values [58, pp. 24-30]. PA also understands non-material values, such as opportunities for education and employment, as if they were tangible material goods that can be allocated between groups.

Opportunity is a concept of enablement rather than possession; it refers to doing more than having. A person has opportunities if he or she is not constrained from doing things, and lives under the enabling conditions for doing them. ... Evaluating social justice according to whether persons have opportunities, therefore, must involve evaluating not a distributive outcome but the social structures that enable or constrain the individuals in relevant situations

To begin with, I suggest shifting the focus of fairness research from intersections of protected attributes to intersections of structural oppression. In the case of algorithms that are biased against Black women, such as the face recognition algorithm that performs worst on Black women, research for fairer algorithms can be guided by the following questions: Through what process is the structure of racial patriarchy is being embedded into AI algorithms? (embedding question!)

In this regard, I suggest that intersectional fairness research center more around non-distributive fairness than around distributive fairness. It is racist-sexist systems and contexts of society (i.e., non-distributive matters) that produces the unfair distributive pattern of error rates from the face recognition algorithm between Black women and white men

Here I propose to distinguish between weak fairness and strong fairness . In a weak sense, AI fairness means passively and retroactively “de-biasing” the algorithm s. Then it proceeds to “fix” the problem by applying the statistical parity standard not only to Blacks/whites and women/men, but to their intersectional subgroups

Thus, AI fairness in a stronger sense means using algorithms to actively and proactively challenge oppression and make society fairer. A central guiding question for strong AI fairness is how to design algorithms to promote fairness in society. Let us consider the recidivism prediction algorithm for example. What is the purpose of developing and using this algorithm anyway? Is it to put people in jail for more years, or to prevent them from going back to factors that could lead to recidivism (such as poverty, violence, drug and alcohol use) and to help them thrive in society? If the algorithm is reoriented from incarceration to rehabilitation, how would its risk rating change? How can and should the algorithm be redesigned to oppose the mass incarceration of poor people of color and the systemic racial-economic inequality?

. I expect that many AI fairness researchers would actually agree with Noble when she says that the goal of her project is to “eliminate social injustice and change the ways in which people are oppressed with the aid of allegedly neutral technologies,” [42, p. 3] because their research, too, has been motivated by the acknowledgment that AI technologies are not neutral but reproduce social injustice