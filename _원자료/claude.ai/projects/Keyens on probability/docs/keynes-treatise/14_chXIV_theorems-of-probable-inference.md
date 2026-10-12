---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part II. Fundamental Theorems"
chapter: "Chapter XIV"
title: "The Fundamental Theorems of Probable Inference"
pages: "161–179"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "174–192"
sections: 8
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part II. Fundamental Theorems*

# Chapter XIV. The Fundamental Theorems of Probable Inference

## §1 (p. 161)

{{p.161}} I shall give proofs in this chapter of most of the fundamental theorems of Probability, with very little comment. The bearing of some of them will be discussed more fully in Chapter XVI.

## §2 (p. 161)

The Addition Theorems:

(24) (a + b)/h = a/h + b/h − ab/h.

In IX. write (a + b) for a, and āb for b.
Then   (a + b)āb/h + (a + b)a̅̄̅b̅/h = (a + b)/h,
whence   āb/h + (a + b)(a + b̄)/h = (a + b)/h   by (iii.),
    ā/bh · b/h + a/h = (a + b)/h   by (iii.) and IX.
That is to say, (a + b)/h = a/h + (1 − a/bh) · b/h,
    = a/h + b/h − ab/h.

In accordance with the principles of Chapter XII. § 6, this should be written, strictly, in the form a/h + (b/h − ab/h), or in the form b/h + (a/h − ab/h). The argument is valid, since the probability (b/h − ab/h) is equal to āb/h, as appears from the preceding proof, and, therefore, exists. This important theorem gives the probability of ‘a or b’ relative to a given hypothesis in terms of the probabilities of ‘a,’ ‘b,’ and ‘a and b’ relative to the same hypothesis.

(24.1) If ab/h = 0, i.e. if a and b are exclusive alternatives relative to the hypothesis, then
    (a + b)/h = a/h + b/h.
This is the ordinary rule for the addition of the probabilities of exclusive alternatives.

{{p.162}} (24.2) ab/h + āb/h = b/h,
since   ab + āb ≡ b   by (iii.), and   aāb/h = 0   by (19) and (8).

(24.3) (a + b)/h = a/h + bā/h. This follows from (24) and (24.2).

(24.4) (a + b + c)/h = (a + b)/h + c/h − (ac + bc)/h
    = a/h + b/h + c/h
    − ab/h − bc/h − ca/h + abc/h.

(24.5) And in general
    (p1 + p2 + . . . + pn)/h = Σ pr/h − Σ pspt/h + Σ prpspt/h . . .
    + (−1)^n − 1p1p2 . . . pn/h.

(24.6) If pspt/h = 0 for all pairs of values of s and t, it follows by repeated application of X. that
    (p1 + p2 + . . . + pn)/h = Σ_{1}^{n} pr/h.

(24.7) If pspt/h = 0, etc., and (p1 + p2 + . . . + pn)/h = 1, i.e. if p1p2 . . . pn form, relatively to h, a set of exclusive and exhaustive alternatives, then
    Σ_{1}^{n} pr/h = 1.

(25) If p1p2 . . . pn form, relative to h, a set of exclusive and exhaustive alternatives,
    a/h = Σ_{1}^{n} pra/h.
{{p.163}} Since (p1 + p2 + . . . + pn)/h = 1 by hypothesis,

∴ (p1 + p2 + . . . + pn)/ah = 1 by (9) if ah is not inconsistent; and since pspt/h = 0 by hypothesis,
    ∴ pspt/ah = 0 by (9), if ah is not inconsistent.
Hence   Σ_{1}^{n} pr/ah = (p1 + p2 + . . . + pn)/ah   by (24.6)
    = 1
Also   pra/h = pr/ah · a/h.
Summing   Σ_{1}^{n} pra/h = a/h · Σ_{1}^{n} pr/ah,
    ∴ a/h = Σ_{1}^{n} pra/h, if ah is not inconsistent.

