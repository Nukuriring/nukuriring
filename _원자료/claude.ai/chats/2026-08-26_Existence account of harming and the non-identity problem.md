---
title: "Existence account of harming and the non-identity problem"
uuid: cbd3d382-4204-419c-ae82-c46c7c9d4f0b
created: 2026-08-26
updated: 2026-08-26
project: ""
url: https://claude.ai/chat/cbd3d382-4204-419c-ae82-c46c7c9d4f0b
turns: 10
type: 원자료/대화
---

> 요약: **Conversation Overview**  The conversation focused on close philosophical analysis of Molly Gardner's 2015 paper "Ergo" on the existence account of harming, specifically its application to the non-identity problem. The person was working through the paper's argumentative structure, asking Claude to explain the text and then probing its logical architecture with increasingly sharp critical questions.  The discussion moved through three stages. First, Claude explained the three competing accounts of harming (comparative/counterfactual, non-comparative, and existence accounts) and how each fares across three test cases: the non-identity problem, Dim Vision, and Loss of Fortune. Second, the person correctly identified that Dim Vision is a case that troubles the non-comparative account, not the comparative account—prompting Claude to clarify that Dim Vision functions as a regression test for the existence account rather than a showcase of its improvements. Third, the person reconstructed Gardner's core argument for the non-identity case (policy X causes harmed state s; S existing without s would be better off; therefore s is a harm; therefore X is wrong) and Claude confirmed the skeleton while adding two necessary intermediate steps: the strength of reasons against harming, and the separate question of comparing alternative policies.  The most analytically productive exchange came when the person asked whether the existence condition does any work in Dim Vision. Claude confirmed it does not—the existence condition is a non-identity-specific device that only activates when the nearest possible world without the bad state would be a world of non-existence. In Dim Vision, Jones exists across all relevant worlds, so the condition has nothing to exclude. The actual work in Dim Vision is done by shifting the negation target from act to state, combined with nearest-world selection. The person then drew the correct conclusion: Dim Vision is not a useful case for understanding what the existence account improves over the comparative account; it is only useful for ruling out the non-comparative account as a cheap alternative. The person demonstrated a preference for precise analytical dissection over expository summary, and pushed back when Claude's framing obscured which theoretical device was doing which work.

## 영진 · 2026-08-26T04:37

In the previous section I introduced the existence account of harming, defended its tenets, and showed how the account can vindicate the harm-based approach to the non-identity problem. In this section I will first explain how the existence account of harming gets the right results in the cases that created trouble for the non-comparative account of harming. I will also consider another objection to the existence account. In response to this objection, I will defend a principle about the strength of the reason against harming. That principle, when conjoined with the existence account, will help diffuse the objection. Here is why the existence account of harming is immune to the problems illustrated by Dim Vision and Loss of Fortune. Recall that in Dim Vision, Dr. Smith causes Jones to be in a state of dim vision. Such a state appears to be bad for Jones, so if the non-comparative account of harming is true, then Dr. Smith harms Jones. However, the existence account of harming does not imply that Dr. Smith harms Jones. Consider the following counterfactual: 17. A theory is committed to the existence of impersonal value if it holds, for example, that a state of affairs containing five people with headaches is ceteris paribus worse than a state of affairs containing five different people, only one of whom has a headache. The former state of affairs is not worse for any particular individual, so if it is worse at all, the worseness must be grounded in impersonal value. Utilitarianism, Rossian pluralism, and any other normative theories that enjoin us to consider aggregated well-being appear to be committed to the claim that well-being has impersonal value. 18. Indeed, the notion that consequentialists are generally concerned with impersonal value, rather than personal value, can explain why many consequentialists are reluctant to acknowledge either the existence or importance of harm at all. See Bradley (2012), who argues that our moral theories should do away with the concept of harm, and Norcross (2005), who writes, “for the purposes of ethical theorizing, harm and benefit do not have the kind of metaphysical grounding required to play fundamental roles in ethical theory, nor do judgments of harm or benefit make any distinctive contributions to reasons for action” (171–172). 438 • Molly Gardner Ergo • vol. 2, no. 17 • 2015 (D) If it were true that both Jones existed and he did not have dim vision, then Jones would be better off in some respect. D states a necessary condition for dim vision’s being a harm for Jones. However, D is false. If Jones were to exist without dim vision, then Dr. Smith would not have operated, and Jones would be completely blind; that would result in Jones’s being worse off in some respect. The state that Dr. Smith causes Jones to be in fails to satisfy a necessary condition for being a harm, and since it is not a harm, Dr. Smith does not harm Jones in causing it. This result may seem worrisome, for as I noted in Section 2, the state of dim vision appears to be non-comparatively bad for Jones. However, it is easy to explain away the appearance of badness. What is actually bad for Jones is not dim vision, but the state of being unable to see very well. And sure enough, the existence account of harming can justify the claim that the state of being unable to see very well is a harm for Jones. Consider the following counterfactual: (D2) If it were true that both Jones existed and he were not unable to see very well, then Jones would be better off in some respect. D2 is true. To say that Jones is not unable to see very well is to say that Jones is able to see very well. And if Jones were to see very well, then he would indeed be better off in some respect. Assuming that Jones’s ability to see very well is a respect in which he can be intrinsically better off, the existence account of harming implies that being unable to see very well is a harm, but Dr. Smith did not cause it. On



