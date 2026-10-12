---
book: "Keynes, A Treatise on Probability (1921)"
part: "Part V. The Foundations of Statistical Inference"
chapter: "Chapter XXVII"
title: "The Nature of Statistical Inference"
pages: "371–375"   # 이 PDF(PG판)에 인쇄된 쪽수
pdf_pages: "384–388"
sections: 5
source: "John Maynard Keynes, A Treatise on Probability (London: Macmillan, 1921). Project Gutenberg eBook #32625 (LaTeX/PDF edition, 2014)"
---
*Part V. The Foundations of Statistical Inference*

# Chapter XXVII. The Nature of Statistical Inference

## §1 (p. 371)

{{p.371}} The Theory of Statistics, as it is now understood,[^371-1] can be divided into two parts which are for many purposes better kept distinct. The first function of the theory is purely descriptive. It devises numerical and diagrammatic methods by which certain salient characteristics of large groups of phenomena can be briefly described; and it provides formulae by the aid of which we can measure or summarise the variations in some particular character which we have observed over a long series of events or instances. The second function of the theory is inductive. It seeks to extend its description of certain characteristics of observed events to the corresponding characteristics of other events which have not been observed. This part of the subject may be called the Theory of Statistical Inference; and it is this which is closely bound up with the theory of probability.

[^371-1]: See Yule, Introduction to Statistics, pp. 1–5, for a very interesting account of the evolution of the meaning of the term statistics.

## §2 (p. 371)

The union of these two distinct theories in a single science is natural. If, as is generally the case, the development of some inductive conclusion which shall go beyond the actually observed instances is our ultimate object, we naturally choose those modes of description, while we are engaged in our preliminary investigation, which are most capable of extension beyond the particular instances which they primarily describe. But this union is also the occasion of a great deal of confusion. The statistician, who is mainly interested in the technical methods of his science, is less concerned to discover the precise conditions in which a description can be legitimately extended by induction. He slips somewhat easily from one to the other, and having found a complete and satisfactory mode of description he may take less pains over the transitional argument, which is to permit him to use this description for the purposes of generalisation.

{{p.372}} One or two examples will show how easy it is to slip from description into generalisation. Suppose that we have a series of similar objects one of the characteristics of which is under observation;—a number of persons, for example, whose age at death has been recorded. We note the proportion who die at each age, and plot a diagram which displays these facts graphically. We then determine by some method of curve fitting a mathematical frequency curve which passes with close approximation through the points of our diagram. If we are given the equation to this curve, the number of persons who are comprised in the statistical series, and the degree of approximation (whether to the nearest year or month) with which the actual age has been recorded, we have a very complete and succinct account of one particular characteristic of what may constitute a very large mass of individual records. In providing this comprehensive description the statistician has fulfilled his first function. But in determining the accuracy with which this frequency curve can be employed to determine the probability of death at a given age in the population at large, he must pay attention to a new class of considerations and must display a different kind of capacity. He must take account of whatever extraneous knowledge may be available regarding the sample of the population which came under observation, and of the mode and conditions of the observations themselves. Much of this may be of a vague kind, and most of it will be necessarily incapable of exact, numerical, or statistical treatment. He is faced, in fact, with the normal problems of inductive science, one of the data, which must be taken into account, being given in a convenient and manageable form by the methods of descriptive statistics.

Or suppose, again, that we are given, over a series of years, the marriage rate and the output of the harvest in a certain area of population. We wish to determine whether there is any apparent degree of correspondence between the variations of the two within this field of observation. It is technically difficult to measure such degree of correspondence as may appear to exist between the variations in {{p.373}} two series, the terms of which are in some manner associated in couples,—by coincidence, in this case, of time and place. By the method of correlation tables and correlation coefficients the descriptive statistician is able to effect this object, and to present the inductive scientist with a highly significant part of his data in a compact and instructive form. But the statistician has not, in calculating these coefficients of observed correlation, covered the whole ground of which the inductive scientist must take cognisance. He has recorded the results of the observations in circumstances where they cannot be recorded so clearly without the aid of technical methods; but the precise nature of the conditions in which the observations took place and the numerous other considerations of one sort or another, of which we must take account when we wish to generalise, are not usually susceptible of numerical or statistical expression.

The truth of this is obvious; yet, not unnaturally, the more complicated and technical the preliminary statistical investigations become, the more prone inquirers are to mistake the statistical description for an inductive generalisation.[^373-1] This tendency, which has existed in some degree, as, I think, the whole history of the subject shows, from the eighteenth century down to the present time, has been further encouraged by the terminology in ordinary use. For several statistical coefficients are given the same name when they are used for purely descriptive purposes, as when corresponding coefficients are used to measure the force or the precision of an induction. The term ‘probable error,’ for example, is used both for the purpose of supplementing and improving a statistical description, and for the purpose of indicating the precision of some generalisation. The term ‘correlation’ itself is used both to describe an observed characteristic of particular phenomena and in the enunciation of an inductive law {{p.374}} which relates to phenomena in general.

[^373-1]: Cf. Whitehead, Introduction to Mathematics, p. 27: “There is no more common error than to assume that, because prolonged and accurate mathematical calculations have been made, the application of the result to some fact of nature is absolutely certain.”

## §3 (p. 374)

I have been at pains to enforce this contrast between statistical description and statistical induction, because the chapters which follow are to be entirely about the latter, whereas nearly all statistical treatises are mainly concerned with the former. My object will be to analyse, so far as I can, the logical basis of statistical modes of argument. This involves a double task. To mark down those which are invalid amongst arguments having the support of authority is relatively easy. The other branch of our investigation, namely, to analyse the ground of validity in the case of those arguments the force of which all of us do in fact admit, presents the same kind of fundamental difficulties as we met with in the case of Induction.

## §4 (p. 374)

The arguments with which we have to deal fall into three main classes:

(i.) Given the probability relative to certain evidence of each of a series of events, what are the probabilities, relative to the same evidence, of various proportionate frequencies of occurrence for the events over the whole series? Or more briefly, how often may we expect an event to happen over a series of occasions, given its probability on each occasion?

(ii.) Given the frequency with which an event has occurred on a series of occasions, with what probability may we expect it on a further occasion?

(iii.) Given the frequency with which an event has occurred on a series of occasions, with what frequency may we probably expect it on a further series of occasions?

In the first type of argument we seek to infer an unknown statistical frequency from an à priori probability. In the second type we are engaged on the inverse operation, and seek to base the calculation of a probability on an observed statistical frequency. In the third type we seek to pass from an observed statistical frequency, not merely to the probability of an individual occurrence, but to the probable values of other unknown statistical frequencies.

{{p.375}} Each of these types of argument can be further complicated by being applied not simply to the occurrence of a simple event but to the concurrence under given conditions of two or more events. When this two or more dimensional classification replaces the one dimensional, the theory becomes what is sometimes termed Correlation, as distinguished from simple Statistical Frequency.

## §5 (p. 375)

In Chapter XXVIII. I touch briefly on the observed phenomena which have given rise to the so-called Law of Great Numbers, and the discovery of which first set statistical investigation going. In Chapter XXIX. the first type of argument, as classified above, is analysed, and the conditions which are required for its validity are stated. The crucial problem of attacking the second and third types of argument is the subject of my concluding chapters.