If ah is inconsistent, i.e. if a/h = 0 (for h is by hypothesis consistent), the result follows at once by (8).

(25.1) If pra/h = Xr, the above may be written
    pr/ah = (Xr) ÷ (Σ_{1}^{n} Xr).

(26) a/h = (a + h̄)/h.

For   (a + h̄)/h = a/h + h̄/h − ah̄/h   by (24),
    = a/h   by (13.1) and (8).

(26.1) This may be written
    a/h = (h ⊃ a)/h.

{{p.164}} (27) If (a + b)/h = 0, a/h = 0.
    a/h + [b/h − ab/h] = 0, by (24) and hypothesis
    ∴ a/h = 0.   by (5)

(27.1) If a/h = 0 and b/h = 0, (a + b)/h = 0. This follows from (24).

(28) If a/h = 1, (a + b̄)/h = 1,
    (a + b̄)/h = a/h + b̄ā/h,   by (24.3)
whence (a + b̄)/h = a/h = 1 by (1.1) and (8), together with the hypothesis. That is to say, a certain proposition is implied by every proposition.

(28.1) If a/h = 0, (ā + b)/h = 1 by substituting ā for a and b for b̄ in (28). That is to say, a certainly false proposition implies every proposition.

(29) If a/(h1 + h2) = 1, a/h1 = 1, a/h2 = 1.
    ā/(h1 + h2) = 0,
and   ∴ ā(h1 + h2)/h1 = 0   by (15). Hence   āh1/h1 = 0   by (27), whence the result.

(29.1) Ifa/h1 = 1 and a/h2 = 1, a/(h1 + h2) = 1.
As in (20)   āh1/(h1 + h2) = 0 and āh2/(h1 + h2) = 0.
Hence   ā(h1 + h2)/(h1 + h2) = 0   by (27.1), whence the result.

(29.2) If a/(h1 + h2) = 0, a/h1 = 0. This follows from (29).

(29.3) If a/h1 = 0 and a/h2 = 0, a/(h1 + h2) = 0. This follows from (29.1).

## §3 (p. 164)

Irrelevance and Independence:

{{p.165}} (30) If a/h1h2 = a/h1, then a/h1h̄2 = a/h1, if h1h̄2 is not inconsistent.
    a/h1 = ah2/h1 + ah̄2/h1   by (24.2),
    = a/h1h2 · h2/h1 + a/h1h̄2 · h̄2/h1,
    = a/h1 · h2/h1 + a/h1h̄2 · h̄2/h1,
    ∴ a/h1 · h̄2/h1 = a/h1h̄2 · h̄2/h1,
whence a/h1 = a/h1h̄2, unless h̄2/h1 = 0, i.e. if h1h̄2 is not inconsistent.

Thus, if a proposition is irrelevant to an argument, then the contradictory of the proposition is also irrelevant.

(31) If a2/a1h = a2/h and a2h is not inconsistent, a1/a2h = a1/h.

This follows by (iv. c), since a2/a1h · a1/h = a1/a2h · a2/h by X. If, that is to say, a1 is irrelevant to the argument a2/h (see XIV.), and a2 is not inconsistent with h: then a2 is irrelevant to the argument a1/h; and a1/h and a2/h are independent (see XIII.).

## §4 (p. 165)

Theorems of Relevance:

(32) If a/hh1 > a/h, h1/ah > h1/h.
ah is consistent since, otherwise, a/hh1 = a/h = 0.
Therefore   a/h · h1/ah = a/hh1 · h1/h   by X.,
    > a/h · h1/h   by hypothesis;
so that   h1/ah > h1/h.

Thus if h1 is favourably relevant to the argument a/h, a is favourably relevant to the argument h1/h.

This constitutes a formal demonstration of the generally accepted principle that if a hypothesis helps to explain a phenomenon, the fact of the phenomenon supports the reality of the hypothesis.