설명부탁

## Claude · 2026-08-26T04:40

## 이 대목의 위치

몰리 가드너(Molly Gardner)가 비동일성 문제(non-identity problem)를 위해(harm) 개념으로 해결하려는 논문의 한 절 첫머리입니다. 앞 절에서 자신의 **존재 설명(the existence account of harming)** 을 제시하고 옹호했으므로, 이 절은 그 설명이 경쟁 이론을 좌초시켰던 반례들을 어떻게 통과하는지 보여 주는 순서로 진행됩니다.

붙여 주신 텍스트 중간에 각주 17, 18과 면주(438 • Molly Gardner)가 끼어들어 있습니다. 본론은 "Consider the following counterfactual: 17."에서 끊겼다가 "(D) If it were true that..."에서 이어집니다.

세 이론을 먼저 갈라 두면 논의가 선명해집니다.

- **반사실적 비교 설명**: 그 행위가 없었더라면 당사자가 더 나은 처지에 있었을 경우에만 위해입니다. 비동일성 사례에서는 그 행위가 없었더라면 당사자가 아예 존재하지 않았을 것이므로 비교 항이 성립하지 않고, 따라서 위해를 인정하지 못합니다.
- **비비교적 설명**: 그 행위가 당사자에게 나쁜 상태를 야기했다면 위해입니다. 비존재와 비교할 필요가 없어서 비동일성 사례를 다룰 수 있지만, Dim Vision과 Loss of Fortune에서 무너집니다.
- **존재 설명**: 어떤 사건 e가 상태 s를 야기하고, 「S가 존재하면서 s가 성립하지 않는다면 S는 어떤 측면에서 더 나은 처지에 있을 것이다」라는 반사실 조건문이 참일 때, e는 S에게 위해를 가합니다.

존재 설명의 핵심은 반사실 조건문의 전건에 **「S가 존재한다」를 명시적으로 못 박아 넣었다**는 데 있습니다. 존재를 고정한 채 상태만 제거하고 비교하기 때문에, 비교 항이 비존재로 미끄러지지 않습니다. 비교의 단위가 「행위의 부재」가 아니라 「상태의 부재」라는 점이 결정적입니다.

## Dim Vision에서 (D)가 거짓인 이유

