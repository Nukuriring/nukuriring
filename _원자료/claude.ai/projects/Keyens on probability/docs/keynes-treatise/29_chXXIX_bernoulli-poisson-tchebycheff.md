---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part V. The Foundations of Statistical Inference"
chapter: "Chapter XXIX"
title: "The Use of à priori Probabilities for the Prediction of Statistical Frequency—the Theorems of Bernoulli, Poisson, and Tchebycheff"
pages: "382–417"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "395–430"
sections: 19
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part V. The Foundations of Statistical Inference*

# Chapter XXIX. The Use of à priori Probabilities for the Prediction of Statistical Frequency—the Theorems of Bernoulli, Poisson, and Tchebycheff

> Hoc igitur est illud Problema, quod evulgandum hoc loco proposui, postquam jam per vicennium pressi, et cujus tum novitas, tum summa utilitas cum pari conjuncta difficultate omnibus reliquis hujus doctrinae capitibus pondus et pretium superaddere potest.—Bernoulli.[^382-1]

[^382-1]: Ars Conjectandi, p. 227.

## §1 (p. 382)

{{p.382}} Bernoulli’s Theorem is generally regarded as the central theorem of statistical probability. It embodies the first attempt to deduce the measures of statistical frequencies from the measures of individual probabilities, and it is a sufficient fruit of the twenty years which Bernoulli alleges that he spent in reaching his result, if out of it the conception first arose of general laws amongst masses of phenomena, in spite of the uncertainty of each particular case. But, as we shall see, the theorem is only valid subject to stricter qualifications, than have always been remembered, and in conditions which are the exception, not the rule.

The problem, to be discussed in this chapter, is as follows: Given a series of occasions, the probability[^382-2] of the occurrence of a certain event at each of which is known relative to certain initial data h, on what proportion of these occasions may we reasonably anticipate the occurrence of the event? Given, that is to say, the individual probability of each of a series of events à priori, what statistical frequency of occurrence of these events is to be anticipated over the whole series? Beginning with Bernoulli’s Theorem, we will consider the various solutions of this problem which have been propounded, {{p.383}} and endeavour to determine the proper limits within which each method has validity.

[^382-2]: In the simplest cases, dealt with by Bernoulli, these probabilities are all supposed equal.

## §2 (p. 383)

Bernoulli’s Theorem in its simplest form is as follows: If the probability of an event’s occurrence under certain conditions is p, then, if these conditions are present on m occasions, the most probable number of the event’s occurrences is mp (or the nearest integer to this), i.e. the most probable proportion of its occurrences to the total number of occasions is p: further, the probability that the proportion of the event’s occurrences will diverge from the most probable proportion p by less than a given amount b, increases as m increases, the value of this probability being calculable by a process of approximation.

The probability of the event’s occurring n times and failing m − n times out of the m occasions is (subject to certain conditions to be elucidated later) p^nq^{m−n} multiplied by the coefficient of this expression in the expansion of (p + q)^m, where p + q = 1. If we write n = mp − h, this term is (m!) ÷ ((mp − h)!(mq + h)!)p^nq^{m−n}. It is easily shown that this is a maximum when h = 0, i.e. when n = mp (or the nearest integer to this, where mp is not integral). This result constitutes the first part of Bernoulli’s Theorem.

For the second part of the theorem some method of approximation is required. Provided that m is large, we can simplify the expression (m!) ÷ ((mp − h)!(mq + h)!)p^nq^{m−n} by means of Stirling’s Theorem, and obtain as its approximate value
    −h2/2mpq
    √
    1/2πmpq̄
    e
As before, this is a maximum when h = 0, i.e. when n = mp.

It is possible, of course, by more complicated formulae to obtain closer approximations than this.[^383-1] But there is an objection, which {{p.384}} can be raised to this approximation, quite distinct from the fact that it does not furnish a result correct to as many places of decimals as it might. This is, that the approximation is independent of the sign of h, whereas the original expression is not thus independent. That is to say, the approximation implies a symmetrical distribution for different values of h about the value for h = 0; while the expression under approximation is unsymmetrical. It is easily seen that this want of symmetry is appreciable unless mpq is large. We ought, therefore, to have laid it down as a condition of our approximation, not only that m must be large, but also that mpq must be large. Unlike most of my criticisms, this is a mathematical, rather than a logical point. I recur to it in § 15.

[^383-1]: See, e.g., Bowley, Elements of Statistics, p. 298. The objection about to be raised does not apply to these closer approximations.

“Par une fiction qui rendra les calculs plus faciles” (to quote Bertrand), we now replace the integer h by a continuous variable z and argue that the probability that the amount of the divergence from the most probable value mp will lie between z and z + dz, is
    −z2/2mpq dz.
    √
    1/2πmpq̄
    e
This ‘fiction’ will do no harm so long as it is remembered that we are now dealing with a particular kind of approximation. The probability that the divergence h from the most probable value mp will be less than some given quantity a is, therefore,
    +a
    ∫   −z2/2mpq dz.
    √   e
    1/2πmpq̄
    −a
If we put √   = t, this is equal to
    z/2mpq̄
    ∫ √a/2mpq̄ 2
    √(2) ÷ ((π))   e^{−t} dt.
    0
{{p.385}}
    √
Thus, if we write a = (2mpq)γ , the probability[^385-1] that the number of occurrences will lie between
    mp + √(2mpq)γ and mp − √(2mpq)γ
    γ 2
is measured by[^385-2] √(2) ÷ ((π)) ∫ e^{−t} dt. This same expression measures the
    0
probability that the proportion of occurrences will lie between
    √   √
    p + 2pq/mγ and p − 2pq/mγ.
    t 2
The different values of the integral √(2) ÷ ((π)) ∫ e^{−t} dt = Θ(t) are given in
    0
tables.[^385-3]

[^385-1]: The replacement of the integer h by the continuous variable z may render the formula rather deceptive. It is certain, for example, that the error does not lie between h and h + 1.

[^385-2]: The above proof follows the general lines of Bertrand’s (Calcul des probabilités, chap. iv.). Some writers, using rather more precision, give the result as   γ   2 √(2) ÷ ((π)) ∫ e^{−t2} dt + √(−γ) ÷ (e/2πmpq) e/2πmpq 0 (e.g. Laplace, by the use of Euler’s Theorem, and more recently Czuber, Wahrscheinlichkeitsrechnung, vol. i. p. 121). As the whole formula is approximate, the simpler expression given in the text is probably not less satisfactory in practice. See also Czuber, Entwicklung, pp. 76, 77, and Eggenberger, Beiträge zur Darstellung des Bernoullischen Theorems.

[^385-3]: A list of the principal tables is given by Czuber, loc. cit. vol. i. p. 122.

The probability that the proportion of occurrences√   will lie between given limits varies with the magnitude of 2pq/m , and this expression is sometimes used, therefore, to measure the ‘precision’ of the series. Given the à priori probabilities, the precision varies inversely with the square root of the number of instances. Thus, while the probability that the absolute divergence will be less than a {{p.386}} given amount a decreases, the probability that the corresponding proportionate divergence (i.e. the absolute divergence divided by the number of instances) will be less than a given amount b, increases, as the number of instances increases. This completes the second part of Bernoulli’s Theorem.

## §3 (p. 386)

Bernoulli himself was not acquainted with Stirling’s theorem, and his proof differs a good deal from the proof outlined in § 2. His final enunciation of the theorem is as follows: If in each of a given series of experiments there are r contingencies favourable to a given event out of a total number of contingencies t, so that r/t is the probability of the event at each experiment, then, given any degree of probability c, it is possible to make such a number of experiments that the probability, that the proportionate number of the event’s occurrences will lie between (r + 1) ÷ (t) and (r − 1) ÷ (t) , is greater than c.[^386-1]

