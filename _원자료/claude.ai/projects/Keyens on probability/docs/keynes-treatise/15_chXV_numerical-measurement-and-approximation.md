---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part II. Fundamental Theorems"
chapter: "Chapter XV"
title: "Numerical Measurement and Approximation of Probabilities"
pages: "180–187"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "193–200"
sections: 7
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part II. Fundamental Theorems*

# Chapter XV. Numerical Measurement and Approximation of Probabilities

## §1 (p. 180)

{{p.180}} The possibility of numerical measurement, mentioned at the close of Chapter III., arises out of the Addition Theorem (24.1). In introducing the definitions and the axiom, which are required in order to make the convention of numerical measurement operative, we may appear, as in the case of the original definitions of Addition and Multiplication, to be arguing in an artificial way. This appearance is due, here as in Chapter XII., to our having given the names of addition and multiplication to certain processes of compounding probabilities in advance of postulating that the processes in question have the properties commonly associated with these names. As common sense is hasty to impute the properties as soon as it hears the names, it may overlook the necessity of formally introducing them.

## §2 (p. 180)

The definitions and the axiom which are needed in order to give a meaning to numerical measurement are the following:—

XVII. a/h + {a/h + [a/h + (a/h + . . . r terms)]} = r · a/h. Def.

XVIII. If r · a/h = b/f , then a/h = 1/r · b/f .   Def.

XIX. If b/f = q · c/g, then 1/r · b/f = q/r c/g.   Def. Thus if b/h = a/h + a/h + . . . to r terms, then the probability b/h is said to be r times the probability a/h; hence if ab/h = 0 and a/h = b/h, the probability (a + b)/h is twice the probability a/h. If a and b are exhaustive as well as exclusive alternatives relatively to h, so that (a + b)/h = 1, since we take the relation of certainty as our unit, then a/h = b/h = 1/2 .

{{p.181}} We also need the following axiom postulating the existence of relations of probability corresponding to all proper fractions:

(vii.) If q and r are any finite integers and q < r, there exists a relation of probability which can be expressed, by means of the convention of the foregoing definitions, as q/r .

## §3 (p. 181)

From these axioms and definitions combined with those of Chapter XII., it is easy to show (certainty being represented by unity and impossibility by zero) that we can manipulate according to the ordinary laws of arithmetic the “numbers” which by means of a special convention we have thus introduced to represent probabilities. Of the kind of proofs necessary for the complete demonstration of this the following is given as an example:

(50)   If a/f = 1/m and b/h = 1/n , a/f + b/h = (m + n) ÷ (mn) .

Let the probability 1/mn = P, which exists by (vii.),
then   n · P = 1/m = a/f   by (XIX.), and   m · P = 1/n = b/h,
    ∴ a/f + b/h = n · P + m · P, if this probability exists,
    = P + P . . . to n terms + P + P . . . to m terms,
    = P + P . . . to m + n terms,
    = (m + n)P = (m + n) ÷ (mn)   by (XIX.).
This probability exists in virtue of (vii.).

## §4 (p. 181)

Many probabilities—in fact all those which are equal to the probability of some other argument which has the same premiss {{p.182}} and of which the conclusion is incompatible with that of the original argument—are numerically measurable in the sense that there is some other probability with which they are comparable in the manner described above. But they are not numerically measurable in the most usual sense, unless the probability with which they are thus comparable is the relation of certainty. The conditions under which a probability a/h is numerically measurable and equal to q/r are easily seen. It is necessary that there should exist probabilities a1/h1, a2/h2 . . ., aq/hq . . . ar/hr, such that
    a1/h1 = a2/h2 = . . . = aq/hq = . . . = ar/hr,
    a/h = Σ_{1}^{q} as/hs, and Σ_{1}^{r} as/hs = 1.

If a/h = q1/r1 and b/h = q2/r2 , it follows from (32) that ab/h = q1q2/r1r2 only if a/h and b/h are independent arguments. Unless, therefore, we are dealing with independent arguments, we cannot apply detailed mathematical reasoning even when the individual probabilities are numerically measurable. The greater part of mathematical probability, therefore, is concerned with arguments which are both independent and numerically measurable.