스미스 의사가 수술을 하여 존스를 흐린 시야 상태에 놓았고, 수술을 하지 않았더라면 존스는 완전히 실명했을 상황입니다. 비비교적 설명은 흐린 시야가 그 자체로 존스에게 나쁜 상태라는 이유로 스미스가 존스에게 위해를 가했다고 판정하는데, 이 판정은 직관에 어긋납니다.

존재 설명은 다음 조건문을 평가합니다.

> (D) 존스가 존재하면서 흐린 시야를 갖지 않는다면, 존스는 어떤 측면에서 더 나은 처지에 있을 것이다.

「흐린 시야를 갖지 않음」이 성립하는 가장 가까운 세계는 스미스가 수술하지 않은 세계이고, 그 세계에서 존스는 완전히 실명한 상태입니다. 그러므로 존스는 더 나은 처지에 있지 않으며, (D)는 거짓입니다. 위해가 되기 위한 필요조건이 충족되지 않으므로 흐린 시야는 위해가 아니고, 그것을 야기한 스미스도 위해자가 아닙니다.

## 겉보기 나쁨을 해소하는 재서술

여기서 곧바로 반문이 생깁니다. 흐린 시야는 아무리 보아도 존스에게 나쁜 상태로 보이는데, 존재 설명은 그 나쁨을 부정하는 것처럼 보이기 때문입니다. 가드너는 나쁨 자체를 부정하지 않고 **나쁨이 귀속되는 상태를 다시 지정**하는 방식으로 대응합니다. 존스에게 실제로 나쁜 상태는 「흐린 시야」가 아니라 「잘 볼 수 없음」이라는 것입니다.

> (D2) 존스가 존재하면서 잘 볼 수 없지 않다면, 존스는 어떤 측면에서 더 나은 처지에 있을 것이다.

「잘 볼 수 없지 않다」는 곧 「잘 볼 수 있다」를 뜻하고, 잘 볼 수 있는 존스는 분명히 더 나은 처지에 있습니다. 따라서 (D2)는 참이고, 「잘 볼 수 없음」은 위해에 해당합니다. 그러나 그 상태를 야기한 것은 스미스가 아닙니다. 스미스가 야기한 것은 완전 실명에서 흐린 시야로의 이행이며, 「잘 볼 수 없음」은 그 이전부터 성립해 있던 상태입니다.

## 논증의 관절

**첫째, 부정 연산의 범위 차이가 두 판정을 갈랐습니다.** 「흐린 시야」는 결정적(determinate) 상태이므로 그것의 부정은 더 좋은 쪽(정상 시력)과 더 나쁜 쪽(완전 실명)을 모두 허용합니다. 반면 「잘 볼 수 없음」은 결여 형식의 상태이므로 그것의 부정은 곧바로 「잘 볼 수 있음」을 함의합니다. 같은 사태를 어떤 술어로 기술하느냐에 따라 반사실 조건문의 진리치가 뒤집히는 구조입니다.

**둘째, 존재 설명은 두 조건을 서로 다른 관계에 걸어 둡니다.** 인과 조건은 사건과 상태의 관계에, 반사실 조건은 상태와 복지의 관계에 각각 부과됩니다. 그래서 「위해가 존재하는가」와 「누가 그 위해를 야기했는가」가 분리되고, Dim Vision에서는 위해는 존재하되 스미스는 그 야기자가 아니라는 판정이 가능해집니다.

**셋째, 재서술 전략에는 대가가 따릅니다.** 상태를 어떻게 개별화하느냐에 따라 판정이 달라지므로, 자의적 재서술을 막을 독립적 기준이 필요합니다. 가드너는 마지막 문장에서 「존스가 잘 볼 수 있음이 그가 내재적으로 더 나아질 수 있는 측면이라고 가정한다면」이라는 단서를 달아, 복지 이론이 인정하는 **내재적 측면**으로 후보 상태를 제한하는 방식으로 이 부담을 감당하려 합니다.