In the following theorems p will be said to be more favourable to a/h, than q is to b/h, if (a/ph) ÷ (a/h) > (b/qh) ÷ (b/h) , i.e. if, in the language of {{p.166}} § 8 below, the coefficient of influence of p on a/h is greater than the coefficient of influence of q on b/h.

(33) If x is favourable to a/h, and h1 is not more favourable to a/hx than x is to a/hh1, then h1 is favourable to a/h.

For a/hh1 = a/h · (a/hx) ÷ (a/h) · (a/hh1x) ÷ (a/hx) · (a/hh1) ÷ (a/hh1x) ; and by hypothesis the second term on the right is greater than unity and the product of the third and fourth terms is greater than or equal to unity.

(33.1) A fortiori, if x is favourable to a/h and not favourable to a/hh1, and if h1 is not unfavourable to a/hx, then h1 is favourable to a/h.

(34) If x is favourable to a/h, and h1 is not less favourable to x/ha than x is to h1/ha, then h1 is favourable to a/h.

This follows by the same reasoning as (33), since by an application of the Multiplication Theorem
    (a/hh1x) ÷ (a/hx) · (a/hh1) ÷ (a/hh1x) = (x/hh1a) ÷ (x/ha) · (h1/ha) ÷ (h1/hax).

(35) If x is favourable to a/h, but not more favourable to it than h1x is, and not less favourable to it than to a/hh1, then h1 is favourable to a/h.

For   a/hh1 = a/h · {(a/h) ÷ (a/hx) · (a/hh1x) ÷ (a/h)} · {(a/hx) ÷ (a/h) · (a/hh1) ÷ (a/hh1x)} .

This result is a little more substantial than the two preceding. By judging the influence of x and h1x on the arguments a/h and a/hh1, we can infer the influence of h1 by itself on the argument a/h.

## §5 (p. 166)

The Multiplication Theorems:

(36) If a1/h and a2/h are independent, a1a2/h = a1/h · a2/h.

For   a1a2/h = a1/a2h · a2/h = a2/a1h · a1/h   by X., {{p.167}} and since a1/h and a2/h are independent,
    a1/a2h = a1/h and a2/a1h = a2/h   by XIII.
Therefore   a1a2/h = a1/h · a2/h.
Hence, when a1/h and a2/h are independent, we can arrive at the probability of a1 and a2 jointly on the same hypothesis by simple multiplication of the probabilities a1/h and a2/h taken separately.

(37) If p1/h = p2/p1h = p3/p1p2h = . . .,
    p1p2p3 . . . pn/h = {p1/h}^n .

For p1p2p3 . . . /h = p1/h · p2/p1h · p3/p1p2h . . . by repeated applications of X.

## §6 (p. 167)

The Inverse Principle:

(38) (a1/bh) ÷ (a2/bh) = (b/a1h) ÷ (b/a2h) · (a1/h) ÷ (a2/h) , provided bh, a1h, and a2h are each consistent.
For   a1/bh · b/h = b/a1h · a1/h,
and   a2/bh · b/h = b/a2h · a2/h   by X., whence the result follows, since b/h ≠ 0, unless bh is inconsistent.

(38.1) If   a1/h = p1, a2/h = p2, b/a1h = q1, b/a2h = q2, and a1/bh + a2/bh = 1 then it easily follows that
    a1/bh = (p1q1) ÷ (p1q1 + p2q2),
and   a2/bh = (p2q2) ÷ (p1q1 + p2q2).

(38.2) If a1/h = a2/h the above reduces to
    a1/bh = (q1) ÷ (q1 + q2),
and   a2/bh = (q2) ÷ (q1 + q2),
{{p.168}} since a1/h ≠ 0, unless a1h is inconsistent.

The proposition is easily extended to the cases in which the number of a’s is greater than two.