[^386-1]: Ars Conjectandi, p. 236 (I have translated freely). There is a brief account of Bernoulli’s proof in Todhunter’s History, pp. 71, 72. The problem is dealt with by Laplace, Théorie analytique, livre ii. chap. iii. For an account of Laplace’s proof see Todhunter’s History, pp. 548–553.

## §4 (p. 386)

We seem, therefore, to have proved that, if the à priori probability of an event under certain conditions is p, the proportion of times most probable à priori for the event’s occurrence on a series of occasions where the conditions are satisfied is also p, and that if the series is a long one the proportion is very unlikely to differ widely from p. This amounts to the principle which Ellis[^386-2] and Venn have employed as the defining axiom of probability, save that if the series is ‘long enough’ the proportion, according to them, will certainly {{p.387}} be p. Laplace[^387-1] believed that the theorem afforded a demonstration of a general law of nature, and in his second edition published in 1814 he replaces[^387-2] the eloquent dedication, A Napoléon-le-Grand, which prefaces the edition of 1812, by an explanation that Bernoulli’s Theorem must always bring about the eventual downfall of a great power which, drunk with the love of conquest, aspires to a universal domination,—“c’est encore un résultat du calcul des probabilités, confirmé par de nombreuses et funestes expériences.”

[^386-2]: On the Foundation of the Theory of Probabilities: “If the probability of a given event be correctly determined, the event will on a long run of trials tend to recur with frequency proportional to this probability. This is generally proved mathematically. It seems to me to be true à priori. . . . I have been unable to sever the judgment that one event is more likely to happen than another from the belief that in the long run it will occur more frequently.”

[^387-1]: Essai philosophique, p. 53: “On peut tirer du théorème précédent cette conséquence qui doit être regardée comme une loi générale, savoir, que les rapports des effets de la nature, sont à fort peu près constans, quand ces effets sont considérés en grand nombre.”

[^387-2]: Introduction, pp. liii, liv.

## §5 (p. 387)

Such is the famous Theorem of Bernoulli which some have believed[^387-3] to have a universal validity and to be applicable to all ‘properly calculated’ probabilities. Yet the theorem exhibits algebraical rather than logical insight. And, for reasons about to be given, it will have to be conceded that it is only true of a special class of cases and requires conditions, before it can be legitimately applied, of which the fulfilment is rather the exception than the rule. For consider the case of a coin of which it is given that the two faces are either both heads or both tails: at every toss, provided that the results of the other tosses are unknown, the probability of heads is 1/2 and the probability of tails is 1/2 ; yet the probability of m heads and m tails in 2m tosses is zero, and it is certain à priori that there will be either 2m heads or none. Clearly Bernoulli’s Theorem is inapplicable to such a case. And this is but an extreme case of a normal condition.

[^387-3]: Even by Mr. Bradley, Principles of Logic, p. 214. After criticising Venn’s view he adds: “It is false that the chances must be realised in a series. It is, however, true that they most probably will be, and true again that this probability is increased, the greater the length we give to our series.”

For the first stage in the proof of the theorem assumes that, if p is the probability of one occurrence, p^r is the probability of r occurrences {{p.388}} running. Our discussion of the theorems of multiplication will have shown how considerable an assumption this involves. It assumes that a knowledge of the fact that the event has occurred on every one of the first r − 1 occasions does not in any degree affect the probability of its occurrence on the rth. Thus Bernoulli’s Theorem is only valid if our initial data are of such a character that additional knowledge, as to the proportion of failures and successes in one part of a series of cases is altogether irrelevant to our expectation as to the proportion in another part. If, for example, the initial probability of the occurrence of an event under certain circumstances is one in a million, we may only apply Bernoulli’s Theorem to evaluate our expectation over a million trials, if our original data are of such a character that, even after the occurrence of the event in every one of the first million trials, the probability in the light of this additional knowledge that the event will occur on the next occasion is still no more than one in a million.

Such a condition is very seldom fulfilled. If our initial probability is partly founded upon experience, it is clear that it is liable to modification in the light of further experience. It is, in fact, difficult to give a concrete instance of a case in which the conditions for the application of Bernoulli’s Theorem are completely fulfilled. At the best we are dealing in practice with a good approximation, and can assert that no realised series of moderate length can much affectγ our initial probability. If we wish to employ the expression √(2) ÷ ((π)) ∫ e^{−t2}dt
    0
we are in a worse position. For this is an approximate formula which requires for its validity that the series should be long; whilst it is precisely in this event, as we have seen above, that the use of Bernoulli’s Theorem is more than usually likely to be illegitimate.

## §6 (p. 388)

The conditions, which have been described above, can be expressed precisely as follows:

Let mxn represent the statement that the event has occurred on m out of n occasions and has not occurred on the others; and {{p.389}} let 1x1/h = p, where h represents our à priori data, so that p is the à priori probability of the event in question. Bernoulli’s Theorem then requires a series of conditions, of which the following is typical: m+1xn+1/mxn · h =1 x1/h, i.e. the probability of the event on the n + 1th occasion must be unaffected by our knowledge of its proportionate frequency on the first n occasions, and must be exactly equal to its à priori probability before the first occasion.

Let us select one of these conditions for closer consideration. If yr represents the statement that the event has occurred on each of r successive occasions, yr/h = yr/yr−1h · yr−1/h and so on, so that yr/h = Π_{s=1}^{s=r} ys/ys−1h. Hence if we are to have yr/h = p^r, we must have ys/ys−1h = p for all values of s from 1 to r. But in many particular examples ys/ys−1h increases with s, so that yr/h > p^r. Bernoulli’s Theorem, that is to say, tends, if it is carelessly applied, to exaggerate the rate at which the probability of a given divergence from the most probable decreases as the divergence increases. If we are given a penny of which we have no reason to doubt the regularity, the probability of heads at the first toss is 1/2 ; but if heads fall at every one of the first 999 tosses, it becomes reasonable to estimate the probability of heads at the thousandth toss at much more than 1/2 . For the à priori probability of its being a conjurer’s penny, or otherwise biassed so as to fall heads almost invariably, is not usually so infinitesimally small as (1/2)^{1000}. We can only apply Bernoulli’s Theorem with rigour for a prediction as to the penny’s behaviour over a series of a thousand tosses, if we have à priori such exhaustive knowledge of the penny’s constitution and of the other conditions of the problem that 999 heads running would not cause us to modify in any respect our prediction à priori.

## §7 (p. 389)

It seldom happens, therefore, that we can apply Bernoulli’s Theorem with reference to a long series of natural events. For in such cases we seldom possess the exhaustive knowledge which is necessary. Even where the series is short, the perfectly rigorous application {{p.390}} of the Theorem is not likely to be legitimate, and some degree of approximation will be involved in utilising its results.

Not so infrequently, however, artificial series can be devised in which the assumptions of Bernoulli’s Theorem are relatively legitimate.[^390-1] Given, that is to say, a proposition a1, some series a1a2 . . . can be found, which satisfies the conditions:
    (i.) a1/h = a2/h . . . = ar/h.
    (ii.) ar/as . . . āt . . . h = ar/h.
Adherents of the Frequency Theory of Probability, who use the principal conclusion of Bernoulli’s Theorem as the defining property of all probabilities, sometimes seem to mean no more than that, relative to given evidence, every proposition belongs to some series, to the members of which Bernoulli’s Theorem is rigorously applicable. But the natural series, the series, for example, in which we are most often interested, where the a’s are alike in being accompanied by certain specified conditions c, is not, as a rule, rigorously subject to the Theorem. Thus ‘the probability of a in certain conditions c is 1/2 ’ is not in general equivalent, as has sometimes been supposed, to ‘It is 500 to 1 that in 40, 000 occurrences of c, a will not occur more than 20, 200 times, and 500 to 1 that it will not occur less than 19, 800 times.’