Loss of Fortune은 언급만 되고 논의되지 않았는데, 문맥상 반대 방향의 반례로 보입니다. 재산을 빼앗긴 뒤의 상태 자체는 내재적으로 나쁘지 않으므로 비비교적 설명은 위해를 포착하지 못하지만, 존재 설명은 그 상태가 없었더라면 더 나았으리라는 조건문이 참이므로 위해를 인정할 수 있습니다. 즉 두 사례가 각각 과잉 산출과 과소 산출을 보여 주는 짝이라는 추정입니다.

## 끼어든 각주와 예고된 논의

각주 17은 **비인격적 가치(impersonal value)** 를 정의합니다. 다섯 명이 두통을 앓는 상황이 다른 다섯 명 중 한 명만 두통을 앓는 상황보다 더 나쁘다고 판정하는 이론은 비인격적 가치에 개입한 것입니다. 전자가 어떤 특정 개인에게 더 나쁜 것은 아니므로, 더 나쁨의 근거가 인격적 가치일 수 없기 때문입니다. 공리주의와 로스식 다원주의처럼 복지의 총합을 고려하라고 요구하는 이론들이 여기에 해당합니다. 각주 18은 그 귀결을 짚습니다. 결과주의자들이 인격적 가치보다 비인격적 가치에 관심을 두기 때문에 위해 개념 자체를 인정하기 꺼린다는 것이며, 브래들리(2012)는 도덕 이론에서 위해 개념을 폐기하자고 주장하고, 노크로스(2005)는 위해와 이익이 윤리 이론의 근본 역할을 맡을 형이상학적 근거를 갖지 못하며 행위 이유에 고유하게 기여하지도 않는다고 주장합니다. 가드너 자신의 전략이 개인에 대한 위해에 정박한다는 점을 대비시키는 배경 설명입니다.

마지막으로 첫 문단에서 예고된 **「위해에 반대하는 이유의 강도에 관한 원리」** 는 아직 나오지 않았습니다. 「무엇이 위해인가」와 「그 위해에 반대하는 이유가 얼마나 강한가」를 분리하는 이층 구조로 예상되는데, 존재 설명이 위해를 지나치게 많이 산출한다는 반론을, 위해 판정을 유지하면서 이유의 강도를 차등화하는 방식으로 흡수하려는 수순으로 보입니다. 다만 이 부분은 붙여 주신 범위 밖이라 추정입니다.

## 영진 · 2026-08-26T04:47

근데 dim vision자체는 원래 비교적 해악이 쉽게 해결하는 case아님?

## Claude · 2026-08-26T04:48

맞습니다. Dim Vision은 비교적 설명의 반례가 아니라 **비비교적 설명의 반례**입니다. 가드너 본인도 그렇게 쓰고 있습니다. 인용하신 첫 문단의 "the cases that created trouble for the non-comparative account of harming"이 바로 Dim Vision과 Loss of Fortune을 가리킵니다. 제가 앞의 설명에서 이 배치를 충분히 앞세우지 않았습니다.

## 세 이론과 세 사례의 배치

| | 비동일성 | Dim Vision | Loss of Fortune |
|---|---|---|---|
| 반사실적 비교 설명 | ✗ 위해 없음 | ○ 위해 없음 | ○ 위해 있음 |
| 비비교적 설명 | ○ 위해 있음 | ✗ 위해 있음 | ✗ 위해 없음 |
| 존재 설명 | ○ | ○ | ○ |

비교적 설명은 Dim Vision을 손쉽게 처리합니다. 수술이 없었더라면 존스는 완전히 실명했을 것이므로 더 나은 처지에 있지 않았고, 따라서 위해가 아닙니다. 이 설명이 무너지는 자리는 오직 비동일성뿐입니다. 반대로 비비교적 설명은 비동일성을 살리려고 비교 항을 아예 없앤 대가로 Dim Vision과 Loss of Fortune을 잃습니다.

## 그렇다면 왜 굳이 통과시켜 보는가

