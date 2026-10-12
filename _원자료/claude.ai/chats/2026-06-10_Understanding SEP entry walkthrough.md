---
title: "Understanding SEP entry walkthrough"
uuid: 74d71b05-fe9d-4352-b981-e71d1af71f24
created: 2026-06-10
updated: 2026-06-10
project: ""
url: https://claude.ai/chat/74d71b05-fe9d-4352-b981-e71d1af71f24
turns: 10
type: 원자료/대화
---

> 요약: **Conversation Overview**  The person is a philosophy researcher and exam developer in Korea working on a non-representationalist, relational account of desire drawing on Travis, Austin, Anscombe, and Thompson. The conversation centered on two extended SEP entry walkthroughs — Ainsworth's "Form vs. Matter" and Millgram's "Practical Reason and the Structure of Actions" — followed by a substantive philosophical exchange about the methodological commitments and theoretical debts the person's own framework incurs.  For the Form vs. Matter entry, the person requested a walkthrough in English first, then asked for a second walkthrough in Korean. Claude covered all four major sections: the introduction of hylomorphism as a response to substantial change, prime matter and the two revisionist challenges (Charlton's non-persisting substrate and the textual underdetermination case), the principle of individuation (Popper's dissolution of the Anscombe-Lukasiewicz dispute, Fine's puzzle and its four escape routes, Ainsworth's landing on particular forms), and the four-position taxonomy of matter-involving forms with its regress structure. Claude flagged the homonymy principle and the *idia*/natural-historical judgment thread as direct connections to the person's Thompson and Foot research. The person then requested that the English walkthrough be saved to Notion, which Claude executed successfully using the Notion MCP integration, creating a structured page titled "Form vs. Matter (SEP) — Walk-Through."  For the Millgram entry, the person requested a walkthrough covering all five research programs (calculative, authorship, challenge-seeking, practice, and evaluation views). Claude organized the walkthrough around Millgram's central diagnostic: that every action-first program derives the bindingness of its inference patterns from the nonoptionality of its conception of action, and that the field's primary pathology is that theorists argue for their own conception without addressing why competing conceptions fail. Claude flagged Thompson's anti-psychologistic, aspect-based treatment of desire-locutions and Brewer's anti-propositional account of what moves us in dialectical activity as the two most directly relevant threads for the person's own project. The walkthrough closed with Millgram's strategic fork between theoretical and practical bindingness, and the pluralism-about-action escape. The person then asked what "bill" their Travis/Austin framework of desire incurs under Millgram's diagnostic framework, prompting Claude to reconstruct the exposure in detail: the framework's principled refusal of Millgram's nonoptionality bill converts into a genuineness-of-occasion-relative-correctness bill, which splits into a source horn (Travis's occasion-relative correctness versus Thompson's life-form-anchored normativity, and the internal tension between them) and a content horn (what correctness consists in for a state with direction of fit but no satisfaction condition, including the Vogler-trap risk of inheriting calculative-only correctness without resources for deliberation of ends). Claude identified hyperintensionality (whether the Aspect conjunct is a genuine alternative to mode of presentation or a verbal relabeling) and occasion-*can* scope (whether Austin's ability-can extends to cover Schapiro's modality of freedom or leaves a gap requiring a separate normativity account) as the two audit sites where the gap-refusal's genuineness gets decided.  The person's framework involves a five-conjunct formalized account of desire (Relatum, Aspect, Instancing, Capacity, Explanation) and has two named open research questions: hyperintensionality and the scope of Austin's occasion-*can*. Claude noted that both open questions map directly onto the load-bearing pressure points in the Millgram audit. The person's communication style is expert-level and compressed; they prefer rigorous, prose-forward philosophical analysis with explicit connection-flagging to their own research rather than exhaustive exposition. Claude flagged connections to Thompson's *Life and Action*, Foot's natural goodness, and Brewer's dialectical activity throughout, and offered to extend the analysis into specific texts (Travis's "The Silence of the Senses," Austin's "Ifs and Cans") at the person's direction.  **Tool Knowledge**  Notion page creation used the `Notion:notion-create-pages` tool with a single-object `pages` array. The working parameter structure included `properties` (with `title` as a string), `icon` (emoji string), and `content` (full Markdown string). Rich Markdown formatting — heading levels, bold, horizontal rules, nested lists, and inline ital

## 영진 · 2026-06-10T04:24
> 파일: form-matter_a4.pdf

Will you be kind and walk me through this SEP Entry?

## Claude · 2026-06-10T04:29

Glad to. This is one of the better SEP entries to read closely, because it has a real argumentative spine rather than just cataloguing positions. Before going section by section, here's the spine, because it's what makes the four parts hang together.

Hylomorphism is born to do one job: explain *change* without violating "nothing comes from nothing." Form and matter enter as a clean contrastive pair purpose-built for that job. The drama of the entry is watching that tidy contrast get progressively strained — and at points nearly broken — as Aristotle puts the same pair to work on problems it wasn't designed for. Each of the three controversies (prime matter, individuation, matter-involving forms) is a site where the neat form/matter opposition buckles under load. Ainsworth says as much in his last paragraph: the contrast is "no less elastic than explanatorily powerful." Keep that arc in view and the whole thing reads as a single escalating pressure test.

**1. Matter and form introduced**

The notions are reverse-engineered from an analysis of change. Aristotle splits change in two: *accidental* change, where a substance gains or loses a property (Socrates turns blue, or puts on weight), and *substantial* change, where a substance comes into or goes out of existence (Socrates is born, or dies). Any change, he says, needs three things — something that underlies and persists, a "lack" (one pole of a pair of opposites), and the form acquired. In accidental change the persisting thing is obvious: Socrates himself stays put while going from unmusical to musical.

The pressure point is substantial change. Here the *substance* is exactly what's coming or going, so it can't be the thing that persists. Something else must — and that something is the substance's **matter**. Bricks survive the building of the house; the elements survive the death of the organism. Deny this and you've got things popping in and out of existence ex nihilo, which Aristotle, siding with Parmenides, won't allow. Note the methodological texture worth flagging: his metaphysics starts from observed phenomena and tries to conserve common sense.

Two refinements do a lot of work later. First, **form is not shape**. The artefact examples (the form of a bronze statue *is* its shape) mislead. For organisms, form is *definition or essence* — and essence is tied to *function*. A statue is human-shaped but isn't human, because it can't do what humans do. This is reinforced by the **homonymy principle**: a dead body is only "homonymously" a body, the way a painted eye is only homonymously an eye — it bears the name by resemblance but can't perform the function the thing exists for. (This functional, life-form-relative way of individuating is the deep Aristotelian backdrop to the neo-Aristotelian naturalism you've been working through in Thompson and Foot — the "dead flesh is only homonymously flesh" move is the same logic that makes natural-historical judgments life-form-relative. I'll come back to this at the *idia* discussion, since that's the even cleaner connection.)