## §5 (p. 182)

It is evident that the cases in which exact numerical measurement is possible are a very limited class, generally dependent on evidence which warrants a judgment of equiprobability by an application of the Principle of Indifference. The fuller the evidence upon which we rely, the less likely is it to be perfectly symmetrical in its bearing on the various alternatives, and the more likely is it to contain some piece of relevant information favouring one of them. In actual reasoning, therefore, perfectly equal probabilities, and hence exact numerical measures, will occur comparatively seldom.

The sphere of inexact numerical comparison is not, however, quite so limited. Many probabilities, which are incapable of numerical measurement, can be placed nevertheless between numerical limits. {{p.183}} And by taking particular non-numerical probabilities as standards a great number of comparisons or approximate measurements become possible. If we can place a probability in an order of magnitude with some standard probability, we can obtain its approximate measure by comparison.

This method is frequently adopted in common discourse. When we ask how probable something is, we often put our question in the form—Is it more or less probable than so and so?—where ‘so and so’ is some comparable and better known probability. We may thus obtain information in cases where it would be impossible to ascribe any number to the probability in question. Darwin was giving a numerical limit to a non-numerical probability when he said of a conversation with Lyell that he thought it no more likely that he should be right in nearly all points than that he should toss up a penny and get heads twenty times running.[^183-1] Similar cases and others also, where the probability which is taken as the standard of comparison is itself non-numerical and not, as in Darwin’s instance, a numerical one, will readily occur to the reader.

[^183-1]: Life and Letters, vol. ii. p. 240.

A specially important case of approximate comparison is that of ‘practical certainty.’ This differs from logical certainty since its contradictory is not impossible, but we are in practice completely satisfied with any probability which approaches such a limit. The phrase has naturally not been used with complete precision; but in its most useful sense it is essentially non-numerical—we cannot measure practical certainty in terms of logical certainty. We can only explain how great practical certainty is by giving instances. We may say, for instance, that it is measured by the probability of the sun’s rising to-morrow. The type which we shall be most likely to take will be that of a well-verified induction.

## §6 (p. 183)

Most of such comparisons must be based on the principles of Chapter V. It is possible, however, to develop a systematic method of {{p.184}} approximation which may be occasionally useful. The theorems given below are chiefly suggested by some work of Boole’s. His theorems were introduced for a different purpose, and he does not seem to have realised this interesting application of them; but analytically his problem is identical with that of approximation.[^184-1] This method of approximation is also substantially the same analytically as that dealt with by Mr. Yule under the heading of Consistence.[^184-2]

[^184-1]: In Boole’s Calculus we are apt to be left with an equation of the second or of an even higher degree from which to derive the probability of the conclusion; and Boole introduced these methods in order to determine which of the several roots of his equation should be taken as giving the true solution of the problem in probability. In each case he shows that that root must be chosen which lies between certain limits, and that only one root satisfies this condition. The general theory to be applied in such cases is expounded by him in Chapter XIX. of The Laws of Thought, which is entitled “On Statistical Conditions.” But the solution given in that chapter is awkward and unsatisfactory, and he subsequently published a much better method in the Philosophical Magazine for 1854 (4th series, vol. viii.) under the title “On the Conditions by which the Solutions of Questions in the Theory of Probabilities are limited.”

[^184-2]: Theory of Statistics, chap. ii.

(51) xy/h always lies between[^184-3] x/h and x/h + y/h − 1 and between y/h and x/h + y/h − 1.
For   xy/h = x/h − xȳ/h   by (24.2),
    = x/h − ȳ/h · x/ȳ/h   by X.
Now   x/ȳh lies between 0 and 1   by (2) and (3),
    ∴ xy/h lies between x/h and x/h − ȳ/h,
    i.e. between x/h and x/h + y/h − 1.
