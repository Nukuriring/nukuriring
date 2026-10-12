---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part III. Induction and Analogy"
chapter: "Chapter XX"
title: "The Value of Multiplication of Instances, or Pure Induction"
pages: "269–278"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "282–291"
sections: 9
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part III. Induction and Analogy*

# Chapter XX. The Value of Multiplication of Instances, or Pure Induction

## §1 (p. 269)

{{p.269}} It has often been thought that the essence of inductive argument lies in the multiplication of instances. “Where is that process of reasoning,” Hume inquired, “which from one instance draws a conclusion, so different from that which it infers from a hundred instances, that are no way different from that single instance?” I repeat that by emphasising the number of the instances Hume obscured the real object of the method. If it were strictly true that the hundred instances are no way different from the single instance, Hume would be right to wonder in what manner they can strengthen the argument. The object of increasing the number of instances arises out of the fact that we are nearly always aware of some difference between the instances, and that even where the known difference is insignificant we may suspect, especially when our knowledge of the instances is very incomplete, that there may be more. Every new instance may diminish the unessential resemblances between the instances and by introducing a new difference increase the Negative Analogy. For this reason, and for this reason only, new instances are valuable.

If our premisses comprise the body of memory and tradition which has been originally derived from direct experience, and the conclusion which we seek to establish is the Newtonian theory of the Solar System, our argument is one of Pure Induction, in so far as we support the Newtonian theory by pointing to the great number of consequences which it has in common with the facts of experience. The predictions of the Nautical Almanack are a consequence of the Newtonian theory, and these predictions are verified many thousand times a day. But even here the force of the argument largely depends, not on the mere number of these predictions, but on the knowledge {{p.270}} that the circumstances in which they are fulfilled differ widely from one another in a vast number of important respects. The variety of the circumstances, in which the Newtonian generalisation is fulfilled, rather than the number of them, is what seems to impress our reasonable faculties.

## §2 (p. 270)

I hold, then, that our object is always to increase the Negative Analogy, or, which is the same thing, to diminish the characteristics common to all the examined instances and yet not taken account of by our generalisation. Our method, however, maybe one which certainly achieves this object, or it may be one which possibly achieves it. The former of these, which is obviously the more satisfactory, may consist either in increasing our definite knowledge respecting instances examined already, or in finding additional instances respecting which definite knowledge is obtainable. The second of them consists in finding additional instances of the generalisation, about which, however, our definite knowledge may be meagre; such further instances, if our knowledge about them were more complete, would either increase or leave unchanged the Negative Analogy; in the former case they would strengthen the argument and in the latter case they would not weaken it; and they must, therefore, be allowed some weight. The two methods are not entirely distinct, because new instances, about which we have some knowledge but not much, may be known to increase the Negative Analogy a little by the first method, and suspected of increasing it further by the second.

It is characteristic of advanced scientific method to depend on the former, and of the crude unregulated induction of ordinary experience to depend on the latter. It is when our definite knowledge about the instances is limited, that we must pay attention to their number rather than to the specific differences between them, and must fall back on what I term Pure Induction.

In this chapter I investigate the conditions and the manner in which the mere repetition of instances can add to the force of the argument. The chief value of the chapter, in my judgment, is {{p.271}} negative, and consists in showing that a line of advance, which might have seemed promising, turns out to be a blind alley, and that we are thrown back on known Analogy. Pure Induction will not give us any very substantial assistance in getting to the bottom of the general inductive problem.

## §3 (p. 271)

The problem of generalisation[^271-1] by Pure Induction can be stated in the following symbolic form:

[^271-1]: In the most general sense we can regard any proposition as the generalisation of all the propositions which follow from it. For if h is any proposition, and we put φ(x) ≡ ‘x can be inferred from h’ and, f(x) ≡ x, then g(φ, f) ≡ h. Since Pure Induction consists in finding as many instances of a generalisation as possible, it is, in the widest sense, the process of strengthening the probability of any proposition by adducing numerous instances of known truths which follow from it. The argument is one of Pure Induction, therefore, in so far as the probability of a conclusion is based upon the number of independent consequences which the conclusion and the premisses have in common.

