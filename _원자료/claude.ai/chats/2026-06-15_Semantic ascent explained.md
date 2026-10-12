---
title: "Semantic ascent explained"
uuid: 9100ff63-bf6f-4a24-96e8-010a3cf1daf5
created: 2026-06-15
updated: 2026-06-15
project: ""
url: https://claude.ai/chat/9100ff63-bf6f-4a24-96e8-010a3cf1daf5
turns: 8
type: 원자료/대화
---

> 요약: **Conversation Overview**  The person is working through Nathan Salmon's paper "Nonexistence" using a structured pedagogical walkthrough, having invoked a `/learn` skill that guides Claude to pace explanations and stop at points of predicted difficulty. The session began with a brief exchange on semantic ascent (Quine's term from *Word and Object* for shifting from object-level talk to talk about words), which Claude connected to Salmon's later use of the concept in §II of the paper. The person then uploaded the Salmon PDF and requested a step-by-step walkthrough, with Claude calibrating explanation depth to their evident background in analytic philosophy of language.  The substantive work focused on §I of the paper: the four theory-relative notions of falsehood (R-false₁, R-false₂, F-false₁, F-false₂) that Salmon uses to dissolve the appearance that Russell's and Frege/Strawson's disagreement over singular negative existentials like "The present king of France is bald" is merely verbal. Claude presented a structured table mapping the four notions to their truth conditions for sentence (1), then asked the person to identify which of Russell's two negations — (2′) the innermost/de re or (2″) the outermost/de dicto — constitutes the authentic contradictory of (1), and what that implies for whether (1) is F-false₁ on Russell's theory. The person then offered their reconstruction in Korean, correctly capturing Russell's scope-based account and the existential failure grounding (2′)'s falsity, while flagging genuine confusion about why F-false₁ requires its negation to be true and how that interacts with Frege's gappiness verdict for (1).  Claude's final response confirmed the Russell reconstruction was accurate and resolved the F-false₁ confusion in three steps: (a) falsehood in general follows the schema "false = its negation is true"; (b) that negation must be a genuine contradictory, not merely a contrary, since contraries can both be false; (c) Frege's choice negation propagates gaps (U → U), so ∼c(1) is also gappy and not true, meaning (1) fails to be F-false₁ on Frege's theory — confirming the person's intuition that gappiness is exactly why. On Russell's theory, (2′) is a contrary (both it and (1) can be false together when no king exists) while (2″) is the genuine contradictory and is true, making (1) F-false₁ on Russell's account. This is Salmon's substantive disagreement: Frege/Strawson slide from "(1) is not R-false₂" to "(1) is not F-false₁," but these track different sentences — (2′) versus (2″) — and only come apart in improper-description cases. The walkthrough paused there, with §II (semantic ascent vs. intensional ascent, and the Church translation argument) identified as the next difficulty spike.

## 영진 · 2026-06-15T02:13

/learn 

what is semantic asencet?

## Claude · 2026-06-15T02:14

[tool_use: view]

"Semantic ascent" is Quine's phrase — *Word and Object* §56. It names the shift from talking about things to talking about the *words* for those things: from "there are miles between cities" up to "the term 'mile' functions thus-and-so." Quine borrows Carnap's contrast here: descending in the **material mode** (about objects), ascending to the **formal mode** (about expressions).

The payoff Quine cares about is strategic, not just classificatory. When two parties disagree about *what there is* — numbers, classes, possibilia — they can often still agree about *the words*, so ascent buys neutral common ground to argue on. And it lets him hold that ontological questions are continuous with science rather than "merely verbal": you can address them through language without the disagreement collapsing into a dispute about usage. It's also load-bearing for his picture of philosophy as not sharply divided from science — ascent is always available, but it earns its keep exactly where object-level talk gets unwieldy through sheer generality.

That's the core. Where are you coming at it from — tracing how it sits against Carnap's formal/material mode, its role in Quine's ontology (the "to be is to be the value of a bound variable" machinery), or something closer to your own occasion-sensitive instincts, where Quinean ascent might look like the move you'd want to *resist*?

## 영진 · 2026-06-15T02:18
> 파일: 33EA8CA6-BBB2-11EE-9529-E8CE5A6FA55B.pdf

/learn 

let's walkthrough this pdf, step by step, stop at where you think I would struggle.

## Claude · 2026-06-15T02:21

