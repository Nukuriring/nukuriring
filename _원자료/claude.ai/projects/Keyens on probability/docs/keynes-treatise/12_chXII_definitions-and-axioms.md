---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part II. Fundamental Theorems"
chapter: "Chapter XII"
title: "The Definitions and Axioms of Inference and Probability"
pages: "146–152"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "159–165"
sections: 8
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part II. Fundamental Theorems*

# Chapter XII. The Definitions and Axioms of Inference and Probability

## §1 (p. 146)

{{p.146}} It is not necessary for the validity of what follows to decide in what manner the set of propositions is determined, which is fundamental to our Universe of Reference, or to make definite assumptions as to what propositions are included in the group which is specified by the data. When we are investigating an empirical problem, it will be natural to include the whole of our logical apparatus, the whole body, that is to say, of formal truths which are known to us, together with that part of our empirical knowledge which is relevant. But in the following formal developments, which are designed to display the logical rules of probability, we need only assume that our data always include those logical rules, of which the steps of our proofs are instances, together with the axioms relating to probability which we shall enunciate.

The object of this and the chapters immediately following is to show that all the usually assumed conclusions in the fundamental logic of inference and probability follow rigorously from a few axioms, in accordance with the fundamental conceptions expounded in Part I. This body of axioms and theorems corresponds, I think, to what logicians have termed the Laws of Thought, when they have meant by this something narrower than the whole system of formal truth. But it goes beyond what has been usual, in dealing at the same time with the laws of probable, as well as of necessary, inference.

## §2 (p. 146)

This and the following chapters of Part II. are largely independent of many of the more controversial issues raised in the preceding chapters. They do not prejudge the question as to whether or not all probabilities are theoretically measurable; and they are not dependent on our theories as to the part played by direct judgment in establishing relations of probability or inference between {{p.147}} particular propositions. Their premisses are all hypothetical. Given the existence of certain relations of probability, others are inferred. Of the conclusions of Chapter III., of the criteria of equiprobability and of inequality discussed in Chapters IV. and V., and of the criteria of inference discussed in §§ 5, 6 of Chapter XI., they are, I think, wholly independent. They deal with a different part of the subject, not so closely connected with epistemology.

## §3 (p. 147)

In this chapter I confine myself to Definitions and Axioms.

Propositions will be denoted by small letters, and relations by capital letters. In accordance with common usage, a disjunctive combination of propositions is represented by the sign of addition, and a conjunctive combination by simple juxtaposition (or, where it is necessary for clearness, by the sign of multiplication): e.g. ‘a or b or c’ is written ‘a + b + c,’ and ‘a and b and c’ is written ‘abc.’ ‘a + b’ is not so interpreted as to exclude ‘a and b.’ The contradictory of a is written ā.

## §4 (p. 147)

Preliminary Definitions:

I. If there exists a relation of probability P between the proposition a and the premiss h
    a/h = P.   Def.

II. If P is the relation of certainty[^147-1]
    P = 1.   Def.

[^147-1]: These symbols were first employed by Leibnitz. See p. 155 below.

III. If P is the relation of impossibility[^147-1]
    P = 0.   Def.

IV. If P is a relation of probability, but not the relation of certainty
    P < 1.   Def.

{{p.148}} V. If P is a relation of probability, but not the relation of impossibility
    P > 0.   Def.

VI. If a/h = 0, the conjunction ah is inconsistent.   Def.

VII. The class of propositions a such that a/h = 1 is the group specified by h or (for short) the group h.   Def.

VIII. If b/ah = 1 and a/bh = 1, (a ≡ b)/h = 1.   Def.

This may be regarded as the definition of Equivalence. Thus we see that equivalence is relative to a premiss h. a is equivalent to b, given h, if b follows from ah, and a from bh.

## §5 (p. 148)

Preliminary Axioms:

We shall assume that there is included in every premiss with which we are concerned the formal implications which allow us to assert the following axioms:

(i.) Provided that a and h are propositions or conjunctions of propositions or disjunctions of propositions, and that h is not an inconsistent conjunction, there exists one and only one relation of probability P between a as conclusion and h as premiss. Thus any conclusion a bears to any consistent premiss h one and only one relation of probability.

(ii.) If (a ≡ b)/h = 1, and x is a proposition, x/ah = x/bh. This is the Axiom of Equivalence.

(iii.)   ( a̅ +̅ b̅ ≡ āb̄ )/h = 1
    (aa ≡ a)/h = 1
    ( ā ≡ a )/h = 1
    (ab + āb ≡ b)/h = 1.
    If a/h = 1, ah ≡ h.
That is to say, if a is included in the group specified by h, h and ah are equivalent.

## §6 (p. 148)

Addition and Multiplication.—If we were to assume that probabilities are numbers or ratios, these operations could be given {{p.149}} their usual arithmetical signification. In adding or multiplying probabilities we should be simply adding or multiplying numbers. But in the absence of such an assumption, it is necessary to give a meaning by definition to these processes. I shall define the addition and multiplication of relations of probabilities only for certain types of such relations. But it will be shown later that the limitation thus placed on our operations is not of practical importance.

We define the sum of the probable relations ab/h and ab̄/h as being the probable relation a/h; and the product of the probable relations a/bh and b/h as being the probable relation ab/h. That is to say:

IX.   ab/h + ab̄/h = ah.   Def.

