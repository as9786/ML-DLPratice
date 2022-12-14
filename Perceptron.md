# THE PERCEPTRON: A PROBABILISTIC MODEL FOR INFORMATION STORAGE AND ORGANIZATION IN THE BRAIN
- 지각 인식, 일반화, 회상 그리고 사고에 대한 고등 유기체의 능력을 이해하려면 아래의 3가지 근본적인 질문에 대한 답을 해야함
1. 물리적 세계에 대한 정보는 생물학적 시스템에 의해 어떻게 감지되는가?
2. 정보는 어떤 형태로 기억되는가?(정보 보유 방법)
3. 메모리에 포함된 정보가 인식 및 행동에 어떠한 영향을 미치는가?
- 해당 논문은 2번과 3번에 대해서 주로 다룸
- 2번 질문에 관하여 두 가지 입장
1. 감각 정보의 저장이 감각 자극과 저장된 패턴 사이의 일대일 매핑과 함께 코딩된 표현 또는 이미지의 형태
- 신경계를 이해하면 유기체가 남긴 기억의 흔적에서 원래의 감각 패턴을 재구성함으로써 유기체가 무엇을 기억하는지 발견해야 함
- 단순성과 준비성 면에서 매력적 -> 많은 신경망 모델 개발
2. 영국의 경험주의
- 자극의 이미지가 전혀 기록되지 않을 수 있음
- 단순히 활동 중심들 사이의 새로운 연결 형태를 취하는 복잡한 교환망으로 작용한다는 추측에 반함
- 반응은 행동보다는 idea
- 자극이 기억으로 단순하게 매핑되는 것이 결코 없음
- 정보는 지형적 정보가 아닌 연결이나 연관성에 포함

- 3번에 관한 두 가지 가설
1. coded memory theorists
- 현재의 자극이 이전에 보였는지를 판단하고 유기체의 적절한 반응을 결정하기 위해 일부 자극의 인식은 감각 패턴과 저장 내용을 비교 및 일치
2. 경험주의 전통
- 2번 질문에 대한 답과 결합
- 저장된 정보는 신경계의 새로운 연결 또는 전달 경로의 형태를 취함 -> 새로운 자극은 생성된 이러한 새로운 경로를 사용하여 인식 또는 식별을 위한 별도의 과정 없이 자동으로 적절한 반응 활성화

- 필자가 제시할 이론은 경험주의(empiricist), 연결주의(connectionist)의 입장
- 이 이론은 퍼셉트론이라고 불리는 가상의 신경계 또는 기계를 위해 개발
- 퍼셉트론은 특정 생물학적 유기체를 유지하는 특수하고 자주 알려지지 않은 조건에 너무 깊이 빠지지 않고 일반적으로 지능 시스템의 몇 가지 기본 특성을 설명하도록 설계
- 확률적 측면에서 현재의 모델을 공식화
- 과거에는 지각과 기억과 같은 기능이 뇌에 의해 실제로 어떻게 이루어지는가보다는 어떤 종류의 결정론적 물리적 시스템에 의해 달성될 수 있는가에 대한 문제에 관심
- 퍼셉트론 이론의 기초가 되는 가정
1. 학습과 인식에 관련된 신경계의 물리적 연결은 한 유기체에서 다른 유기체로 갈 때 동일하지 않음. 가장 중요한 네트워크 구성은 무작위
2. 신경 활동이 일정 기간 지속된 후, 뉴런 자체의 오래 지속되는 변화로 인해, 한 세트의 세포에 가해진 자극이 다른 세트의 반응에 영향을 줄 수 있음
3. 비슷한 자극은 동일한 반응 세포의 집합으로 경로를 형성하는 경향이 있음
4. 긍정적 또는 부정적 자극은 현재 진행 중인 연결의 형성을 촉진하거나 방해할 수 있음
5. 이러한 시스템에서의 유사성은 동일한 세포 집합을 활성화하기 위한 유사한 자극의 경향에 의해 신경계의 어느 수준에서 표현. 자극 환경의 생태뿐만 아니라 시스템의 구조는 지각 세계가 나뉘는 것들의 종류에 따라 영향을 크게 받음

## THE ORGANIZATION OF A PERCEPTRON
- 전형적인 photo-perceptron

