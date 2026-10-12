---
title: "Wittgenstein's relationship to Frege's distinction"
uuid: fb7e51cf-979c-46f8-8173-9b6c167828dc
created: 2026-06-18
updated: 2026-06-18
project: ""
url: https://claude.ai/chat/fb7e51cf-979c-46f8-8173-9b6c167828dc
turns: 16
type: 원자료/대화
---

> 요약: **Conversation Overview**  This conversation was a graduate-level philosophy discussion focused on Wittgenstein's *Tractatus Logico-Philosophicus*, conducted in an informal but technically rigorous register. The person demonstrated significant expertise in analytic philosophy, working fluently with Frege's Sinn/Bedeutung distinction, Russell's theory of descriptions, and the landscape of formal semantics. The discussion unfolded as a series of probing questions about early Wittgenstein's relationship to Frege and Russell, with the person actively testing their own understanding and pushing back when Claude's formulations seemed to outrun the argument.  The conversation covered several interconnected topics: whether Tractatus-Wittgenstein accepted Frege's sense/reference distinction or followed Russell, how truth-values are computed from truth-functions in the Tractatus, the claim that a proposition just *is* its truth-conditions, the hyperintensionality problem for attitude contexts (belief, knowledge), Frege's own resources for handling substitution failure in oblique contexts via reference-shift and the Sinn/Bedeutung distinction, and finally whether formal logical systems exist for Fregean sense. Claude worked through these using a layered pedagogical approach: direct answers followed by the structural reasoning behind them, concrete examples (the N-operator, truth-table notation as propositional sign, the color-exclusion problem), and closing questions designed to advance the person's own thinking rather than close off inquiry. The person engaged critically throughout, catching a genuine tension between the "meaning is truth-conditions" claim and the stronger "proposition is exhausted by truth-conditions" claim, and independently identifying that the Tractatus and possible-worlds intensional semantics share the same coarse grain—making their substitution objection hyperintensional from the start. Key philosophical figures and texts discussed included Frege's *Grundlagen* and *Begriffsschrift*, Russell's "On Denoting" and multiple-relation theory of judgment, Church's Logic of Sense and Denotation, Carnap's *Meaning and Necessity*, Montague's intensional logic, Tichý's Transparent Intensional Logic, Moschovakis on sense as algorithm, Berto and Jago on impossible worlds, Fine's truthmaker semantics, and Zalta's object-theoretic framework. The person mentioned working on hyperintensionality and relational desire as open research concerns. The conversation closed with a brief shift to Korean for an unrelated interpersonal question about whether to contact a friend awaiting interview results, which Claude addressed directly with a short practical recommendation.

## 영진 · 2026-06-18T08:22

/learn 

did witt accpet the bedetung/sein distinction of frege? or is he just loyal follower of Russel? I am consdierting the tracta-witt.

## Claude · 2026-06-18T08:25

[tool_use: view]

Short answer: neither, quite. The Tractatus isn't loyally Russellian, and it doesn't take over Frege's distinction *as Frege drew it*. What Wittgenstein does is **redistribute** the two terms — and that redistribution is where the picture theory lives.

(I'm reading your "bedeutung/sein" as Frege's **Sinn/Bedeutung** — sense/reference. Say if you meant something else.)

The cleanest way to see it is to ask, for each thinker: at which level does *Sinn* live, and at which *Bedeutung*?

| | **Name** | **Proposition** |
|---|---|---|
| **Frege** | Sinn (mode of presentation) + Bedeutung (the object) | Sinn (the thought) + Bedeutung (**a truth-value**); sentence = complex name |
| **Russell** (post-1905) | meaning = the bearer, no Sinn | no Sinn; analyzed via propositional functions, not a name |
| **Tractatus** | Bedeutung = the object, **no Sinn** | **Sinn only** (the depicted situation / truth-conditions), **no Bedeutung** |

Read across the rows and the structure jumps out. For Frege, names *and* sentences each carry both sense and reference, and a sentence is a species of name whose reference is the True or the False. The Tractatus refuses exactly that: a proposition has a sense (4.022, the situation it shows) and **no Bedeutung at all** — it is emphatically *not* a name, so not a name of a truth-value.