Dim Vision은 가드너에게 풀어야 할 난제가 아니라 **회귀 시험**입니다. 논증의 형세가 이렇게 짜여 있습니다. 위해 기반 접근으로 비동일성을 해결하려면 비교적 설명을 그대로 쓸 수 없고, 그것을 손보는 가장 손쉬운 방법이 비비교적 설명으로 갈아타는 것인데, 그 길목을 막고 있는 것이 Dim Vision과 Loss of Fortune입니다. 즉 이 두 사례는 「값싼 수정을 배제하는 제약」으로 기능합니다. 새 이론이 비동일성을 얻으면서 이 두 사례를 되잃지 않았음을 보이는 절차가 이 절의 앞부분입니다.

## 다만 통과가 자명하지는 않습니다

존재 설명이 비교적 설명과 갈라지는 지점은 두 곳입니다.

1. 반사실 조건문의 전건에 「S가 존재한다」를 고정합니다. 이것이 비동일성을 얻는 장치입니다.
2. 부정하는 대상을 **사건에서 상태로** 옮깁니다. 비교적 설명은 「수술이 없었더라면」을 묻지만, 존재 설명은 「흐린 시야가 성립하지 않았더라면」을 묻습니다.

Dim Vision에서 위험한 것은 2번입니다. 사건을 부정하면 실명 세계가 곧바로 지정되지만, 상태를 부정하면 실명 세계와 정상 시력 세계가 모두 후보로 열립니다. 정상 시력 세계가 선택되는 순간 (D)는 참이 되고, 존재 설명은 비비교적 설명과 똑같이 스미스를 위해자로 판정하게 됩니다. 가드너가 (D)를 거짓으로 확정할 수 있는 근거는 「흐린 시야가 없는 최근접 세계는 스미스가 수술하지 않은 세계이다」라는 유사성 판단뿐입니다. 그러므로 통과는 자동으로 보장되지 않고, 최근접 세계 선택이라는 실질적 전제에 의존합니다.

## 이 의존이 곧 D2의 취약점입니다

(D)에서는 최근접 세계 추론으로 「흐린 시야 없음」을 실명으로 채우고, (D2)에서는 논리적 동치로 「잘 볼 수 없지 않음」을 「잘 볼 수 있음」으로 바로 환원합니다. 두 조건문에서 부정을 처리하는 방식이 서로 다릅니다. 결여 형식의 술어는 부정이 곧장 긍정 상태를 함의하지만, 결정적 술어는 부정이 여러 세계를 열어 두기 때문에 생기는 비대칭입니다. 재서술 전략이 이 비대칭을 이용하는 이상, 상태를 어떻게 개별화하고 어떤 술어로 기술할지를 통제할 독립 기준이 없다면 판정은 기술 방식에 따라 흔들립니다.

지문 소재로 재단하실 생각이라면, 이 비대칭이 사실 가장 값나가는 자리입니다. Dim Vision 통과 자체는 결과 확인에 그치지만, 「같은 사태를 어떤 술어로 잘라 내느냐에 따라 반사실 조건문의 진리치가 뒤집힌다」는 구조는 〈보기〉 탄약으로 쓸 만한 논점입니다.

## 영진 · 2026-08-26T04:53

아니 그러면 여기서 Existence가 일을 하는거야?

## Claude · 2026-08-26T04:54

안 합니다. 정확한 지적입니다. Dim Vision에서 존재 조건은 충족되기는 하지만 아무것도 가려내지 못합니다.

## 두 장치를 분리해야 합니다

존재 설명에는 비교적 설명과 갈라지는 장치가 두 개 들어 있는데, 이름은 하나만 반영하고 있습니다.

**(가) 상태 부정**: 부정 대상을 행위에서 상태로 옮깁니다. 「수술이 없었더라면」이 아니라 「흐린 시야가 성립하지 않았더라면」을 묻습니다.