Let h represent the general à priori data of the investigation; let g represent the generalisation which we seek to establish; let x1x2 . . . xn represent instances of g.

Then x1/gh = 1, x2/gh = 1 . . . xn/gh = 1; given g, that is to say, the truth of each of its instances follows. The problem is to determine the probability g/hx1x2 . . . xn, i.e. the probability of the generalisation when n instances of it are given. Our analysis will be simplified, and nothing of fundamental importance will be lost, if we introduce the assumption that there is nothing in our à priori data which leads us to distinguish between the à priori likelihood of the different instances; we assume, that is to say, that there is no reason à priori for expecting the occurrence of any one instance with greater reliance than any other, i.e.
    x1/h = x2/h = . . . = xn/h.
Write   g/hx1x2 . . . xn = pn
and   xn+1/hx1x2 . . . xn = yn+1;
{{p.272}} then
    (pn) ÷ (pn−1) = (g/hx1 . . . xn) ÷ (g/hx1 . . . xn−1) = (gxn/hx1 . . . xn−1) ÷ (g/hx1 . . . xn−1 · xn/hx1 . . . xn−1)
    = (xn/ghx1 . . . xn−1) ÷ (xn/hx1 . . . xn−1)
    = 1/yn.
∴ (pn) ÷ (pn−1) = 1/yn , and hence pn = (1) ÷ (y1y2 . . . yn) · p0, where p0 = g/h, i.e. p0 is the à priori probability of the generalisation.

It follows, therefore, that pn > pn−1 so long as yn > 1.

Further,
    x1x2 . . . xn/h = xn/hx1x2 . . . xn−1 · x1x2 . . . xn−1/h
    = yn · x1x2 . . . xn−1/h
    = ynyn−1 . . . y1.
    ∴ pn = (p0) ÷ (y1y2 . . . yn) = (p0) ÷ (x1x2 . . . xn/h)
    = (p0) ÷ (x1x2 . . . xng/h + x1x2 . . . xnḡ/h)
    = (p0) ÷ (g/h + x1x2 . . . xn/ḡh · ḡ/h)
    = (p0) ÷ (p0 + x1x2 . . . xn/ḡh(1 − p0))

This approaches unity as a limit, if x1x2 . . . xn/ḡh · 1/p0 approaches zero as a limit, when n increases.

## §4 (p. 272)

We may now stop to consider how much this argument has proved. We have shown that if each of the instances necessarily follows from the generalisation, then each additional instance increases the probability of the generalisation, so long as the new instance {{p.273}} could not have been predicted with certainty from a knowledge of the former instances.[^273-1] This condition is the same as that which came to light when we were discussing Analogy. If the new instance were identical with one of the former instances, a knowledge of the latter would enable us to predict it. If it differs or may differ in analogy, then the condition required above is satisfied.

[^273-1]: Since pn > pn−1 so long as yn ≠ 1.

The common notion, that each successive verification of a doubtful principle strengthens it, is formally proved, therefore, without any appeal to conceptions of law or of causality. But we have not proved that this probability approaches certainty as a limit, or even that our conclusion becomes more likely than not, as the number of verifications or instances is indefinitely increased.

## §5 (p. 273)

What are the conditions which must be satisfied in order that the rate, at which the probability of the generalisation increases, may be such that it will approach certainty as a limit when the number of independent instances of it are indefinitely increased? We have already shown, as a basis for this investigation, that pn approaches the limit of certainty for a generalisation g, if, as n increases, x1x2 . . . xn/ḡh becomes small compared with p0, i.e. if the à priori probability of so many instances, assuming the falsehood of the generalisation, is small compared with the generalisation’s à priori probability. It follows, therefore, that the probability of an induction tends towards certainty as a limit, when the number of instances is increased, provided that
    xr/x1x2 . . . xr−1ḡh < 1 − ϵ