On *names*, yes, he's with Russell: 3.203, "the name means the object; the object is its meaning." Pure "Fido"-Fido, no sense hovering beside the name. But the move on propositions is an *explicit argument against Frege*, not a Russellian reflex — 4.063 and 4.431 go after Frege's idea that the True and the False are objects sentences denote (if they were, he says, the sense of ~p wouldn't even be fixed). A "loyal follower of Russell" wouldn't need to bother refuting Frege.

And the thing that kills the just-Russell reading outright: the deepest commitment in the book is Fregean — the **context principle**, 3.3, "only the proposition has sense; only in the context of a proposition does a name have meaning." That's *Grundlagen* almost verbatim, and Russell has nothing like it. The bipolarity of the proposition, the function/argument scaffolding, the anti-psychologism — Frege, not Russell. Meanwhile he breaks with *Russell* hard too: 5.5422 against the multiple-relation theory of judgment (a correct theory must make judging a nonsense impossible), and the whole say/show distinction quietly does the job Russell wanted the theory of types to do.

So the honest one-liner: **Russellian about what a name does** (object = meaning), **Fregean about the architecture** (context principle, sense of the proposition, anti-psychologism), **and his own man about the proposition** (it pictures; it isn't a name).

Here's where I'd push you, since you're heading into the text. The fight that actually settles your question is over *how a Tractatus name gets its Bedeutung* — and it turns on holding 3.203 and 3.3 together. Does the object come first, given independently (by acquaintance, say), with the name then pinned to it, so the context principle is just decoration? Or does 3.3 do real work, so that *which* object a name means is settled only through its use in propositions? The first reading makes him basically Russellian about names; the second (Ishiguro, McGuinness) makes him surprisingly Fregean even there.

Which way do you currently read the 3.203 ↔ 3.3 relation — and what do you want it to deliver for the passage you're considering?

## 영진 · 2026-06-18T08:28

wow, then How did the witt calculate the truth value of propostion form its expressions truth functiion?

## Claude · 2026-06-18T08:30

The slightly subversive answer first: in the Tractatus there isn't an extra step where you *calculate* a truth-value on top of the meaning. The truth-conditions **are** the sense (that was the 4.022/4.2 point from before), so once the world fixes the base, the value just falls out. "Calculation" is bookkeeping, not a further semantic act.

Here's the machinery, bottom-up.

The base is the **elementary propositions** — names in immediate concatenation (4.21–4.221). Each is bipolar, T or F, and it gets its value directly from the world: it pictures a state of affairs, and it's true iff that state of affairs obtains. Nothing logical happens at this level. For *n* elementary propositions there are 2ⁿ truth-possibilities (4.27).

Then the load-bearing thesis (5): **every proposition is a truth-function of elementary propositions.** A complex proposition simply *agrees or disagrees* with some selection of those 2ⁿ possibilities, and that pattern of agreement/disagreement is its sense (4.431). This is why Wittgenstein can say the truth-table itself can serve as the propositional sign (4.442) — the column of T's and F's isn't a tool *for* describing the proposition, it *is* the proposition.

So the actual "calculation" of a truth-value is: take the real values of the elementary propositions (which states of affairs obtain), locate that row, read off T or F. No extra facts are consulted, because — this is the *Grundgedanke*, 4.0312 — the logical constants aren't representatives. There's nothing in the world that "∧" or "¬" stands for to be evaluated. The connectives are pure truth-functional structure.

What makes this systematic rather than a pile of ad hoc tables is that the whole space is generated by **one operation**: joint denial, N(ξ̄) = "none of these are true." Everything is a nesting of it:

```
¬p      =  N(p)
p ∨ q   =  N( N(p, q) )
p ∧ q   =  N( N(p), N(q) )
```

That's the content of the general form of the proposition (6), `[p̄, ξ̄, N(ξ̄)]`: start from all elementary propositions, apply N, iterate. The entire propositional space = the truth-functional closure of the elementary base. Generality is folded in the same way — let the bracket range over all values of *fx* and N gives you ¬∃x fx (5.52), with ∀ built from there.

The two degenerate cases tell you where the system's edges are. A **tautology** is the truth-function whose column is all T, a **contradiction** all F — the value no longer depends on the world at all. They're *sinnlos*, they say nothing, but they show the scaffolding, which is exactly why logic consists of tautologies (6.1). "Calculating" a logical truth needs no facts because the column is constant by construction.

Now the place I'd point you, since you're weighing the Tractatus. This entire engine presupposes that elementary propositions are **logically independent** — from one, no other follows (4.211, 5.134); otherwise the 2ⁿ rows aren't all genuinely possible and the truth-functional reading breaks. Then look at 6.3751: "*a* is red all over" and "*a* is blue all over" can't both be true, yet each looks elementary. If they are, their independence fails; if they're not, what hidden structure makes "red" and "blue" exclude each other — and where in the name/object apparatus does that structure live? That single crack is what dragged Wittgenstein back to philosophy in 1929.

So: do you read color-exclusion as a local repair the framework could absorb, or as load-bearing failure that takes the truth-functional picture down with it?

## 영진 · 2026-06-18T08:33

a- then proposition does not denote 'true' 'false' -> proposition is a truth-table. right
?

## Claude · 2026-06-18T08:34

The first half is exactly right, no qualification — no *Bedeutung*, so it names no truth-value.

The arrow is the only thing to tighten. The two halves aren't premise and conclusion; they're one fact stated first negatively, then positively. Negatively: it doesn't name the True or the False. Positively: a proposition is nothing over and above its truth-conditions — and 4.442 is blunt that the truth-table can serve as the propositional sign *itself*. That's why 5.141 holds: two propositions with the same column are the same proposition. So read "is a truth-table" as "is exhausted by its truth-conditions," not as something the no-denotation claim *entails*.

One guardrail so this doesn't tip into pure formalism. A truth-table is always a table *over elementary propositions* — and those aren't truth-tables of anything. They touch reality by picturing. So the table supplies the logical form; the elementary pictures supply the content. A proposition is a truth-function of elementary propositions *that picture* — drop the second clause and you've got an empty grid.

Quick test of whether you've got the edge of the claim: a tautology has a truth-table too — the all-T column. Is it therefore a proposition, or a truth-table that has stopped being one?

## 영진 · 2026-06-18T08:36

what I don't get is 'propostion' = 'its truth-condition' claim

it totally makes sense that this proposition's meaning is just its truth-condition. But, 'this proposition is truth-condition(table?)' -> I find it absurd...

## Claude · 2026-06-18T08:37

Your discomfort is well-placed — it's tracking a real commitment, not a slip. The gap you feel between "its *meaning* is the truth-conditions" and "it *is* the truth-conditions" is exactly the size of what Frege had and Wittgenstein threw out. Let me dissolve the absurd-sounding part, then show why you can't keep the comfortable claim without the uncomfortable one.

Start with "is." 4.442 doesn't say the proposition equals an abstract grid. It says the truth-table *is a propositional sign* — one legitimate way to *write* the proposition. "p∨q", "¬(¬p∧¬q)", and the truth-table column are three signs for one and the same proposition (5.141: same truth-conditions ⇒ literally one proposition, not two). So "the proposition is a truth-table" means "the truth-table is a perspicuous notation for it," not "the proposition is identical to a Platonic object."

The analogy you'll find natural: the function *halving*. "÷2", "×0.5", "x ↦ x/2" are different signs, but the function is individuated purely by its input→output behaviour and there's nothing more to it than that mapping. A Tractatus proposition is individuated purely by its possibility→{T,F} behaviour, and the truth-table is that mapping written out. We don't find "the function *is* its mapping" absurd — same here. (Wittgenstein wouldn't reify sense as a set-theoretic object, but as a picture of *individuation* this is right.)

Now the part you wanted to resist. Why can't you keep "(a) meaning = truth-conditions" while rejecting "(b) the proposition is exhausted by them"? Because you already granted the proposition has no *Bedeutung*. Frege had a residue — the sentence carried a reference (a truth-value) over and above its sense, so it wasn't exhausted by truth-conditions. Pull the reference out, as the Tractatus does, and ask what's left of the proposition *besides* its truth-conditions. The sign is just a fact among facts, ink on a page (3.14); the only thing making it *this* proposition is which possibilities it affirms and denies. So (b) isn't a bolder claim bolted onto (a) — it's what (a) collapses into once nothing remains underneath it.

So, a check: on this view, are "p∨q" and "¬(¬p∧¬q)" one proposition or two — and what, if anything, is the difference between them? (Worth noting: Frege might not give the same answer. Hold that thought — it runs straight into your hyperintensionality worry.)

## 영진 · 2026-06-18T08:41

it is the same proposition according to the view. But in some context, such as belief or know-context, the substitution does not seem to hold.

## Claude · 2026-06-18T08:43

Right — and that failure is the whole engine of the hyperintensionality literature. Truth-conditional individuation (Tractatus, and equally possible-worlds semantics) is *coarse*: necessarily equivalent contents come out identical, hence freely substitutable everywhere — except in belief, knowledge, "it's informative that…", which is exactly where we *don't* want them substitutable. Push it to the limit and all tautologies are one *sinnlos* thing, so knowing one logical truth would be knowing them all. That's logical omniscience, the bullet.

Here's the part worth knowing: Wittgenstein *saw* this threat, and 5.541–5.5421 is his pre-emptive defense. The worry he states (5.541) is that "A believes that p" looks like a context where p occurs *not* as a truth-argument — which, if real, falsifies the general-form thesis that every proposition is a truth-function of elementary ones. A genuinely non-extensional context wrecks the whole "everything is iterated N" edifice from before.

His answer (5.542) is the cryptic one: "A believes p" is really of the form ' "p" says p '. No relation between a person A and a proposition-as-object — instead a *correlation of facts*: A's thinking is itself a fact (a picture whose psychical constituents go proxy for objects) that depicts the same situation the sentence does. Belief isn't a Russellian attitude-relation at all; 5.5421 then denies there's even a simple subject A to stand in one. He blocks your substitution worry by *denying the opaque occurrence exists* — "believes" never relates anyone to a proposition in the first place.

Now the fork, which is your hyperintensionality problem in Tractatus dress. Does ' "p" says p ' actually block substitution, or just relocate the grain? If A's thought-fact *pictures the situation*, it pictures the same situation whether we write it "p∨q" or "¬(¬p∧¬q)" — same truth-conditions, so substitution slides right through and omniscience is back. The only way to stop it is to make the believing sensitive to the *picturing fact itself* — the sign "p" as a fact (3.14), which is genuinely distinct for the two equivalents even though the proposition is one. But that move makes the object of belief the *representation*, not the truth-conditions — and that difference between equivalent signs is precisely what the rest of the book calls logically inessential, the thing a good Begriffsschrift erases. Anscombe presses on exactly this obscurity in her *Introduction*.

So here's the pressure, which is your own question sharpened: when substitution fails in "A knows that p", is that telling us (i) content must be finer than truth-conditions — go hyperintensional — or (ii) "knows" doesn't relate us to contents at all, but to representations? Read charitably, the Tractatus is forced onto (ii). Which horn do you actually think the attitude data supports — and does your relational-desire work lean the same way, or the opposite?

## 영진 · 2026-06-18T08:48

What is Frege's answer to this problem? - sinn/bedetung distinction was enough for him to treat hyper-intensionality problem? (And I am wondering, do we even need hyperintensionality to produce objection? only intensionality isn't enough?

## Claude · 2026-06-18T08:50

Two moving parts in Frege's answer, and they map onto your second question better than you might expect.

**Frege (Q1).** First, sense is *already* the fine grain. A thought is individuated by *mode of presentation*, not by what's presented — so two expressions can share a reference, even necessarily, and still differ in sense. "Hesperus"/"Phosphorus", "2+2=4"/Fermat: same referent or truth-value, different senses. Evans's reconstruction (the "intuitive criterion of difference") gives the test: the senses differ if a rational subject could take opposing attitudes to the two without irrationality. That cuts *below* necessary equivalence — so Fregean sense is hyperintensional from birth. It's arguably the origin of the idea.

Second, reference-shift in oblique contexts (*ungerade Bedeutung*): inside "A believes that …", an expression stops denoting its customary reference and denotes its customary *sense*. So substitutivity isn't *violated* — it still requires sameness of the relevant reference, but in the belief the relevant reference *is* the sense. Co-referential-but-not-co-sensical terms therefore can't be swapped. A fully referential, compositional semantics is preserved.

So yes, Sinn/Bedeutung was "enough" — but only because sense was *built* to be hyperintensional and the oblique-context machinery routes attitudes to it. The familiar costs: the infinite hierarchy of indirect senses for iterated attitudes, and Davidson's worry that we have no independent grip on those higher senses.

**Q2 — do we even need hyperintensionality?** This is the right question, and the answer is: depends which substitution failure you're modelling. Three rungs:

| Grain | individuated by | distinguishes | first breaks under |
|---|---|---|---|
| Extensional | reference / truth-value | — | modal operators |
| Intensional | worlds → extension | contingently co-referential terms (descriptions: "morning star"/"evening star") | attitudes with *necessary* equivalents |
| Hyperintensional | mode of presentation / structure | necessary equivalents (logical & math equivalence; rigid Hesperus/Phosphorus) | — |

Reading off it: substitution failure *per se* needs no hyperintensionality — modal contexts already break extensional substitution ("necessarily 9>7" true, "necessarily the number of planets >7" false: co-referential, not co-*intensional*). Pure possible-worlds intensionality handles that.

What intensionality *can't* touch is the **necessary-equivalence** band: logically/mathematically equivalent sentences (same set of worlds) and rigid co-referring names (Hesperus/Phosphorus share an intension, once you grant rigidity). There the intensions are identical, so substitution should go through — yet attitudes pry them apart. Only finer-than-intensional content distinguishes them.

And here's the bite for our thread: your Tractatus case — "p∨q" vs "¬(¬p∧¬q)" — is a *logical* equivalence. Same truth-possibilities, same intension. An intensional possible-worlds theory would collapse them *exactly* as the Tractatus does, and fail in belief contexts *exactly* as the Tractatus does. The Tractatus's grain just *is* the intensional grain — regions of logical space are sets of worlds. So your objection was hyperintensional from the start; intensionality buys nothing against it. You were already on the top rung. (Slogan: necessity is the canonical *intensional* operator; the attitudes are the canonical *hyper*intensional ones, because even necessary equivalents resist them.)

Where I'd push, and it's live in your own hyperintensionality work: granting we need *some* grain below intension — *how far down*? Frege is indeterminate here. Compositionality pushes sense toward full sentence-structure (structured propositions, maximally fine), while objectivity and shareability pull back up. Is there a *stable* rung between intension and full structure that the attitude data actually require — or does any principled finer-than-intensional grain slide all the way down to structure? That's what decides whether "hyperintensional" names one level or a whole zoo.

## 영진 · 2026-06-18T08:51

Is there any logical system for the Fregean sinn?

## Claude · 2026-06-18T08:54

Yes — there's a whole lineage, and it's really the formal face of the "how fine is sense?" question I left you on. The systems differ precisely by what they take a sense to *be*.

The literal one is **Church's Logic of Sense and Denotation** (1951, revised through the 90s). Church took Frege at his word and built a typed higher-order logic in which, above each type of denotation, sits a type of *sense* that presents it — so the sense-of-a-sense regress isn't a bug, it's the type hierarchy. He then gave a series of "Alternatives" (0, 1, 2) that *calibrate the grain*: (0) near Carnap's intensional isomorphism, very fine; the others progressively coarser. The Carnap–Church dispute over synonymy, and the *paradox of analysis* lurking in it (how can "brother = male sibling" be both correct and informative if the senses are identical?), is exactly your grain question fought out formally. Carnap's *Meaning and Necessity* (1947) is the sparring partner.

Then sense read as a *procedure*. Moschovakis ("A logical calculus of meaning and synonymy," 2006) makes it exact: the sense of a term is the *algorithm* that computes its denotation, two terms synonymous iff their algorithms are isomorphic — denotation is the value, sense is the recursion that gets you there. Tichý's **Transparent Intensional Logic** (carried on by Duží, Jespersen, Materna) does the same with "constructions," structured procedures as meanings. This is the most natural cash-out of "mode of presentation," and straightforwardly hyperintensional.

The structural reading just identifies sense with syntactic structure: **structured meanings** (Cresswell 1985; the King–Soames–Salmon family), a meaning as a tuple mirroring the parse tree. Maximal grain — the "slides all the way to structure" horn I warned about, where synonymy collapses toward syntactic identity.

The worlds-based attempts are instructive mostly by where they *fail*. **Montague's** intensional logic models only the *intensional* rung — world→extension functions — so it can't separate necessary equivalents and inherits logical omniscience wholesale; not a logic of sense, the cautionary case. **Two-dimensional semantics** (Chalmers's "Fregean"/epistemic 2D) recovers *cognitive significance* via primary intensions, handling Hesperus/Phosphorus and the necessary a posteriori — but it's still world-indexed, so it strains on purely logical/mathematical equivalence. **Impossible-worlds** semantics (Rantala, Hintikka's "impossible possible worlds," now Berto & Jago, *Impossible Worlds* 2019) is the clever fix: admit logically impossible worlds where p∨q and ¬(¬p∧¬q) come apart, and you get hyperintensional grain *plus* a tunable knob — how impossible you let the worlds be — which is exactly what epistemic logic uses to model non-omniscient believers.

That last point closes our loop. The tools built to defeat logical omniscience in epistemic logic — impossible worlds, **awareness logic** (Fagin–Halpern), **justification logic** (Artemov) — are "logics for sense" aimed squarely at the belief-substitution failure you raised. And the current metaphysical front is hyperintensional too: Fine's **truthmaker semantics** (propositions individuated by *exact* truthmakers, so necessary equivalents differ), and the fine-grained object-theoretic systems of **Zalta** (Fregean senses reconstructed as abstract objects, hierarchy and all) and **Bealer**.

So the real answer to "is there a logic for *Sinn*?" is: there are several, and choosing among them just *is* choosing a synonymy criterion — fixing the grain. Church or Zalta if you want the full Fregean sense-of-sense regress handled; Moschovakis or TIL if you want sense as computation; impossible worlds if you want to stay in a modal frame but break omniscience.

Which are you actually after — the system that *handles the sense-of-sense hierarchy*, or the one that *blocks logical omniscience*? They pull toward different machinery, and I'd guess your desire work wants the procedural/structural flavour over the worlds one.

## 영진 · 2026-06-18T08:55

잠깐 딴 이야기, 면접 합격 소식 기다리고 있는 친구에게 결과 나오는 시간에 바로 물어보는 연락을 해도 좋을까?

## Claude · 2026-06-18T08:56

음, 결과 딱 나오는 시간 맞춰서 "어떻게 됐어?" 하고 바로 묻는 건 좀 조심스러워. 붙었으면야 당연히 반갑게 얘기하겠지만, 혹시 안 됐을 경우엔 그 순간에 바로 결과를 입 밖으로 꺼내게 만드는 게 부담이 될 수 있거든. "누가 지켜보고 있다가 나오자마자 확인하는" 느낌이 들면 더 그렇고.

그래서 보통은 결과 자체를 캐묻기보다, *기억하고 있었다 + 응원한다*를 중심에 두고 타이밍은 친구한테 넘기는 쪽이 안전해. 예를 들면 "오늘 결과 나오는 날이지. 계속 응원하고 있었어. 편할 때 얘기해줘" 정도. 이러면 잘됐으면 바로 신나서 답할 거고, 잘 안 됐어도 자기 페이스로 말할 여유가 생기지.

다만 이건 사이에 따라 갈려. 평소에 "나왔어?!" 하면서 같이 동동거리는 막역한 사이면 오히려 바로 물어보는 게 더 반갑고 자연스러울 수도 있어. 너랑 그 친구가 그런 결이면 직접 물어도 돼.

원하면 둘 사이 분위기에 맞춰서 문구 몇 개 잡아줄게.