**(나) 존재 고정**: 전건에 「S가 존재한다」를 연언으로 못 박습니다.

(나)는 적극적인 판정 원리가 아니라 **비교 세계의 정의역에 걸어 둔 제한**입니다. 상태를 부정했을 때 최근접 세계가 당사자의 비존재 세계로 미끄러지는 경우에만 발동하고, 그렇지 않으면 아무 일도 하지 않습니다.

비동일성 사례에서는 이 제한이 실제로 물립니다. 페블스가 실명하지 않은 최근접 세계는 윌마가 임신을 미뤄 페블스가 존재하지 않는 세계이고, 존재 고정이 바로 그 세계를 정의역에서 배제합니다. 반면 Dim Vision에서 존스는 모든 관련 세계에 존재하므로, 배제할 세계가 애초에 없습니다. Loss of Fortune도 사정이 같습니다. 즉 (나)는 비동일성 전용 장치입니다.

## 그렇다면 (D)를 거짓으로 만든 것은 무엇인가

(가)와 최근접 세계 판단입니다. 「존스에게 흐린 시야가 없다」가 성립하는 가장 가까운 세계는 스미스가 수술하지 않은 세계이고, 거기서 존스는 완전히 실명해 있습니다.

그런데 이 추론의 실질은 「수술이 없었더라면」을 다시 세운 것입니다. 존재 설명은 Dim Vision을 **비교적 설명의 판정을 재도출하는 방식으로** 통과합니다. 이 사례에서만큼은 비교적 설명처럼 행동하는 셈입니다.

## 이것이 결함인지

설계 의도로 보면 결함이 아닙니다. 비교적 설명이 이미 옳은 답을 내는 자리에서는 그 답을 그대로 물려받고, 비교 항이 비존재로 붕괴하는 자리에서만 개입하는 **보수적 확장**이기 때문입니다. Dim Vision 통과는 새 이론의 성과가 아니라 기존 성과를 잃지 않았음을 확인하는 절차이고, 그 확인을 위해 존재 조건이 놀고 있는 것은 정상입니다.

다만 부담이 어디로 옮겨 갔는지는 분명해집니다.

**첫째, (가)가 스스로 문제를 만들어 냈습니다.** 비교적 설명은 행위를 부정하므로 「수술하지 않음」이라는 세계가 하나로 확정되고 다의성이 없습니다. 상태를 부정하는 순간 실명 세계와 정상 시력 세계가 함께 열리고, 그 다의성을 최근접 세계 판단으로 봉합해야 합니다. (D)와 (D2)의 갈림은 이 봉합 방식이 술어에 따라 달라진 결과입니다.

**둘째, 전건에 무엇을 고정할지가 원리 문제로 승격됩니다.** 존재를 고정하기로 한 이상, 왜 존재만 고정하는지 답해야 합니다. 「스미스가 수술했다」를 함께 고정하면 (D)는 참이 되고 스미스는 위해자가 됩니다. 「존스는 완전 실명 상태였다」를 고정해도 마찬가지입니다. 가드너가 기댈 수 있는 방어는 존재 고정이 사후 조정이 아니라 도식에 미리 명시된 항목이며 모든 사례에 균일하게 적용된다는 점뿐입니다. 이 방어가 성립하려면 도식 자체가 독립적으로 정당화되어야 합니다.

**셋째, 비동일성과 Dim Vision에서 최근접 세계를 대하는 태도가 반대입니다.** 앞에서는 최근접 세계를 명시적으로 기각하고, 뒤에서는 최근접 세계를 그대로 채택합니다. 두 처리를 가르는 것이 존재 고정 조항 하나라면, 그 조항의 정당화가 이론 전체를 떠받치게 됩니다.

정리하면 이렇습니다. 존재 조건은 비동일성에서만 일하고, Dim Vision과 Loss of Fortune에서 일하는 것은 상태 부정과 최근접 세계 판단입니다. 이론의 이름이 붙은 장치와 이 절에서 실제로 작동하는 장치가 서로 다릅니다.