![캡처](https://user-images.githubusercontent.com/80622859/189482413-fc7c9891-48c3-41f1-9db9-b6e585a87d3f.PNG)

- 조직의 규칙
1. 자극은 감각 단위(S-points)의 망막에 충돌하는데, 이는 일부 모델에서는 전부 또는 전혀 반응하지 않거나, 다른 모델에서는 자극 강도에 비례하는 펄스 진폭 또는 주파수로 반응한다고 가정. 여기서 고려되는 모델에서는 모두 또는 전혀 응답이 없는 것으로 가정
2. 자극은 projection area(투영 영역,$A_1$)에 있는 연관 세포(A-units)로 전달. 투영 영역의 cell은 각각 감각점으로부터 다수의 연결을 받음. 특정 A 단위로 자극을 전달하는 점들의 집합을 해당 A 단위의 원점이라고 함(origin points).
3. Projection area와 연관 지역 사이에 연결들은 무작위. A2 집합의 각 A 단위는 A1 집합의 원점으로부터 일정 수의 연결을 받지만, 이러한 원점들은 투영 영역 전체에 무작위로 존재. 연결 분포를 제외하고, A2 장치는 A1 장치와 동일하며, 유사한 조건에서 응답.
4. 반응 R1, R2,...,Rn은 A-unit과 거의 같은 방식으로 반응. 위의 그림의 화살표는 신경망을 통한 방향을 나타냄. A까지 모든 연결이 전달되고 feedback은 없음. 마지막 연결 집합인 A_2과 R-units 사이에 연결은 양방향. 피드백 연결을 제어하는 규칙은 아래와 같은 대안 존재

(a) 각 반응에는 own-source-set에 대한 excitatory feedback(흥분 피드백) 연결이 있거나
(b) 각 반응에는 own-source-set에 대한 inhibitory feedback(억제 피드백) 연결이 있음

- 통계적 분리 가능성 이론에 부합하는 단순화된 퍼셉트론

![캡처](https://user-images.githubusercontent.com/80622859/189483487-ee9a4f8a-a2f4-4f23-82b1-21217aaf5ce6.PNG)

- A-unit에 의해 전달되는 자극은 전송을 완료할 확률인 특정값 V로 특정지어질 수 있음
- A가 높은 값을 갖는 경우, 모든 출력 pulse는 낮은 값을 갖는 A 단위로부터의 pulse보다 더 효과적이거나 말단 node에 도달할 가능성이 더 높다고 간주
- A-unit의 값은 절대적으로 일정하지는 않음
- 일반적으로 활동 기간은 cell의 가치를 증가시키는 경향이 있는 반면, 그 값은 비활성으로 붕괴될 수 있음

![캡처](https://user-images.githubusercontent.com/80622859/189483745-a1e3419e-afc3-4183-b65a-3f67b08b9499.PNG)

- $\alpha$ system : 활성 cell은 단순히 모든 자극에 대한 값의 증가를 얻고, 이 값을 무한히 유지
- $\beta$ system : 각 source 집합은 일정한 비율의 이득이 허용, 증가분은 source set의 cell들 사이에 그들의 활동에 비례하여 할당
- $\gamma$ system : 활성 cell은 source set의 비활성 cell을 희생하여 값을 얻음 => source set의 총 값은 항상 일정
- 분석 목적을 위해 자극에 대한 시스템의 반응에서 두 단계를 구별하는 것이 편리

![캡처](https://user-images.githubusercontent.com/80622859/189483857-9bf9b577-42bf-42a0-a111-2d6db3d23197.PNG)

- predominant phase(지배적 단계) : A-unit의 일부 비율(그림에서의 실선)은 자극에 반응하지만, R-unit은 여전히 비활성화.  이 단계는 일시적인 현상이며 반응 중 하나를 활성화하고 자체 source-set을 비활성화시킴. => 다른 반응의 발생 방지(postdominant phase)
- predominant phase는 무작위적이지만 A-unit이 강화되면(활성 유닛이 값을 얻도록 허용되면), 나중에 동일한 자극이 나타낼 때, 동일한 반응이 더 강하게 재발하는 경향이 있고 이는 학습이 일어났다고 말할 수 있음

## ANALYSIS OF THE PREDOMINANT PHASE
- 항상 A-unit의 활성화를 위한 고정 임계값인 $\theta$를 가정
- 고정 임계값 퍼셉트론의 학습 곡선을 예측하기 위해 두 변수를 정의
- $P_a$ : 주어진 크기의 자극에 의해 활성화된 A-unit의 예상 비율
- $P_c$ : 주어진 자극인 $S_1$에 반응하는 A-unit이 또 다른 주어진 자극 $S_2$에 반응할 조건부 확률
- Retina의 크기가 커짐에 따라 S-points의 수가 빠르게 유의미한 parameter가 되지 않게 되고, $P_a$와 $P_c$의 값이 무한히 많은 retina에 대해 가질 수 있는 값에 근접.
- Retina Equationm

![캡처](https://user-images.githubusercontent.com/80622859/189484180-e03b8f6c-2bcf-4772-8d04-469d480fe662.PNG)

![캡처](https://user-images.githubusercontent.com/80622859/189484198-248254ff-f147-4230-80fd-cd3d1f08827c.PNG)

- L : 첫 번째 자극인 S1에 의해 조명되는 S점의 비율(S2에 의해 조명되지 않음)
- G : 두 번째 자극에 포함된 잔류 S-set의 비율