It will be worth while to translate this theorem into familiar language. Let b represent the occurrence of an event B, a1 and a2 the hypotheses of the existence of two possible causes A1 and A2 of B, and h the general data of the problem. Then p1 and p2 are the à priori probabilities of the existence of A1 and A2 respectively, when it is not known whether or not the event B has occurred; q1 and q2 the probabilities that each of the causes A1 and A2, if it exists, will be followed by the event B. Then (p1q1) ÷ (p1q1 + p2q2) and (p2q2) ÷ (p1q1 + p2q2) are the probabilities of the existence of A1 and A2 respectively after the event, i.e. when, in addition to our other data, we know that the event B has occurred. The initial condition, that bh must not be inconsistent, simply ensures that the problem is a possible one, i.e. that the occurrence of the event B is on the initial data at least possible.

The reason why this theorem has generally been known as the Inverse Principle of Probability is obvious. The causal problems to which the Calculus of Probability has been applied are naturally divided into two classes—the direct in which, given the cause, we deduce the effect; the indirect or inverse in which, given the effect, we investigate the cause. The Inverse Principle has been usually employed to deal with the latter class of problem.

## §7 (p. 168)

Theorems on the Combination of Premisses:

The Multiplication Theorems given above deal with the combination of conclusions; given a/h1 and a/h2 we considered the relation of a1a2/h to these probabilities. In this paragraph the corresponding problem of the combination of premisses will be treated; given a/h1 and a/h2 we shall consider the relation of a/h1h2 to these {{p.169}} probabilities.

(39) a/h1h2h = (ah1h2/h) ÷ (h1h2/h) = (ah1h2/h) ÷ (ah1h2/h + āh1h2/h) by X. and (24.2)
    = (u) ÷ (u + v),
where u is the à priori probability of the conclusion a and both hypotheses h1 and h2 jointly, and v is the à priori probability of the contradictory of the conclusion and both hypotheses h1 and h2 jointly.

(40) a/h1h2 = (ah1/h2) ÷ (ah1/h2 + āh1/h2) = (h1/ah2 · q) ÷ (h1/ah2 · q + h1/āh2 · (1 − q)),
    = (h2/ah1 · p) ÷ (h2/ah1 · p + h2/āh1 · (1 − p)),
where p = a/h1 and q = a/h2.

(40.1) If p = 1/2 , a/h1h2 = (h2/ah1) ÷ (h2/ah1 + h2/āh1),
and increases with   (h2/ah1) ÷ (h2/āh1).

These results are not very valuable and show the need of an original method of reduction. This is supplied by Mr. W. E. Johnson’s Cumulative Formula, which is at present unpublished but which I have his permission to print below.[^169-1]

[^169-1]: The substance of propositions (41) to (49) below is derived in its entirety from his notes,—the exposition only is mine.

## §8 (p. 169)

It is first of all necessary to introduce a new symbol. Let us write

XV.   a/bh = {a^hb}a/h   Def. {{p.170}} We may call {a^hb} the coefficient of influence of b upon a on hypothesis h.

XVI.   {a^hb} · {ab^hc} = {a^hb^hc}   Def. and similarly   {a^hb} · {ab^hcd^he} = {a^hb^hcd^he}.
These coefficients thus belong by definition to a general class of operators, which we may call separative factors.

(41)   ab/h = {a^hb} · a/h · b/h,
since   ab/h = a/bh · b/h.
Thus we may also call {a^hb} the coefficient of dependence between a and b on hypothesis h.

(41.1)   abc/h = {a^hb^hc} · a/h · b/h · c/h.
For   abc/h = {ab^hc}ab/h · c/h   by (41),
    = {ab^hc} · {a^hb} · a/h · b/h · c/h   by (41).

(41.2) And in general
    abcd . . . /h = {a^hb^hc^hd^h . . .} · a/h · b/h · c/h · d/h . . .

(42)   {a^hb} = {b^ha},
since   a/bh · b/h = b/ah · a/h.