for all values of r, and p0 > η, where ϵ and η are finite probabilities, separated, that is to say, from impossibility by a value of some finite amount, however small. These conditions appear simple, but the meaning of a ‘finite probability’ requires a word of explanation.[^273-2]

[^273-2]: The proof of these conditions, which is obvious, is as follows: x1x2 . . . xn/ḡh = xn−1ḡh · x1x2 . . . xn−1/ḡh < (1 − ϵ)^n, where ϵ is finite and p0 > η where η is finite. There is always, under these conditions, some finite value of n such that both (1 − ϵ)^n and ((1 − ϵ)n) ÷ (η) are less than any given finite quantity, however small.

{{p.274}} I argued in Chapter III. that not all probabilities have an exact numerical value, and that, in the case of some, one can say no more about their relation to certainty and impossibility than that they fall short of the former and exceed the latter. There is one class of probabilities, however, which I called the numerical class, the ratio of each of whose members to certainty can be expressed by some number less than unity; and we can sometimes compare a non-numerical probability in respect of more and less with one of these numerical probabilities. This enables us to give a definition of ‘finite probability’ which is capable of application to non-numerical as well as to numerical probabilities. I define a ‘finite probability’ as one which exceeds some numerical probability, the ratio of which to certainty can be expressed by a finite number.[^274-1] The principal method, in which a probability can be proved finite by a process of argument, arises either when its conclusion can be shown to be one of a finite number of alternatives, which are between them exhaustive or, at any rate, have a finite probability, and to which the Principle of Indifference is applicable; or (more usually), when its conclusion is more probable than some hypothesis which satisfies this first condition.

[^274-1]: Hence a series of probabilities p1p2 . . . pr approaches a limit L, if, given any positive finite number ϵ however small, a positive integer n can always be found such that for all values of r greater than n the difference between L and pr is less than ϵ · γ, where γ is the measure of certainty.

## §6 (p. 274)

The conditions, which we have now established in order that the probability of a pure induction may tend towards certainty as the number of instances is increased, are (1) that xr/x1x2 . . . xr−1ḡh falls short of certainty by a finite amount for all values of r, and (2) that p0, the à priori probability of our generalisation, exceeds impossibility by a finite amount. It is easy to see that we can {{p.275}} show by an exactly similar argument that the following more general conditions are equally satisfactory:

(1) That xr/x1x2 . . . xr−1ḡh falls short of certainty by a finite amount for all values of r beyond a specified value s.

(2) That ps, the probability of the generalisation relative to a knowledge of these first s instances, exceeds impossibility by a finite amount.

In other words Pure Induction can be usefully employed to strengthen an argument if, after a certain number of instances have been examined, we have, from some other source, a finite probability in favour of the generalisation, and, assuming the generalisation is false, a finite uncertainty as to its conclusion being satisfied by the next hitherto unexamined instance which satisfies its premiss. To take an example, Pure Induction can be used to support the generalisation that the sun will rise every morning for the next million years, provided that with the experience we have actually had there are finite probabilities, however small, derived from some other source, first, in favour of the generalisation, and, second, in favour of the sun’s not rising to-morrow assuming the generalisation to be false. Given these finite probabilities, obtained otherwise, however small, then the probability can be strengthened and can tend to increase towards certainty by the mere multiplication of instances provided that these instances are so far distinct that they are not inferrible one from another.

## §7 (p. 275)

Those supposed proofs of the Inductive Principle, which are based openly or implicitly on an argument in inverse probability, are all vitiated by unjustifiable assumptions relating to the magnitude of the à priori probability p0. Jevons, for instance, avowedly assumes that we may, in the absence of special information, suppose any unexamined hypothesis to be as likely as not. It is difficult to see how such a belief, if even its most immediate implications had been properly apprehended, could have remained plausible to a mind of so sound a practical judgment as his. The arguments against it and {{p.276}} the contradictions to which it leads have been dealt with in Chapter IV. The demonstration of Laplace, which depends upon the Rule of Succession, will be discussed in Chapter XXX.