## 영진 · 2026-08-26T04:55

그니까 정책 X로 인해 태어난 사람들이 피해를 입은 상태라면, 그들이 존재하면서 그러한 나쁨이 없었다면 더 나았을 거니까, 그 상태는 해악이고, X가 그 해악을 초래했으니 나쁘다는거지?

## Claude · 2026-08-26T04:55

네, 골격은 정확합니다. 다만 마지막 한 걸음에 잘라 넣을 마디가 두 개 있습니다.

## 재구성이 맞는 부분

정책 X가 사람 S를 존재하게 하면서 나쁜 상태 s에 놓았을 때,

1. 「S가 존재하고 s가 성립하지 않는다면 S는 어떤 측면에서 더 나은 처지에 있을 것이다」가 참입니다. 존재를 고정했으므로, s가 없는 최근접 세계가 S의 비존재 세계로 미끄러지는 일이 차단됩니다.
2. 따라서 s는 S에 대한 위해입니다.
3. X가 s를 야기했으므로, X는 S에게 위해를 가했습니다.

여기까지가 존재 설명이 산출하는 결론이고, 비동일성 문제를 위해 기반으로 다루려던 목표는 이 지점에서 달성됩니다. 비교적 설명이 「X가 없었더라면 S는 존재하지 않았고, 비존재보다 나쁘지는 않다」에서 멈추던 자리를 통과한 것입니다.

## 잘라 넣어야 할 두 마디

**첫째, 「해악이다」와 「나쁘다」 사이에 이유의 강도가 들어갑니다.** 위해가 성립한다는 판정은 X에 반대하는 이유가 있다는 것까지만 보증하고, 그 이유가 X를 그르게 만들 만큼 강한지는 별개입니다. 인용하신 첫 문단에서 가드너가 예고한 「위해에 반대하는 이유의 강도에 관한 원리」가 정확히 이 마디를 메우려는 장치입니다. 반론자가 「그 사람은 존재하는 편이 낫고 삶 전체로는 살 만하다」고 응수할 때, 가드너는 위해 판정을 취소하는 대신 이유의 강도를 조정해서 흡수하려는 것으로 보입니다. 즉 「위해다, 그러나 이 경우 반대 이유는 상쇄된다」는 형태가 가능해집니다.

**둘째, 그 사람에게 위해라는 판정만으로는 정책 비교가 끝나지 않습니다.** 비동일성 문제의 원래 물음은 「X가 그 사람에게 나쁜가」가 아니라 「X와 Y 중 무엇을 택해야 하는가」입니다. Y를 택하면 S가 아니라 T가 태어나고, 존재 설명은 X 안의 위해를 짚어 줄 뿐 X와 Y를 저울에 올려 주지는 않습니다. 각주 17에서 비인격적 가치를 정의해 둔 이유가 여기에 있습니다. 총합 비교로 답하는 길을 명시적으로 구분해 두고, 자신은 인격적 위해에 정박하는 노선임을 밝히는 배치입니다.

## 상태 개별화 부담은 여기서도 그대로입니다

「그러한 나쁨」을 어떤 술어로 잡느냐에 따라 1번의 진리치가 갈립니다. 「잘 볼 수 없음」처럼 결여 형식으로 잡으면 부정이 곧장 개선을 함의해서 조건문이 참이 되지만, 「흐린 시야」처럼 결정적 상태로 잡으면 부정이 여러 세계를 열고 최근접 세계가 더 나쁜 쪽일 수 있습니다. 정책 사례에서도 마찬가지여서, 「S가 실명 상태에 있음」으로 잡느냐 「S가 볼 수 없음」으로 잡느냐가 판정을 좌우합니다. 가드너가 내재적 복지 측면으로 후보 상태를 제한한 것이 이 부담에 대한 대응인데, 앞 답변에서 말씀드린 대로 이 제한이 자의적 재서술을 충분히 막는지는 별도로 따져야 합니다.