X.   ab/h = a/bh · b/h = b/ah · a/h.   Def.

Before we proceed to the axioms which will make these symbols operative, the definitions may be restated in more familiar language. IX. may be read: “The sum of the probabilities of ‘both a and b’ and of ‘a but not b,’ relative to the same hypothesis, is equal to the probability of ‘a’ relative to this hypothesis.” X. may be read: “The probability of ‘both a and b,’ assuming h, is equal to the product of the probability of b, assuming h, and the probability of a, assuming both b and h.” Or in the current terminology[^149-1] we should have: “The probability that both of two events will occur is equal to the probability of the first multiplied by the probability of the second, assuming the occurrence of the first.” It is, in fact, the ordinary rule for the multiplication of the probabilities of events which are not ‘independent.’ It has, however, a much more central position in the development of the theory than has been usually recognised.

[^149-1]: E.g. Bertrand, Calcul des probabilités, p. 26.

Subtraction and division are, of course, defined as the inverse operations of addition and multiplication:

XI. If PQ = R, P = R/Q .   Def.

{{p.150}} XII. If P + Q = R, P = R − Q.   Def.

Thus we have to introduce as definitions what would be axioms if the meaning of addition and multiplication were already defined. In this latter case we should have been able to apply the ordinary processes of addition and multiplication without any further axioms. As it is, we need axioms in order to make these symbols, to which we have given our own meaning, operative. When certain properties are associated, it is often more or less arbitrary which we take as defining properties and which we associate with these by means of axioms. In this case I have found it more convenient, for the purposes of formal development, to reverse the arrangement which would come most natural to common sense, full of preconceptions as to the meaning of addition and multiplication. I define these processes, for the theory of probability, by reference to a comparatively unfamiliar property, and associate the more familiar properties with this one by means of axioms. These axioms are as follows:

(iv.) If P, Q, R are relations of probability such that the products PQ, PR and the sums P + Q, P + R exist, then:

(iv.a) If PQ exists, QP exists, and PQ = QP. If P + Q exists, Q + P exists and P + Q = Q + P.

(iv.b) PQ < P unless Q = 1 or P = 0; P + Q > P unless Q = 0.
    PQ = P if Q = 1 or P = 0; P + Q = P if Q = 0.

(iv.c) If PQ ⪋ PR, then Q ⪋ R unless P = 0. If P + Q ⪋ P + R, then Q ⪋ R and conversely.

A meaning has not been given, it is important to notice, to the signs of addition and multiplication between probabilities in all cases. According to the definitions we have given, P + Q and PQ have not an interpretation whenever P and Q are relations of probability, but in certain conditions only. Furthermore, if P + Q = R and Q = S + T, it does not follow that P + S + T = R, since no meaning has been assigned to such an expression as P + S + T. The equation must be written P + (S + T) = R, and we cannot infer from the foregoing axioms that (P + S) + T = R. The following axioms allow us to make {{p.151}} this and other inferences in cases in which the sum P + S exists, i.e. when P + S = A and A is a relation of probability.

(v.)   [±P ± Q] + [±R ± S] = [±P ± R] − [∓Q ∓ S]
    = [±P ± R] + [±Q ± S]
    = [±P ± Q] − [∓R ∓ S]
in every case in which the probabilities [±P ± Q], [±R ± S], [±P ± R], etc., exist, i.e., in which these sums satisfy the conditions necessary in order that a meaning may be given to them in the terms of our definition.

(vi.) P(R ± S) = PR ± PS, if the sum R ± S and the products PR and PS exist as probabilities.

## §7 (p. 151)

From these axioms it is possible to derive a number of propositions respecting the addition and multiplication of probabilities. They enable us to prove, for instance, that if P + Q = R + S then P−R = S−Q, provided that the differences P−R and S−Q exist; and that (P+Q)(R+S) = (P+Q)R+(P+Q)S = [PR+QR]+[PS+QS] = [PR+QS]+[QR+PS], provided that the sums and products in question exist. In general any rearrangement which would be legitimate in an equation between arithmetic quantities is also legitimate in an equation between probabilities, provided that our initial equation and the equation which finally results from our symbolic operations can both be expressed in a form which contains only products and sums which have an interpretation as probabilities in accordance with the definitions. If, therefore, this condition is observed, we need not complicate our operations by the insertion of brackets at every stage, and no result can be obtained as a result of leaving them out, if it is of the form prescribed above, which could not be obtained if they had been rigorously inserted throughout. We can only be interested in our final results when they deal with actually existent and intelligible probabilities—for our object is, always, to compare one probability with another—and we are not incommoded, therefore, in one symbolic {{p.152}} operations by the circumstance that sums and products do not exist between every pair of probabilities.

## §8 (p. 152)

Independence:

XIII. If a1/a2h = a1/h and a2/a1h = a2/h, the probabilities a1/h and a2/h are independent.   Def.

Thus the probabilities of two arguments having the same premisses are independent, if the addition to the premisses of the conclusion of either leaves them unaffected.

Irrelevance:[^152-1]

[^152-1]: This is repeated for convenience of reference from Chapter IV. § 14. It is only necessary here to take account of irrelevance on the whole, not of the more precise sense.

XIV. If a1/a2h = a1/h, a2 is irrelevant on the whole, or, for short, irrelevant to a1/h.   Def.