## §8 (p. 276)

The prior probability, which must always be found, before the method of pure induction can be usefully employed to support a substantial argument, is derived, I think, in most ordinary cases— with what justification it remains to discuss—from considerations of Analogy. But the conditions of valid induction as they have been enunciated above, are quite independent of analogy, and might be applicable to other types of argument. In certain cases we might feel justified in assuming directly that the necessary conditions are satisfied.

Our belief, for instance, in the validity of a logical scheme is based partly upon inductive grounds—on the number of conclusions, each seemingly true on its own account, which can be derived from the axioms—and partly on a degree of self-evidence in the axioms themselves sufficient to give them the initial probability upon which induction can build. We depend upon the initial presumption that, if a proposition appears to us to be true, this is by itself, in the absence of opposing evidence, some reason for its being as well as appearing true. We cannot deny that what appears true is sometimes false, but, unless we can assume some substantial relation of probability between the appearance and the reality of truth, the possibility of even probable knowledge is at an end.

The conception of our having some reason, though not a conclusive one, for certain beliefs, arising out of direct inspection, may prove important to the theory of epistemology. The old metaphysics has been greatly hindered by reason of its having always demanded demonstrative certainty. Much of the cogency of Hume’s criticism arises out of the assumption of methods of certainty on the part of those systems against which it was directed. The earlier realists were hampered by their not perceiving that lesser claims in the beginning might yield them what they wanted in the end. And transcendental {{p.277}} philosophy has partly arisen, I believe, through the belief that there is no knowledge on these matters short of certain knowledge, being combined with the belief that such certain knowledge of metaphysical questions is beyond the power of ordinary methods.

When we allow that probable knowledge is, nevertheless, real, a new method of argument can be introduced into metaphysical discussions. The demonstrative method can be laid on one side, and we may attempt to advance the argument by taking account of circumstances which seem to give some reason for preferring one alternative to another. Great progress may follow if the nature and reality of objects of perception,[^277-1] for instance, can be usefully investigated by methods not altogether dissimilar from those employed in science and with the prospect of obtaining as high a degree of certainty as that which belongs to some scientific conclusions; and it may conceivably be shown that a belief in the conclusions of science, enunciated in any reasonable manner however restricted, involves a preference for some metaphysical conclusions over others.

[^277-1]: A paper by Mr. G. E. Moore entitled, “The Nature and Reality of Objects of Perception,” which was published in the Proceedings of the Aristotelian Society for 1906, seems to me to apply for the first time a method somewhat resembling that which is described above.

## §9 (p. 277)

Apart from analysis, careful reflection would hardly lead us to expect that a conclusion which is based on no other than grounds of pure induction, defined as I have defined them as consisting of repetition of instances merely, could attain in this way to a high degree of probability. To this extent we ought all of us to agree with Hume. We have found that the suggestions of common sense are supported by more precise methods. Moreover, we constantly distinguish between arguments, which we call inductive, upon other grounds than the number of instances upon which they are based; and under certain conditions we regard as crucial an insignificant number of experiments. The method of pure induction may be a useful means of strengthening a probability based on some other ground. In the {{p.278}} case, however, of most scientific arguments, which would commonly be called inductive, the probability that we are right, when we make predictions on the basis of past experience, depends not so much on the number of past experiences upon which we rely, as on the degree in which the circumstances of these experiences resemble the known circumstances in which the prediction is to take effect. Scientific method, indeed, is mainly devoted to discovering means of so heightening the known analogy that we may dispense as far as possible with the methods of pure induction.

When, therefore, our previous knowledge is considerable and the analogy is good, the purely inductive part of the argument may take a very subsidiary place. But when our knowledge of the instances is slight, we may have to depend upon pure induction a good deal. In an advanced science it is a last resort,—the least satisfactory of the methods. But sometimes it must be our first resort, the method upon which we must depend in the dawn of knowledge and in fundamental inquiries where we must presuppose nothing.
