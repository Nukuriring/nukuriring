---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part II. Fundamental Theorems"
chapter: "Chapter XVII"
title: "Some Problems in Inverse Probability, including Averages"
pages: "214–248"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "227–261"
sections: 12
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part II. Fundamental Theorems*

# Chapter XVII. Some Problems in Inverse Probability, including Averages

## §1 (p. 214)

{{p.214}} The present chapter deals with ‘problems’—that is to say, with applications to particular abstract questions of some of the fundamental theorems demonstrated in Chapter XIV. It is without philosophical interest and should probably be omitted by most readers. I introduce it here in order to show the analytical power of the method developed above and its advantage in ease and especially in accuracy over other methods which have been employed.[^214-1] § 2 is mainly based upon some problems discussed by Boole. §§ 3–7 deal with the fundamental theory connecting averages and laws of error. §§ 8–11 treat discursively the Arithmetic Average, the Method of Least Squares, and Weighting.

[^214-1]: Such examples as these might sometimes be set to test the wits of students. The problems on Probability usually given are simply problems on mathematical combinations. These, on the other hand, are really problems in logic.

## §2 (p. 214)

In the following paragraph solutions are given of some problems posed by Boole in chapter xx. of his Laws of Thought. Boole’s own method of solving them is constantly erroneous,[^214-2] and the difficulty of his method is so great that I do not know of any one but himself who has ever attempted to use it. The term ‘cause’ is frequently used in these examples where it might have been better to use the term ‘hypothesis.’ For by a possible cause of an event no more is here meant than an antecedent occurrence, the knowledge of which is relevant to our anticipation of the event; it does not mean an antecedent from which the event in question must follow.

[^214-2]: For the reason given in § 6 of Chapter XVI. The solutions of problems I.–VI., for example, in the Laws of Thought, chap. xx., are all erroneous.

(56) The à priori probabilities of two causes A1 and A2 are c1 and c2 respectively. The probability that if the cause A1 occur, an {{p.215}} event E will accompany it (whether as a consequence of A1 or not), is p1, and the probability that E will accompany A2, if A2 present itself, is p2. Moreover, the event E cannot appear in the absence of both the causes A1 and A2. Required the probability of the event E.

This problem is of great historical interest and has been called Boole’s ‘Challenge Problem.’ Boole originally proposed it for solution to mathematicians in 1851 in the Cambridge and Dublin Mathematical Journal. A result was given by Cayley[^215-1] in the Philosophical Magazine, which Boole declared to be erroneous.[^215-2] He then entered the field with his own solution.[^215-3] “Several attempts at its solution,” he says, “have been forwarded to me, all of them by mathematicians of great eminence, all of them admitting of particular verification, yet differing from each other and from the truth.”[^215-4] After calculations of considerable length and great difficulty he arrives at the conclusion that u is the probability of the event E where u is that root of the {{p.216}} equation
    [1 − c1(1 − p1) − u] [1 − c2(1 − p2) − u]
    = ((u − c1p1)(u − c2p2)) ÷ (c1p1 + c2p2 − u)
    1 − u
which is not less than c1p1 and c2p2 and not greater than 1−c1(1−p1), 1 − c2(1 − p2) or c1p1 + c2p2.

[^215-1]: Phil. Mag. 4th series, vol. vi.

[^215-2]: Cayley’s solution was defended against Boole by Dedekind (Crelle’s Journal, vol. 1. p. 268). The difference arises out of the extreme ambiguity as to the meaning of the terms as employed by Cayley.

[^215-3]: “Solution of a Question in the Theory of Probabilities,” Phil. Mag. 4th series, vol. vii., 1854. This solution is the same as that printed by Boole shortly afterwards in the Laws of Thought, pp. 321–326. In the Phil. Mag. Wilbraham gave as the solution u = c1p1 + c2p2 − z, where z is necessarily less than either c1p1 or c2p2. This solution is correct so far as it goes, but is not complete. The problem is also discussed by Macfarlane, Algebra of Logic, p. 154.

[^215-4]: In proposing the problem Boole had said: “The motives which have led me, after much consideration, to adopt, with reference to this question, a course unusual in the present day, and not upon slight grounds to be revived, are the following: First, I propose the question as a test of the sufficiency of received methods. Secondly, I anticipate that its discussion will in some measure add to our knowledge of an important branch of pure analysis.” When printing his own solution in the Laws of Thought, he adds, that the above “led to some interesting private correspondence, but did not elicit a solution.”

This solution can easily be seen to be wrong. For in the case where A1 and A2 cannot both occur, the solution is u = c1p1 + c2p2; whereas Boole’s equations do not reduce to this simplified form. The mistake which Boole has made is the one general to his system, referred to in Chapter XVI., § 6.[^216-1]

[^216-1]: Boole’s error is pointed out and a correct solution given in Mr. McColl’s “Sixth Article on the Calculus of Equivalent Statements” (Proc. Lond. Math. Soc. vol. xxviii. p. 562).

The correct solution, which is very simple, can be reached as follows:

Let a1, a2, e assert the occurrences of the two causes and the event respectively, and let h be the data of the problem.

Then we have a1/h = c1, a2/h = c2, e/a1h = p1, e/a2h = p2: we require e/h. Let e/h = u, and let a1a2/eh = z. Since the event cannot occur in the absence of both the causes,
    e/ā1ā2h = 0.
It follows from this that ā1ā2/eh = 0, unless e/h = 0,
i.e.   (a1 + a2)/eh = 1,
whence   a1/eh + a2/eh = 1 + a1a2/eh   by (24). Now   a1/eh = c1p1/u and a2/eh = c2p2/u,
    ∴ u = (c1p1 + c2p2) ÷ (1 + z),
where z is the probability after the event that both the causes were present.

{{p.217}} If we write ea1a2/h = y,
    y = a1a2/eh · e/h = uz
so that   u = (c1p1 + c2p2) − y.

Boole’s solution fails by attempting to be independent of y or z.

(56.1) Suppose that we wish to find limits for the solution which are independent of y and z: then, since y ⪕ 0, u ⪕ c1p1 + c2p2.