[tool_use: visualize:read_me]

Good — this connects straight to where we just were: the "semantic-ascent theory of existence" Salmon dismantles in §II is the very Quinean device from footnote 13. But let's start at the top as you asked.

**The on-ramp (§I, roughly pp. 277–281).** I'll assume this part is routine for you, so just the skeleton: Salmon sets the target as *true singular negative existentials* — (0) "Sherlock Holmes does not exist" read as about reality. Moore frames the paradox (to deny something *being* you seem to grant it being). Then the two classical responses you know cold: Russell's Theory of Descriptions (the (1)–(4) battery, the primary/secondary scope split in (2), names abbreviating descriptions so (0) → (0′)) versus Frege/Strawson (presupposition, truth-value gaps, Compositionality for Reference). None of that should slow you down.

**Where I'd predict the first real stop (pp. 280–282, plus fn. 10).** It's not a *concept* that's hard here — it's the *bookkeeping*. Salmon refuses Russell's "merely verbal" dismissal of Strawson by splitting "false" into four theory-laden notions and showing they don't line up cleanly across the two theories. Here's the geography for (1) "The present king of France is bald":

| notion | keyed to | for (1) | reading |
|---|---|---|---|
| **R-false₁** | outermost negation true → (2″) | **true** → (1) is R-false₁ | de dicto / "untruth" |
| **R-false₂** | innermost negation true → (2′) | false → (1) **not** R-false₂ | de re |
| **F-false₁** | choice (authentic-contradictory) negation true | Frege: (1) **not** F-false₁ (it's U) | the 'F' of the 3-valued table |
| **F-false₂** | exclusion negation true | (1) is F-false₂ | "untrue" |

The clean part: R-false₁ ≈ F-false₂ ≈ untruth, and *everyone* grants (1) is "false" in that sense. The trap is the other diagonal. Both camps will say "(1) is *not*-false in a second sense" — Russell via "not R-false₂," Frege via "not F-false₁" — and it *looks* like they're agreeing, which is what makes "merely verbal" tempting. Salmon says no: R-false₂ and F-false₁ are different animals (scope ambiguity vs. lexical ambiguity), so the apparent symmetry is an illusion.

So here's the question I'd stop you on before moving to §II:

Salmon insists (p. 282 / fn. 10) that for Russell to actually *rebut* Frege's claim "(1) is neither true nor F-false₁," it is **not enough** for Russell to concede "(1) is neither true nor R-false₂." Given the table — and in particular how F-false₁ has to be read once you take it as truth of the *authentic contradictory* — what further thing must Russell positively assert, and what's the confusion he's accusing Frege/Strawson of? Work it in terms of which sentence, (2′) or (2″), each notion actually keys on.

(If this one's beneath your struggle threshold, say so and I'll roll straight into §II, where I think the genuine difficulty starts — the intensional-ascent theory and why it survives the Church translation argument when semantic ascent doesn't.)

## 영진 · 2026-06-15T02:26

woow... more explanation needed

## Claude · 2026-06-15T02:28

Yeah — this is the part that *looks* like routine Russell-vs-Strawson and is actually doing fiddly three-valued bookkeeping. Let me build the machinery piece by piece, slowly, and then hand you back the one inference.

**First, why "false" splinters at all.** The two theories have ambiguities in *different places*, and that's the whole engine.

**Russell's ambiguity is structural (scope).** Descriptions are quantifiers, so "the present king of France is not bald" is two different sentences depending on where the negation sits relative to the quantifier:

- (2′) = (∃x)[uniquely-KoF(x) ∧ ¬Bald(x)] — quantifier outside, negation *inside*. "There's a unique king of France, and he's non-bald." Since there's no king, this is **false**.
- (2″) = ¬(∃x)[uniquely-KoF(x) ∧ Bald(x)] — negation *outside*, quantifier inside. "It's not the case that some unique king of France is bald." Vacuously **true**.

Salmon then renames these by where the *negation* ends up: (2″) is the **outermost** negation (description squeezed to narrowest scope), (2′) is the **innermost** negation (description widest). And he defines:

- (1) is **R-false₁** iff its *outermost* negation (2″) is true → since (2″) is true, **(1) is R-false₁**.
- (1) is **R-false₂** iff its *innermost* negation (2′) is true → since (2′) is false, **(1) is not R-false₂**.

He also gives these a theory-neutral gloss: outermost = the *de dicto* negation ("it's not true that the PKoF is bald"), innermost = the *de re* negation ("the PKoF is such that he's non-bald"). Hold onto that — it's how he later compares across theories.

**Frege's ambiguity is lexical — inside the word 'not' itself.** No scope play (descriptions are singular terms, so there's just one negation), but 'not' comes in two flavors, separated by their three-valued tables:

- **Choice** negation ∼c: behaves Kleene-style. True→F, False→T, and crucially **gap→gap**.
- **Exclusion** negation ∼e: True→F, False→T, but **gap→true**. So ∼e P just says "P is *not* true," i.e. P is untrue.

For Frege, (1) is a **gap** (U) — the description fails to refer, so by Compositionality for Reference the whole sentence has no truth value. Now run both negations:

- (1) is **F-false₁** iff its *choice* negation is true. ∼c(1) is "PKoF is not-c bald" — gap in, gap out, so **not true** → **(1) is not F-false₁**. (This is the genuine-gap verdict: (1) isn't false *in the truth-table sense*.)
- (1) is **F-false₂** iff its *exclusion* negation is true. ∼e(1) = "it's not-true that PKoF is bald" — and (1) *is* untrue, so this is **true** → **(1) is F-false₂**. F-false₂ is just "untrue."

**Now the two diagonals.** Line them up against the neutral *de re/de dicto* gloss:

- **R-false₁ ≈ F-false₂ ≈ plain untruth.** Both camps agree (1) is "false" here. No fight.
- The *other* two — **R-false₂** and **F-false₁** — are each camp's "(1) is *not* false in this stricter sense." Russell: "(1) is not R-false₂." Frege: "(1) is not F-false₁." They *sound* like the same concession, which is what makes Russell's "it's merely verbal" tempting.

And here's the keystone Salmon adds, which is the thing I want you to push on: **F-false₁ has to mean truth of the choice negation taken as the *authentic contradictory* of (1)** — not just any choice-negation reading, but the one that genuinely contradicts the original. (A choice negation that doesn't actually contradict (1) is irrelevant to whether (1) is F-false₁.)

So now the last step, which I'll leave to you because it's the whole point:

On Russell's theory, the original (1) splits its negation into (2′) and (2″). **Which one is "the authentic contradictory of (1)"** — the thing that genuinely says the opposite — and is it true or false? Once you answer that, you'll have located whether **(1) is F-false₁ *on Russell's own theory*** — and you can compare that verdict to the separate fact that (1) is *not* R-false₂. If those two come apart, you've got Salmon's point: why agreeing "(1) is not R-false₂" doesn't buy Russell "(1) is not F-false₁," and what the Fregean is allegedly sliding between.

Take a swing at just that — which of (2′)/(2″) is the authentic contradictory, and what does that make (1) on the F-false₁ question?

## 영진 · 2026-06-15T03:09

내가 이해한게 맞는지 봐봐.. 

그니깐 러셀은 (1)이 두 가지 방식을 부정되는데, (2'')만 (1)이랑 모순이고, (2')은 (1)이랑 똑같이 거짓이라는 거지. 그런데 거짓인 이유가, 지칭하는 존재가 없으니, 안에 있는 존재 진술에 걸려서, 거짓이 되는 거고. 그래서 2''이 참이면 (1)이 R-1 false고 2'이 참이면, (1) R-2 false라는 거지?

프레게는 Negation의 종류를 나눠서 해결하려고 하고. 근데 둘이 비슷한 결론을 내는 것처럼 보이지만... F-false 1이 어떻게 (1)에 대한 진짜 모순이 되어야 하지? 그게 이해가 안되네. 그니까 (1)이 부정이 참이어야 (1)이 F-false1이라는 건데, 왜? (1)은 Frege에게 Gappy한거 아니야?

## Claude · 2026-06-15T03:11

러셀 쪽은 정확하게 잡았어. 특히 **(2′)이 왜 거짓인지** — "유일한 왕이 존재하고 그가 비대머리다"인데 존재 진술 `(∃x)[유일-KoF(x) ∧ ¬대머리(x)]`의 존재 연언지가 깨져서 통째로 거짓이 된다는 것 — 이건 핵심이고 네가 말한 그대로야. (2″) 참 → (1)은 R-false₁, (2′) 참 → (1)은 R-false₂, 도 맞아.

이제 막힌 지점, F-false₁. 두 가지를 분리해서 보면 풀려.

**(가) F-false₁은 "거짓 = 그것의 부정이 참"이라는 일반 도식의 한 사례야.** "거짓"이 뭐든 간에 그건 "참의 반대편"이지. 그래서 양 진영 모두 *false = 그 문장의 부정이 참* 으로 정의할 수 있어. 프레게는 부정이 두 종류(choice ∼c / exclusion ∼e)니까 falsehood도 두 개로 갈라져 — F-false₁(=choice 부정이 참), F-false₂(=exclusion 부정이 참).

**(나) 그런데 여기서 그 '부정'은 아무 부정이 아니라 진짜 *모순*(contradictory)이어야 해.** 왜냐면 "부정이 참이면 원문이 거짓"이라는 도식은, 그 부정이 원문과 진리치가 *반드시 반대로* 가는 놈일 때만 성립하거든. 단순한 **반대(contrary)**로는 안 돼 — 반대는 둘 다 거짓일 수 있어서, "부정이 참"이 원문의 거짓을 추적하지 못해.

**(다) 이걸 프레게에 적용해봐 — 그러면 네 직관이 정확히 답이야.** 프레게에게 (1)은 gappy(U)지. 그런데 choice 부정 ∼c는 *gap이 들어가면 gap이 나와* (∼c의 3치 표에서 U → U). 그러니까 ∼c(1)도 U, 즉 **참이 아니야**. 따라서 정의상 (1)은 **F-false₁이 아니다.** → 이게 바로 프레게/스트로슨의 주장이야: (1)은 *참도 아니고 F-false₁도 아니다* = 진짜 진리치 빈틈. 네가 "(1)은 프레게에겐 gappy하잖아?"라고 한 게 정확히 (1)이 F-false₁이 아닌 *이유*야. 부정이 참이어야 한다는 건 그냥 이 falsehood의 정의이고, gap이 choice 부정을 타고 그대로 전파되니까 (1)도 그 부정도 참이 못 돼서 둘 다 빈틈에 빠지는 거지.

**(라) 그럼 (나)의 "진짜 모순" 조건은 어디서 일을 하느냐 — 러셀 이론에 F-false₁을 얹어볼 때야.** 러셀에겐 (1)의 부정이 (2′), (2″) 둘이잖아. 어느 게 (1)의 *진짜 모순*일까?

- (1′) "유일한 KoF가 대머리" vs (2′) "유일한 KoF가 비대머리" → 왕이 없으면 **둘 다 거짓**. 둘 다 거짓일 수 있으니 이건 **반대(contrary)**지 모순이 아니야.
- (2″) "유일한 KoF가 대머리인 것은 아니다" → (1′)과 진리치가 반드시 반대로 가는 놈. 이게 **진짜 모순(contradictory)**.

(1′)이 거짓이니까 그 진짜 모순인 (2″)은 **참**. 그래서 **러셀 이론에서는 (1)이 F-false₁이야.**

**결론.** 같은 (1)을 두고:
- 프레게 이론: (1)은 F-false₁ *아님* (choice 부정이 gappy).
- 러셀 이론: (1)은 F-false₁ *임* (진짜 모순 (2″)이 참).

이건 말장난이 아니라 실질적 불일치야. 그리고 새먼이 프레게/스트로슨에게 씌우는 혼동이 바로 이거야 — 그들은 **"(1)은 R-false₂가 아니다"** 를 슬쩍 **"(1)은 F-false₁이 아니다"** 로 바꿔치기해. 그런데 R-false₂는 (2′)(de re/innermost)에 걸리고 F-false₁은 (2″)(진짜 모순/outermost)에 걸려서, **서로 다른 문장**에 의존해. 그래서 러셀이 "(1)은 R-false₂ 아님"을 인정해도 "(1)은 F-false₁임"은 멀쩡히 살아남는 거지. 부정이 둘로 갈라지는 improper description 케이스에서만 이 둘이 벌어지고, 그 틈을 프레게는 (부정이 하나뿐이라) 못 보고 뭉개버리는 거야.

여기까지가 §I의 진짜 매듭이야. 정리되면 §II — semantic-ascent vs intensional-ascent, 그리고 Church 번역 논증 — 로 넘어갈까? 거기가 다음 난도 스파이크라고 봐.