[^390-1]: In the discussion in Chapter XVI., p. 195, of the probability of a divergence from an equality of heads and tails in coin-tossing, an example has been given of the construction of an artificial series in which the application of Bernoulli’s Theorem is more legitimate than in the natural series.

## §8 (p. 390)

Bernoulli’s Theorem supplies the simplest formula by which we can attempt to pass from the à priori probabilities of each of a series of events to a prediction of the statistical frequency of their occurrence over the whole series. We have seen that Bernoulli’s Theorem involves two assumptions, one (in the form in which it is usually enunciated) tacit and the other explicit. It is assumed, first, that a knowledge of what has occurred at some of the trials would {{p.391}} not affect the probability of what may occur at any of the others; and it is assumed, secondly, that these probabilities are all equal à priori. It is assumed, that is to say, that the probability of the event’s occurrence at the rth trial is equal à priori to its probability at the nth trial, and, further, that it is unaffected by a knowledge of what may actually have occurred at the nth trial.

A formula, which dispenses with the explicit assumption of equal à priori probabilities at every trial, was proposed by Poisson,[^391-1] and is usually known by his name. It does not dispense, however, with the other inexplicit assumption. The difference between Poisson’s Theorem and Bernoulli’s is best shown by reference to the ideal case of balls drawn from an urn. The typical example for the valid application of Bernoulli’s Theorem is that of balls drawn from a single urn, containing black and white balls in a known proportion, and replaced after each drawing, or of balls drawn from a series of urns, each containing black and white balls in the same known proportion. The typical example for Poisson’s Theorem is that of balls drawn from a series of urns, each containing black and white balls in different known proportions.

[^391-1]: Recherches, pp. 246 et seq.

Poisson’s Theorem may be enunciated as follows:[^391-2] Let s trials be made, and at the λth trial (λ = 1, 2 . . . s) let the probabilities for the occurrence and non-occurrence of the event be pλ, qλ respectively. Then, if pλ/sΣ = p, the probability that the number of occurrences m of the event in the s trials will lie between the limits sp ± l is given by
    l   −
    l2/k2s
    ∫ −x2/k2s
    P = (2) ÷ (k (πs))√   e   dx + (e l2/k2s) ÷ (k (πs))√
    0
    √
where k = (2 pλqλ) ÷ (s)Σ   .

[^391-2]: For the proof see Poisson, Recherches, loc. cit., or Czuber, Wahrscheinlichkeitsrechnung, vol. i. pp. 153–159.

{{p.392}} By substituting (x) ÷ (k (s))√ = t and (l) ÷ (k (s))√ = γ , this may be written in a form corresponding to that of Bernoulli’s Theorem,[^392-1] namely:

[^392-1]: For the analogous form of Bernoulli’s Theorem see p. 385 (footnote).

The probability that the number of occurrences of the event will
    √
lie between sp ± γk (s) is given by
    γ 2^2
    P = √(2) ÷ ((π)) ∫ e^{−t} dt + (e−γ) ÷ (k (πs))√
    0

## §9 (p. 392)

This is a highly ingenious theorem and extends the application of Bernoulli’s results to some important types of cases. It embraces, for example, the case in which the successive terms of a series are drawn from distinct populations known to be characterised by differing statistical frequencies; no further complication being necessary beyond the calculation of two simple functions of these frequencies and of the number of terms in the series. But it is important not to exaggerate the degree to which Poisson’s method has extended the application of Bernoulli’s results. Poisson’s Theorem leaves untouched all those cases in which the probabilities of some of the terms in the series of events can be influenced by a knowledge of how some of the other terms in the series have turned out.

Amongst these cases two types can be distinguished. In the first type such knowledge would lead us to discriminate between the conditions to which the different instances are subject. If, for example, balls are drawn from a bag, containing black and white balls in known proportions, and not replaced, the knowledge whether or not the first ball drawn was black affects the probability of the second ball’s being black because it tells us how the conditions in which the second ball is drawn differ from those in which the first ball was drawn. In the second type such knowledge does not lead us to discriminate between the conditions to which the different instances are subject, but it leads us to modify our opinion as to the nature {{p.393}} of the conditions which apply to all the terms alike. If, for instance, balls are drawn from a bag, which is one, but it is not certainly known which, out of a number of bags containing black and white balls in differing proportions, the knowledge of the colour of the first ball drawn affects the probabilities at the second drawing, because it throws some light upon the question as to which bag is being drawn from.

This last type is that to which most instances conform which are drawn from the real world. A knowledge of the characteristics of some members of a population may give us a clue to the general character of the population in question. Yet it is this type, where there is a change in knowledge but no change in the material conditions from one instance to the next, which is most frequently overlooked.[^393-1] It will be worth while to say something further about each of these two {{p.394}} types.[^394-1]

[^393-1]: Numerous instances could be quoted. To take a recent English example, reference may be made to Yule, Introduction to the Theory of Statistics, p. 251. Mr. Yule thinks that the condition of independence is satisfied if “the result of any one throw or toss does not affect, and is unaffected by, the results of the preceding and following tosses,” and does not allow for the cases in which knowledge of the result is relevant apart from any change in the physical conditions.

[^394-1]: The types which I distinguish under four heads (the Bernoullian, the Poissonian, and the two described above) Bachelier (Calcul des probabilités, p. 155) classifies as follows: (i.) When the conditions are identical throughout, the problem has uniformité; (ii.) When they vary from stage to stage, but according to a law given from the beginning and in a manner which does not depend upon what has happened at the earlier stages, it has indépendance; (iii.) When they vary in a manner which depends upon what has happened at the earlier stages, it has connexité. Bachelier gives solutions for each type on the assumption that the number of trials is very great, and that the number of successes or failures can be regarded as a continuous variable. This is the same kind of assumption as that made in the proof of Bernoulli’s Theorem given in § 2, and is open to the same objections,—or rather the value of the results is limited in the same way.

## §10 (p. 394)

For problems of the first type, where there is physical or material dependence between the successive trials, it is not possible, I think, to propose any general solution; since the probabilities of the successive trials may be modified in all kinds of different ways. But for particular problems, if the conditions are precise enough, solutions can be devised. The problem, for instance, of an urn, containing black and white balls in known proportions, from which balls are drawn successively and not replaced,[^394-2] is ingeniously solved by Czuber[^394-3] with the aid of Stirling’s Theorem. If σ is the number of balls and s the number of drawings, he reaches the interesting conclusion (assuming that σ, s and σ − s are all large) that the probability of the number of black balls lying within given limits is the same as it would be if the balls were replaced after each drawing and the number of drawings were (σ − s) ÷ (σ)s instead of s.

[^394-2]: It is of no consequence whether the balls are drawn successively and not replaced, or are drawn simultaneously.

[^394-3]: Loc. cit. vol. i. pp. 163, 164.

In addition to the assumptions already stated, Professor Czuber’s solution applies only to those cases where the limits, for which we wish to determine the probability, are narrow compared with the {{p.395}} total number of black balls pσ. Professor Pearson[^395-1] has worked out the same problem in a much more general manner, so as to deal with the whole range, i.e. the frequency or probability of all possible ratios of black balls, even where s > pσ. The various forms of curve, which result, according to the different relations existing between p, s, and σ, supply examples of each of the different types of frequency curve which arise out of a classification according to (i.) skewness or symmetry, (ii.) limitation of range in one, both or neither direction; and he designates, therefore, the curves which are thus obtained as generalised probability curves. His discussion of the properties of these curves is interesting, however, to the student of descriptive statistics rather than to the student of probability. The most generalised and, mathematically, by far the most elegant treatment of this problem, with which I am acquainted, is due to Professor Tschuprow.[^395-2]