(42.1)   {a^hb^hc} = a^hc^hb,
since   a/h · b/h · c/h = a/h · c/h · b/h.

(42.2) And in general we have a commutative rule, by which the order of the terms may be always commuted—
e.g.   {a^hbc^hdef^hg} = {bc^ha^hg^hdef}
    {a^hbc^hdef^hg} = {a^hcb^hfed^hg}.

{{p.171}} (43) As a multiplier the separative factor operates so as to separate the terms that may be associated (or joined) in the multiplicand. Thus   {ab^hcd^he} · {a^hb} = {a^hb^hcd^he},
for   abcde/h = {ab^hcd^he} · ab/h · cd/h · e/h
    = {ab^hcd^he} · {a^hb} · a/h · b/h · cd/h · e/h,
and also abcde/h = {a^hb^hcd^he} · a/h · b/h · cd/h · e/h.
Similarly (for example)
    {abc^hd^hef} · {ab^hc} · {a^hb} = {a^hb^hc^hd^hef}.
(44)   {a^hb} · {ab} = {a^hb}.
For   ab/h = {ab}ab/h.
By a symbolic convention, therefore, we may put {ab} = 1.

(44.1) If {a^hb} = 1, it follows that a/h and b/h are independent arguments; and conversely.

(45) Rule of Repetition {aa^hb} = {a^hb}.
For   aab/h = ab/h   by (vi.) and (12).

(46) The Cumulative Formula:
x/ah : x′/ah : x′′/ah : . . .
    = x/h · a/xh : x′/h · a/x′h : x′′/h · a/x′′h : . . .   by (38).
    Take n + 1 propositions a, b, c . . . Then by repetition
x/ah · x/bh · x/ch . . . : x′/a · x′/b · x′/c . . . : x′′/a · x′′/b · x′′/c . . . : . . .
    = (x/h)^{n+1}a/xh · b/xh . . . : (x′/h)^{n+1}a/x′h · b/x′h . . .
    : (x′′/h)^{n+1}a/x′′h · b/x′′h . . .
{{p.172}} which may be written
    Π^{n+1} x/ah : Π^{n+1} x′/ah : Π^{n+1} x′′/ah : . . .
    = (x/h)^{n+1} Π^{n+1} a/xh : (x′/h)^{n+1} Π^{n+1} a/x′h : . . .
    Now
x/habc . . . : x′/habc . . . : x′′/habc . . .
    = x/h · (abc . . .)/xh : x′/h · (abc . . .)/x′h : . . . by (38),
    and
    abc . . . /xh = {a^{xh}b^{xh}c . . .} Π^{n+1} a/xh   by (41.2),
    ∴ (x/h)^n · x/habc . . . : (x′/h)^n · x′/habc . . . : (x′′/h)^n · x′′/habc . . . : . . .
    ′h x′h   ′   ′

= {a^{xh}b^{xh}c . . .}x/ah · x/bh · x/ch . . . : {a^x b c . . .}x /ah · x /bh
    · x′/ch . . . : . . .
which may be written
    (x/h)^n · x/habc . . . ∝ {a^{xh}b^{xh}c . . .} · x/ah · x/bh · x/ch . . .
where variations of x are involved.

The cumulative formula is to be applied when, having accumulated the evidence a, b, c . . ., we desire to know the comparative probabilities of the various possible inferences x, x′ . . . which may be drawn, and already know determinately the force of each of the items a, b, c . . . separately as evidence for x, x′ . . ..

Besides the factors x/ah, x/bh, etc., we require to know two other sets of values, viz.: (1) x/h, etc., i.e. the à priori probabilities of x, etc., and (2) {a^{xh}b^{xh}c . . .}, etc., i.e. the coefficients of dependence {{p.173}} between a, b, and c . . . on hypotheses xh, etc. It may be remarked that the values {a^{xh}b^{xh}c . . .}, {a^x′^hb^x′^hc . . .} . . . are not in any way related, even when x′ ≡ x̄.

