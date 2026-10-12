# [C1-16] Railton, “A Deductive-Nomological Model of Probabilistic Explanation” (2/3) §4 확률적 설명의 D-N 모형(D-N-P)

| 항목 | 내용 |
|---|---|
| 문헌 | Peter Railton, “A Deductive-Nomological Model of Probabilistic Explanation” (*Philosophy of Science* 45, 1978, pp. 206–26) |
| 수록 | Curd, Cover & Pincock (eds.), *Philosophy of Science: The Central Issues*, 2nd ed. (Norton, 2013), ch. 6, pp. 691–710 |
| 이 대목 | §4 확률적 설명의 D-N 모형(D-N-P) · 알파 붕괴 사례, 도식 (4a)–(4d), 괄호 속 부언과 설명의 참 |
| 쪽 | pp. 697–702 (C&C 2판 쪽수) |
| 분량 | 약 2,500단어 · 멈춤 9곳 |
| 순서 | 3개 대목 중 2번째 · 이전: C1-15 · 다음: C1-17 |
| 원문 파일 | NSJ/Philosophy of science the central issues Second Edition (Martin Curd , J. A. Cover etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf · PDF 721–726쪽 |

> **표기 규약** · `[p. 257]`은 Curd & Cover 2판 257쪽이 시작되는 지점입니다. `⟦멈춤 n⟧`은 논증 단계가 바뀌는 자리로, 여기서 읽기를 멈추고 앞 단계를 자기 말로 재구성합니다. 해설은 넣지 않았습니다. 스캔본을 OCR로 읽은 텍스트라서 원주 번호가 기호나 숫자로 붙어 있고(예: `research.*`, `naming,’`), 원주와 편자 주는 `C1-Railton-DNP_주석.md`에 모았습니다. OCR 오류는 확인한 범위에서 바로잡았으며, 인용하기 전에 의심스러운 곳은 원문 PDF와 대조합니다.

---
### 4 A D-N Model of Probabilistic Explanation

I will present my account of probabilistic explanation by developing an example of just such “practically negligible” —but physically real and lawful— chance: alpha-decay in long-lived radioactive elements. The mean-life of the more stable radionuclides is so long as to make the probability for any particular nucleus of such an element to decay during our lifetimes effectively zero. But our nuclear theory shows that it is not zero, and explains how such rarities can occur.


**⟦멈춤 1⟧**

On the account offered here, probabilistic explanations will be either true or false independent of our epistemic situation. Moreover, to explain, they must be true. Here I am following Hempel’s usage in calling an explanatory argument true just in case it is valid and its premises are true ([3], p. 338). Such an explanation will not be true if the probabilistic laws it invokes are not true; in particular, it will not be true unless the process responsible for the explanandum is genuinely indeterministic. If alpha-decay is to serve as our paradigm for probabilistic explanation, we must be correct in assuming that the probabilistic wave-mechanical account of particle transmission through the nuclear potential barrier tells us all there is to know about the cause of alpha-decay. At least, it must be true that there are no hidden variables characterizing unknown initial conditions that suffice to account for alpha-decay deterministically. However, I take it to be uncontroversial that alpha-decay is an indeterministic process, if any is.


**⟦멈춤 2⟧**

Let us suppose that we are given an individual instance of alpha-decay to explain: a nucleus of radionuclide uranium²³⁸, call it ‘u’, has emitted an alpha-particle during the time interval lasting from t₀ to t₀+θ, where θ is very small and expressed in standard units. Since the mean-life of U²³⁸ is [p. 698] 6.5 × 10⁹ years, the probability of observing a decay by u during this interval is exceedingly small, but unquestionably exists (witness the decay). This probability can be given precisely by using the radioactive decay constant A,,, characteristic of all atoms of U***. Significantly, we need not know when in the course of the history of u time t, occurs: the probability of decay is unaffected by the age of the atom. Therefore, as long as decay has not yet occurred, individual “trials’—consisting of observing a single isolated radioactive nucleus for successive intervals of the same length—are statistically independent. Using these two facts we can determine the probability of decay for individual nuclei during any time interval chosen: it will be 1 minus the probability that any such nucleus survives the interval intact; for u, (l—exp(— A,3. - 8)).*

To obtain experimental confirmation of this value, we infer from the probability to decay of individual nuclei to statistical features of sample populations of nuclei, for example, half-life and mean-life. These predicted statistical features are then checked against actual observed relative frequencies in large populations over long intervals. Physical probabilities of the sort being considered here are therefore to be contrasted with statistical probabilities; the former express the strength of a certain physical possibility for a given system, while the latter reduce to claims about the (limiting) relative frequencies of traits in sample populations. Much well-founded doubt has been expressed about the applicability of statistical probabilities to single cases, but physical probabilities are located in the features of the single case. Therefore, we can understand our nuclear theory as implying strictly universal (physical) probability-attributing laws of the form:

> (1)  All nuclei of radioelement E have probability (1 − exp(−λ_E · t)) to emit an alpha-particle during any time interval of length t, unless subjected to environmental radiation.


**⟦멈춤 3⟧**

Because schema (1) is universal in form, its instances are candidates for law premises in deductive-nomological inferences concerning individual nuclei. Thus, for u:

```
(2) a  All nuclei of U²³⁸ have probability (1 − exp(−λ₂₃₈ · θ)) to emit an alpha-particle during any interval of length θ, unless subjected to environmental radiation.
    b  u was a nucleus of U²³⁸ at time t₀, and was subjected to no environmental radiation before or during the interval t₀ − (t₀+θ).
    ─────────────────
    c  u had probability (1 − exp(−λ₂₃₈ · θ)) to emit an alpha-particle during the interval t₀ − (t₀+θ).
```


**⟦멈춤 4⟧**

[p. 699] (2), it appears, gives a D-N explanation only of the fact that u had such-and-such a probability to decay during the interval in question, but we should look a bit closer. I submit that (2), when supplemented as follows, is the probabilistic explanation of u’s decay:

> (3)  A derivation of (2a) from our theoretical account of the mechanism at work in alpha-decay.
>      The D-N inference (2).
>      A parenthetic addendum to the effect that u did alpha-decay during the interval t₀ − (t₀+θ).


**⟦멈춤 5⟧**

Am I merely making a virtue of necessity, and saying that since (3) contains all we can say about u’s decay, (3) must explain it? In fact, there is a great deal more we could say about u’s decay. Deliberately left out of (3) are innumerable details about the experimental apparatus (temperature, pressure, location, etc.), about the beliefs and expectations of those monitoring the experiment, and about the epistemic position of the scientific community at the time. These facts are omitted as explanatorily irrelevant to u’s decay because they are causally irrelevant to the physical possibility for decay that obtained during the interval in question, and to whether or not that possibility was realized.’ A full account of these notions of explanatory and causal relevance is not possible here, so instead I will go on to argue that what (3) comprises is explanatorily relevant, and explanatory.

I must begin this task with a defense of the nomological status of (2a), and of the legitimacy of treating it as a covering law for u’s decay. The following criterion of nomologicality will be used: a law is a universal truth derivable from our theory without appeal to particular facts. This criterion of course lacks generality (what counts as theory if not the laws themselves?), fails to segregate natural from logical laws, picks out only so-called “universal” (as opposed to “local”) laws, and is entirely too vague (how to distinguish “particular facts” from the rest?). But I trust it will do for now. The motive for excluding “particular facts” is that some true, universal statements derivable from our theory plus particular facts would not normally be regarded as universal laws, but would at best be “local laws,” for example, “All Homo neanderthalensis live during the late Pleistocene age.”

The generalization in question here, (2a), is derived by solving the Schrédinger wave equation for an alpha-particle of energy =4.2 MeV for the potential regions in and around the nucleus of an element with atomic number 92 and atomic weight 238, none of which are “particular facts,” plus some simplifying assumptions about the structure of the nucleus and the distinctness of the alpha-particle within it prior to decay. While it is forbidden by classical physics for a low-energy particle like the 4.2 MeV alpha-particle associated with U?*® to pass through the 24.2 MeV potential barrier surrounding so massive a nucleus, the quantum theory predicts that the probability amplitude for finding such an alpha-particle outside the potential barrier is non-zero. Thus a transmission coefficient for U?** alpha-particles [p. 700] is determined, which, given certain simplifying assumptions about the goings-on inside the nucleus, yields the probability that such a particle will tunnel out of the potential well “per unit time for one nucleus,” namely, Anz ([1], p. 175). (2a) thus neither reports a summary of past observations nor expresses a mere statistical uniformity that scattered initial conditions would lead us to anticipate. Instead, it is a law of irreducibly probabilistic form, assigning definite, physically determined probabilities to individual systems.

It follows that the derivation of conclusions from (2a) by universal instantiation and modus ponens is unexceptionable.* Were (2a) but a we tical generalization, properly understood as meaning “(1 —exp(— A,3, - ® of U*** nuclei in samples of sufficiently large size N, on average, decay dor ing the interval t,—(t,+8),” it could not undergo universal instantiation, and would not permit detachment of a conclusion about the probability obtaining in a single case.

Further, if the wave equation does indeed tell us all there is to know about the mechanism involved in nuclear barrier penetration, it follows that nothing more can be said to explain why the observed decay of u took place, once we have shown how (2a) is derived from our account of this mechanism, and established that (2) is valid and that (3)’s parenthetic addendum is true.


**⟦멈춤 6⟧**

Still, does (3) explain why the decay took place? It does not explain why the decay had to take place, nor does it explain why the decay could be expected to take place. And a good thing, too: there is no had to or could be expected to about the decay to explain—it is not only a chance event, but a very improbable one. (3) does explain why the decay improbably took place, which is how it did. (3) accomplishes this by demonstrating that there existed at the time a small but definite physical possibility of decay, and noting that, by chance, this possibility was realized. The derivation of (2a) that begins (3) shows, by assimilating alpha-decay to the chance process of potential barrier tunneling, how this possibility comes to exist. If alpha-decays are chance phenomena of the sort described, then once our theory has achieved all that (3) involves, it has explained them to the hilt, however unsettling this may be to a priori intuitions. To insist upon stricter sub-sumption of the explanandum is not merely to demand what (alas) cannot be, but what decidedly should not be: sufficient reason that one probability rather than another be realized, that is, chances without chance.

Because of the peculiar nature of chance phenomena, it is explanatorily relevant whether the probability in question was realized, even though there is no before-the-fact explanatory argument, deductive or inductive, to this conclusion. Indeed, it is the absence of such an argument that makes a place in probabilistic explanation for a parenthetic addendum concerning [p. 701] whether the possibility became actual in the circumstances given. These addenda may offend those who believe that explanations must always be arguments, but at the most general level explanations are accounts, not arguments. It so happens that for indeterministic phenomena inferences of a particular kind—D-N arguments meeting the desiderata suggested in section 1—are explanatory accounts, and this for good reasons. However, indeterministic phenomena are a different matter, and explanatory accounts of them must be different as well. If the present model is accepted, then almost all of the explanatory burden in probabilistic explanation can be placed on deductive arguments—those characterizing the indeterministic mechanism and those attributing a certain probability to the explanandum. But these arguments leave out a crucial part of the story: did the chance fact obtain?

The parenthetic addendum fills this gap in the account, and communicates information that is relevant to the causal origin of the explanandum by telling us that it came about as the realization of a particular physical possibility. Further, it permits us to chain probabilistic explanations together to make more comprehensive explanations, in which each link is able to bear the full explanatory burden for the fact it covers, and is capable of leading us on to the next fact in the causal sequence being explained. From (2) alone we cannot move directly to an account of what the alpha-particle did to a nearby photographic plate, but only to a probability (and a miserably low one) that this account will be true. The parenthetic addendum to (3) furnishes a non-probabilistic premise from which to begin an account of the condition of the photographic plate: the occurrence of an alpha-decay in the vicinity. Dropping off the addendum leaves an explanation, but it is a D-N explanation of the occurrence of a particular probability, not a probabilistic explanation of the occurrence of a particular decay.


**⟦멈춤 7⟧**

The scheme for probabilistic explanation of particular chance facts by nomic subsumption that is being offered here, the deductive-nomological-probabilistic (D-N-P) model, is this. First we display (or truthfully claim an ability to display) a derivation from our theory of a law of essentially probabilistic form, complete with an account of how the law applies to the indeterministic process in question. The derived law is of the form:*

> (4a)  (t)(x)[F_x,t → Prob(G)_x,t = p]
>       “At any time, anything that is F has probability p to be G.”

Next, we adduce the relevant fact(s) about the case at hand, e:

> (4b)  F_e,t₀
>       “e is F at time t₀.”

[p. 702] and draw the obvious conclusion:

> (4c)  Prob(G)_e,t₀ = p
>       “e has probability p to be G at time t₀.”

To which we add parenthetically, and according to how things turn out:

> (4d)  (G_e,t₀ / −G_e,t₀)
>       “(e did/did not become G at t₀).”


**⟦멈춤 8⟧**

Whether a D-N-P explanation is true will depend solely upon the truth-values of its premises and addendum, and the validity of its logic. I leave open what becomes of a D-N-P explanation that contains true laws, initial facts, and addendum, but botches the theoretical account of the laws invoiced. Let us simply say that the more botched, the less satisfactory the explanation.

The law premise (4a) will be true if all things at all times satisfy the conditional ‘F_, - Prob(G), ,=p’, using whatever reading of “—’ we decide upon for the analysis of natural laws in general. It will be false if there exists a partition of the F's into those with physical probability r to be G and those with physical probability s to be G, where s#r#p. Such a partition might exist according to some other interpretation of probability, but this would not affect the truth of (4a). For example, suppose that a coin toss meeting certain specifications is an indeterministic event with probability !/2 of yielding heads. We now perform the experiment of repeating such a toss a great many times. Curiously, all and only even numbered tosses yield heads. This result supplies certain frequentists with grounds for saying that Prob(heads, even-numbered toss)=1, while Prob(heads, odd-numbered toss)=0.° But because all tosses met the specification laid down, the probability of heads was the same, !/2, on each toss, despite the curious behavior. Such behavior may make us suspicious of our original claims about the indeterminacy of the process or about the physical probability it has of producing heads, but is no proof against them. Indeed, the original probability attribution requires us to assign a definite physical probability to just such an untoward sequence of outcomes, the occurrence of which therefore hardly contradicts this attribution.

The particular fact premise (4b) will be true iff [if and only if] e is an F during the time in question, and not either an F* (with probability r#p to be G) or an F** (with probability g=p to be G, but unlike an F in other respects). Using the (let us say) true law that all F*“s have probability q=p to be G, and the falsehood that e is an F'**, we could derive a true conclusion, indistinguishable from (4c). Hence the requirement that the premises be true if the argument is to explain; and if we reason logically from true premises, the conclusion will take care of itself.


**⟦멈춤 9 · 대목 끝⟧**