Second, the four causes get quietly compressed. Aristotle lists four — material, formal, efficient, final — but observes that for living things the last three tend to collapse into one answer (a human is *defined as* something that lives a rational life, that's *what a human is for*, and humans are *made by* humans). So the four causes really reduce to two ineliminable explanatory roles: matter and form.

Then comes the section's genuine puzzle, and it's sharper than it first looks. Artefact matter is only *contingently* enmattered — the same bronze that's now a statue can be melted into jewelry. That contingency is exactly what lets matter play the "persisting substrate" role. But organic matter looks different. Your body doesn't obviously pre-date you the way bricks pre-date the house, and (by the homonymy principle) it doesn't survive you either. So a human's matter seems to need to be *contingently* alive (to underlie coming-to-be) yet *essentially* alive (because it's functionally defined). That's a flat contradiction.

The resolution is **levels of matter**, and it's the most important structural idea in the section. Matter is relative — always the matter *of* something — and itself decomposes into matter-plus-form, all the way down: body → flesh and bones → … → the four elements. The *proximate* matter (the organic body) is essentially alive and exists exactly as long as the organism does. But further down, the *remote* matter (ultimately the elements) need not be alive and can survive the organism's death. So the substrate that underlies substantial generation lives at the bottom of the hierarchy, which dissolves the contradiction. The homoiomerous/heteromerous distinction (structureless stuffs vs. structured organs) and the denial of atomism (matter is infinitely divisible) ride along here, but the load-bearing move is the hierarchy.

**2. Prime matter**

This section just pushes the level-of-matter question to its limit: how far down does the substrate go? The pressure point is *elemental* change. The four elements are defined by paired opposites (hot/cold, wet/dry), and they transform into one another. By Aristotle's own analysis, water→air needs something underlying that persists — but it can't be any element, since it has to take on each element's properties in turn. That seems to demand a bottom rung: **prime matter**, pure potentiality with no essential properties of its own, mirror image of the unmoved movers as pure actuality. The traditional reading (Augustine, Simplicius, Aquinas) attributes exactly this to him, and Ainsworth flags the Platonic ancestry — the *Timaeus* receptacle, motivated by the very same elemental-transformation phenomenon.

The revisionist case has two prongs worth separating.

The *textual* prong: Aristotle does use "prime matter," but he himself says the phrase is ambiguous between a thing's proximate matter and its ultimate matter, so the vocabulary settles nothing. In several places he's studiedly noncommittal — the *Metaphysics* ix 7 conditional ("*if* there is something primary…") and his coined adjective "that-en" show him entertaining prime matter as a *possibility* without endorsing it. The vii 3 "by matter I mean that which in itself is neither substance nor quantity…" passage is the strongest pro-prime-matter text, but opponents can reread it as a *reductio*: regard matter as substance and you'd absurdly be committed to a wholly indeterminate substrate.

The *philosophical* prong is the more interesting. Charlton's move is to deny that change *always* requires a persisting thing. In elemental change there's an underlying thing — the initial element — but it doesn't persist; it's consumed. The vulnerability is immediate and Ainsworth presses it: if nothing persists through water→air, what distinguishes that from water vanishing into nothing and air materializing from nothing — the very thing Aristotle forbids?

Then the two objections to prime matter, which you'll want to keep distinct because they're different in kind. The *epistemic* objection (it's unknowable, since we only ever perceive what it underlies) is the weaker one — Ainsworth defuses it with the quark analogy; unobservables earn their keep by theoretical work. The *logical* objection is the real threat: prime matter is supposed to have no essential properties (so it can take any form), yet we want to call it eternal, invisible, the ultimate bearer — and worse, when Socrates turns blue, the prime matter underlying him "turns blue" too, so it must be simultaneously invisible *and* blue. The proposed fix — distinguish prime matter's essential from its accidental properties — threatens a regress (what underlies *those* essential properties?), staved off only by stipulating that prime matter underlies its own essential properties without being a further compound. Whether that stipulation is principled or ad hoc is where the live debate sits (Oderberg and Brower defend coherence; Koslicki resists).

**3. The principle of individuation**

The single most clarifying move in the entry is **Popper's dissolution** at the top of this section, and it's a model of how to handle a "scholars disagree" setup. Anscombe and Lukasiewicz look opposed — matter vs. form as the principle of individuation — but they're answering *different questions*. Lukasiewicz wants to know what makes a thing-with-many-parts *one* individual rather than a heap; that's a question about **unity**, and form answers it. Anscombe wants to know what makes this individual *numerically distinct* from another of the same kind; that's a question about **distinctness**, and matter answers it. Both can be true at once. Ainsworth then fixes the terminology: call the unity-answer a *principle of unity* and reserve *principle of individuation* for the distinctness-answer.

There's a second framing question stacked underneath: is individuation a *metaphysical* issue (what makes Socrates distinct from Callias?) or merely *epistemological* (how do we *tell* them apart?) — Charlton presses the latter. And there's a skeptical challenge worth dwelling on, because the dialectic is elegant: maybe numerical distinctness is just *brute* — nothing makes Socrates distinct from Callias, they simply are. The matter-theorist's natural reply ("matter explains its own distinctness — it's just *this* matter") backfires, because "this matter is distinct because it's this matter" has exactly the same form as "Socrates is distinct because he's Socrates" — both are x explaining its own distinctness. But the matter-theorist adopted her view *precisely because* she found that kind of self-explanation unsatisfying. So she can't help herself to it. The upshot both sides accept: explanation stops somewhere; they only disagree about *where* the brute fact sits.

The centerpiece is **Fine's puzzle** (1994), and it's the part most worth having crisp. It's a valid argument that matter-as-individuation can't survive:

1. It's possible that Socrates and Callias are composed of numerically the same matter (at different times).
2. Socrates and Callias have the same form.
3. Each is a compound of matter and form.
4. Therefore it's possible that Socrates and Callias are numerically the same — which is absurd.

So a premise must go, and the four escape routes map the live options:

*Equivocate on "matter"* — same remote matter (elements), different proximate matter (body). Tidy, but Ainsworth shows it can be neutralized: push the "same form" requirement down through every level of matter, and the equivocation closes, leaving the argument valid again.

*Reject P1* (matter is essential to the person). Plausible for *proximate* matter (homonymy principle again — your dead body isn't really your body), but not for *remote* matter: the elements survive in the dead stump and can migrate into a new tree, which is all the puzzle needs. Prime matter doesn't rescue you here either — if it can underlie anything, it can't be confined to one kind of thing.

*Reject P2* (co-specific things share a form) — this requires **particular forms**, and it's the route Ainsworth ultimately favors. The catch he flags is a circularity trap: if particular forms are just indexed universals (the universal paired with its bearer), then the form depends on the substance for its identity, and a form can't individuate the very substance it depends on. Particular forms have to be defined *independently* of their bearers to do the job (Koslicki's neo-Aristotelianism bites this bullet).

*Reject P3* (a compound is matter-plus-form *at a time*) — relativize the compound to times (and worlds). This handles the puzzle directly but collides with a commitment Aristotle won't surrender: that form *unifies* a compound (*Metaphysics* viii 6, vii 17). Time can't be one more ingredient for form to unify, and letting form unify the same matter into different objects at different times stops deserving the name "unification." So this route is exegetically dead.

Ainsworth's landing: separate the two questions one last time — what keeps *this* giraffe the same giraffe over time (unity; "giraffeness in general" may suffice) versus what makes *this* giraffe distinct from *that* one (individuation; neither the shared universal nor the potentially-shared matter can do it). Particular forms are the only candidate left standing.

**4. Matter-involving forms**

The final strain on the contrast. The motive is anti-Platonic: Aristotle wants his forms *enmeshed in matter*, unlike Plato's separable Forms, and his banner case is the **snub** — concavity-realized-in-a-nose, where you can't specify the form without mentioning the matter. The question is how literally to take this. Does a natural form *itself contain* a specification of its matter (Balme, Charles, Peramatzis), or is that a conflation of the very roles form and matter were introduced to keep apart (Frede, Corkum, Meister)?

The textual situation in *Metaphysics* vii 11 is genuinely undecidable, and Ainsworth is honest about why. The pivotal sentence about flesh and bones can be printed as a *statement* ("in truth no, they are the matter…" — so flesh and bones are *not* part of the form) or as a *question* ("or are they rather matter…?" — leaving open that they *are*). Since punctuation is a later editorial addition, the Greek itself doesn't decide it, and the surrounding passages (the doubts about circle and triangle, the "reduce everything to matter is futile / Socrates the Younger" remark) cut both ways. The whole textual battlefield is, by Ainsworth's lights, a draw.

So the weight shifts to the *philosophical* motivation: only material things change, so if forms are to explain a thing's characteristic changes, they must be matter-involving. The example is falling-when-unsupported, explained by being made mostly of the heavy elements. And here is the cleanest connection to your own terrain — the deflationary reply runs through **hypothetical necessity** and **idia**. Properties like *all and only humans can laugh* attach necessarily to a species but aren't part of its essence; laughter *follows from* rationality plus how the world is. Likewise *all ducks waddle*, but waddling isn't in the duck's function — anything meeting the functional spec must, in a world like ours, walk inelegantly. That "S's do/are F" form is exactly the natural-historical judgment Thompson builds *Life and Action* around, and Foot's Aristotelian categoricals. The point Ainsworth is making with *idia* is the same point Thompson exploits: a characteristic generic can be necessary and life-form-relative without being written into the essence — which is precisely why the form needn't ingest its matter to explain the change. If you want, I can draw out how this bears on your relational/teleological-generic account of wanting, since the logical shape is identical.

The section ends with a taxonomy you'll find genuinely useful, four positions in ascending order of matter-involvement:

1. **Pure forms** — the compound's form/essence is not matter-involving at all.
2. The compound's form *involves* matter, but *that* form has a further essence that's pure.
3. As (2), the compound's form involves matter, but forms simply *have no* further essences.
4. As (2)/(3), and the forms are *themselves* matter-form compounds with further matter-involving essences, all the way down.

The dialectic among them is clean. Position (4) generates a *vicious infinite regress* — an endless series of forms behind every compound, which finite knowers could never complete; and crucially, (2) escapes this because its second-order form is pure. The natural way to dodge (4) is to deny that being matter-involving requires being a hylomorphic compound, which collapses you into (3). But (3) is unstable: forms are *definitions*, definitions have linguistic-style structure with separable parts, and you can always ask of those parts whether they're matter-involving. If some are, you slide back toward the (4) regress; if none are, you become "intolerably similar to (2)." So (3) can't hold its ground.

That leaves the apparently merely-verbal (1)-vs-(2) question, which Ainsworth argues is not merely verbal. (2) posits *two* essences/forms per substance, and since an essence is a *thing in the world* (the human essence *is* a soul) rather than a mere linguistic definition, that's a genuine extra ontological commitment. (1) need only grant a broader *definition* that mentions matter, which costs nothing extra. So unless matter-involving forms earn real theoretical work, parsimony favors pure forms — though, characteristically, Ainsworth leaves the verdict conditional.

That's the tour. The thing I'd most want you to carry away is the structural rhyme across the three controversies: in each, a *traditional* reading takes Aristotle to be making a robust metaphysical commitment (prime matter; matter-as-individuator; matter-involving forms), and a *revisionist* reading either deflates the commitment or relocates it (Charlton's non-persisting substrate; particular forms; pure-forms-plus-broad-definition) — and in each, the deciding consideration is some combination of textual underdetermination plus a charity-or-parsimony argument. It's a remarkably consistent dialectical engine.

Happy to go deeper on any one section — the Fine puzzle and the four-position taxonomy are the two richest, and the *idia*/natural-historical-judgment thread is the one most directly continuous with your own work if you'd like to pull on it.

## 영진 · 2026-06-10T04:38

한글로 walk thorugh해줘

## Claude · 2026-06-10T04:40

좋습니다. 이 항목의 전체 구조부터 잡고 들어가겠습니다.

## 전체 아크 — 왜 네 부분이 하나인가

*Hylomorphism*은 단 하나의 일을 하려고 탄생했습니다: **변화를 설명하되, "무에서 유가 생기지 않는다"는 원칙을 위반하지 않으면서**.

형상(form)과 질료(matter)는 그 일을 위해 정밀하게 설계된 깔끔한 대비쌍으로 들어옵니다. 이 항목의 드라마는 그 깔끔한 대비가 점진적으로 얼마나 경직되는지, 어떤 지점에서 거의 부서지는지를 보여주는 데 있습니다. 아리스토텔레스가 같은 이 쌍을 설계되지 않은 문제들에 계속 적용하면서요.

세 가지 논쟁지점——**소질료(prime matter)**, **개별화 원리**, **질료 포함적 형상**——이 바로 그 깔끔한 형상/질료 대비가 압력을 받는 지점들입니다. Ainsworth가 마지막 단락에서 명시하듯이, 그 대비는 "설명력만큼이나 유연한(elastic)" 것입니다. 이 호를 염두에 두면 전체가 하나의 **점증적인 압력 테스트**로 읽힙니다.

---

## 1절. 형상과 질료의 도입

개념들이 **변화의 분석**에서 역으로 엔지니어링됩니다.

아리스토텔레스는 변화를 두 가지로 나눕니다:
- **우발적 변화(accidental change)**: 실체가 속성을 얻거나 잃음. 예: 소크라테스가 파란색으로 변함, 살이 찜
- **본질적 변화(substantial change)**: 실체가 생겨나거나 소멸함. 예: 소크라테스가 태어남, 죽음

모든 변화는 세 가지가 필요합니다: (1) 변화를 거쳐도 남는 무언가, (2) "결핍(lack)"(대립쌍의 한 극), (3) 획득되는 형상.

우발적 변화에서는 남는 것이 명백합니다: 소크라테스 자신이 음악을 모르는 상태에서 음악을 아는 상태로 바뀌어도 소크라테스는 그대로죠.

**압력점은 본질적 변화입니다.** 실체 자체가 생겨나거나 사라지는데, 그러면 남는 것이 무엇인가? 그것이 바로 **질료**입니다. 벽돌은 집 건설을 거쳐도 남고, 원소들은 유기체의 죽음을 거쳐도 남습니다. 이를 부인하면 무에서 무언가가 생기거나 무로 사라진다는 뜻인데, 파르메니데스를 따르는 아리스토텔레스는 이를 절대 허용하지 않습니다.

여기서 중요한 방법론적 특징: **그의 형이상학은 관찰된 현상에서 출발하고, 상식적 믿음을 최대한 보존하려 합니다.**

두 가지 정교화가 나중에 많은 일을 합니다:

**첫째, 형상은 모양이 아닙니다.** 청동 동상의 예가 오도합니다. 동상의 형상은 확실히 그 모양이지만, 유기체의 경우 형상은 **정의 또는 본질**이며, 본질은 **기능**과 묶여 있습니다. 동상은 인간 모양이지만 인간이 아닙니다. 인간이 할 수 있는 일들(생각하기, 지각, 움직이기, 욕망하기, 먹고 자라기 등)을 할 수 없기 때문입니다.

이건 **동음어성 원리**로 강화됩니다: 죽은 시체는 오직 "동음어적으로만" 신체입니다. 마치 그린 눈이 그림 속에서만 "동음어적으로" 눈인 것처럼——이름은 같지만 진짜 눈이 존재하는 이유인 기능(시각)을 수행할 수 없습니다.

**중요한 포인트**: 이 기능-중심적, 생명형식-상대적인 개별화 방식이 당신이 최근에 Thompson과 Foot 읽으면서 다뤄온 **신아리스토텔레스 자연주의**의 깊은 배경입니다. "죽은 살은 오직 동음어적으로만 살이다"라는 이 동작이 바로 자연-역사적 판단을 생명형식-상대적으로 만드는 같은 논리입니다. 이건 뒤에서 *idia* 논의할 때 다시 나옵니다.

**둘째, 네 원인이 조용히 압축됩니다.** 아리스토텔레스는 네 가지——물질인, 형식인, 동인, 목적인——을 나열하지만, 살아있는 것의 경우 마지막 세 가지가 하나의 답으로 수렴됨을 관찰합니다(인간은 합리적인 삶을 사는 것으로 정의되고, 그것이 인간의 목적이며, 인간은 인간에 의해 생성됨). 그래서 네 원인은 실제로 두 개의 제거 불가능한 설명 역할로 축약됩니다: **질료와 형상**.

그런데 이제 진짜 수수께끼가 나옵니다. **인공물(artefact)의 질료는 오직 우연히만 그 형상을 가집니다.** 같은 청동이 지금은 동상이었다가 녹여서 장신구가 될 수 있습니다. 그 우연성이 정확히 질료로 하여금 "남는 기층(persisting substrate)" 역할을 할 수 있게 합니다.

그런데 **유기체 질료는 달라 보입니다.** 당신의 신체가 벽돌들이 집보다 먼저 존재하듯 당신보다 먼저 존재한다고 보기 어렵습니다. 그리고 동음어성 원리에 따르면 당신 사후에도 생존하지 않습니다. 그럼 인간의 질료는 **우연히 살아있어야 할** (본질적 생성을 기초하기 위해) 동시에 **본질적으로 살아있어야 합니다** (기능적으로 정의되기 때문에). 이건 **평면적 모순**입니다.

**해결책: 질료의 수준들(levels of matter)**

이게 이 절에서 가장 중요한 구조적 아이디어입니다.

질료는 항상 상대적입니다——어떤 것의 질료입니다——그리고 자기 자신도 질료-더하기-형상으로 분해됩니다. 계속 내려가면:

신체 → 살과 뼈 → … → 네 원소

**근접 질료(proximate matter)**(유기체 신체)는 본질적으로 살아있으며 유기체가 존속하는 정확히 그만큼만 존속합니다.

**원격 질료(remote matter)**(궁극적으로 원소)는 살아있을 필요가 없으며 유기체의 죽음을 거쳐 생존할 수 있습니다.

따라서 본질적 생성을 기초하는 기층은 위계의 밑바닥에 있으며, **모순이 해소됩니다.**

Homoiomerous(구조 없는 물질 같은 살)/heteromerous(구조 있는 기관 같은 눈) 구분과 원자론 부정(질료는 무한히 가분적)은 여기에 따라붙지만, 하중을 지탱하는 이동은 위계 자체입니다.

---

## 2절. 소질료(Prime Matter)

이 절은 "질료의 수준" 질문을 그 한계까지 밀어붙입니다: 기층이 얼마나 아래로 내려가는가?

**압력점은 원소적 변화입니다.** 네 원소는 대립쌍으로 정의되고(뜨거움/차가움, 습함/건조함), 서로 변환됩니다. 아리스토텔레스 자신의 분석에 따르면, 물→공기 변화는 남는 무언가가 필요한데——그것이 순차적으로 각 원소의 속성을 취할 수 있어야 하므로 어떤 원소일 수도 없습니다.

이게 **밑바닥 한계**를 요구하는 것처럼 보입니다: **소질료**, 어떤 본질적 속성도 갖지 않는 순수 잠재성. 부동의 동자들이 순수 현실성으로서 완전히 대칭입니다.

전통 독법(어거스틴, 심플리키우스, 토마스)은 정확히 이걸 그에게 귀속시킵니다. Ainsworth는 플라톤 계보를 표시합니다——*Timaeus*의 receptacle, 정확히 같은 원소 변환 현상으로 동기지어집니다.

**재검토주의 케이스**는 두 갈래입니다:

**텍스트 갈래:** 아리스토텔레스는 "소질료(prôtê hulê)"를 쓰긴 하지만, 그 자신이 이 표현이 근접 질료와 궁극 질료 사이에서 애매함을 말하므로 어휘만으로는 아무것도 결정되지 않습니다. 여러 곳에서 그는 신중하게 중립적입니다——*Metaphysics* ix 7의 조건문("*만약* 어떤 주요한 것이 있다면...")과 그가 만든 형용사 "that-en"은 소질료를 **가능성으로서** 생각하되 그것을 승인하지 않습니다.

vii 3의 "내가 질료라 하는 것은 자체로는 실체도 양도 ... 아닌 그것"이라는 구절이 가장 강한 소질료 우호 텍스트인데, 반대파는 이를 **귀류법**으로 다시 읽을 수 있습니다: 질료를 실체로 간주하면 완전히 결정되지 않은 기층의 존재에 (황당하게) 헌신하게 된다는 뜻입니다.

**철학적 갈래**가 더 흥미롭습니다. Charlton의 동작은 변화가 **항상** 남는 것을 필요로 한다는 걸 부정하는 것입니다. 원소적 변화에는 기초하는 것이 있지만——초기 원소——그것이 남지 않습니다. 여기서 취약성이 즉시 드러납니다. Ainsworth가 누르는 지점: 물→공기를 거쳐 아무것도 남지 않으면, 이를 "물이 무로 사라지고 공기가 무에서 현현한다"는 바로 그 불가능한 상황과 어떻게 구분합니까?

그 다음 소질료에 대한 두 가지 반대——조금 다른 종류입니다.

**인식론적 반대**(그것은 알 수 없습니다. 우리는 오직 그것이 기초하는 것만 지각합니다): 더 약한 것입니다——Ainsworth가 쿼크 비유로 무력화합니다. 관찰 불가능한 것들은 이론적 작업으로 그들의 봉급(salary)을 버니다.

**논리적 반대**가 진짜 위협입니다: 소질료는 어떤 형상이든 취할 수 있어야 하므로(모든 본질적 속성을 갖지 않기 위해) 본질적 속성을 갖지 않는다고 되어있습니다. 그런데 우리는 그것을 영원하다, 보이지 않는다, 궁극의 기층이라고 부르고 싶습니다——그리고 더 악화되어, 소크라테스가 파란색으로 변할 때, 그를 기초하는 소질료도 "파란색으로" 변하므로, 그것은 동시에 보이지 않으면서도 파란색이어야 합니다.

제안된 수정——소질료의 본질적과 우발적 속성을 구분——무한 회귀를 위협합니다(어떤 것이 *그* 본질적 속성들을 기초합니까?). 소질료가 자신의 본질적 속성을 자신을 기초로 하지 않은 채 기초한다고 명시함으로써만 피해집니다. 그 명시가 원칙적인지 임시변통인지가 현재 논쟁이 앉는 곳입니다(Oderberg와 Brower가 일관성을 옹호; Koslicki가 저항).

---

## 3절. 개별화 원리(The Principle of Individuation)

**이 항목에서 가장 명확화하는 동작**은 섹션 맨 위의 **Popper의 해체**입니다. 이건 "학자들이 불일치한다" 상황을 어떻게 다루는지의 모델입니다.

Anscombe과 Lukasiewicz가 대립하는 것처럼 보입니다——질료 대 형상이 개별화 원리입니다——**그런데 그들은 다른 질문들에 대답하고 있습니다.**

**Lukasiewicz**: 많은 부분을 가진 것이 무엇이 사람(heap) 아닌 **하나의 개별 개체**가 되게 하는가? 이건 **통일성(unity)** 질문이고, **형상**이 대답합니다.

**Anscombe**: 이 개별자가 같은 종의 **다른 개별자와 수적으로 다른** 것이 무엇인가? 이건 **구별성(distinctness)** 질문이고, **질료**가 대답합니다.

둘 다 참일 수 있습니다. Ainsworth가 용어를 고정합니다: 통일성 답을 **통일의 원리**라 부르고, 구별성 답에만 **개별화 원리**를 예약합니다.

아래 깔려있는 두 번째 구도 질문: 개별화는 **형이상학적** 이슈입니까(소크라테스가 칼리아스와 다른 것은 무엇입니까?) 아니면 **인식론적**입니까(우리가 어떻게 둘을 **구분하는가**?)——Charlton이 후자를 누릅니다.

그리고 가치 있는 회의적 도전이 있습니다. 아마 수적 구별성은 그냥 **자명한(brute)** 것입니다——아무것도 소크라테스를 칼리아스와 다르게 만들지 않습니다. 그들은 단순히 그럴 뿐입니다.

질료주의자의 자연스러운 답변("질료가 자신의 구별성을 설명합니다——그냥 *이* 질료입니다")은 역효과를 냅니다. "이 질료는 이 질료이기 때문에 구별된다"는 정확히 "소크라테스는 소크라테스이기 때문에 구별된다"와 같은 형태입니다——둘 다 x가 자신의 구별성을 설명합니다.

그런데 질료주의자는 정확히 **그 종류의 자기-설명이 불만족스럽다고 생각해서** 자신의 입장을 채택했습니다. 그래서 자신을 거기에 도움을 청할 수 없습니다.

**결과**: 양쪽 다 인정하는 것——설명은 어딘가에서 멈춘다. 그들은 오직 **어디서** 자명한 사실이 있을지 놓고만 불일치합니다.

가운데피스는 **Fine의 퍼즐**(1994)입니다. 이게 가장 명확하게 잡을 가치가 있습니다. 이건 질료-즉-개별화를 이길 수 없는 유효한 논증입니다:

1. 소크라테스와 칼리아스가 수적으로 같은 질료로 이루어질 가능성이 있습니다(다른 시간에).
2. 소크라테스와 칼리아스는 같은 형상을 갖습니다.
3. 각각은 질료와 형상의 화합입니다.
4. 따라서 소크라테스와 칼리아스가 수적으로 같을 가능성이 있습니다——이는 터무니없습니다.

전제 하나가 가야 합니다. 네 가지 탈출로가 현재의 선택지들을 매핑합니다:

**탈로 1 — "질료"에서 동음어성**: 같은 원격 질료(원소), 다른 근접 질료(신체).

깔끔해 보이지만 Ainsworth가 보입니다 중립화할 수 있습니다: "같은 형상" 요구를 질료의 모든 수준으로 밀어 내려가면, 동음어성이 닫혀 논증이 유효하게 남습니다.

**탈로 2 — P1 거부**(질료는 사람에게 본질적): 근접 질료에는 그럴듯합니다(동음어성 원리 다시——당신의 죽은 신체는 정말로 당신의 신체가 아님). 하지만 원격 질료에는 아닙니다: 원소들은 죽은 그루터기에 남아있고 새 나무로 이동할 수 있는데, 그것이 퍼즐이 필요로 하는 전부입니다. 소질료도 여기 당신을 구조하지 않습니다——그것이 무엇이든 기초할 수 있다면, 한 종류의 것에 국한될 수 없습니다.

**탈로 3 — P2 거부**(같은 종의 것들이 형상을 공유): 이건 **특수 형상(particular forms)**을 필요로 하고, 그것이 Ainsworth가 궁극적으로 선호하는 경로입니다.

걸리는 점은 순환성 덫입니다: 특수 형상이 그냥 인덱싱된 보편(보편과 그 담지자를 쌍으로)이면, 형상이 자신의 담지 실체에 정체성을 의존하고, 형상은 자신이 의존하는 정확히 그 실체를 개별화할 수 없습니다.

특수 형상들은 그들의 담지자와 **독립적으로** 정의되어야 일을 합니다(Koslicki의 신아리스토텔레스주의가 이 탄환을 깨물음).

**탈로 4 — P3 거부**(복합물은 질료-더하기-형상 *한 시점에서*) — 복합물을 시간(그리고 세계)에 상대화.

퍼즐을 직접 다룹니다만 아리스토텔레스가 포기하지 않을 헌신과 충돌합니다: 형상이 복합물을 **통일한다**는 것(*Metaphysics* viii 6, vii 17). 시간이 통일할 하나의 성분 더가 될 수 없고, 형상이 같은 질료를 다른 시점의 다른 대상들로 통일하도록 놓으면 "통일"이라는 이름 받을 자격을 잃습니다. 그래서 이 경로는 해석론적으로 죽었습니다.

**Ainsworth의 착지:** 한 번 더 두 질문을 분리합니다——**이** 기린을 시간에 걸쳐 **같은** 기린으로 만드는 것은 무엇입니까(통일성; "기린성 자체"가 충분할 수 있음) 대 **이** 기린을 **그** 기린과 다르게 만드는 것은 무엇입니까(개별화; 공유된 보편도, 잠재적으로 공유된 질료도 이를 할 수 없음).

**특수 형상이 남은 유일한 후보입니다.**

---

## 4절. 질료-포함적 형상들(Matter-involving Forms)

최종 대비의 긴장입니다.

동기는 반플라톤적입니다: 아리스토텔레스는 자신의 형상을 **질료에 얽혀있기**를 원합니다——플라톤의 분리된 Forms와 달리——그의 배너 사례는 **snub(들린 코)**입니다——오목함-코에-실현됨, 형상을 명시하려면 질료를 언급하지 않을 수 없습니다.

질문은 이를 얼마나 문자적으로 취할지입니다. 자연 형상 자체가 그것의 질료를 명시하는 것을 **포함하는가**(Balme, Charles, Peramatzis), 아니면 그건 형상과 질료가 도입된 매우 역할들을 분리하기 위한 혼동인가(Frede, Corkum, Meister)?

*Metaphysics* vii 11의 텍스트 상황은 정말로 결정 불가능합니다. Ainsworth가 왜인지 정직합니다.

살과 뼈에 관한 중심 문장은 **진술문**으로 인쇄할 수 있습니다("정말로 아니, 그들은 질료입니다……"——그래서 살과 뼈는 형상의 **부분이 아닙니다**) 또는 **질문문**으로("아니면 오히려 질료인가……?"——그들이 **부분인지** 열어 놓음).

문장 기호는 나중의 편집 추가이므로, 그리스어 자체는 그것을 결정하지 않습니다. 주변 구절들(원과 삼각형에 대한 의심, "모든 것을 질료로 축약하는 것은 무익함/소크라테스 젊은이" 언급)은 양쪽 자르를 받습니다.

**전체 텍스트 전장이, Ainsworth 평가로, 비김입니다.**

그래서 무게가 **철학적 동기**로 옮겨집니다: 오직 물질 있는 것만이 변하고, 만약 형상이 어떤 것의 특징적 변화를 설명하려면, 그들은 질료-포함적이어야 합니다.

예: 지탱되지 않을 때의 하강——무거운 원소들의 구성으로 설명됨.

그리고 여기가 **당신 자신의 지형과의 가장 깔끔한 연결**입니다——축소주의적 답변이 **가설적 필연성(hypothetical necessity)**과 ***idia***를 거칩니다.

"모든 인간만이 웃을 수 있다"처럼 종에 필연적으로 붙는 속성들은 그것의 본질의 부분이 아닙니다. 웃음은 합리성**에서 따르오는데**, 더하기 세계가 어떻게 되어있는지.

마찬가지로 "모든 오리는 뒷걸음질한다"이지만, 뒷걸음질하기는 오리의 기능에 있지 않습니다——기능적 명시를 만족하는 무엇이든, 우리 같은 세계에서, 어색하게 걸어야 합니다.

그 "S들이 F이다/다" 형식이 정확히 **자연-역사적 판단**이고, Thompson이 *Life and Action* 전체를 지으며, Foot의 아리스토텔레스적 범주문장입니다.

Ainsworth가 *idia*로 만드는 요점은 Thompson이 활용하는 같은 요점입니다: **특징적 생(generic)이 필연적일 수 있고 생명형식-상대적일 수 있으면서도 본질에 쓰여지지 않는다**——그리고 정확히 그 이유로 형상이 자신의 변화를 설명하려고 질료를 섭취할 필요가 없습니다.

(만약 당신이 원하면, 이게 당신의 관계적/목적론적-생-중심적 욕망 계정에 어떻게 베어는지 끌어낼 수 있습니다. 논리적 형태가 정확히 동일하기 때문입니다.)

섹션은 **분류법**으로 끝나는데, 당신은 이걸 정말로 유용하게 찾을 겁니다——질료-포함의 정도 상승 순서의 네 위치:

1. **순수 형상(Pure forms)**: 복합물의 형상/본질이 질료-포함적이 아닙니다.

2. 복합물의 형상이 질료를 **포함하지만**, 그 형상 자체가 **또 다른** 본질을 갖고 그건 순수입니다.

3. (2)처럼, 복합물의 형상이 질료를 포함하지만, 형상들은 단순히 **어떤** 추가 본질도 갖지 않습니다.

4. (2)/(3)처럼, 그리고 형상들은 **자신들도** 질료-형상 복합물이고 추가 질료-포함적 본질을 가집니다, 계속 내려.

이들 간 변증법은 깔끔합니다. 

위치 **(4)는 악순환 무한 회귀를 생성합니다**——모든 복합물 뒤의 형상들의 끝없는 계열인데, 유한한 아는 자들이 절대 완성할 수 없습니다. 결정적으로, **(2)는 탈출합니다** 왜냐하면 그것의 이차 형상이 순수이기 때문입니다.

(4)를 피하는 자연스러운 방식은 질료-포함적인 것이 hylomorphic 복합물일 필요가 있다는 것을 부정하는 것인데, 그럼 **(3)으로 무너집니다.**

그런데 **(3)은 불안정합니다**: 형상은 **정의**이고, 정의는 언어적-유사 구조를 가지며 분리 가능한 부분들로 나뉩니다. 당신은 항상 그 부분들에 대해 묻을 수 있습니다 그들이 질료-포함적인지.

만약 일부라면, (4) 회귀로 다시 미끄러집니다. 아무도 아니라면, 당신은 "(2)에 견디기 힘들게 유사해집니다."

그래서 (3)은 자신의 입장을 지킬 수 없습니다.

**남는 것은 seemingly 단순 언어적인 (1)-대-대-(2) 질문인데, Ainsworth가 논증하기로는 단순 언어적이 아닙니다.**

(2)는 실체당 **두 개**의 본질/형상을 가정하고, 본질이 세계의 **사물**(인간 본질은 영혼) 지 그냥 언어적 정의가 아니므로, 그건 진정한 추가 존재론적 헌신입니다.

(1)은 질료를 언급하는 더 넓은 **정의**만 인정하면 되고, 이건 추가 비용이 없습니다.

그래서 **질료-포함적 형상이 진짜 이론적 일을 하지 않는 한**, 인절주의는 순수 형상을 선호합니다——물론 Ainsworth는 평결을 조건부로 둡니다.

---

## 결론 — 당신을 위한 두 가지 포인트

당신이 가장 잡을 가치가 있는 것은 **세 가지 논쟁지점을 가로지르는 구조적 운율**입니다:

- **전통** 독법은 아리스토텔레스가 강건한 형이상학적 헌신을 만든다고 봅니다(소질료; 질료-즉-개별화자; 질료-포함적 형상).

- **재검토** 독법은 헌신을 축소하거나 재배치합니다(Charlton의 비-남는 기층; 특수 형상; 순수-형상-더하기-넓은-정의).

각각에서 결정 요인은 **텍스트 결정-불가능 + 자비나 절약성의 주장**의 결합입니다.

그건 놀랍도록 일관된 변증법 엔진입니다.

당신이 가져가고 싶은 것:

**Fine 퍼즐** (**당신의 출제 일에 가장 직접 적용**)——이건 명제적-논리적 재건, 반례적 사고, 그리고 각 탈출로의 비용-편익이 깔끔하게 매핑됩니다.

**네 위치의 분류법** ——이건 재귀 구조와 존재론적 헌신 수준을 생각할 깔끔한 툴입니다.

***idia* 스레드와 자연-역사적 판단** ——이게 당신의 욕망 계정과 가장 직접적으로 연결됩니다. 당신이 Thompson의 목적론적 제네릭과 당신의 relational/non-representationalist 욕망 틀을 꿰맬 때, 이게 정확히 Ainsworth가 "형상이 변화를 설명할 필요는 질료를 포함할 필요를 창출하지 않는다"는 걸 보이는 동작입니다.

뭔가 깊이 파고 싶으신 섹션 있으시면 말씀해주세요. **Fine 퍼즐과 네 위치 분류**가 가장 풍부합니다.

## 영진 · 2026-06-10T04:45

Save english walk through in notion

## Claude · 2026-06-10T04:46

[tool_use: tool_search]

[tool_use: Notion:notion-create-pages]

완료했습니다! 영문 walk-through가 Notion에 저장되었습니다.

**📖 페이지 링크**: [Form vs. Matter (SEP) — Walk-Through](https://app.notion.com/p/37b97cdd867e816faa00f363203351a5)

저장된 내용:
- **전체 구조 아크** (4개 주요 섹션)
- **Section 1**: Matter and Form Introduced (레벨 위계, 동음어성 원리)
- **Section 2**: Prime Matter (소질료 논쟁, 두 가지 재검토 도전)
- **Section 3**: Principle of Individuation (Popper 해체, Fine의 퍼즐, 4가지 탈출로)
- **Section 4**: Matter-Involving Forms (4 위치 분류법, 철학적 동기)
- **결론**: 변증법적 엔진, 세 논쟁지점의 구조적 운율

책갈피 아이콘으로 표시했으니 Notion sidebar에서 쉽게 찾을 수 있습니다.

앞으로 이 텍스트를 Parfit 분석 보고서, 비평 작업, 또는 출제 자료로 참고할 때 Notion 링크로 빠르게 돌아올 수 있습니다.

## 영진 · 2026-06-10T05:52
> 파일: practical-reason-action_a4.pdf

WIll you be kind again and walk me through this Entry?

## Claude · 2026-06-10T05:59

Happy to — and this one sits right on top of your own terrain, since Vogler, Thompson, and Anscombe are doing the load-bearing work in Section 1, and Brewer in Section 5 is close to your desire project. Let me give the map first, because the entry's coherence (or rather, its deliberate lack of it) is the thing to grasp before the parts.

## The shared argument, and what to track

Every program in this entry is organized by one implicit syllogism: *practical reasoning is figuring out what to do; to do is to act; so the forms of practical inference can be read off the structure or features of action.* This is the "action-first" turn. Earlier analytic work registered the action–rationality link but then bolted toward the *mind* — the interplay of beliefs and desires (instrumentalism: Humean, Davidsonian, Williamsian), or procedures for checking that a plan is supported by sufficient consistent reasons (Kantian), or the trained sensibilities of the practically intelligent reasoner (Aristotelian). The new family's hallmark is, first, sustained attention to *"What does it take to be an action at all?"*, and second, a distinction between full-fledged action and a lesser relative ("mere activity," "mere behavior"). The schematic shape of every argument: reasons brought to bear on choice must have *some particular logical form*, on pain of the doing lapsing into something less than action.

Three things are worth tracking throughout, because they're what the walkthrough turns on.

First, **the hinge is what-an-action-is.** Millgram says explicitly in Section 6 that the *primary source* of every downstream disagreement — about the correct patterns of inference, about bindingness, about the moral upshot — is a prior disagreement about what it takes to count as an action. The five programs are just five answers to that one question.

Second, **this is a field of non-communication.** Millgram's framing confession is that the dialectic is "transitional": these theorists mostly don't speak to each other's work, differ in their underlying motivations, and so the considerations lack the mutual organization of a settled problem-space. His job is to *map*, not adjudicate, and he flags that he is deliberately *not* pressing the internal objections — his lovely aside is that if you notice an obvious unaddressed objection, don't assume you're making a mistake, but don't let it sidetrack you. Keep that editorial stance in mind: he's neutral among the theories but pointedly *not* neutral about the field's health.

Third, **two cross-cutting patterns recur in every program.** (a) Each posits a *further reason* or *constitutive aim/standard* that silently accompanies all your first-order reasons — for Vogler a calculative reason, for Korsgaard universalizability, for Velleman the desire to make sense of yourself, for Katsafanas the will to power, for Schapiro Intendo's standards, for Buss/Brewer an evaluation. (b) Each faces the same structural vulnerability — *nonoptionality*. A theory only gets the bindingness of its inference-patterns if it can show its favored conception of action is not merely *a* conception but a *mandatory* one. The slacker, walking away from Intendo, "why not just do something less" — these are all the same pressure, and Section 6 makes it the explicit agenda. Watching that pattern recur is the most efficient way to read the entry.

## 1. The Calculative View — Vogler, then Thompson

The core claim: action has a *calculative* (means-end / part-whole) structure, and the logic of practical reason is read off that. The organizing contrast running through this section is **psychologism vs. anti-psychologism** — Millgram's term for the thesis that the right way to do logic and theory of rationality is *first to figure out how the mind works*. Since the early '70s almost all mainstream work has been psychologistic (Smith's Humean theory of motivation, turning on what desires are). Both calculative theorists reject that.

**Vogler** (*Reasonably Vicious*) runs the Fregean anti-psychologistic move into practical philosophy, following Anscombe (following Aquinas). Her diagnosis of instrumentalism is the key: instrumentalism (all reasons are means-end reasons) is the default view and has been refuted many times over — but the refutations, she thinks, only kill the *psychologistic* renditions of it. Strip the psychologism and you recover what instrumentalism was right about. The Fregean analogy: don't look inward to the gears of the mind, look *outward* to the logical relations among abstract objects and read inference off them; the practical analog is to look past beliefs and desires to *actions*, the external products of deploying practical reasons, and read the logic of practical reason off the structure of actions the way truth-functional logic is read off relations among propositions. (This pre-empts the "you can't reconstruct the process from the product" worry — you don't learn how chairs are made by studying chairs — because Vogler denies that rationality questions are questions about the *processes* leading to a decision at all.)

Actions get picked out and segmented by Anscombe's "Why?"-questions ("Why are you chopping the nuts?" "I'm making a salad"), so an action's internal structure is a *series of steps toward a termination point* — a place where the action stops. A step is rational by being a step toward that point, irrational otherwise (you finished the salad but keep obsessively chopping). The **calculative view** proper: whenever (or almost whenever) you have a reason, you have a *calculative reason* — one whose force is "this is a step toward the termination point of my action" — in two flavors, means-end (buy the cress) and part-whole (chopping the nuts). The thesis isn't that there are no other reasons; it's that whenever you have a reason of any other sort, you must *also* have a calculative one.

The load-bearing move is an **asymmetry**: noncalculative considerations organize and modulate actions and therefore *presuppose* calculative structure, but calculative structure presupposes nothing further — you can *just* tie your shoes, and a theory requiring that such acts be informed by a large-scale conception of the good is modeling rationality on a paranoid psychopathology. That asymmetry is, for Vogler, the deep insight under instrumentalism: because any action big enough to care about must be calculatively well-formed to *work*, calculative reasons are *nonoptional* — you can't shrug off criticism of them the way you can shrug off criticism of your pleasures. And the moral payoff is the book's title: if noncalculative reasons are optional, then immorality of even the most extreme kind need not be irrational — one can be *reasonably vicious*. (The "internalist" label puzzle is worth knowing as a footnote: Vogler calls her anti-psychologistic view internalist only because Williams, post-Korsgaard, quietly shifted "internalism" to mean that reasons can differ person to person — no level at which they must be the same — which an anti-psychologist can happily affirm.)

**Thompson** (*Life and Action*, Part II) is equally anti-psychologistic but *reverses the arrow*. Where Vogler reads the logic off the structure of actions, Thompson uses the *other* reading of Frege — what comes first is our grasp of *inference*, and the inferences in the "practical Begriffsschrift" have actions as their subject matter, so it's an account of action read *off* the inference patterns. Same destination, though: the goal is to show calculative practical reasons are *not psychological states* like desires or intentions.

This is the stretch most directly continuous with your own reading, so let me lay out his machinery as Millgram compresses it. The strategy is Sellarsian (cf. Sellars, Brandom, Nagel): identify a core practice — here, reason-giving — that adduces only *actions*, then show what work the apparently-psychological locutions ("because I want to…") do *inside* that practice. The pivot is **grammatical aspect**: action descriptions are perfective ("I made the salad") or progressive ("I'm making the salad"), and the difference is not ornamental — from the perfective it follows that a salad came to exist; from the progressive it doesn't (the phone rang). Thompson marks *naive* rationalizations — those that use the progressive to place one action inside another ("Why are you chopping the nuts?" "I'm making a salad") — off against *sophisticated* ones that seem to name a psychological state ("I want to make a salad"). Then the constructive argument: imagine an "action-theoretic state of nature" with only naive rationalization. Such agents say "I'm B-ing because I'm A-ing" when B is a part of A — but parts come in *sequence*, so an agent can be A-ing yet, at this moment, not B-ing, producing the confusing "I'm B-ing because I'm A-ing, but I'm not B-ing." To defuse the confusion they develop devices that locate an action in its *temporal phase*: "I'm going to B" marks the run-up, "I intend to A" the planning phase, "I want to A" a pre-planning phase. Once you see that placing actions in their temporal sequence is the *function* of these locutions, reading them as names of inner states is a category mistake — and here is the Sellarsian punchline: **desires are a mistake on a par with sense-data.** Just as the sense-datum theorist mistakes a device for *hedging a commitment* ("it appears to be…") for the name of an inner item (an appearance), the belief-desire theorist mistakes a device for *ordering subsidiary actions* ("…because I want to…") for the name of a motivating state (a desire).

That last move is the one I'd flag hardest for your project. Millgram's Thompson is doing to "I want to…" exactly what your Travis/Austin program does to perceptual and desire talk: refusing to read an inner *representational* relatum off a piece of language whose real job is something else — in Thompson's case, situating an action within its aspectual and temporal structure. It's a gap-refusal of precisely your shape: no inner intermediary posited behind the surface, because the surface locution is already fully accounted for by its place in the practice. If your relational, non-representationalist account of wanting wants a fellow-traveler in the calculative-action literature, this is it, and the aspectual apparatus (perfective/progressive, the teleological generic) is the same machinery your five-conjunct account leans on. Two divergences from Vogler to keep filed: Thompson does *not* restrict mandatory practical rationality to calculative reasons (other parts of *Life and Action* treat further nonoptional forms), and where Vogler was concessive about atomic actions, Thompson argues *all* actions have further actions as proper parts.

## 2. The Authorship View — Korsgaard, then Velleman

Here the essential feature is not stepwise structure but that action is *authored*: no action without an owner, as there's no belief without an owner. The two developed versions diverge sharply, and the divergence is instructive.

**Korsgaard** (*Self-Constitution*) locates ownership in attribution to *the person as a whole* rather than a subpersonal part (a drive, a strong desire). Whole-person attribution requires a *constitution* — psychic organization and regulation, the small-scale analog of a state's political constitution — and an action is owned (hence full-fledged) only when produced through that constitution's procedures. The principles of practical rationality just *are* those procedures at a suitably abstract level. Note that, against Vogler, this makes Korsgaard's theory *psychologistic*: actions have explanatory priority, but they're the starting point of an argument that determines what psychology an agent must have to author actions, which in turn fixes the correct forms of inference. The motivations are partly forensic (responsibility) but mainly about *bindingness* — explaining the normative force of reasons.

The engine is the **constitutive-standard / artifact analogy**: a chair you can't sit on is defective because being sit-on-able is constitutive of being a chair; likewise there are constitutive standards for action, and the question why a thing should meet the constitutive standards for its type "answers itself." So if Korsgaard can show that deploying reasons of a certain form is *constitutive* of action, and that the form is Kantian, she's shown why you must act on Kantian reasons. The bridge to Kant runs through the acts/actions distinction: setting the table is an *act*; setting the table to be ready before the guests arrive is an *action* — acts plus their ends, bound by a *formally universal* principle. For attribution to be contentful there must be a real line between your actions and mere events produced by your psychic parts, and we can draw it only if you identify with a principle of choice that's universal in form. Hence reasons must be universal in form, which (she argues) yields the universalizability requirement of Kantian morality.

The famous pressure is the **slacker objection** (Enoch's "schmagency," Ferrero, Tubert, Katsafanas): why must we produce *actions* at all? Why not drift aimlessly like the characters in Linklater's *Slacker*? If the penalty is being a *defective agent*, the slacker shrugs: agents come with one set of constitutive standards, slackers with another — why hold me to the standards for agency? The objection charges a sleight of hand: an ambitious, optional notion of action smuggled in for a minimal, plausibly-nonoptional one. Korsgaard's reply comes in **three laps**, and they're worth separating because only the second does the real work. Lap one borrows from Wittgenstein the thought that normativity requires the possibility of *correction*: you count as violating a standard only if you can't simply shrug the correction off, so if you could switch kinds at will ("I've decided I'm not an agent but a slacker") you could shrug off anything — hence there must be kinds you *can't* shrug. This is an existence proof and a softening-up; it doesn't yet show that "agent" and "action" are among the unshruggable kinds. Lap two is the pod-creature thought experiment, and it's the heart of it: people, unlike chairs, *dissolve* — an agent constitutes itself by acting or ceases to be an agent. Picture *Invasion of the Body Snatchers* with peapod-sized pods, so that many pod-creatures must coordinate to impersonate one Earthling; to fool Aunt Millie they must behave as a single person, and in coordinating closely they *make themselves into a collective agent* (the tell is the first-person plural — "we're going to go off to the left" — a point of view that is none of theirs individually). That's why action must be generated by you-as-a-whole. And it dissolves the slacker objection by relocating the necessity: there are things we *have* to get done the way the pods *have* to fool Aunt Millie; acting is our "plight," and the necessity of agency is therefore *practical, not metaphysical* — the objection misread it as definitional. Lap three is an argument that you can't choose a character with "fault lines," whose unity is "contingent and unstable"; Millgram calls it too opaque to reconstruct uncontroversially, and instead states the challenge it answers — that the moment-to-moment reconstituting of agency must be a *formal* feature of any personality, replacing the *substantive, contingent* pressures (wartime on a state) with a standing commitment to sustain one's agency "come what may." (The political analogy is the worth-keeping flourish: a state that makes all activity its own action is totalitarian; liberal orders leave most activity *un*attributable, coordinating via markets and regulatory frameworks rather than by forestalling all competition — so full attributability of action is mandatory only if the practical pressures genuinely require the totalitarian rather than the market style of organization, which is exactly what's not yet shown.)

**Velleman** (*The Possibility of Practical Reason*, *How We Get Along*) shares the authorship frame — action "par excellence" is owned, ownership requires definite structure — but disagrees about the structure and, pointedly, about whether being authored by the whole means *not* being authored by a part. His route in is the freedom-of-the-will **regress**: can you honestly dissociate from your action ("it wasn't me, it was the alcohol")? Endorsement ("it really *was* me") just regenerates the problem, since you can dissociate from the endorsement too — the Frankfurt (second-order desire) → Watson (fit with your values) → Benson (what makes the values yours) regress that won't halt. Velleman halts it by finding a psychological element you *can't* disown without ceasing to be an agent: since to act is to act for reasons, you can't dissociate from *the desire to act for reasons*. When such a desire contributes in the canonical way (weighing in for the desires it endorses, tipping the decision), *you* produce the action — as "your intestines digest the food" becomes "you digest the food." So: an action is what's owned; owned means un-disownable; the only un-disownable anchor is the desire to act for reasons.

That desire is then the **constitutive aim of action** (as truth is the constitutive aim of belief), and so it fixes which putative reasons are *good* practical reasons (as truth fixes good reasons for belief). But its content can't literally be "to act for reasons" — viciously circular — so Velleman reads it as the desire to *know what one is doing* / *make sense to oneself*. A good practical reason is then whatever makes your action *intelligible to you* as you perform it. The view evolves: from a default schema (act on a desire → the action makes sense → instrumentalist authorship view), to *narrative* reasons (emotion cascades — denial, anger, bargaining, acceptance — are the spines of narratives; an action is intelligible as the next step of such a cascade), to *character* (stay in character and what you do makes sense). Two deeper motivations sit underneath. One is a **reduction of practical to theoretical reason**: reasons for action are picked out as what would *explain* the action, and on pain of circularity we must borrow an independent notion of explanation — which has to be *theoretical*, the same kind that explains any fact (desires are reasons because they *causally* explain action). Decisions become *self-fulfilling predictions of one's own actions* (with Anscombe's caveat that "I'm going to be sick" is a prediction, not an intention, even if self-fulfilling), and an action is just such a prediction fulfilling itself. The other is the **self-knowledge thesis** — that when you act you know what you're doing — which Velleman treats as both constitutive and empirically present, and which his readers resist (the apathetic students, the people who visibly *prefer* not to understand what they're doing even as they do it; and the cognitive-dissonance evidence cuts the wrong way, since its hallmark is that subjects are *unaware* of it). Millgram's diagnosis is that the self-knowledge thesis is best read not as a free-standing datum but as a *cognitive requirement* falling out of the other two pressures: anchoring attribution and reducing practical to theoretical reason. He then walks three difficulties — the deferral of "what is a practical reason?" to the philosophy of explanation (not every prediction yields a reason; predicting your own *mistakes* and treating them as reasons is next door to Moore's paradox, so the scope of admissible explanations must be restricted, and that's left open); the implausibility/unattractiveness of an agent forever asking "what would someone like me do?" (answered by making practical reasoning *sporadic* — rationality "in the passenger seat," mostly on autopilot, at the cost of loosening the action–motivation tie); and a pair of circularities (that desires *explain* action is a legacy of treating them as *reasons*; that one emotion *naturally* succeeds another presupposes culturally available narrative training — so the rationality-theories would come *first* and the account would be viciously circular). Velleman's escape, which Millgram reconstructs by connecting dots, is his "kinda Kantian" finish line: because we are pervaded by the drive to understand ourselves, over time we *simplify* ourselves — flattening our typology of persons, removing asymmetries in social roles — and gradually *become* agents of whom belief-desire psychology and the emotion-cascades are simply *true*; once that's happened, the explanations are straightforwardly causal and it no longer matters how they got that way.

A **bridge to the next view**: Katsafanas (the entry's one genuine inter-theoretic disputant) argues that neither Velleman nor Korsgaard can show that having *more* self-knowledge, or *more* unity, is a *constitutive end* of action — so neither can build the comparative notion we actually need, "having *more* reason to do this than that." That gap motivates his own positive view.

## 3. The Challenge-Seeking View — Katsafanas

Actions, on this view (Katsafanas, *Agency and the Foundations of Ethics*, crediting Nietzsche), are generated by *drives*, so whatever is characteristic of drive-generated activity is characteristic of all action. Drives have *aims* (the shopping drive aims at having lots of stuff) and they *generate objects* — when an object is attained the desire for it evaporates and the drive throws up a new one (the gewgaw, then the garment at 30% off). A drive working like that is, more deeply, directed at *encountering and overcoming resistance*. Now layer in agency: deliberation's outcome *settles* what you'll do — and note the deliberate contrast with Velleman, since if it didn't settle but merely *predicted*, you'd be relating to your own future action the way you relate to other people's. Choice involves *assessment*, which moves you only if you *approve*, so action aspires to be *active*: you approve of what you do and would *go on* approving if you understood its real motivational inputs (all of them, not just the official ones — the way you claim to weigh a request's pros and cons while actually responding to the requester's looks or class). Being fully active therefore requires approving your drives' role, which requires approving their core feature — the ongoing production of *challenging goals*. Hence the further reason that accompanies all your reasons (the cross-cutting pattern again): an interest in *more rather than less* challenging-but-attainable objectives, which Katsafanas labels *will to power*. That comparative interest is precisely what he says the authorship views couldn't supply. The moral upshot he draws is bracing: since overcoming resistance involves *suffering*, that kind of suffering counts as a good.

## 4. The Practice View — Rawls to Schapiro

The starting point is **Rawls 1955** ("Two Concepts of Rules"): a *practice* generalizes a *game*, and its key feature is that it introduces *statuses* internal to it (in baseball, 'foul', 'strike', 'home run'), and with them both *standards* (a home run must satisfy baseball's rules) and *reasons* internal to the practice — which may be means-end (baseball's object is to win by outscoring) or other kinds (in squash, the opponent's head between racquet and ball is reason to call a 'let', not because it's the best way to win — calculative reasons modulated by gentlemanly ones).

**Schapiro** extends this into a theory of action: 'action' is a status within the *completely generic* practice — the game you're playing whenever you do anything — the way 'move' is a status in chess. Millgram dubs the generic practice **Intendo**; 'agent' is its generic role. Since 'practical reason' is itself a practice-status, Intendo fixes what forms practical reasons can take. And here's the leverage: practical reasons are practical only if they could bear on a decision issuing in action, being an action is a status *within* Intendo, so there are no practical reasons coming *from outside* Intendo (unlike local practices, which must accommodate outside reasons — in chess the object is to win, but I may have personal reasons not to play to win). Therefore, if Intendo imposes any standard on its reasons — say, universalizability — then *all* reasons must meet it. A nice byproduct is Schapiro's answer about the **modality of freedom** (the force of "may/must/should" when the issue is what you have reason to do): it's the modality of the "can" in "*Can* he do that?" said of someone who just ran the bases backwards — freedom of the will ranges over the *allowable moves* of Intendo.

Millgram is careful about where Schapiro *departs* from Rawls — Rawls thought few moral-life actions are practice-defined and worried about the conservatism of treating one's society's practices as the standard of justification; he objected to the "summary" (one-office) conception of rules; and his Wittgensteinian roots would make him skeptical of hunting for *the deepest features common to all practices*, since (Wittgenstein) there's no nontrivial feature common to all games. None of this refutes Schapiro; it's a warning not to assume her generic practice inherits all the structure of the familiar local ones. Her finish line is Kantian: universal laws on the model of practice rules, so that "the law of freedom" is an *indeterminate* practice rule requiring you to make every movement *as if* it were a move in some possible global practice — a paraphrase of the categorical imperative. Her motivations are a *history* (the practice view as the "Hegelian synthesis" of an older *consequence-oriented* conception — actions as ways of producing effects in a given natural world — and an *expressivist* one — actions as evaluative pronouncements, capturing the truth in each) and an *appreciation* of the value of a world textured by practice-statuses. Note that her view is *non-psychologistic without being motivated by anti-psychologism* (assessing a practice's reasons — king in check, so move it — you read the constitutive rules, not anyone's head); this is Millgram's evidence that Kantianism is not *essentially* psychologistic, even though Korsgaard built her Kantianism that way.

Then the nonoptionality problem, in its sharpest form. For the Kantian conclusions to bind, the practice conception must both *entail* them and be shown *nonoptional* — but baseball you can decline, quit, or the rules end for you, so Intendo must be a game you *can't walk away from*. Why can't you stop playing Intendo and produce non-practice-governed activity? One answer is the value of the practice-informed world; another is that you *can't*, where the "can't" carries the modality of freedom (since reasons are practice-statuses, questions of practical reason don't even *arise* for the alternative). The stress test is the **murderer at the door** (Schapiro 2006): Kant forbids lying, the murderer asks where his intended victim is, and the casuistical task is to license lying *consistently with the theory*. Schapiro's solution: moral reasons are statuses in Intendo, so if the murderer *refuses to play the game*, your moves can't be responses to his moves — honesty as a contribution to the "co-legislation game" is simply not an available move, and if proper honesty isn't on the board, other moves may be. The resulting **tension** is exact: you must act from the moral law *because you can't opt out* of Intendo, yet you may lie to the murderer *because he has opted out*. Schapiro splits the difference with a label — the murderer is *betraying* the generic practice without *opting out* of it — but, Millgram notes, the distinction the label marks is so far unexplained, and the view's future will be shaped by accommodating these two pulls.

## 5. Evaluation as Essential to Action — Buss, then Brewer

The thesis here is that *evaluation* is essential to action, or to a privileged kind of it.

**Buss** distinguishes mere "movements of the human body" from full-fledged intentional action by requiring, for the latter, that the agent *endorse* the action as it's initiated — the endorsement amounting to treating the agent's reasons as *sufficient* to go ahead. Anything less is a *spectatorial* stance toward your own conduct: you note some desires, note that an action would satisfy them, but never form the evaluative belief "that's good enough" — so you're just sitting back to watch whether the desires move your body. Her argument against Humeanism is clean and dramatic: Humean moral psychology draws reasons from two exclusive classes, desires and (evaluatively empty) beliefs, so it has *no room for an evaluative belief*; but intentional action *requires* exactly such a belief; therefore Humean moral psychology is incompatible with there being intentional actions at all, and a theory of practical reasoning built on it aims at choosing actions while being incompatible with actions' being chosen — *incoherent*. The slogan version: *if your will is to be free, instrumentalism must be false.* Millgram flags the overlap with Velleman (both pivot on acting for one's sufficient/good-enough reasons — a desire in Velleman, an evaluation in Buss) but the different motive: Velleman is halting a regress in the *structure* of agency, Buss is articulating that action is *active rather than passive*, and beyond rejecting Humeanism she's open-minded about what reasons turn out to be.

**Brewer** (*The Retrieval of Ethics*) brings a shift of key, and this is the second stretch I'd flag hard for you. He *relabels*: where everyone else made "action" the first-class category and "activity" the lesser, Brewer makes *dialectical activity* the privileged kind and *actions* the inferior class. An action is merely structured to produce a "pre-envisioned state of affairs"; a *dialectical* activity is marked by two features — coming to understand better *what the activity is* is itself an essential part of the activity, and arriving at a deeper understanding of the *good* of the activity is too. Friendship is the paradigm: part of what it is to be in a good friendship is developing a deepening sense of what *this* friendship is about, and of friendship as such (the lineage is Aristotle). Because his anchor is *not* "to do is thereby to act," Brewer is a *penumbral* member of the family; his two claims are that mere actions usually won't make sense outside the context of a dialectical activity, and (suggested, not quite argued) that dialectical activities exhaust what is *intrinsically valuable* for human beings.

The reason this matters for your project is concentrated in his **argument against propositional desire**, which is almost a manifesto for a relational, non-representational account. On the views he opposes, actions are motivated by desires understood as *propositional attitudes* — descriptions of future states of affairs you then act to make true. But what *moves* you (as against what *motivates* you) in a dialectical activity *cannot be captured by a proposition*, for two reasons. First, a proposition has *definite, stable* content — it partitions the possible worlds once and for all — whereas the content of what moves you is *deepening and evolving*, with no point at which grasping it is properly over; so no proposition could demarcate what the activity is after. Second, desire-as-standardly-conceived sets a proposition to be made true *in the future*, but the object of dialectical activity *doesn't lie in the future*: living your life is a dialectical activity and you are *already* living; if you're someone's friend you are *already* participating. So dialectical activity cannot be construed as desire-driven in the standard propositional sense — even though the simpler subsidiary actions it spins off can be. That is a relational, anti-propositionalist, present-tensed account of what moves us, and Brewer (the entry notes) even tries to *reappropriate the concept of desire* for it — which is your move, from a neighboring direction. If you want an ally in the action-theory literature for the non-representationalist desire account you're building out of Travis, Austin, Anscombe, and Thompson, Brewer is a more explicit one than almost anyone else here, and his "what moves you is evolving and doesn't lie in the future" is the kind of formulation worth setting beside your own.

The rest of Brewer's view follows from this. The Vegas/Home Depot illustration — two friends biking to Vegas, then years later in the gardening aisle, then something else again — shows activity and action as *interdependent*: the friendship continuously *emits* end-directed actions, but because the participants' conception of it keeps shifting, those actions can't be specified up front; and conversely the deepening grasp depends on the *friction* the end-directed actions generate (it was the Vegas trip going wrong, and the quarrel, that made them rethink and start gardening). The stakes: on rationalization-by-desires the segments of a life get unified into a trajectory only *retrospectively*, and the inability to grasp the activity as unified *while it's in progress* actually *undercuts* its unity (Augustine not understanding his life as a search for God until late, though that's what it had been all along) — so operating only on desire-rationalization risks a life "empty of the goods that really matter." And the upshots for rationality are squarely your kind of thesis: since the evolving conception is *deliberative rather than arational*, there must be reasoning that modifies not just *how* to get what you already want but *your view of what you're after* — i.e., **deliberation of ends**, over and above instrumental rationality. From that, three further consequences: the primary object of practical attention is *the action already in progress* (the model is an author rereading his half-finished paper, completing a train of thought he's in the middle of rather than about to start), so the survey-assess-then-initiate picture has the phenomenology backwards; the operative question becomes "*What have I been doing?*", answered largely in *thick ethical concepts* — descriptions whose application requires mobilizing your evaluative capacities (Williams's "obscene," opaque to the Martian exobiologist) — which Brewer takes to undercut the very theoretical/practical-reason distinction the entry used to frame itself; and our resistance to *outsourcing* deliberation to experts is vindicated, because if practical thought is "a seamless part of" friendship or philosophy or living, then contracting it out is to forgo the valuable activity itself. The neat closing contrast: for Buss the evaluation that matters is the *settled output* of evaluating; for Brewer it's the *evaluating* — the ongoing activity.

## 6. Prospects — the real agenda

Millgram closes by naming the field's pathology and its task. The shared methodology notwithstanding, these theorists disagree on nearly everything — their reasons for the approach, the correct theory, the source of bindingness, the moral upshot — and the *root* of all of it is the prior disagreement about **what it takes to count as an action**: stepwise/nested structure, authorship, location in a practice, or entailing an evaluation (with Brewer's dialectical-activity variant). Some of these now come with *supporting arguments*, which is a real advance on twenty years ago — but the norm is still to *omit any account of why the competing conceptions are wrong*. His diagnostic citation is **Nozick** on Newcomb's Problem: advocates of each side were ready to say why their own view was right but not what was *wrong* with the other's argument, and that posture is unacceptable — "it will not do to rest content with one's belief … nor will it do to just repeat one of the arguments, loudly and slowly." So the agenda is inter-theoretic: produce arguments that *decide between* conceptions of action, because you can't hang a whole theory of practical reason and morality on an account of action that your colleagues treat as obviously false while having no story about why yours is right and theirs isn't.

And he frames the strategic fork cleanly, which is the single most useful takeaway for thinking about *any* of these programs. Because every view derives the bindingness of its inference-patterns from the *nonoptionality of its conception of action*, every view owes an answer to one question: *given what you mean by "action," why not produce activity of some other kind?* — why not use noncalculative control structures (against Vogler); why not let it "just kind of happen" rather than *author* it (against Korsgaard/Velleman); why not behave like a market on the inside, or decline to play Intendo the way you'd decline a round of pinochle (against Schapiro); why bother *evaluating* my reasons rather than just being responsive to them (against Buss); why not skip friendship and philosophy and just harvest a stream of sensual pleasures (against Brewer). There are exactly two shapes an answer can take, and they determine the *kind* of bindingness the theory inherits: a **theoretical** answer shows there is nothing else you *can* — metaphysically — do, because whatever you do in the thinnest sense *is* action in the theory's thick sense; a **practical** answer shows that, given the alternatives, producing actions in the thick sense is, as Millgram puts it, *an offer you can't refuse*. And his honest closing caveat is that we shouldn't *assume* any mode of action is nonoptional: if the pressures fall short of genuine practical necessity, the right conclusion might be *pluralism about action* — no single privileged thing that all doing must be.

## The structural rhyme, and what's most useful for you

Set against the Form-vs-Matter entry, the recurring engine here is different in kind. That entry's drama was a *traditional* metaphysical reading repeatedly deflated by a *revisionist* one. This entry's drama is that *five programs agree on a method and a slogan* — derive practical inference from the structure of action — *and then diverge completely because they smuggle five different answers to "what is an action?" into the same blank*, after which each is left holding the same unpaid bill: showing that its answer is *mandatory* rather than merely *available*. The whole field is, in effect, an argument about which conception of action gets to occupy that one variable, conducted (Millgram's complaint) without the participants actually arguing *against each other*.

For your own work I'd single out three things. The Thompson material in Section 1 is the most direct ally for your non-representationalist desire account — the "desire-locutions don't name an inner state, they place an action in its aspectual/temporal structure" argument is a gap-refusal of exactly your shape, and worth reading Millgram's compression of against your own close reading of *Life and Action*. Brewer in Section 5 is the second, and arguably the richer one for the *relational* side of your view: his "what moves you can't be captured by a proposition — it's evolving and it doesn't lie in the future" is a fully developed anti-propositionalist account of desire from a neighboring tradition, complete with an attempt to reappropriate "desire" that parallels yours. And the Section 6 fork — theoretical vs. practical bindingness, with pluralism-about-action as the live third option — is a clean diagnostic grid you could lay over any action-theoretic passage you're building, since it tells you precisely which nonoptionality bill a given view has to pay.

Happy to go deeper on any of these — the Thompson aspect argument and the Brewer anti-propositionalism are the two I'd expect to repay the most for your desire project, and I can pull either one apart against your Travis/Austin framework if that's useful. I can also save this to Notion alongside the Form-vs-Matter walkthrough if you'd like the pair together.

## 영진 · 2026-06-10T06:33

then what kind of bill do I have to pay when I pursue my Travis/Austin Frame work of desire(Action)

## Claude · 2026-06-10T06:38

The short answer is that your framework doesn't *pay* Millgram's bill — it *refuses* it, and the refusal is principled, but refusing converts the debt into a sharper one rather than cancelling it. Let me make that precise, because the conversion is where the real exposure lives.

Millgram's bill is owed by any view that grounds the *bindingness* of practical-inference patterns in the *nonoptionality of a thick conception of action* — "to be an action you must satisfy form F, so reasons must have form F, so F is binding." A Travis/Austin view is built to deny exactly that at the root: occasion-sensitivity just *is* the thesis that there is no occasion-invariant form F that every doing (or every wanting) must satisfy. So your honest first move against Millgram is to say *I don't owe the nonoptionality bill in your currency, because I reject the premise that practical correctness must be grounded in one nonoptional thick form of action.* That's not evasion; it's the same refusal Travis makes against the representationalist who demands fixed satisfaction conditions for perception. But the moment you deny that bindingness flows from a nonoptional form-of-action, you inherit the question that form was supposed to answer: **where does practical correctness come from at all, and what fixes it on the occasion?** Call this the *genuineness-of-occasion-relative-correctness* bill. It is the practical face of the deepest standing objection to Travis on perception — that occasion-relative "correctness" either smuggles back something doing the representation's work, or floats free and stops being correctness. Travis insists occasion-sensitivity is not anything-goes; you have to make that insistence stick for desire, and desire makes it *harder*, because desire has direction of fit and the representationalist's whole account of what individuates a want is its satisfaction condition. Banish the satisfaction condition and you owe a replacement notion of fulfilment and frustration.

That master bill has two horns, and the first is the one peculiar to *your* synthesis, which is why it's the load-bearing one. You draw your gap-refusal from Travis and your normativity from Thompson — but **Travis localizes correctness to the occasion, and Thompson anchors it in the life-form**, and those answer the source-question in opposite directions. Lean Thompsonian and you have a genuine source of normativity (the natural-historical judgment, the Aristotelian categorical "S's do F," grounding defect), and that *is* Millgram's *theoretical* answer relocated from action-as-such to the life-form — "nothing else you can metaphysically be is the doing of a creature of this kind, and what it is to do it well is fixed by the form." But you've then imported a relatively *fixed* form to do the grounding, which is in tension with thoroughgoing occasion-sensitivity: a life-form that fixes correctness across occasions is doing, at the form-level, the work Travis banished at the content-level, and you owe an argument that this isn't a representation wearing Aristotelian clothing. And you inherit Thompson's *own* unpaid bill on top — showing that natural-historical judgment *generates* normativity rather than presupposing it (the standing is/ought worry against Foot–Thompson naturalism). Lean the other way — keep Travisian purity, correctness is occasion-relative — and you keep the gap-refusal clean but you have *not* yet answered the source-question, because the occasion plus "the understanding a reasonable person would have" tells you what's *taken*, not what's *correct*; that reasonable-person standard is itself doing load-bearing work and needs its own scrutiny. So the first bill is: reconcile occasion-relative correctness with a form-anchored source, or pick one horn and pay it. You can't quietly draw normativity from Thompson while drawing anti-fixity from Travis and assume they cohere.

The second horn is *content*: what does the correctness of a want *consist in*, given direction of fit and no satisfaction condition? Your **perfective/progressive** resource (Thompson's aspect) buys you *completion* — the salad got made or it didn't — but completion is not aptness; an action can complete and still be the discharge of a defective or vicious want. And if your **Explanation** conjunct rests correctness on naive rationalization ("I'm B-ing because I'm A-ing"), you land exactly in Vogler's spot: you can certify that a want is well-formed *as a step toward its end* while saying nothing about whether the end is choiceworthy — which is *reasonably vicious*. Thompson escaped that by not restricting practical reason to the calculative, leaning on natural-historical goodness for the rest — but that escape is only available to you if you've already paid the Thompsonian horn of the first bill. So the content horn and the source horn are tied: a Travisian-pure version of your view is at risk of capturing only calculative/aspectual correctness and inheriting Vogler's result, with no room for the *deliberation of ends* that Brewer insists you need.

Now the genuinely useful part, because your two named open fronts turn out to be the two *audit sites* where "is the gap-refusal real or merely verbal?" actually gets adjudicated.

**Hyperintensionality is the acid test, and your Aspect conjunct is the thing on trial.** Wanting to see the morning star without wanting to see the evening star is the kind of substitution failure Frege introduced *sense* to explain. Your bet is that the *aspect* under which something is wanted does that work without *being* a mode of presentation — the aspect is a feature of the form of the wanting, not a sense interposed between agent and object. The bill is exact: if "aspect" is individuated finely enough to block every substitution that sense was posited to block, then by the ordinary abductive standard you have posited something that plays the sense-role, and calling it "aspect" rather than "sense" is a verbal difference unless you can exhibit a *functional* difference — something sense does that aspect doesn't, or conversely. This is precisely the standard charge against Travis on perception (that his occasion-sensitive "understanding" individuates exactly as content would, so the no-content claim is verbal), transposed to desire. Hyperintensionality is where you find out whether your gap-refusal cuts metaphysical ice or only relabels the representation.

**Occasion-*can* scope is the modality bill, and Millgram hands you its sharp form through Schapiro.** There are two "can"s in play. Austin's *can* — ability and opportunity — is what your Capacity conjunct captures. Schapiro's *modality of freedom* is a different modal: the normative "Can he do that?" said of the runner who went round the bases backwards, who *can* in Austin's sense (he had the ability and opportunity) but *can't* in hers (it isn't a legal move). So the question of how far your occasion-*can* reaches is the question of whether your Capacity conjunct covers only ability or also *entitlement*. If only ability, then capacity-to-pursue is not permission-to-pursue, you have a gap, and you need a separate account of the practical *may* — which loops straight back to the source bill. If you want one *can* to discharge both faces, you owe an argument that occasion-sensitive ability-talk *generates* the modality of freedom, and that runs uncomfortably close to deriving the normative from the ability — the wrong direction, given "ought implies can." Whether occasion-*can* purchase extends that far is, in Millgram's terms, exactly the question of whether you need one modal notion or two, and if two, the relation between them is the unpaid item.

So, to name the single bill that sinks the view if it goes unpaid: it is not "explain action" and it is not "show action is mandatory" — Millgram's two — it is **show that occasion-relative practical correctness is genuine correctness and not mere uptake, and do it without letting your aspect (in want) or your reasonable-person standard (in correctness) quietly become the representation you set out to eliminate.** Hyperintensionality and occasion-*can* are simply the two places that bill comes due first. Millgram's own *pluralism about action* escape, incidentally, is congenial to you — occasion-sensitivity is natively pluralist — but it doesn't dissolve this bill; it only changes its shape, because Travis is emphatic that occasion-relativity is not anything-goes, which means a pluralist owes *occasion-relative correctness that is still correctness*, which is the same debt under a different name.

If you want, I can take either audit site and work it out against the actual text — the hyperintensionality one against Travis's LL/LAI machinery from "The Silence of the Senses," since that's where the "does the understanding individuate like content?" question was first sharp for you, or the occasion-*can* one against Austin's "Ifs and Cans" directly.