Again
e/h = eā1/h+ea1/h ⪕ ā1/h+ea1/h ⪕ 1−c2+c2p2 by (24.2) and (4). Similarly e/h ⪕ −c2 + c2p2. From the same equations it appears that e/h ⪕ c1p1 and c2p2.
∴ u lies between
    c1p1 + c2p2
    ( c1p1
    the greatest of   and the least of 1 − c1(1 − p1)
    c2p2
    1 − c2(1 − p2).

It will be seen that these numerical limits are the same as the limits obtained by Boole for the roots of his equations.

(56.2) Suppose that the à priori probabilities of the causes c1 and c2 are to be eliminated. The only limit we then have is u < p1 + p2.

(56.3) Suppose that one of the à priori probabilities c2 is to be eliminated. We then have limits c1p1 ⪕ u ⪕ 1 − c1 + c1p1. If, therefore, c1 is large, u does not differ widely from c1p1.

(56.4) Suppose p2 is to be eliminated. We then have
    c1p1 ⪕ u ⪕ c1p1 + c2
    ⪕ c1p1 + 1 − c1.

If therefore c1 is large or c2 small, u does not differ widely from c1p1.

{{p.218}} (56.5) If a1/a2h = a1/h, i.e. if our knowledge of each of the causes is independent, we have a closer approximation. For
    y = ea1a2/h = e/a1a2h · a1/a2h · a2/h = e/a1a2h · c1c2,
    ∴ u = c1p1 + c2p2 − c1c2 · e/a1a2h,
    ∴ u > c1p1 + c2p2 − c1c2.

(57) We may now generalise (56) and discuss the case of n causes. If an event can only happen as a consequence of one or more of certain causes A1, A2, . . . An, and if c1 is the à priori probability of the cause A1 and p1 the probability that, if the cause A1 be known to exist, the event E will occur: required the probability of E.

This is Boole’s problem VI. (Laws of Thought, p. 336). As the result of ten pages of mathematics, he finds the solution to be the root lying between certain limits of an equation of the nth degree which he cannot solve. I know no other discussion of the problem. The solution is as follows:
    e/h = eā1/h + ea1/h = eā1/h + e/a1h · a1/h = eā1/h + c1p1 (i.)
    eā1/h = eā1ā2/h + eā1/a2h · a2/h = eā1ā2/h + c2 · eā1/a2h,
    eā1/a2h = e/a2h − ea1/a2h = p2 − 1/c2 · ea1a2/h,
    ∴ e/h = eā1ā2/h + c1p1 + c2p2 − ea1a2/h,
    eā1ā2/h = eā1ā2ā3/h + eā1ā2a3/h,
and   eā1ā2a3/h = eā1ā2/a3h · c3 = c3 {e/a3h − ea̅̄̅1̅a̅̄̅2̅/a3/h}
    = c3p3 − ea̅̄̅1̅a̅̄̅2̅a3/h,

∴ e/h = eā1ā2ā3/h + c1p1 + c2p2 + c3p3 − eā1a2/h − ea̅̄̅1̅a̅̄̅2̅a3/h. {{p.219}} In general
    eā1ā2 . . . ār−1/h = eā1ā2 . . . ār−1ār/h + eā1ā2 . . . ār−1ar/h
    = eā1 . . . ār/h + eā1 . . . ār−1/arh · cr
    = eā1 . . . ār/h + cr {e/arh − e̅a̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅/arh}
    = eā1 . . . ār/h + crpr − ea̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅ar/h.
    ∴ finally we have e/h = eā1 . . . ān/h + Σ_{1}^{n} crpr − Σ_{2}^{n} ea̅̄̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅ar/h.
But since the n causes are supposed to be exhaustive
    eā1 . . . ān/h = 0,
    ∴ e/h = Σ_{1}^{n} crpr − Σ_{2}^{n} ea̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅ar/h   (ii.).
Let   ea̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅ar/h = nr;
then   e/h = Σ_{1}^{n} crpr − Σ_{2}^{n} nr   (iii.).

(57.1) If our knowledge of the several causes is independent, if, that is to say, our knowledge of the existence of any one of them is not relevant to the probability of the existence of any other, so that ar/ash = ar/h = cr, then
    ea̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅ar/h = ea̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅/arh · cr
    = cr · ea̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅arh{1 − ā1 . . . ār−1/arh}
    = cr [1 − Π_{1}^{r−1} (1 − c1) . . . (1 − cr−1)] e/a̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅arh.
Let   e/a̅̄̅1̅ .̅ .̅ .̅ a̅̄̅r̅−̅1̅arh = mr,
    s=r−1
then   e/h = Σ_{r=1}^{r=n} crpr − Σ_{r=2}^{r=n} cr [1 − Π_{s=1} (1 − cs)] mr.

{{p.220}} These results do not look very promising as they stand, but they lead to some useful approximations on the elimination of mr and nr and to some interesting special cases.

(57.2) From equation (i.) it follows that e/h ⪖ c1p1 and e/h ⪕ 1 − c1(1 − p1); and from equation (ii.) that e/h ⪕ Σ_{1}^{n} crpr;

∴ e/h lies between
    Σ_{1}^{n} crpr
    c1p1
    ...   1 − c1(1 − p1)
    the greatest of   and the least of
    ...
    cnpn
    1 − cn(1 − pn).

(57.3) Further, if the causes are independent it follows from (57.1) that
    e/h ⪖ Σ_{1}^{n} crpr − Σ_{2}^{n} cr[1 − Π_{1}^{r−1} (1 − cs)],
so that e/h lies between
    Σ_{1}^{n} c p Σ_{2}^{n} c [1 − Π_{1}^{r−1} (1 − c )]   Σ_{1}^{n} c p
    r r −   r   s   r r

the
    c p   and the 1 − c1(1 − p1)
    greatest^{11}
    least of   ...
    ...
    of
    cnpn   1 − cn(1 − pn).

(57.4) Now consider the case in which p1 = p2 = . . . = pn = 1, i.e. in which any of the causes would be sufficient, and in which the causes are independent. Then mr = 1; so that
    s=r−1
    e/h = Σ_{r=1}^{r=n} cr − Σ_{r=2}^{r=n} cr [1 − Π_{s=1} (1 − cs)]
    = 1 − (1 − c1)(1 − c2) . . . (1 − cn).

{{p.221}} (57.5) Let c1, c2 . . . cn be small quantities so that their squares and products may be neglected.

Then   e/h = Σ crpr,
i.e. the smaller the probabilities of the causes the more do they approach the condition of being mutually exclusive.[^221-1]

[^221-1]: Boole arrives at this result, Laws of Thought, p. 345, but I doubt his proof.

(57.6) The à posteriori probability of a particular cause ar after the event has been observed is
    ar/eh = (e/arh · ar/h) ÷ (e/h)
    = (prcr) ÷ (e/h).

(This is Boole’s problem IX., p. 357).

(58) The probability of the occurrence of a certain natural phenomenon under given circumstances is p. There is also a probability a of a permanent cause of the phenomenon, i.e. of a cause which would always produce the event under the circumstances supposed. What is the probability that the phenomenon, being observed n times, will occur the n + 1th?

This is Boole’s problem X. (Laws of Thought, p. 358). Boole arrives by his own method at the same result as that given below. It is necessary first of all to state the assumption somewhat more precisely. If xr asserts the occurrence of the event at the rth trial and t the existence of the ‘permanent cause’ we have
    xr/h = p, t/h = a, xr/th = 1,
and we require   xn+1/x1 . . . xnh = yn+1.
It is also assumed that if there is no permanent cause the probability {{p.222}} of xs is not affected by the observations xr, etc., i.e.
    xs/xr . . . xtt̄h = xs/t̄h,[^222-1]
    xs/t̄h = (xst̄/h) ÷ (t̄/h) = (xs/h − xst/h) ÷ (t̄/h) = (p − a) ÷ (1 − a),

[^222-1]: This assumption, which is tacitly introduced by Boole, is not generally justifiable. I use it here, as my main purpose is to illustrate a method. The same problem, without this assumption, will be discussed in dealing with Pure Induction.

xr/x1 . . . xr−1h = xrt/x1 . . . xr−1h + xrt̄/x1 . . . xr−1h
    = t/x1 . . . xr−1h + xr/t̄x1 . . . xr−1h · t̄/x1 . . . xr−1h
    = (x1 . . . xr−1t/h) ÷ (x1 . . . xr−1/h) + (p − a) ÷ (1 − a) · (x1 . . . xr−1/t̄h · t̄/h) ÷ (x1 . . . xr−1/h)
    r−1
    ((p − a) ÷ (1 − a)) (1 − a)
    = (a) ÷ (y1y2 . . . yr−1) + (p − a) ÷ (1 − a)   ,
    y̅1̅y̅2̅ .̅ .̅ .̅ y̅r̅−̅1̅
    r−1
    a + (p − a) ((p − a) ÷ (1 − a))
i.e.   yr =   .
    y̅1̅y̅2̅ .̅ .̅ .̅ y̅r̅−̅1̅
    a + (p − a)(p − a) ÷ (1 − a)
Also   y1 = p and y2 =   ,
    y̅1̅
    n
    a + (p − a) ((p − a) ÷ (1 − a))
so that   yn+1 =   (̅   )̅n̅−̅1̅ .
    a + (p − a) (p − a) ÷ (1 − a)

(58.1) If p = a, yn = 1; for if an event can only occur as the result of a permanent cause, a single occurrence makes future occurrences certain under similar conditions.

{{p.223}} (58.2)
    n−2
    a(p − a) ((p − a) ÷ (1 − a)) ((1 − (p − a) ÷ (1 − a))
    yn+1 − yn = "   n−1#("   n−2#
    a + (p − a) ((p − a) ÷ (1 − a))   a + (p − a) ((p − 1) ÷ (1 − a))
(by easy algebra);

and p is always > a andr< 1.

So that (p − a) ((p − a) ÷ (1 − a)) is positive and decreases as r increases,
    ∴ yn+1 > yn.

As n increases yn = 1 − ϵ, where
    n−2
    [   (   )]   ((p − a) ÷ (1 − a))
    ϵ = (p − a) 1 − (p − a) ÷ (1 − a)   (̅   )̅n̅−̅2̅ ,
    a + (p − a) (p − a) ÷ (1 − a)
so that for any positive value of η however small a value of n can be found such that ϵ < η so long as a is not zero.

(58.3) tn the à posteriori probability of a permanent cause after n successful observations is
    t/x1 . . . xnh = (x1 . . . xn/th · t/h) ÷ (x1 . . . xn/h) = (a) ÷ (y1y2 . . . yn),
i.e.   tn = a/n(   ) ,
    a + (p − a) (p − a) ÷ (1 − a)
    n
    (p − a) ((p − a) ÷ (1 − a))
    tn = 1 − ϵ′, where ϵ′ =   (   )n̄ .
    a + (p − a) (p − a) ÷ (1 − a)
{{p.224}} So that tn approaches the limit unity as n increases, so long as a is not zero.

## §3 (p. 224)

The following is a common type of statistical problem.[^224-1] We are given a series of measurements, or observations, or estimates of the true value of a given quantity; and we wish to determine what function of these measurements will yield us the most probable value of the quantity, on the basis of this evidence. The problem is not determinate unless we have some good ground for making an assumption as to how likely we are in each case to make errors of given magnitudes. But such an assumption, with or without justification, is frequently made.

[^224-1]: The substance of §§ 3–7 has been printed in the Journal of the Royal Statistical Society, vol. lxxiv. p. 323 (February 1911).

The functions of the original measurements which we commonly employ, in order to yield us approximations to the most probable value of the quantity measured, are the various kinds of means or averages—the arithmetic mean, for example, or the median. The relation, which we assume, between errors of different magnitudes and the probabilities that we have made errors of those magnitudes, is called a law of error. Corresponding to each law of error which we might assume, there is some function of the measurements which represents the most probable value of the quantity. The object of the following paragraphs is to discover what laws of error, if we assume them, correspond to each of the simple types of average, and to discover this by means of a systematic method.

## §4 (p. 224)

Let us assume that the real value of the quantity is either b1, . . . br . . . bn, and let ar represent the conclusion that the value is, in fact, br. Further let xr represent the evidence that a measurement has been made of magnitude yr.

If a measurement yp has been made, what is the probability that the real value is bs? The application of the theorem of inverse {{p.225}} probability yields the following result:
    as/xph = (xp/ash · as/h) ÷ (Σ_{r=1}^{r=n} xp/arh · ar/h)
(the number of possible values of the quantity being n), where h stands for any other relevant evidence which we may have, in addition to the fact that a measurement xp has been made.

Next, let us suppose that a number of measurements y1 . . . ym have been made; what is now the probability that the real value is bs? We require the value of as/x1x2 . . . xmh. As before,
    as/x1x2 . . . xmh = (x1 . . . xm/ash · as/h) ÷ (Σ_{r=1}^{r=x} x1 . . . xm/arh · ar/h).

At this point we must introduce the simplifying assumption that, if we knew the real value of the quantity, the different measurements of it would be independent, in the sense that a knowledge of what errors have actually been made in some of the measurements would not affect in any way our estimate of what errors are likely to be made in the others. We assume, in fact, that xr/xp . . . xsarh = xr/arh. This assumption is exceedingly important. It is tantamount to the assumption that our law of error is unchanged throughout the series of observations in question. The general evidence h, that is to say, which justifies our assumption of the particular law of error which we do assume, is of such a character that a knowledge of the actual errors made in a number of measurements, not more numerous than those in question, are absolutely or approximately irrelevant to the question of what form of law we ought to assume. The law of error which we assume will be based, presumably, on an experience of the relative frequency with which errors of different magnitudes have been made under analogous circumstances in the past. The above assumption {{p.226}} will not be justified if the additional experience, which a knowledge of the errors in the new measurements would supply, is sufficiently comprehensive, relatively to our former experience, to be capable of modifying our assumption as to the shape of the law of error, or if it suggests that the circumstances, in which the measurements are being carried out, are not so closely analogous as was originally supposed.

With this assumption, i.e. that x1, etc., are independent of one another relatively to evidence arh, etc., it follows from the ordinary rule for the multiplication of independent probabilities that
    x1 . . . xm/ash = Π_{q=1}^{q=m} xq/ash.
    as/h · Π_{q=1}^{q=m} xq/ash
Hence   as/x1x2 . . . xmh =   [   ].
    Σ̅_̅{̅r̅=̅1̅}̅^̅{̅r̅=̅n̅}̅ Π̅_̅{̅q̅=̅1̅}̅^̅{̅q̅=̅m̅}̅ xq/arh · ar/h

The most probable value of the quantity under measurement, given the m measurements y1, etc.—which is our quaesitum—is therefore that value which makes the above expression a maximum. Since the denominator is the same for all values of bs, we must find the value which makes the numerator a maximum. Let us assume that a1/h = a2/h = . . . = an/h. We assume, that is to say, that we have no reason à priori (i.e. before any measurements have been made) for thinking any one of the possible values of the quantity more likely than any other. We require, therefore, the value of bs which makes the expression Π_{q=1}^{q=m} xq/ash a maximum. Let us denote this value by y.

We can make no further progress without a further assumption. Let us assume that xq/ash—namely, the probability of a measurement yq assuming the real value to be bs—is an algebraic function f of yq and bs, the same function for all values of yq and bs within the limits {{p.227}} of the problem.[^227-1] We assume, that is to say, xq/ash = f(yq, bs), and we have to find the value of bs, namely y, which makes Π_{q=1}^{q=m} f(yq, y) a maximum. Equating to zero the differential coefficient of this expression with respect to y, we have Σ_{q=1}^{q=m} (f′(yq, y)) ÷ (f(yq, y)) = 0,[^227-2] where f′ = df/dy . This equation may be written for brevity in the form
    ′
Σ fq/fq = 0.

[^227-1]: Gauss, in obtaining the normal law of error, made, in effect, the more special assumption that xq/ash is a function of eq only, where eq is the error and eq = bs − yq. We shall find in the sequel that all symmetrical laws of error, such that positive and negative errors of the same absolute magnitude are equally likely, satisfy this condition—the normal law, for example, and the simplest median law. But other laws, such as those which lead to the geometric mean, do not satisfy it.

[^227-2]: Since none of the measurements actually made can be impossible, none of the expressions f(yq, y) can vanish.

If we solve this equation for y, the result gives us the value of the quantity under observation, which is most probable relatively to the measurements we have made.

The act of differentiation assumes that the possible values of y are so numerous and so uniformly distributed within the range in question, that we may, without sensible error, regard them as continuous.

## §5 (p. 227)

This completes the prolegomena of the inquiry. We are now in a position to discover what laws of error correspond to given assumptions respecting the algebraic relation between the measurements and the most probable value of the quantity, and vice versa. For the law of error determines the form of f(yq, y). And the
    ′
form f(yq, y) determines the algebraic relation Σ fq/fq = 0 between the measurements and the most probable value. It may be well to repeat {{p.228}} that f(yq, y) denotes the probability to us that an observer will make a measurement yq in observing a quantity whose true value we know to be y. A law of error tells us what this probability is for all possible values of yq and y within the limits of the problem.

(i.) If the most probable value of the quantity is equal to the arithmetic mean of the measurements, what law of error does this imply?
    ′
    Σ fq/fq = 0 must be equivalent to Σ(y − yq) = 0, since the
    most probable value y must equal 1/m Σ_{q=1}^{q=m} yq.
    ′
    ∴ fq/fq = φ′′(y)(y − yq) where φ′′(y) is some function which
    is not zero and is independent of yq.
Integrating,
    log fq = ∫ φ′′(y)(y − yq) dy + ψ(yq) where ψ(yq) is some
    function independent of y.
    = φ′(y)(y − yq) − φ(y) + ψ(yq).
    ′(y)(y−yq)−φ(y)+ψ(yq)
So that fq = e^φ   .

Any law of error of this type, therefore, leads to the arithmetic mean of the measurements as the most probable value of the quantity measured.

If we put φ(y) = −k^2y^2 and ψ(yq) = −k^2y2/q + log A, we obtain
    2(y−yq)2
    fq = Ae^{−k}   , the form normally assumed,
    2z2
    = Ae^{−kq} ,
where zq is the absolute magnitude of the error in the measurement yq.

This is, clearly, only one amongst a number of possible solutions. But with one additional assumption we can prove that this is the {{p.229}} only law of error which leads to the arithmetic mean. Let us assume that negative and positive errors of the same absolute amount are equally likely.

In this case fq must be of the form Be^{θ(y−yq)2},
    ∴ φ′(y)(y − yq) − φ(y) + ψ(yq) = θ(y − yq)^2.

Differentiating with respect to y,
    φ′′(y) = 2(d) ÷ (d(y − yq)2)θ(y − yq)^2.

But φ′′(y) is, by hypothesis, independent of yq.

∴ (d) ÷ (d(y − yq)2)θ(y − yq)^2 = −k^2 where k is constant; integrating, θ(y − yq)^2 = −k^2(y − yq)^2 +log C and we have fq = Ae^{−k2(y−yq)2} (where A = BC).

(ii.) What is the law of error, if the geometric mean of the measurements leads to the most probable value of the quantity?
    ′

In this case Σ fq/fq = 0 must be equivalent to Π_{q=1}^{q=m} yq = y^m, i.e. to
    log
    Σ   yq/y = 0.
Proceeding as before, we find that the law of error is
    φ′(y) log +^∫   dy+ψ(y )
    yq/y (φ′(y)) ÷ (y)   q
    fq = Ae   .
There is no solution of this which satisfies the condition that negative and positive errors of the same absolute magnitude are equally likely. For we must have
    φ′(y) log yq/y + ∫ (φ′(y)) ÷ (y) dy + ψ(yq) = φ(y − yq)^2
    or φ′′(y) log yq/y = d/dyφ(y − yq)^2,
{{p.230}} which is impossible.

The simplest law of error, which leads to the geometric mean, seems to be obtained by putting φ′(y) = −ky, ψ(yq) = 0. This gives
    ky
fq = A (y/yq) e^{−ky}.

A law of error, which leads to the geometric mean of the observations as the most probable value of the quantity, has been previously discussed by Sir Donald McAlister (Proceedings of the Royal Society, vol. xxix. (1879) p. 365). His investigation depends upon the obvious fact that, if the geometric mean of the observations yields the most probable value of the quantity, the arithmetic mean of the logarithms of the observations must yield the most probable value of the logarithm of the quantity. Hence, if we suppose that the logarithms of the observations obey the normal law of error (which leads to their arithmetic mean as the most probable value of the logarithms of the quantity), we can by substitution find a law of error for the observations themselves which must lead to the geometric mean of them as the most probable value of the quantity itself.

If, as before, the observations are denoted by yq, etc., and the quantity by y, let their logarithms be denoted by lq, etc., and by l. Then, if lq, etc., obey the normal law of error, f(lq, l) = Ae^{−k2(lq−l)2}. Hence the law of error for yq, etc., is determined by
    2(log yq−log y)2
    f(yq, y) = Ae^{−k}
    −k^2(log )^2
    yq/y
    = Ae   ,
and the most probable value of y must, clearly, be the geometric mean of yq, etc.

This is the law of error which was arrived at by Sir Donald McAlister. It can easily be shown that it is a special case of the generalised form which I have given above of all laws of error leading to the geometric mean. For if we put ψ(yq) = −k^2(log yq)^2, and {{p.231}} φ′(y) = 2k^2 log y, we have
    2k^{2log} y log +^∫ 2k^{2logy} dy−k^2(log y )^2
    yq/y   ȳ   q
    fq = Ae
    2 log y log yq−2k2(log y)2+k2(log y)2−k2(log yq)2
    = Ae^{2k}
    −k^2(log yq/y)^2
    = Ae   .

A similar result has been obtained by Professor J. C. Kapteyn.[^231-1] But he is investigating frequency curves, not laws of error, and this result is merely incidental to his main discussion. His method, however, is not unlike a more generalised form of Sir Donald McAlister’s. In order to discover the frequency curve of certain quantities y, he supposes that there are certain other quantities z, functions of the quantities y, which are given by z = F(y), and that the frequency curve of these quantities z is normal. By this device he is enabled in the investigation of a type of skew frequency curve, which is likely to be met with often, to utilise certain statistical constants corresponding to those which have been already calculated for the normal curve.

[^231-1]: Skew Frequency Curves, p. 22, published by the Astronomical Laboratory at Groningen (1903).

In fact the main advantage both of Sir Donald McAlister’s law of error and of Professor Kapteyn’s frequency curves lies in the possibility of adapting without much trouble to unsymmetrical phenomena numerous expressions which have been already calculated for the normal law of error and the normal curve of frequency.[^231-2]

[^231-2]: It may be added that Professor Kapteyn’s monograph brings forward considerations which would be extremely valuable in determining the types of phenomena to which geometric laws of error are likely to be applicable.

This method of proceeding from arithmetic to geometric laws of error is clearly capable of generalisation. We have dealt with the geometric law which can be derived from the normal arithmetic law. Similarly if we start from the simplest geometric law of
{{p.232}}
    k^2y 2
error, namely, fq = A (y/yq) e^{−ky}, we can easily find, by writing log y = l and log yq = lq, the corresponding arithmetic law, namely, fq = Ae^{k2el(l−lq)−k2el}, which is obtained from the generalised arithmetic law by putting φ(l) = k^2e^l and ψ(lq) = 0. And, in general, corresponding to the arithmetic law
    ′(y)(y−yq)−φ(y)+ψ(yq)
    fq = Ae^φ   ,
we have the geometric law
    φ′(z) log +^∫   dz+ψ (z )
    l   zq/z (φl(z)) ÷ (z)   l q
    fq = Ae   ,
where
    y = log z, yq = log zq, ∫ (φ′1(z)) ÷ (z) dz = φ(log z) and ψl(zq) = ψ(log zq).

(iii.) What law of error does the harmonic mean imply?
    ′

In this case, Σ fq/fq = 0 must be equivalent to Σ((1/yq − 1/y) = 0.
    ⟨   ⟩ ∫
    φ′(y) 1/yq−1/y − (φ′(y)) ÷ (y2) dy+ψ(yq)

Proceeding as before, we find that fq = Ae   . A simple form of this is obtained by putting φ′(y) = −k^2y^2 and
    k2/yq(y−yq)^2   −k^2 zq2/yq
    2
ψ(yq) = −k yq. Then fq = Ae   = Ae    . With this law, positive and negative errors of the same absolute magnitude are not equally likely.

(iv.) If the most probable value of the quantity is equal to the median of the measurements, what is the law of error?

The median is usually defined as the measurement which occupies the middle position when the measurements are ranged in order of magnitude. If the number of measurements m is odd, the most probable value of the quantity is the (m + 1) ÷ (2) th, and, if the number is even, all values between the m/2 th and the (m/2 + 1)th are equally {{p.233}} probable amongst themselves and more probable than any other. For the present purpose, however, it is necessary to make use of another property of the median, which was known to Fechner (who first introduced the median into use) but which seldom receives as much attention as it deserves. If y is the median of a number of magnitudes, the sum of the absolute differences (i.e. the difference always reckoned positive) between y and each of the magnitudes is a minimum. The median y of y1y2 . . . ym is found, that is to say, by making Σ_{1}^{m} |yq − y| a minimum where |yq − y| is the difference always reckoned positive between yq and y.

We can now return to the investigation of the law of error corresponding to the median.

Write |y − yq| = zq. Then since Σ_{1}^{m} zq is to be a minimum we must have Σ_{1}^{m} (y − yq) ÷ (zq) = 0. Whence, proceeding as before, we have
    ^∫ (y−yq) ÷ (zq) φ′′(y) dy+ψ(yq).
    fq = Ae

The simplest case of this is obtained by putting
    φ′′(y) = −k^2,
    ψ(yq) = (y − yq) ÷ (zq) k^2yq,
    2|y−yq|   −k2zq
whence   fq = Ae^{−k}   = Ae   .

This satisfies the additional condition that positive and negative errors of equal magnitude are equally likely. Thus in this important respect the median is as satisfactory as the arithmetic mean, and the law of error which leads to it is as simple. It also resembles the normal law in that it is a function of the error only, and not of the magnitude of the measurement as well.

{{p.234}} The median law of error, fq = Ae^{−k2zq}, where zq is the absolute amount of the error always reckoned positive, is of some historical interest, because it was the earliest law of error to be formulated. The first attempt to bring the doctrine of averages into definite relation with the theory of probability and with laws of error was published by Laplace in 1774 in a memoir “sur la probabilité des causes par les événemens.”[^234-1] This memoir was not subsequently incorporated in his Théorie analytique, and does not represent his more mature view. In the Théorie he drops altogether the law tentatively adopted in the memoir, and lays down the main lines of investigation for the next hundred years by the introduction of the normal law of error. The popularity of the normal law, with the arithmetic mean and the method of least squares as its corollaries, has been very largely due to its overwhelming advantages, in comparison with all other laws of error, for the purposes of mathematical development and manipulation. And in addition to these technical advantages, it is probably applicable as a first approximation to a larger and more manageable group of phenomena than any other single law. So powerful a hold indeed did the normal law obtain on the minds of statisticians, that until quite recent times only a few pioneers have seriously considered the possibility of preferring in certain circumstances other means to the arithmetic and other laws of error to the normal. Laplace’s earlier memoir fell, therefore, out of remembrance. But it remains interesting, if only for the fact that a law of error there makes its appearance for the first time.

[^234-1]: Mémoires présentés à l’Académie des Sciences, vol. vi.

Laplace sets himself the problem in a somewhat simplified form: “Déterminer le milieu que l’on doit prendre entre trois observations données d’un même phénomène.” He begins by assuming a law of error z = φ(y), where z is the probability of an error y; and finally, by means of a number of somewhat arbitrary assumptions, arrives at the result φ(y) = m/2e^{−my}. If this formula is to follow from his arguments, {{p.235}} y must denote the absolute error, always taken positive. It is not unlikely that Laplace was led to this result by considerations other than those by which he attempts to justify it.

Laplace, however, did not notice that his law of error led to the median. For, instead of finding the most probable value, which would have led him straight to it, he seeks the “mean of error”—the value, that is to say, which the true value is as likely to fall short of as to exceed. This value is, for the median law, laborious to find and awkward in the result. Laplace works it out correctly for the case where the observations are no more than three.

## §6 (p. 235)

I do not think that it is possible to find by this method a law of error which leads to the mode. But the following general formulae are easily obtained:

(v.) If Σ θ(yq, y) is the law of relation between the measurements and the most probable value∫ of the quantity, then the law of error fq(yq, y) is given by fq = Ae^{θ(yqy)φ}′′^{(y)dy+ψ(yq)}. Since fq lies between 0 and 1, ∫ θ(yqy)φ′′(y) dy + ψ(yq) + log A must be negative for all values of yq and y that are physically possible; and, since the values of yq are between them exhaustive,
    A^∫ θ(y y)φ′′(y) dy+ψ(y )
    Σ e^{qq} = 1,
where the summation is for all terms that can be formed by giving yq every value à priori possible.

(vi.) The most general form of the law of error, when it is assumed that positive and negative errors of the same magnitude are equally probable, is Ae^{−k2f(y−yq)2}, where the most probable value of the quantity is given by the equation
    Σ(y − yq)f ′(y − yq)^2 = 0, where f ′(y − yq)^2 = (d) ÷ (d(y − yq)2)f(y − yq)^2.
The arithmetic mean is a special case of this obtained by putting f(y − yq)^2 = (y − yq)^2; and the median is a special case obtained by putting f(y − yq)^2 = +√((y − yq))^2.

{{p.236}} We can obtain other special cases by putting
    f(y − yq)^2 = (y − yq)^4,
when the law of error is Ae^{−k2(y−yq)2} and the most probable values
    y
are the roots of my^3 − 3y^2(Σ yq + 3y Σ y2/q − Σ 3/q = 0; and by putting f(y − yq)^2 = log(y − yq)^2, when the law of error is (A) ÷ ((y − yq)) = 0 and the most probable values the roots of Σ (1) ÷ ((y − yq)) = 0. In all these cases the law is a function of the error only.

## §7 (p. 236)

These results may be summarised thus. We have assumed:

(a) That we have no reason, before making measurements, for supposing that the quantity we measure is more likely to have any one of its possible values than any other.

(b) That the errors are independent, in the sense that a knowledge of how great an error has been made in one case does not affect our expectation of the probable magnitude of the error in the next.

(c) That the probability of a measurement of given magnitude, when in addition to the à priori evidence the real value of the quantity is supposed known, is an algebraic function of this given magnitude of the measurement and of the real value of the quantity.

(d) That we may regard the series of possible values as continuous, without sensible error.

(e) That the à priori evidence permits us to assume a law of error of the type specified in (c); i.e. that the algebraic function referred to in (c) is known to us à priori.

Subject to these assumptions, we have reached the following conclusions:

(1) The most general form of the law of error is
    ∫ ′′
    fq = Ae^{φ(y)θ(yqy)dy+ψ(yq)},
leading to the equation Σ θ(yqy) = 0, connecting the most probable value and the actual measurements, where y is the most probable value and yq, etc., the measurements.

{{p.237}} (2) Assuming that positive and negative errors of the same absolute magnitude are equally likely, the most general form is fq = Ae^{−k2f(y−yq)2}, leading to the equation Σ(y − yq)f′(y − yq)^2 = 0, where f′z = d/dzfz. Of the special cases to which this form gives rise, the most interesting were   2 2

(3) fq = Ae^{−k2(y−yq)2} = Ae^{−kzq} , where zq = |y − yq|, leading to the arithmetic mean of the measurements as the most probable value of the quantity; and

(4) fq = Ae^{−k2zq}, leading to the median.

(5) The most general form leading to the arithmetic mean is fq = Ae^φ′^{(y−yq)−φ(y)+ψ(yq)}, with the special cases (3), and

(6) fq = Ae^{k2ey(y−yq)−k2ey}.

(7) The most general form leading to the geometric mean is
    φ′(y) log +^∫   dy+ψ(y )
    yq/y (φ′(y)) ÷ (y)   q
fq = Ae   , with the special cases:
    k^2y 2

(8) fq = A (y/yq) e^{−ky}, and
    −k^2(log yq/y)^2

(9) fq = Ae   .

(10) The⟨ most⟩ ∫ general form leading to the harmonic mean is
    φ′(y) 1/yq−1/y − (φ′(y) ÷ (y2) dy+ψ(yq)
fq = Ae   , with the special case
    −k^2((y−yq)2) ÷ (yq)   −k^2 zq2/yq

(11) fq = Ae   = Ae    .

(12) The most general form leading to the median is
    φ′(y)(y−yq) ÷ (zq)+ψ(yq)
    fq = Ae   ,
with the special case (4).

In each of these expressions, fq is the probability of a measurement yq, given that the true value is y.

## §8 (p. 237)

The doctrine of Means and the allied theory of Least Squares comprise so extensive a subject-matter that they cannot be adequately treated except in a volume primarily devoted to them. As, however, they are one of the important practical applications of the theory of {{p.238}} probability, I am unwilling to pass them by entirely; and the following discursive observations, chiefly relating to the Normal Law of Error, will serve, taken in conjunction with the paragraphs immediately preceding, to illustrate the connection between the theories of this treatise and the general treatment of averages.

## §9 (p. 238)

The Claims of the Arithmetic Average.—By definition the arithmetic average of a number of quantities is nothing more than their arithmetic sum divided by their number. But the utility of an average generally consists in our supposed right to substitute, in certain cases, this single measure for the varying measures of which it is a function. Sometimes this requires no justification; the word “average” is in these cases used for the sake of shortness, and merely to summarise a set of facts: as, for instance, when we say that the birth-rate in England is greater than the birth-rate in France.

But there are other cases in which the average makes a more substantial claim to add to our knowledge. After a number of examiners of equal capacity have given varying marks to a candidate for the same paper, it may be thought fair to allow the candidate the average of the different marks allotted: and in general if several estimates of a magnitude have been made, between the accuracy of which we have no reason to discriminate, we often think it reasonable to act as if the true magnitude were the average of the several measurements. Perhaps De Witt, in his report on Annuities to the States General in 1671,[^238-1] was the first to use it scientifically. But as Leibniz points out: “Our peasants have made use of it for a long time according to their natural mathematics. For example, when some inheritance or land is to be sold, they form three bodies of appraisers; these bodies are called Schurzen in Low Saxon, and each body makes an estimate of the property in question. Suppose, then, that the first estimates its value to be 1000 crowns, the second, 1400, the third, 1500; the sum of these three estimates is taken, viz. 3900, and {{p.239}} because they were three bodies, the third, i.e. 1300, is taken as the mean value asked for. This is the axiom: aequalibus aequalia, equal suppositions must have equal consideration.”[^239-1]

[^238-1]: De vardye van de lif-renten na proportie van de los-renten. The Hague, 1671.

[^239-1]: Nouveaux Essais. Engl. transl. p. 540.

But this is a very inadequate axiom. Equal suppositions would have equal consideration, if the three estimates had been multiplied together instead of being added. The truth is that at all times the arithmetic mean has had simplicity to recommend it. It is always easier to add than to multiply. But simplicity is a dangerous criterion: “La nature,” says Fresnel, “ne s’est pas embarassée des difficultés d’analyse, elle n’a évité que la complication des moyens.”

With Laplace and Gauss there began a series of attempts to prove the worth of the arithmetic mean. It was discovered that its use involved the assumption of a particular type of law of error for the à priori probabilities of given errors. It was also found that the assumption of this law led on to a more complicated rule, known as the Method of Least Squares for combining the results of observations which contain more than one doubtful quantity. In spite of a popular belief that, whilst the Arithmetic Mean is intuitively obvious, the Method of Least Squares depends upon doubtful and arbitrary assumptions, it can be demonstrated that the two stand and fall together.[^239-2]

[^239-2]: Venn (Logic of Chance, p. 40) thinks that the Normal Law of Error and the Method of Least Squares “are not only totally distinct things, but they have scarcely even any necessary connection with each other. The Law of Error is the statement of a physical fact. . . . The Method of Least Squares, on the other hand, is not a law at all in the scientific sense of the term. It is simply a rule or direction. . . .”

The analytical theorems of Laplace and Gauss are complicated, but the special assumptions upon which they are based are easily stated.[^239-3] {{p.240}} Gauss supposes (a) that the probability of a given error is a function of the error only and not also of the magnitude of the observation, (b) that the errors are so small that their cubes and higher powers may be neglected. Assumption (a) is arbitrary,[^240-1] and Gauss did not state it explicitly. These two assumptions, together with certain others, lead us to the result. For let φ(z) be the law of error where z is the error, and let us assume, as it always is assumed in these proofs, that φ(z) can be expanded by Maclaurin’s Theorem. Then φ(x) = φ(0)+zφ′(0)+ (z2) ÷ (2!)φ′′(0)+ (z3) ÷ (3!)φ′′′(0)+. . .. It is also supposed that positive and negative errors are equally probable, i.e. φ(z) = φ(−z), so that φ′(0) and φ′′′(0) vanish. Since we may neglect z^4 in comparison with z^2, φz = φ(0) + 1/2z^2φ′′(0). But (neglecting z^4 and higher powers)
    bz^2   bz^2
a + bz^2 = ae ā , so that φ(z) = ae ā .

[^239-3]: For an account of the three principal methods of arriving at the Method of Least Squares and the Arithmetic Mean, see Ellis, Least Squares. Gauss’s first method is in the Theoria Motus, and his second in the Theoria Combinationis Observationum. Laplace’s investigations are in chap. iv. of the second Book of the Théorie analytique. Laplace’s method was improved by Poisson in the Connaissance des temps for 1827 and 1832.

[^240-1]: It does not follow, as G. Hagen argues (Grundzüge der Wahrscheinlichkeitsrechnung, p. 29), that, because a larger error is less probable than a smaller, therefore the probability of a given error is a function of its magnitude only.

Gauss’s proof looks much more complicated than this, but he
    bz^2
obtains the form ae ā by neglecting higher powers of z, so that this expression is really equivalent to a + bz^2. By this approximation he has reduced all the possible laws to an equivalent form.[^240-2] It is true, therefore, that the normal law of error is, to the second power of the error, equivalent to any law of error, which is a function of the error only, and for which positive and negative errors are equally probable. Laplace also introduces assumptions equivalent to these.

[^240-2]: This is pointed out by Bertrand, Calcul des probabilités, p. 267.

While mathematicians have endeavoured to establish the normal law of error and the arithmetic mean as a law of logic, others have claimed for it the testimony of experience and have deemed it a law of nature.[^240-3]

[^240-3]: This is, of course, a very common point of view indeed. Cf. Bertrand, op. cit. p. 183: “Malgré les objections précédentes, la formule de Gauss doit être adoptée. L’observation la confirme: cela doit suffire dans les applications.”

{{p.241}} That this cannot be so, is evident. For suppose that x1x2 . . . xn are a set of observations of an unknown quantity x. Then, by
    x
this principle, x = 1/n Σ r gives the most probable value of x. But suppose we had wished to determine x^2, our observations, assuming that we can multiply correctly, would be x2/1, x2/2 . . . x2/n, and the most
    x    x    x
probable value of x^2 = 1/n Σ 2/r. But (1/n Σ r)^2 = 1/n Σ 2/r. And in
    f    x
general, 1/n Σ (xr) ≠ f(1/n Σ r). Nor is this a consideration which can safely be ignored in practice. For our “observations” are often the result of some manipulation, and the particular shape in which we get them is not necessarily fixed for us. It is not easy to say what the direct observation is. In particular if any such law of sensation, as that enunciated by Fechner, is true (i.e. that sensation varies as the logarithm of the stimulus), the arithmetic mean must break down as a practical rule in all cases where human sensation is part of the instrument by means of which the observations are recorded.[^241-1]

[^241-1]: This was noticed by Galton.

Apart, however, from theoretical refutations, statisticians now recognise that the arithmetic mean and the normal law of error can only be applied to certain special classes of phenomena. Quetelet[^241-2] was, I think, the first to point this out. In England, Galton drew attention to the fact many years ago, and Professor Pearson[^241-3] has shown “that the Gaussian-Laplace normal distribution is very far from being a general law of frequency distribution either for errors of observation or for the distribution of deviations from type such as occur in organic populations. . . . It is not even approximately correct, for example, in the distribution of barometric variations, of grades of {{p.242}} fertility and incidence of disease.”

[^241-2]: E.g. Letters on the Theory of Probabilities, p. 114.

[^241-3]: On “Errors of Judgment, etc.,” Phil. Trans. A, vol. cxcviii. pp. 235–299. The following quotation is from his memoir On the General Theory of Skew Correlation and Non-linear Regression, where further references are given.

The Arithmetic Mean occupies, therefore, no unique position; and it is worth while, from the point of view of probability, to discuss the properties of other possible means and laws of error, as, for example, on the lines indicated in the earlier part of this chapter.

## §10 (p. 242)

The Method of Least Squares.—The problem, to which this method is applied, is no more than the application of the same considerations, as those which we have just been discussing, to cases where the relation between the observed measurements and the quantity whose most probable value we require, involves more than one unknown.

Owing to the surprising character of its conclusions, if they could be accepted as universally valid, and to the obscurity of the mathematical fabric that has been reared on and about it, this method has been surrounded by an unnecessary air of mystery. It is true that in recent times scepticism has grown at the expense of mystery. It is also true that just views have been held by individuals for sixty years past, notably by Leslie Ellis. But the old mistakes are not always corrected in the current text-books, and even so useful and generally used a treatise on Least Squares, as Professor Mansfield Merriman’s, opens with a series of very fallacious statements.

The controversial side of the Method of Least Squares is purely logical; in the later developments there is much elaborate mathematics of whose correctness no one is in doubt. What it is important to state with the utmost possible clearness is the precise assumptions on which the mathematics is based; when these assumptions have been set forth, it remains to determine their applicability in particular cases.

In dealing with averages we supposed ourselves to be presented with a number of direct observations of some quantity which it is desired to determine. But it is obvious that direct observations will be in many cases either impracticable or inconvenient; and our natural course will be to measure certain other quantities which we know {{p.243}} to bear fixed and invariable relations to the unknowns we wish to determine. In surveying, for instance, or in astronomy, we constantly prefer to take measurements of angles or distances in which we are not interested for their own sakes, but which bear known geometrical relationships to the set of ultimate unknowns.

If we wish to determine the most probable values of a set of unknowns x1, x2, . . . xr, instead of obtaining a number of sets of direct observations of each, we may obtain a number of equations of observation of the following type:
    a1x1 + a2x2 + . . . + arxr = V1,
    b1x1 + b2x2 + . . . + brxr = V2,
    .   .   .   .   .   .   .
    k1x1 + k2x2 + . . . + krxr = Vn,
where V1, etc., are the quantities directly observed, and the a′s, b′s, etc., are supposed known (n > r).

We have in such a case n equations to determine r unknowns, and since the observations are likely to be inexact, there may be no precise solution whatever. In these circumstances we wish to know the most probable set of values of the x’s warranted by these observations.

The problem is precisely similar in kind to that dealt with by averages and differs only in the degree of its complexity. It is the problem of finding the most probable solution of such a set of discrepant equations of observation that the Method of Least Squares claims to solve.

By 1750 the astronomers were obtaining such equations of observation in the course of their investigations, and the question arose as to the proper manner of their solution. Boscovich in Italy, Mayer and Lambert in Germany, Laplace in France, Euler in Russia, and Simpson in England proposed different methods of solution. Simpson, in 1757, was the first to introduce, by way of simplification, the assumption or axiom that positive and negative errors are equally {{p.244}} probable.[^244-1] The Method of Least Squares was first definitely stated by Legendre in 1805, who proposed it as an advantageous method of adjusting observations. This was soon followed by the ‘proofs’ of Laplace and Gauss. But it is easily shown that these proofs involve the normal law of error y = ke^{−k2x2}, and the theory of Least Squares simply develops the mathematical results of applying to equations of observation, which involve more than one unknown, that law of error which leads to the Arithmetic Mean in the case of a single unknown.

[^244-1]: See Merriman’s Method of Least Squares, p. 181, for an historical sketch, from which the above is taken. In 1877 Merriman published in the Transactions of the Connecticut Academy a list of writings relating to the Method of Least Squares and the theory of accidental errors of observation, which comprised 408 titles—classified as 313 memoirs, 72 books, 23 parts of books.

## §11 (p. 244)

The Weighting of Averages.—It is necessary to recur to the distinction made at the beginning of § 9 between the two types to which our average, or, as it is generally termed in social inquiries, our index number, may belong. The average or index number may simply summarise a set of facts and give us the actual value of a composite quantity, as, for example, the index number of the cost of living. In such cases the composite quantity, in which we are interested, need not contain precisely the same number of units of each of the elementary quantities of which it is composed, so that the ‘weights,’ which denote the numbers of each elementary quantity appropriate to the composite quantity, are part of the definition of the composite quantity, and can no more be dispensed with than the magnitudes of the elementary quantities themselves. Nor in such cases is the rejection of discordant observations permissible; if, that is to say, some of the elementary quantities are subject to much wider variation, or to variations of a different type than the majority, that is no reason for rejecting them.

On the other hand, the individual items, out of which the average is composed, may each be indications or approximate estimates of some one single quantity; and the average, instead of representing {{p.245}} the measure of a composite quantity, may be selected as furnishing the most probable value of the single quantity, given, as evidence of its magnitude, the values of the various terms which make up the average.

If this is the character of our average, the problem of weighting depends upon what we know about the individual observations or samples or indications, out of which our average is to be built up. The units in question may be known to differ in respects relevant to the probable value of the quaesitum. Thus there may be reasons, quite apart from the actual results of the individual observations or samples, for trusting some of them more than others. Our knowledge may indicate to us, in fact, that the constants of the laws of error appropriate to the several instances, even if the type of the law can be assumed to be constant, should be varied according to the data we possess about each. It may also indicate to us that the condition of independence between the instances, which the method of averages presumes, is imperfectly satisfied, and consequently that our mode of combining the instances in an average must be modified accordingly.

Some modern statisticians, who, really influenced perhaps by practical considerations, have been inclined to deprecate the importance of weighting on theoretical grounds, have not always been quite clear what kind of average they supposed themselves to be dealing with. In particular, discussions of the question of weighting in connection with index numbers of the value of money have suffered from this confusion. It has not been clear whether such index numbers really represent measures of a composite quantity or whether they are probable estimates of the value of a single quantity formed by combining a number of independent approximations towards the value of this quantity. The original Jevonian conception of an index number of the value of money was decidedly of the latter type. Modern work on the subject has been increasingly dominated by the other conception. A discussion of where the truth lies would lead me too far into the field of a subject-matter alien to that of this treatise.

{{p.246}} Theoretical arguments against weighting have sometimes been based on the fact that to weight the items of the average in an irrelevant manner, or, as it is generally expressed, in a random manner, is not likely, provided the variations between the weights are small compared with the variations between the items, to affect the result very much. But why should any one wish to weight an average “at random”? Such observations overlook the real meaning and significance of weights. They are probably inspired by the fact that a superficial treatment of statistics would sometimes lead to the introduction of weights which are irrelevant. In drawing a conclusion, for example, from the vital statistics of various towns, the figures of population for the different towns may or may not be relevant to our conclusion. It depends on the character of the argument. If they are relevant, it may be right to employ them as weights. If they are irrelevant, it must be wrong and unnecessary to do so. The fact that what is a more important article of consumption than pins may, on certain assumptions, be irrelevant to the usefulness of variations in the price of each article as indications of variation in the value of money. With other assumptions, it may be extremely relevant. Or again, we may know that observations with a particular instrument tend to be too large and must, therefore, be weighted down. It is contrary both to theory and to common sense to suppose that the possession of information as to the relative reliability of different statistics is not useful. There is no place, therefore, in my judgment, for a generalised argument as to the propriety or impropriety of weighting an average.

It should be added that, where we seek to build up an index number of a conception, which is quantitative but is not itself numerically measurable in any defined or unambiguous sense, by combining a number of numerical quantities, which, while they do not measure our quaesitum are nevertheless indications of its quantitative variations and tend to fluctuate in the same sense, as, for example, by means of what are sometimes called economic barometers of the state of business, or the prosperity of the country or the like, some {{p.247}} very confusing questions can arise both as to what sort of a thing our resulting index really is, and as to the mode of compilation appropriate to it.

These confusing questions always arise when, instead of measuring a quantity directly, we seek an index to fluctuations in its magnitude by combining in an average the fluctuations of a series of magnitudes, which are, each of them in a different way, to some extent (but only to some extent), correlated with fluctuations in our quaesitum. I must not burden this book with a discussion of the problems of Index Numbers. But I venture to think that they would be sooner cleared up if the natures and purposes of differing index numbers were more sharply distinguished—those, namely, which are simply descriptive of a composite commodity, those which seek to combine results differing from one another in a way analogous to the variations of an instrument of precision, and those which combine results, not of the quaesitum itself, but of various other quantities, variations in which are partly due to variations in the quaesitum, but which we well know to be also due to other distinguishable influences. Index numbers of the third type are often treated by methods and arguments only appropriate to those of the second type.

## §12 (p. 247)

The Rejection of Discordant Observations.—This differs from the problem just discussed, because we have supposed so far that our system of weighting is determined by data which we possess prior to and apart from our knowledge of the actual magnitude of the items of our average. The principle of the rejection of discordant observations comes in when it is argued that, if one or more of our observations show great discrepancies from the results of the greater number, these ought to be partly or entirely neglected in striking the average, even if there is no reason, except their discrepancy from the rest, for attributing less weight to them than to the others. By some this practice has been thought to be in accordance with the dictates of common sense; by others it is denounced as savouring even of {{p.248}} forgery.[^248-1]

[^248-1]: E.g. G. Hagen’s Grundzüge der Wahrscheinlichkeitsrechnung, p. 63: “Die Täuschung, die man durch Verschweigen von Messungen begeht, lässt sich eben so wenig entschuldigen, als wenn man Messungen fälschen oder fingiren wollte.”

This controversy, like so many others in Probability, is due to a failure to understand the meaning of ‘independence.’ The mathematics of the orthodox theory of Averages and Least Squares depend, as we have seen, upon the assumption that the observations are ‘independent’; but this has sometimes been interpreted to mean a physical independence. In point of fact, the theory requires that the observations shall be independent, in the sense that a knowledge of the result of some does not affect the probability that the others, when known, involve given errors.

Clearly there may be initial data in relation to which this supposition is entirely or approximately accurate. But in many cases the assumption will be inadmissible. A knowledge of the results of a number of observations may lead us to modify our opinion as to the relative reliabilities of others.

The question, whether or not discordant observations should be specially weighted down, turns, therefore, upon the nature of the preliminary data by which we have been guided in initially adopting a particular law of error as appropriate to the observations. If the observations are, relevant to these data, strictly ‘independent,’ in the sense required for probability, then rejection is not permissible. But if this condition is not fulfilled, a bias against discordant observations may be well justified.