정리하면, 재구성하신 3단은 존재 설명의 산출 구조로서 옳고, 그 뒤에 「이유의 강도」와 「대안 정책과의 비교」가 이어져야 규범적 결론에 닿습니다.

## 영진 · 2026-08-26T04:56

근데 그러면 존재 설명을 비교적 설명에서 무엇을 개선한 것인지 보려면 dim vision은 별로 유의미하지 않네?

## Claude · 2026-08-26T04:56

네, 그 방향의 물음에는 Dim Vision이 기여하지 않습니다. 다만 사례가 무의미한 것은 아니라, **묻는 방향에 따라 하는 일이 다릅니다.**

## 방향을 나누면

**개선 방향(비교적 설명 → 존재 설명)**: 여기서 유의미한 사례는 비동일성뿐입니다. 두 이론이 갈리는 곳이 그곳밖에 없기 때문입니다. Dim Vision과 Loss of Fortune에서는 판정도 같고, 앞 답변에서 확인한 대로 그 판정에 이르는 실질도 같습니다. 비교적 설명은 이미 만점이라 개선의 여지 자체가 없습니다.

**대안 배제 방향(비비교적 설명 ✗ 존재 설명)**: 여기서는 Dim Vision이 핵심입니다. 비동일성을 얻으려고 비교 항을 통째로 버리는 값싼 길이 있는데, 그 길을 막는 것이 이 사례입니다.

## 그런데 이 둘은 같은 논증의 두 축입니다

가드너가 세워야 하는 명제는 「존재 설명이 비교적 설명보다 낫다」가 아니라 **「비동일성을 해결하면서 Dim Vision을 잃지 않는 이론이 존재 설명이다」**입니다. 이 명제는 두 사례가 함께 있어야 성립합니다.

- 비동일성만 쓰면, 비비교적 설명도 통과하므로 존재 설명을 채택할 이유가 없습니다.
- Dim Vision만 쓰면, 비교적 설명도 통과하므로 역시 채택할 이유가 없습니다.

두 사례가 각각 한 경쟁자씩 떨어뜨리고, 존재 설명만 둘을 동시에 통과합니다. **개선 폭이 아니라 통과 조합이 논증의 단위**입니다. 그래서 Dim Vision은 존재 설명의 우월성을 보여 주는 사례가 아니라, 비교적 설명을 버리고 나서도 되찾아야 하는 자산의 목록입니다.

## 이 구도에서 실제로 물어야 할 것

「무엇을 개선했는가」보다 **「비동일성을 얻는 대가로 무엇을 새로 떠안았는가」**가 남는 물음입니다. 앞에서 짚은 것들이 그 대가입니다.

첫째, 부정 대상을 행위에서 상태로 옮긴 탓에 상태 개별화 부담이 생겼습니다. 비교적 설명에는 없던 문제입니다. 둘째, 전건에 존재만 고정하는 선택을 정당화해야 합니다. 셋째, (D)에서는 최근접 세계를 채택하고 비동일성에서는 기각하는 비대칭을 지탱해야 합니다.

즉 개선 목록은 항목 하나(비동일성)이고, 부담 목록은 그보다 깁니다. 이 이론의 값어치는 「비동일성 해결이 그 부담을 지불할 만한가」에 달려 있습니다.

## 지문 설계 쪽으로 보면

이 구조는 그대로 문항 재료가 됩니다. 세 이론 × 세 사례의 판정표는 〈보기〉 격자로 재단하기 좋고, 「Dim Vision에서 존재 조건이 판정에 관여하는가」는 언더리딩을 걸러 내는 선지로 쓸 만합니다. 표면적으로는 존재 설명이 통과한 사례로 제시되어 있어서, 존재 조건이 그 통과에 기여했다고 읽기 쉬운 자리이기 때문입니다.