As xy/h ≮ 0, the above limits may be replaced by x/h and 0, if x/h + y/h − 1 < 0.

[^184-3]: In this and the following theorems the term ‘between’ includes the limits.

{{p.185}} We thus have limits for xy/h, close enough sometimes to be useful, which are available whether or not x/h and y/h are independent arguments. For instance, if y/h is nearly certain, xy/h = x/h nearly, quite independently of whether or not x and y are independent. This is obvious; but it is useful to have a simple and general formula for all such cases.

(52) x1x2 . . . xn+1/h is always greater than Σ_{1}^{n+1} xr/h − n.
For by (51) x1x2 . . . xn+1/h > x1x2 . . . xn/h + xn+1/h − 1
    > x1x2 . . . xn−1/h + xn/h + xn+1/h − 2,
and so on.

(53) xy/h + x̄ȳ/h is always less than x/h − y/h + 1, and less than y/h − x/h + 1.
For as in (51)   xy/h = x/h − xȳ/h
and   x̄ȳ/h = ȳ/h − xȳ/h,
    ∴ xy/h + x̄ȳ/h = x/h − y/h + 1 − 2xȳ/h,
whence the required result.

(54) xy/h − x̄ȳ/h = x/h + y/h − 1.

This proposition, which follows immediately from the above, is really out of place here. But its close connection with conclusions (51) and (53) is obvious. It is slightly unexpected, perhaps, that the difference of the probabilities that both of two events will occur and that neither of them will, is independent of whether or not the events themselves are independent.

## §7 (p. 185)

It is not worth while to work out more of these results here. Some less systematic approximations of the same kind are given in the course of the solutions in Chapter XVII.

In seeking to compare the degree of one probability with that of another we may desire to get rid of one of the terms, on account of its not being comparable with any of our standard probabilities. Thus {{p.186}} our object in general is to eliminate a given symbol of quantity from a set of equations or inequations. If, for instance, we are to obtain numerical limits within which our probability must lie, we must eliminate from the result those probabilities which are non-numerical. This is the general problem for solution.

(55) A general method of solving these problems when we can throw our equations into a linear shape so far as all symbols of probability are concerned, is best shown in the following example:—

Suppose we have   λ + ν = a   (i.)
    λ + σ = b   (ii.)
    λ + ν + σ = c   (iii.)
    λ + μ + ν + ρ = d   (iv.)
    λ + μ + σ + τ = e   (v.)
    λ + μ + ν + ρ + σ + τ + υ = 1   (vi.)
where λ, μ, ν , ρ, σ, τ , υ represent probabilities which are to be eliminated, and limits are to be found for c in terms of the standard probabilities a, b, d, e, and 1.

λ, μ, etc., must all lie between 0 and 1.

From (i.) and (iii.) σ = c − a; from (ii.) and (iii.) ν = c − b.

From (i.), (ii.), and (iii.) λ = a + b − c,
whence
    c − a ⪖ 0, c − b ⪖ 0, a + b − c ⪖ 0,
substituting for σ, ν , λ in (iv.), (v.), and (vi.)
    μ + ρ = d − a, μ + τ = e − b, μ + ρ + τ + υ = 1 − c,
whence

ρ = d − a − μ, τ = e − b − μ, υ = 1 − c − d + a − e + b + μ,
    ∴ d − a − μ ⪖ 0, e − b − μ ⪖ 0, 1 − c − d + a − e + b + μ ⪖ 0.
{{p.187}} We have still to eliminate μ.
    μ ⪖ d − a, μ ⪖ e − b,
    μ ⪖ c + d + e − a − b − 1,
    ∴ d − a ⪖ c + d + e − a − b − 1 and e − b ⪖ c + d + e − a − b − 1.
Hence we have:

Upper limits of c:—b + 1 − e, a + 1 − d, a + b (whichever is least),

Lower limits of c:—a, b (whichever is greatest).

This example, which is only slightly modified from one given by Boole, represents the actual conditions of a well-known problem in probability.