[^395-1]: “Skew Variation in Homogeneous Material,” Phil. Trans. (1895), p. 360.

[^395-2]: “Zur Theorie der Stabilität statistischer Reihen,” p. 216, published in the Skandinavisk Aktuarietidskrift for 1919.

Poisson, in attempting a somewhat similar problem,[^395-3] arrives at a result, which seems obviously contrary to good sense, by a curious, but characteristic, misapprehension of the meaning of ‘independence’ in probability. His problem is as follows: If l balls be taken out from an urn, containing c black and white balls in known proportions, and not replaced, and if a further number of balls μ be then taken out, the probability that a given proportion (m) ÷ (m + n) of these μ balls will be black is independent of the number and the colour of the l balls originally drawn out. For, he argues, if l + μ balls are drawn out, the probability of a combination, which is made up of l black and white balls in given proportions followed by μ balls, of which m are white and n black, must be the same as that of a similar combination in which the μ balls precede the l balls. Hence the probability of m white balls in μ drawings, given that the l balls have already been drawn out, must be equal to the probability of the same result, when {{p.396}} no balls have been previously drawn out. The reader will perceive that Poisson, thinking only of physical dependence, has been led to his paradoxical conclusion by a failure to distinguish between the cases where the proportion of black and white balls amongst the l balls originally drawn is known and where it is not. The fact of their having been drawn in certain proportions, provided that only the total number drawn is known and the proportions are unknown, does not influence the probability. Poisson states in his conclusion that the probability is independent of the number and colour of the l balls originally drawn. If he had added—as he ought—‘provided the number of each colour is unknown,’ the air of paradox disappears. This is an exceedingly good example of the failure to perceive that a probability cannot be influenced by the occurrence of a material event but only by such knowledge, as we may have, respecting the occurrence of the event.[^396-1]

[^395-3]: Loc. cit. pp. 231, 232.

[^396-1]: For an attempt to solve other problems of this type see Bachelier, Calcul des probabilités, chap. ix. (Probabilités connexes). I think, however, that the solutions of this chapter are vitiated by his assuming in the course of them both that certain quantities are very large, and also, at a later stage, that the same quantities are infinitesimal. On this account, for example, his solution of the following difficult problem breaks down: Given an urn A with m white and n black balls and an urn B with m′ white and n′ black balls, if at each move a ball is taken from A and put into B, and at the same time a ball is taken from B and put into A, what is the probability after x moves that the urns A and B shall have a given composition?

## §11 (p. 396)

For problems of the second type, where knowledge of the result of one trial is capable of influencing the probability at the next apart from any change in the material conditions, there is, likewise, no general solution. The following artificial example, however, will illustrate the sort of considerations which are involved.

In the cases where Bernoulli’s Theorem is applied to practical questions, the à priori probability is generally obtained empirically by reference to the statistical frequency of each alternative in past experience under apparently similar conditions. Thus the à priori {{p.397}} probability of a male birth is estimated by reference to the recorded proportion of male births in the past.[^397-1] The validity of estimating probabilities in this manner will be discussed later. But for the purposes of this example let us assume that the à priori probability has been calculated on this basis. Thus the à priori probability p (= r/s) of an event is based on the observation of its occurrence r times out of s occasions on which the given conditions were present. Now, according to Bernoulli’s Theorem directly applied, then probability of the event’s occurring n times running is p^n or (r/s) . But, if the event occurs at the first trial, the probability at the second becomes (r + 1) ÷ (s + 1) , and so on. Hence the probability P, properly calculated, of n successive occurrences is
    r/s · (r + 1) ÷ (s + 1) · (r + 2) ÷ (s + 2) . . . (r + n − 1) ÷ (s + n − 1).
{{p.398}} Hence
    P = ((r + n − 1)! (s − 1)!) ÷ ((s + n − 1)! (r − 1)!)
    r+n−1/2 −(r+n−1) s−1/2 −(s−1)
    (r + n − 1)   e   s e
    =   1   1   by Stirling’s
    (s + n − 1)^{s+n−}2̄ e^{−(s+n−1)}r^{r−}2̄ e^{−(r−1)}
    Theorem, provided that r and s are large;
    (   )r+n−1/2
    n 1 + (n − 1) ÷ (r)
    = (r/s)
    (̅   )̅s̅+̅n̅−̅1̅/̅2̅
    1 + (n − 1) ÷ (s)
    1/2
    (   )(r−1/2) ÷ (n)+1.
    1 + (n − 1) ÷ (r)
    = p^nQ^n, where Q =
    1/2
    (̅   )̅(s−1/2) ÷ (n)+̅1̅.̅
    1 + (n − 1) ÷ (s)
Thus, in this case, the assumption of Bernoulli’s Theorem is approximately correct, only if Q is nearly unity. This condition is not satisfied unless n is small both compared with r and compared with s. It is very important to notice that two conditions are involved. Not only must the experience, upon which the à priori probability is based, be extensive in comparison with the number of instances to which we apply our prediction; but also the number of previous instances multiplied by the probability based upon them, i.e. sp (= r), must be large in comparison with the number of new instances. Thus, even where the prior experience, upon which we found the initial probability P, is very extensive, we must not, if P is very small, say that the probability of n successive occurrences is approximately p^n, unless n is also small. Similarly if we wish to determine, by the methods of Bernoulli, the probability of n occurrences and m failures on m + n occasions, it is necessary that we should have m and n small {{p.399}} compared with s, n small compared with r, and m small compared with s − r.[^399-1]

[^397-1]: Cf. Yule, Theory of Statistics, p. 258: “We are not able to assign an à priori value to the chance p (i.e. of a male birth) as in the case of dice-throwing, but it is quite sufficiently accurate for practical purposes to use the proportion of male births actually observed if that proportion be based on a moderately large number of observations.”

[^399-1]: This paragraph is concerned with a different point from that dealt with in Professor Pearson’s article “On the Influence of Past Experience on Future Expectation,” to which it bears a superficial resemblance. Professor Pearson’s article which deals, not with Bernoulli’s Theorem, but with Laplace’s “Rule of Succession,” will be referred to in § 16 of this chapter and in § 12 of the next.

The case solved above is the simplest possible. The general problem is as follows: If an event has occurred x times in the first y trials, its probability at the y + 1th is (r + x) ÷ (s + y) ; determine the à priori probability of the event’s occurring p times in q trials. If the à priori probability in question is represented by φ(p, q), we have
    φ(p, q) = (r + p − 1) ÷ (s + q − 1) φ(p − 1, q − 1) + (s + q − 1 − r − p) ÷ (s + q − 1) φ(p, q − 1).
I know of no solution of this, even approximate. But we may say that the conditions are those of supernormal dispersion as compared with Bernoulli’s conditions. That is to say, the probability of a proportion differing widely from r/s is greater than in Bernoullian conditions; for when the proportion begins to diverge it becomes more probable that it will continue to diverge in the same direction. If, on the other hand, the conditions of the problem had been such, that when the proportion begins to diverge it becomes more probable that it will recover itself and tend back towards r/s (as when we draw balls without replacing them from a bag of known composition), we should have subnormal dispersion.[^399-2]

[^399-2]: Bachelier (Calcul des probabilités, p. 201) classifies these two kinds of conditions as conditions accélératrices and conditions retardatrices.

## §12 (p. 399)

The condition elucidated in the preceding paragraph is frequently overlooked by statisticians. The following example from Czuber[^399-3] will be sufficient for the purpose of illustration. Czuber’s {{p.400}} argument is as follows:

[^399-3]: Loc. cit. vol. ii. p. 15. I choose my example from Professor Czuber because he is usually so careful an exponent of theoretical statistics.

In the period 1866–1877 there were registered in Austria
    m = 4, 311, 076 male births
    n = 4, 052, 193 female births
    s̅ =̅ 8̅,̅ 3̅6̅3̅,̅ 2̅6̅9̅ ;
for the succeeding period, 1877–1899, we are given only
    m′ = 6, 533, 961 male births;
what conclusion can we draw as to the number n′ of female births? We can conclude, according to Czuber, that the most probable value
    n′/0 = nm′/m = 6, 141, 587,
and that there is a probability P = .9999779 that n′ will lie between the limits 6, 118, 361 and 6, 164, 813.

It seems in plain opposition to good sense that on such evidence we should be able with practical certainty (P = .9999779 = 1 − 1/45250) to estimate the number of female births within such narrow limits. And we see that the conditions laid down in § 11 have been flagrantly neglected. The number of cases, over which the prediction based on Bernoulli’s Theorem is to extend, actually exceeds the number of cases upon which the à priori probability has been based. It may be added that for the period, 1877–1894, the actual value of n′ did lie between the estimated limits, but that for the period, 1895–1905, it lay outside limits to which the same method had attributed practical certainty.

That Professor Czuber should have thought his own argument plausible, is to be explained, I think, by his tacitly taking account in his own mind of evidence not stated in the problem. He was relying upon the fact that there is a great mass of evidence for believing that {{p.401}} the ratio of male to female births is peculiarly stable. But he has not brought this into the argument, and he has not used as his à priori probability and as his coefficient of dispersion the values which the whole mass of this evidence would have led him to adopt. Would not the argument have seemed very preposterous if m had been the number of males called George, and n the number of females called Mary? Would it not have seemed rather preposterous if m had been the number of legitimate births and n the number of illegitimate births? Clearly we must take account of other considerations than the mere numerical values of m and n in estimating our à priori probability. But this question belongs to the subject-matter of later chapters, and, quite apart from the manner of calculation of the à priori probability, the argument is invalidated by the fact than an à priori probability founded on 8, 363, 269 instances, without corroborative evidence of a non-statistical character, cannot be assumed stable through a calculation which extends over 12, 700, 000 instances.

## §13 (p. 401)

Before we leave the theorems of Bernoulli and Poisson, it is necessary to call attention to a very remarkable theorem by Tchebycheff, from which both of the above theorems can be derived as special cases. This result is reached rigorously and without approximation, by means of simple algebra and without the aid of the differential calculus. Apart from the beauty and simplicity of the proof, the theorem is so valuable and so little known that it will be worth while to quote it in full:[^401-1]

[^401-1]: From Journ. Liouville (2), xii., 1867, “Des valeurs moyennes,” an article translated from the Russian of Tchebycheff. This proof is also quoted by Czuber, loc. cit. p. 212, through whom I first became acquainted with it. Most of Tchebycheff’s work was published previous to 1870 and appeared originally in Russian. It was not easily accessible, therefore, until the publication at Petrograd in 1907 of the collected edition of his works in French. His theorems are, consequently, not nearly so well known as they deserve to be, although his most important theorems were reproduced from time to time in the Journals of Euler and Liouville. For full references see the Bibliography.

{{p.402}} Let x, y, z . . . represent certain magnitudes, of which x can take the values x1x2 . . . xk with probabilities p1p2 . . . pk respectively, y the values y1y2 . . . yl with probabilities q1q2 . . . ql, z the values z1z2 . . . zm with probabilities r1r2 . . . rm and so on, so that
    Σ_{1}^{k} p = 1, Σ_{1}^{l} q = 1, Σ_{1}^{m} r = 1, etc.
Write   Σ_{1}^{k} pκxκ = a, Σ_{1}^{l} qλyλ = b, Σ_{1}^{m} rμzμ = c, etc.,
and   Σ_{1}^{k} pκx2/κ = a1, Σ_{1}^{l} qλy2/λ = b1, Σ_{1}^{m} rμz2/μ = c1, etc.,
so that we can describe a as the mathematical expectation or average value of x and a1 as the mathematical expectation or average value of x^2, etc.

Consider the expression:
    Σ(xκ + yλ + zμ + . . . − a − b − c − . . .)^2pκqλrμ . . .
    p    p    p
    2   2   2   2