What corresponds to the cumulative formula has been employed, sometimes, by mathematicians in a simplified form which is, except under special conditions, incorrect. First, it has been tacitly assumed that {a^{xh}b^{xh}c . . .}, {a^x′^hb^x′^hc . . .} . . . are all unity: so that
    (x/h)^nx/habc . . . ∝ x/ah · x/bh · x/ch . . .
Secondly, the factor (x/h)^n has been omitted, so that
    x/habc . . . ∝ x/ah · x/bh · x/ch . . .

It is this second incorrect statement of the formula which leads to the fallacious rule for the combination of the testimonies of independent witnesses ordinarily given in the text-books.[^173-1]

[^173-1]: See p. 207 below.

(46.1). If abc . . . /xh = {a^{xh}b^{xh}c . . .}a/xh · b/xh · c/xh . . .
then   x/habc . . . ∝ {a^{xh}b^{xh}c . . .}x/ah · x/bh · x/ch . . . .
This result is exceedingly interesting. Mr. Johnson is the first to arrive at the simple relation, expressed above, between the direct and the inverse formulæ: viz. that the same coefficient is required for correcting the simple formulæ of multiplication in both cases. As he remarks, however, while the direct formula gives the required probability directly by multiplication, the inverse formula gives only the comparative probability.

{{p.174}} (46.2) If x, x′, x′′ . . . are exclusive and exhaustive alternatives,
    (x/h)^{−n} · {a^{xh}b^{xh}c . . .} Π^{n−1} x/ah
    x/habc . . . = [   ],
    Σ( (x′/h)^{−n} · {a^x′^hb^x′^hc . . .} Π^{n−1} x′/ah
since   x/habc . . . ∝ (x/h)^{−n}{a^{xh}b^{xh}c . . .} Π^{n−1} x/ah,
    x′
and   Σ /habc . . . = 1   by (24.7).

(47). (x/habc . . .) ÷ (x/h) = (a/h · b/h · c/h . . .) ÷ (abc . . . /h)
    · (abc . . . /xh) ÷ (a/xh · b/xh · c/xh . . .) · [(x/ah) ÷ (x/h) · (x/bh) ÷ (x/h) . . .] .
For   abc . . . x/h = x/h · abc . . . /xh,
    ∴ (abc . . . x/h) ÷ (abc . . . /h · x/h) = (abc . . . /xh) ÷ (abc . . . /h) = (a/h · b/h · c/h . . .) ÷ (abc . . . /h)
    · (abc . . . /xh) ÷ (a/xh · b/xh · c/xh . . .) · [(a/xh) ÷ (a/h) · (b/xh) ÷ (b/h) . . .] ,
whence the result, since (a/xh) ÷ (a/h) = (x/ah) ÷ (x/h) , etc.

(47.1) The above formula may be written in the condensed form
    xh xh . . .   h   h   h
    h
    xh
{abc . . . x} = (1) ÷ ({ahbhch . . .}) · {a b c   } · [{a x} · {b x} · {c x} . . .].

(48.) ({x/h}nx/habc . . .) ÷ ({x̄/h}nx̄/habc . . .) = ({axhbxhcxh . . .}) ÷ ({ax̄hbx̄hcx̄h . . .}) · (x/ah · x/bh · x/ch . . .) ÷ (x̄/ah · x̄/bh · x̄/ch . . .). {{p.175}} This follows at once from (46.2), since x and x̄ are exclusive and exhaustive alternatives. (It is assumed that xh, x̄h, and ah, etc., are not inconsistent.)

This formula gives x/habc . . . in terms of x/ah, x/bh, etc., together with the three values x/h, {a^{xh}b^{xh}c^{xh} . . .}, and {a^{x̄h}b^{x̄h}c^{x̄h} . . .}.

(48.1)   (x/habcd . . .) ÷ (x̄/habcd . . .) : (x/hbcd . . .) ÷ (x̄/hbcd . . .) = ({axhbcd . . .} · x/ah) ÷ ({ax̄hbcd . . .} · x̄/ah) : (x/h) ÷ (x̄/h). This gives the effect on the odds (prob. x : prob. x̄) of the extra knowledge a.

(49) When several data co-operate as evidence in favour of a proposition, they continually strengthen their own mutual probabilities, on the assumption that when the proposition is known to be true or to be false the data jointly are not counterdependent.

I.e. if {a^{xh}b^{xh}c . . .} and {a^{x̄h}b^{x̄h}c . . .} are not less than unity, and x/kh > x/h where k is any of the data a, b, c . . ., then {a^hb^hc^hd . . .} beginning with unity, continually increases, as the number of its terms is increased.
    abc . . . /h = xabc . . . /h + x̄abc . . . /h   by (24.2).
    = x/h · abc . . . /xh + x̄/h · abc . . . /x̄h.
    ≥ x/h · Π a/xh · b/xh . . . + x̄h Π a/x̄h · b/x̄h . . .
    (since {a^{xh}b^{xh}c . . .} and {a^{x̄h}b^{x̄h}c . . .} are not less than unity),
    ≥ x/h · Π([(ax/h) ÷ (x/h) · (bx/h) ÷ (x/h) . . .] + x̄/h · Π([(ax̄/h) ÷ (x̄/h) · (bx̄/h) ÷ (x̄/h) . . .] ,
    ∴ (abc . . . /h) ÷ ([a/h · b/h . . .])Π   ≥ x/h · Π([(x/ah) ÷ (x/h) · (x/bx) ÷ (x/h) . . .]
    + x̄/h · Π(⟨(x̄/ah) ÷ (x̄/h) · (x̄/bh) ÷ (x̄/h) . . . ⟩.

{{p.176}} We can show that each additional piece of evidence a, b, c . . . increases the value of this expression. For let x/h · G + x̄/h · G′ be its value when all the evidence up to k exclusive is taken, so that
    x/kh · G + x̄/kh · G′
is its value when k is taken. Now G > G′ since x/ah > x/h, etc., and x̄/ah < x̄/h, etc., by the hypothesis that the evidence favours x; and for the same reason x/kh − x/h, which is equal to x̄/h − x̄/kh, is positive.
    ∴ G(x/kh − x/h) > G′(x̄/h − x̄/kh),
i.e.   x/kh · G + x̄/kh · G′ > x/h · G + x̄/h · G′,
whence the result.

(49.1) The above proposition can be generalised for the case of exclusive alternatives x, x′, x′′ . . . (in place of x, x̄).
For {a^hb^hc^h . . .}
    = x/h.{a^{xh}b^{xh}c . . .}{a^hx}{b^hx}{c^hx} . . .
    ′h x′h   h ′ h ′ h ′
    + x′/h.{a^x b c . . .}{a x }{b x }{c x } . . .
    ′′h x′′h   h ′′ h ′′ h ′′
    + x′′/h.{a^x b c . . .}{a x }{b x }{c x } . . . + . . . ;
from which, it follows that, if {a^{xh}b^{xh}c . . .}etc. ≮ 1, and if {a^hx − 1}, {b^hx − 1}, {c^hx − 1}, etc., have the same sign, then {a^hb^hc . . .} is increasing (with the number of letters) from unity.

Mr. Johnson describes this result as a generalisation of the corrected “middle term fallacy” (see Chap. V. § 4).
    APPENDIX
    ON SYMBOLIC TREATMENTS OF PROBABILITY

The use of the symbol 0 for impossibility and 1 for certainty was first introduced by Leibnitz in a very early pamphlet, entitled {{p.177}} Specimen certitudinis seu demonstrationum in jure, exhibitum in doctrina conditionum, published in 1665 (vide Couturat, Logique de Leibnitz, p. 553). Leibnitz represented intermediate degrees of probability by the sign 1/2 , meaning, however, by this symbol a variable between 0 and 1.

Several modern writers have made some attempt at a symbolic treatment of Probability. But with the exception of Boole, whose methods I have discussed in detail in Chapters XV., XVI., and XVII., no one has worked out anything very elaborate.

Mr. McColl published a number of brief notes on Probability of considerable interest—see especially his Symbolic Logic, Sixth Paper on the Calculus of Equivalent Statements, and On the Growth and Use of a Symbolical Language. The conception of probability as a relation between propositions underlies his symbolism, as it does mine.[^177-1] The probability of a, relative to the à priori premiss h, he writes a/ϵ ; and the probability, given b in addition to the à priori premiss, he writes a/b . Thus a/ϵ = a/h , and a/b = a/bh. The difference a/b − a/ϵ , i.e. the change in the probability of a brought about by the addition of b to the evidence, he calls ‘the dependence of the statement a upon the statement b,’ and denotes it by δ a/b . Thus δ a/b = 0, where, in my terminology, b is irrelevant to a on evidence h. The multiplication and addition formulæ he gives as follows: ab/ϵ = a/ϵ · b/a = b/ϵ · a/b .
    (a + b) ÷ (ϵ) = a/ϵ + b/ϵ − ab/ϵ.
Also   δ a/b = A/Bδ b/a, where A = a/ϵ.

[^177-1]: I did not come across these notes until my own method was considerably developed. Mr. McColl has been the first to use the fundamental symbol of Probability.

It is surprising how little use he succeeds in making of these good {{p.178}} results. He arrives, however, at the inverse formula in the shape—
    cr
    v/cr
    cr/v = (ϵ̄) ÷ (Σ_{r=1}^{r=n} cr/ϵ · v/cr),
    cr/ϵ v/cr
where c1 . . . cn are a series of mutually exclusive causes of the event v and include all possible causes of it; reaching it as a generalisation of the proposition
    a/ϵ · b/a
    a/b =
    a/ϵ · b/a + (ā) ÷ (ϵ) · (b) ÷ (ā)

In a paper entitled “Operations in Relative Number with Applications to the Theory of Probabilities,”[^178-1] Mr. B. I. Gilman attempted a symbolic treatment based on a frequency theory similar to Venn’s, but made more precise and more consistent with itself: “Probability has to do, not with individual events, but with classes of events; and not with one class, but with a pair of classes,—the one containing, the other contained. The latter being the one with which we are principally concerned, we speak, by an ellipsis, of its probability without mentioning the containing class; but in reality probability is a ratio, and to define it we must have both correlates given.” But Mr. Gilman’s symbolic treatment leads to very little. More recently R. Laemmel, in his Untersuchungen über die Ermittlung von Wahrscheinlichkeiten, made a beginning on somewhat similar lines; but in his case also the symbolic treatment leads to no substantial results.

[^178-1]: Published in the volume of Johns Hopkins Studies in Logic.

Apart from the writers mentioned above, there are a few who have incidentally made use of a probability symbol. It will be sufficient to cite Czuber.[^178-2] He denotes the probability of an event E by W(E), {{p.179}} and the probability of the event E given the occurrence of an event F by WF(E). He uses this symbol to give WF(E) = WF̄(E) as the criterion of the independence of the events E and F (F̄ denoting the non-occurrence of F); WF(E) = 1, as the expression of the fact that E is a necessary consequence of F; and one or two other similar results.

[^178-2]: Wahrscheinlichkeitsrechnung, vol. i. pp. 43–48.

Finally there is in the Bulletin of the Physico-mathematical Society of Kazan for 1887 a memoir in Russian by Platon S. Porotzki entitled “A Solution of the General Problem of the Theory of Probability by Means of Mathematical Logic.” I have seen it stated that Schröder intended to publish ultimately a symbolic treatment of Probability. Whether he had prepared any manuscript on the subject before his death I do not know.