Now Σ_{1}^{k}(xκ − 2axκ + a )pκ =(Σ κxκ − 2a(Σ κxκ + a (Σ κ
    = a1 − 2a^2 + a^2 = a1 − a^2.
Also Σ qλrμ . . . = 1 summed for all values of λ, μ . . ., and
    Σ_{1}^{k} 2(xκ − a)(yλ − b)pκ = Σ_{1}^{k} 2(xκyλ − bxκ − ayλ + ab)pκ
    p    p    p    p
    = 2 (yλ Σ κxκ − b(Σ κxκ − ayλ Σ κ + ab(Σ κ)
    = 2(ayλ − ab − ayλ + ab) = 0.
Therefore   Σ(xκ + yλ + zμ + . . . − a − b − c . . .)^2pκqλrμ . . .
    = a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 − . . . ,
    Σ(xκ + yλ + zμ + . . . − a − b − c . . .)^2pκqλrμ . . .
whence   = 1/α2,
    α^2(a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 − . . .)
{{p.403}} where the summation extends over all values of κ, λ, μ . . . and α is some arbitrary number greater than unity.

If we omit those terms of the sum on the left-hand side of the above equation for which
    (xκ + yλ + zμ + . . . − a − b − c . . .)^2
    < 1,
    α^2(a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 − . . .)
and write unity for this expression in the remaining terms, both these processes diminish the magnitude of the left-hand side. Hence
    p
Σ κqλrμ . . . < 1/α2 , where the summation covers those sets of values only for which
    (xκ + yλ + zμ + . . . − a − b − c . . .)^2
    ≥ 1.
    α^2(a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 . . .)

If P is the probability that
    (xκ + yλ + zμ + . . . − a − b − c . . .)^2
    α^2(a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 − . . .)
is equal to or less than unity, it follows that
    1 − P < 1/α2
i.e.   P > 1 − 1/α2
Hence the probability that the sum
    xκ + yλ + zμ . . .   lies between the limits
    a + b + c + . . . − α√a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 − . . .
and a + b + c + . . . + α√a1 + b1 + c1 + . . . − a^2 − b^2 − c^2 − . . . is greater than 1 − 1/α2 , where α is some number greater than unity.

{{p.404}} This result constitutes Tchebycheff’s Theorem. It may also be written in the following form:

Let n be the number of the magnitudes x, y, z . . ., and write α = √
((n)) ÷ (t) ; then the probability that the arithmetic mean (xκ + yλ + zμ + . . .) ÷ (n) lies between the limits
    √
    (a + b + c + . . .) ÷ (n) ± 1/t (a1 + b1 + c1 + . . .) ÷ (n) − (a2 + b2 + c2 + . . .) ÷ (n)
is greater than 1 − t2/n .

It is also easy to show[^404-1] as a deduction from Tchebycheff’s Theorem that, if an amount A is won when an event of probability p [p = 1 − q] occurs and an amount B lost when it fails, then in s trials the probability that the total winnings (or losses) will lie between the limits
    √
    s(pA − qB) ± α(A + B) (spq)
is greater than 1 − 1/α2 .

[^404-1]: For a proof see Czuber, loc. cit. vol. i. p. 216.

## §14 (p. 404)

From this very general result for the probable limits of a sum composed of a number of independently varying magnitudes, Bernoulli’s Theorem is easily derived. For let there be s observations or trials, and s magnitudes x1x2 . . . xs corresponding, such that x = 1 when the event under consideration occurs, and x = 0 when it fails. If the probability of the events occurrence is p, we have a = p, b = p, etc., and a1 = p, b1 = p, etc. Hence the probability P that the number of the event’s occurrences will lie between the limits sp ± α√(sp − sp)^2,
    √
i.e. between the limits sp ± α (spq) where q = 1 − p, is > 1 − 1/α2 . If we compare this formula with the formula for Bernoulli’s Theorem already given, we find that, where this formula gives P > 1 − 1/α2 , {{p.405}} Bernoulli’s Theorem with greater precision gives P = Θ (√(α) ÷ ((2))). The degree of superiority in the matter of precision supplied by the latter can be illustrated by the following table:
    α^2.   Θ ((α) ÷ ((2))√ ) .   1 − 1/α2.
    1.5   .7788   .333
    2   .8427   .5
    4.5   .9661   .7778
    8   .9953   .875
    12.5   .9996   .92
    18   .99998   .9445
Thus when the limits are narrow and α is small, Bernoulli’s formula gives a value of P very much in excess of 1 − 1/α2 . But Bernoulli’s formula involves a process of approximation which is only valid when s is large. Tchebycheff’s formula involves no such process and is equally valid for all values of s. We have seen in § 11 that there are numerous cases in which for a different reason Bernoulli’s formula exaggerates the results, and, therefore, Tchebycheff’s more cautious limits may sometimes prove useful.

The deduction of a corresponding form of Poisson’s Theorem from Tchebycheff’s general formula obviously follows on similar lines. For we put[^405-1] a = p1, b = p2, etc., and a1 = p1, b1 = p2, etc., and find that the probability that the number of the event’s occurrences will lie between the limits
    √
    Σ_{1}^{λ} pλ ± α (Σ_{1}^{λ} pλ − Σ_{1}^{λ}) p2/λ,
{{p.406}}
    √ p
i.e. between the limits   sp ± α (Σ^{λ}) λqλ,
    √   √
i.e. between the limits   sp ± (2) αk (s),
is greater than t − 1/α2 .

[^405-1]: I am using the same notation as that used for Poisson’s Theorem in § 8.

In Crelle’s Journal[^406-1] Tchebycheff proves Poisson’s Theorem directly by a method similar to his general method, and also obtains several supplementary results such as the following:

[^406-1]: Vol. 33 (1846), Démonstration élémentaire d’une proposition générale de la théorie des probabilités.

I. If the chances of an event E in μ consecutive trials are p1p2 . . . pμ respectively, and their sum is s, the probability that E will occur at least m times is less than
    √
    m   μ−m+1
    (1) ÷ (2(m − s)) (m(μ − m)) ÷ (μ) (s/μ) (((μ − s) ÷ (μ − m))
    provided that m > s + 1;
II. and the probability that E will not occur more than n times is less than   √
    μ−n   n+1
    (1) ÷ (2(s − n)) (μ(μ − n)) ÷ (μ) ((μ − s) ÷ (μ − n)) ((s/n)
    provided that n < s − 1.
III. Hence the probability that E will occur less than m times and more than n is greater than
    √
    m^{μ−m+1}
    1 − (1) ÷ (2(m − s)) (m(μ − m)) ÷ (μ) (s/m) ((μ − s) ÷ (μ − m))
    √
    n+1^{n−μ}
    − (1) ÷ (2(s − n)) (n(μ − n)) ÷ (μ) (s/n) ((μ − s) ÷ (μ − n))
{{p.407}}
    provided m > s + 1, n < s − 1.

## §15 (p. 407)

Tchebycheff’s methods have been set out and his results admirably extended by A. A. Markoff.[^407-1] And some developments along the same lines by Tschuprow (“Zur Theorie der Stabilität statistischer Reihen,” Skandinavisk Aktuarietidskrift, 1919) have convinced me that Tchebycheff’s discovery is far more than a technical device for solving a special problem, and points the way to the fundamental method for attacking these questions on the mathematical side. The Laplacian mathematics, although it still holds the field in most text-books, is really obsolete, and ought to be replaced by the very beautiful work which we owe to these three Russians.

[^407-1]: The reader is referred to Markoff’s Wahrscheinlichkeitsrechnung, and particularly to p. 67, for a striking development, along mathematical lines, of Tchebycheff’s leading idea. Further references to later memôirs, which, being in the Russian language, are inaccessible to me, will be found in the Bibliography.

## §16 (p. 407)

There is one other investigation relating to Bernoulli’s Theorem which deserves remark. I have already pointed out, in § 2, that the dispersion about the most probable value, even when the conditions for the applicability of Bernoulli’s Theorem in its non-approximate form are strictly fulfilled, is unsymmetrical. The fact, that the usual approximation for the probability of a divergence h from the most probable number of occurrences (the notation is that of
    −h2/2mpq ,
§ 2 above) takes the form √   e   which is the same for +h
    1/2πmpq̄
as for −h, has led to this want of symmetry being very generally overlooked; and it is not uncommon to assume that the probability of a given divergence less than pm is equal to that of the same divergence in excess of pm, and, in general, that the probability of the frequency’s exceeding pm in a set of m trials is equal to that of its falling short of pm.

That this is not strictly the case is obvious. If a die is cast 60 times, the most probable number of appearances of the ace is 10; but the ace is more likely to appear 9 times than 11 times; and {{p.408}} much more likely (about 5 times as likely) not to appear at all than to appear exactly 20 times. That this must be so will be clear to the reader (without his requiring to trouble himself with the algebra), when he reflects that the ace cannot appear less often than not at all, whereas it may well appear more than 20 times, so that the smallness of the possible divergence in defect from the most probable value 10, as compared with the possible divergence in excess, must be made up for by the greater frequency of any given defection as compared with the corresponding excess. Thus the actual frequency in a series of trials of an event, of which the probability at each trial is less than 1/2 , is likely to fall short of its most probable value more often than it exceeds it. What is in fact true is that the mathematical expectation of deficiency is equal to the mathematical expectation of excess, i.e. that the sum of the possible deficiencies each multiplied by its probability is equal to the sum of the possible excesses each multiplied by its probability.

The actual measurement of this want of symmetry and the determination of the conditions, in which it can be safely neglected, involves laborious mathematics, of which I am only acquainted with one direct investigation, that published in the Proceedings of the London Mathematical Society by Mr. T. C. Simmons.[^408-1]

[^408-1]: “A New Theorem in Probability.” Mr. Simmons claimed novelty for his investigation, and so far as I know this claim is justified; but recent investigations obtaining closer approximations to Bernoulli’s Theorem by means of the Method of Moments are essentially directed towards the same problem. A somewhat analogous point has, however, been raised by Professor Pearson in his article (Phil. Mag., 1907) on “The Influence of Past Experience on Future Expectation.” He brings out an exactly similar want of symmetry in the probabilities of the various possible frequencies about the most probable frequency, when the calculation is based, not on Bernoulli’s Theorem as in Mr. Simmons’s investigation, but on Laplace’s rule of succession (see next chapter). The want of symmetry has also been pointed out by Professor Lexis (Abhandlungen, p. 120).

For the details of the proof I must refer the reader to {{p.409}} Mr. Simmons’s article. His principal theorem[^409-1] is as follows: If (1) ÷ (a + 1) is the probability of the event at each trial and n(a + 1) the number of trials, n and a being integers,[^409-2] the probability that the frequency of occurrence will fall short of n is always greater than the probability that it will exceed n; the difference between the two probabilities being a maximum when n = 1, constantly diminishing as n increases, lying always between 1/3 (a − 1) ÷ (a + 1) times the greatest term
    n(a+1)
in ((a) ÷ (a + 1) + (1) ÷ (a + 1))   and 1/3 (a − 1) ÷ (a + 1) times the greatest term in
    (n+1)(a+1)
((a) ÷ (a + 1) + (1) ÷ (a + 1))   , and being approximately equal, when n is very large, to 1/3 √(a − 1) ÷ (2πna(a + 1))̄ .

[^409-1]: I am not giving his own enunciation of it.

[^409-2]: Mr. Simmons does not seem to have been able to remove this restriction on the generality of his theorem, but there does not seem much reason to doubt that it can be removed.

The following table gives the value of the excess ∆ of the probability of a frequency less than pm over the probability of a frequency greater than pm for various values of p the probability and m the number of trials [p = (1) ÷ (a + 1), m = n(a + 1)], as calculated by {{p.410}} Mr. Simmons:
    p.   m.   ∆.
    1/3   3   .037037
    1/3   15   .02243662
    1/3   24   .0182706
    1/4   4   .054687
    1/4   20   .03201413
    1/10   10   .084777
    1/10   20   .068673713
    1/100   100   .101813
    1/100   200   .081324387
    1/1000   1000   .103454
Thus unless not only m but mp also is large the want of symmetry is likely to be appreciable. Thus it is easily found that in 100 sets of 4 trials each, where p = 1/4 , the actual frequency is likely to exceed the most probable 26 times and to fall short of it 31 times; and in 100 sets of 10 trials each, where p = 1/10 , to exceed 26 times and to fall short 34 times.

Mr. Simmons was first directed to this investigation through noticing in the examination of sets of random digits that “each digit presented itself, with unexpected frequency, less than 1/10 of the number of times. For instance, in 100 sets of 150 digits each, I found that a digit presented itself in a set more frequently under 15 times than over 15 times; similarly in the case of 80 sets each of 250 digits, and also in other aggregations.” Its possible bearing on such experiments with dice and roulette, as are described at the end of this chapter, is clear. But apart from these artificial experiments, it is sometimes worth the statistician’s while to bear in mind this {{p.411}} appreciable want of symmetry in the distribution about the mode or most probable value in many even of those cases in which Bernoullian conditions are strictly fulfilled.

## §17 (p. 411)

I will conclude this chapter by an account of some of the attempts which have been made to verify à posteriori the conclusions of Bernoulli’s Theorem. These attempts are nearly useless, first, because we can seldom be certain à priori that the conditions assumed in Bernoulli’s Theorem are fulfilled, and, secondly, because the theorem predicts not what will happen but only what is, on certain evidence, likely to happen. Thus even where our results do not verify Bernoulli’s Theorem, the theorem is not thereby discredited. The results have bearing on the conditions in which the experiments took place, rather than upon the truth of the theorem. In spite, therefore, of the not unimportant place which these attempts have in the history of probability, their scientific value is very small. I record them, because they have a good deal of historical and psychological interest, and because they satisfy a certain idle curiosity from which few students of probability are altogether free.[^411-1]

[^411-1]: Mr. Yule (Introduction to Statistics, p. 254) recommends its indulgence: “The student is strongly recommended to carry out a few series of such experiments personally, in order to acquire confidence in the use of the theory.” Mr. Yule himself has indulged moderately.

## §18 (p. 411)

The data for these investigations have been principally drawn from four sources—coin-tossing, the throw of dice, lotteries, and roulette; for in such cases as these the conditions for Bernoulli’s Theorem seem to be fulfilled most nearly. The earliest recorded experiment was carried out by Buffon,[^411-2] who, assisted by a child tossing a coin into the air, played 2048 partis of the Petersburg game, in which a coin is thrown successively until the parti is brought to an end by the appearance of heads. The same experiment was repeated by a young pupil of De Morgan’s ‘for his own satisfaction.’[^411-3] {{p.412}} In Buffon’s trials there were 1992 tails to 2048 heads; in Mr. H.’s (De Morgan’s pupil) 2044 tails to 2048 heads. A further experiment, due to Buffon’s example, was carried out by Quetelet[^412-1] in 1837. He drew 4096 balls from an urn, replacing them each time, and recorded the result at different stages, in order to show that the precision of the result tended to increase with the number of the experiments. He drew altogether 2066 white balls and 2030 black balls. Following in this same tradition is the experiment of Jevons,[^412-2] who made 2048 throws of ten coins at a time, recording the proportion of heads at each throw and the proportion of heads altogether. In the whole number of 20, 480 single throws, he obtained heads 10, 353 times; More recently Weldon[^412-3] threw twelve dice 4096 times, recording the proportion of dice at each throw which showed a number greater than three.

[^411-2]: Essai d’arithmètique morale (see Bibliography), published 1777, said to have been composed about 1760.

[^411-3]: Formal Logic, p. 185, published 1847. De Morgan gives Buffon’s results, as well as his pupil’s, in full. Buffon’s results are also investigated by Poisson, Recherches, pp. 132–135.

[^412-1]: Letters on the Theory of Probabilities (Eng. trans.), p. 37.

[^412-2]: Principles of Science (2nd ed.), p. 208.

[^412-3]: Quoted by Edgeworth, “Law of Error” (Ency. Brit. 10th ed.), and by Yule, Introduction to Statistics, p. 254.

All these experiments, however, are thrown completely into the shade by the enormously extensive investigations of the Swiss astronomer Wolf, the earliest of which were published in 1850 and the latest in 1893.[^412-4] In his first set of experiments Wolf completed 1000 sets of tosses with two dice, each set continuing until every one of the 21 possible combinations had occurred at least once. This involved altogether 97, 899 tosses, and he then completed a total of 100, 000. These data enabled him to work out a great number of calculations, of which Czuber quotes the following, namely a proportion of .83533 {{p.413}} of unlike pairs, as against the theoretical value .83333, i.e. 5/6 . In his second set of experiments Wolf used two dice, one white and one red (in the first set the dice were indistinguishable), and completed 20, 000 tosses, the details of each result being recorded in the Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich. He studied particularly the number of sequences with each die, and the relative frequency of each of the 36 possible combinations of the two dice. The sequences were somewhat fewer than they ought to have been, and the relative frequency of the different combinations very different indeed from what theory would predict.[^413-1] The explanation of this is easily found; for the records of the relative frequency of each face show that the dice must have been very irregular, the six face of the white die, for example, falling 38 per cent more often than the four face of the same die. This, then, is the sole conclusion of these immensely laborious experiments,—that Wolf’s dice were very ill made. Indeed the experiments could have had no bearing except upon the accuracy of his dice. But ten years later Wolf embarked upon one more series of experiments, using four distinguishable dice,—white, yellow, red, and blue,—and tossing this set of four 10, 000 times. Wolf recorded altogether, therefore, in the course of his life 280, 000 results of tossing individual dice. It is not clear that Wolf had any well-defined object in view in making these records, which are published in curious conjunction with various astronomical results, and they afford a wonderful example of the pure love of experiment and observation.[^413-2]

[^412-4]: See Bibliography. Of the earliest of these investigations I have no first-hand knowledge and have relied upon the account given by Czuber, loc. cit. vol. i. p. 149. For a general account of empirical verifications of Bernoulli’s Theorem reference may be made to Czuber, Wahrscheinlichkeitsrechnung, vol. i. pp. 139–152, and Czuber, Entwicklung der Wahrscheinlichkeitstheorie, pp. 88–91.

[^413-1]: Czuber quotes the principal results (loc. cit. vol. i. pp. 149–151). The frequencies of only 4, instead of 18, out of the 36 combinations lay within the probable limits, and the standard deviation was 76.8 instead of 23.2.

[^413-2]: The latest experiment of the kind, of which I am aware, is that of Otto Meissner (“Würfelversuche,” Zeitschrift für Math. und Phys. vol. 62 (1913), pp. 149–156), who recorded 24 series of 180 throws each with four distinguishable dice.

## §19 (p. 413)

Another series of calculations have been based upon the {{p.414}} ready-made data provided by the published results of lotteries and roulette.[^414-1]

[^414-1]: For the publication of such returns there has always been a sufficient demand on the part of gamblers. An Almanach romain sur la loterie royale de France was published at Paris in 1830, which contained all the drawings of the French lottery (two or three a month) from 1758 to 1830. Players at Monte Carlo are provided with cards and pins with which to record the results of successive coups, and the results at the tables are regularly published in Le Monaco. Gamblers study these returns on account of the belief, which they usually hold, that as the number of cases is increased the absolute deviation from the most probable proportion becomes less, whereas at the best Bernoulli’s Theorem shows that the proportionate deviation decreases while the absolute deviation increases. Cf. Houdin’s Les Tricheries des Grecs dévoilées: “In a game of chance, the oftener the same combination has occurred in succession, the nearer we are to the certainty that it will not recur at the next cast or turn-up. This is the most elementary of the theories on probabilities; it is termed the maturity of the chances.” Laplace (Essai philosophique, p. 142) quotes an amusing instance of the same belief not drawn from the annals of gambling: “J’ai vu des hommes désirant ardemment d’avoir un fils, n’apprendre qu’avec peine les naissances des garçons dans le mois où ils allaient devenir pères. S’imaginant que le rapport de ces naissances à celles des filles devait être le même à la fin de chaque mois, ils jugaient que les garçons déjà nés rendaient plus probables les naissances prochaines des filles.” The literature of gambling is very extensive, but, so far as I am acquainted with it, excessively lacking in variety, the maturity of the chances and the martingale continually recurring in one form or another. The curious reader will find tolerable accounts of such topics in Proctor’s Chance and Luck, and Sir Hiram Maxim’s Monte Carlo Facts and Fallacies.

Czuber[^414-2] has made calculations based on the lotteries of Prague (2854 drawings) and Brünn (2703 drawings) between the years 1754 and 1886, in which the actual results agree very well with theoretical predictions. Fechner[^414-3] employed the lists of the ten State lotteries of Saxony between the years 1843 and 1852. Of a rather {{p.415}} more interesting character are Professor Karl Pearson’s investigations[^415-1] into the results of Monte Carlo Roulette as recorded in Le Monaco in the course of eight weeks. Applying Bernoulli’s Theorem, on the hypothesis of the equiprobability of all the compartments throughout the investigation, he found that the actually recorded proportions of red and black were not unexpected, but that alternations and long runs were so much in excess that, on the assumption of the exact accuracy of the tables, the à priori odds were at least a thousand millions to one against some of the recorded deviations. Professor Pearson concluded, therefore, that Monte Carlo Roulette is not objectively a game of chance in the sense that the tables on which it is played are absolutely devoid of bias. Here also, as in the case of Wolf’s dice, the conclusion is solely relevant, not to the theory or philosophy of Chance, but to the material shapes of the tools of the experiment.

[^414-2]: Zum Gesetz der grossen Zahlen. The results are summarised in his Wahrscheinlichkeitsrechnung, vol. i. p. 139.

[^414-3]: Kollektivmasslehre, p. 229. These results also are summarised by Czuber, loc. cit.

[^415-1]: The Chances of Death, vol. i.

Professor Pearson’s investigations into Roulette, which dealt with 33, 000 Monte Carlo coups, have been overshadowed, just as all other tosses of coins and dice have been outdone by Wolf, by Dr. Karl Marbe,[^415-2] who has examined 80, 000 coups from Monte Carlo and elsewhere. Dr. Marbe arrived at exactly opposite conclusions; for he claims to have shown that long runs, so far from being in excess, were greatly in defect. Dr. Marbe introduces this experimental result in support of his thesis that the world is so constituted that long runs do not as a matter of fact occur in it.[^415-3] Not merely are long runs very {{p.416}} improbable. They do not, according to him, occur at all. But we may doubt whether roulette can tell us very much either of the laws of logic or of the constitution of the universe.

[^415-2]: Naturphilosophische Untersuchungen zur Wahrscheinlichkeitstheorie.

[^415-3]: Dr. Marbe’s monograph has given rise in Germany to a good deal of discussion, not directed towards showing what a preposterous method this is for demonstrating a natural law, but because the experimental result itself does not really follow from the data and is due to a somewhat subtle error in Marbe’s reasoning, by which he has been led into an incorrect calculation of the probable proportions à priori of the various sequences. The problem is discussed by Von Bortkiewicz, Brömse, Bruns, Grimsehl, and Grünbaum (for exact references to these see the Bibliography), and by Lexis (Abhandlungen, pp. 222–226) and Czuber (Wahrscheinlichkeitsrechnung, vol. i. pp. 144–149). Largely as a result of this controversy, Von Bortkiewicz has lately devoted a complete treatise (Die Iterationen) to the mathematics of ‘runs.’ Dr. Marbe has been given far more attention by his colleagues in Germany than he conceivably deserves.

Dr. Marbe’s main thesis is identical, as he himself recognises, with one of the heterodox contentions of D’Alembert.[^416-1] But this principle of variety, precisely opposite to the usual principle of Induction, can have no claim to be accepted à priori and, as a general principle, there is no adequate evidence to support it from experience. Its origin is to be found, perhaps, in the fact that in a certain class of cases, especially where conscious human agency comes in, it may contain some element of truth. The fact of an act’s having been done in a particular way once may be a special reason for thinking that it will not be performed on the next occasion in precisely the same manner. Thus in many so-called random events some slight degree {{p.417}} of causal and material dependence between successive occurrences may, nevertheless, exist. In these cases ‘runs’ may be fewer and shorter than those which we should predict, if a complete absence of such dependence is assumed. If, for example, a pack of cards be dealt, collected, and shuffled, to the extent that card-players do as a rule shuffle, there may be a greater presumption against the second hand’s being identical with the first than against any other particular distribution. In the case of croupiers long experience might possibly suggest some psychological generalisation,—that they are very mechanical, giving an excess of numbers belonging to a particular section of the wheel, or, on the other hand, that when a croupier sees a run beginning, he tends to vary his spin more than usual, thus bringing runs to an end sooner than he ought.[^417-1] At any rate, it is worth emphasising once more that from such experiments as these this is the only kind of knowledge which we can hope to obtain,—knowledge of the material construction of a die or of the psychology of a croupier.

[^416-1]: D’Alembert’s principal contributions to Probability are most accessible in the volumes of his Opuscules mathématiques (1761). Works on Probability usually contain some reference to D’Alembert, but his sceptical opinions, rejected rather than answered by the orthodox school of Laplace, have not always received full justice. D’Alembert has three main contentions to which in his various papers he constantly recurs: (1) That a probability very small mathematically is really zero; (2) That the probabilities of two successive throws with a die are not independent; (3) That ‘mathematical expectation’ is not properly measured by the product of the probability and the prize. The first and third of these were partly advanced in explanation of the Petersburg paradox (see p. 362). The second is connected with the first, and was also used to support his incorrect evaluation of the probability of heads twice running; but D’Alembert, in spite of many of his results being wrong, does not altogether deserve the ridicule which he has suffered at the hands of writers, who accepted without sceptical doubts the hardly less incorrect conclusions of the orthodox theory of that time.

[^417-1]: A good roulette table is, however, so delicate an instrument that no probable degree of regularity of habit on the part of the spinner could be sufficient to produce regularity in the result.
