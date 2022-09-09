# Does Machine Learning Really Work?
- 실험실 시연 분야에서 상당한 상업적 가치가 있는 분야로 발전
- 새로운 표현의 장기 기억 문제, 베이지안 추론과 귀납적 추론 등과 같은 문제를 탐구하기 시작
- 데이터 마이닝 ~ 자율주행자동차를 연구하면서 해당 분야에서 이론과 알고리즘 부분에서 중요한 발전이 있었음

## The Niche for Machine Learning
- 기계 학습을 이해하는 방법 : 컴퓨터 과학의 더 넓은 분야에서 기계 학습의 역할을 고려
1. 데이터 마이닝
2. 프로그래밍하기 어려운 app
3. 맞춤형 소프트웨어 app

### Data mining
- 과거 DB를 사용하여 후속 의사 결정을 개선하는 process
- ex) 은행은 과거 data를 분석하여 어떤 미래 대출 신청자가 신용 가치가 높은지를 결정하는데 판단
- 매년 online data 양이 증가함에 따라 ML의 틈새시장은 커지고 있음

### Difficult-to-program applications
- 얼굴 인식 및 음성 인식과 같은 전통적인 app에서는 어렵다고 생각한 기술들이 ML에서는 실현 가능 => ML은 software app에 있어서 필수적인 역할

### Customized software applications
- 사람들은 개인의 요구에 자동으로 맞춤화되는 system을 원함 = RS
- ex) 개별 사용자의 독서 관심사에 맞는 추천
- 기계 학습은 software가 개별 사용자에게 매력적인 option을 제공

## Data Mining: Predicting Medical Outcomes from Historical Data
- Data Mining : 기계 학습 방법을 과거 data에 적용하여 미래의 data에 대한 예측값을 개선

![캡처](https://user-images.githubusercontent.com/80622859/189293365-92957616-5877-4ded-aa1d-c77a0d3c7b18.PNG)

- 위의 예에서는 9714명의 임산부에 대한 data, 각 여성은 215개의 다른 속성(건강 이력, 초음파 결과 등)으로 분류.(시계열 data)
- 관심있는 부분은 미래의 결과치
- ex) 어떤 미래 환자가 응급 제왕절개를 요구할 시 위험 수위 예측
- 위의 그림에서 하단 부분은 과거 data에서 학습된 일반적인 규칙을 제공
- 2/3을 훈련용으로 나머지를 test set으로 유지하여 정확도를 검증
- 위와 같은 학습을 통해서 고위험 환자군을 성공적으로 식별
- 과거 기계 학습 알고리즘 : C4.5(Decision Tree), CN2, FOIL(규칙 학습), 신경망 학습, Multi tasking 등
- 위와 같은 system의 특징은 관심 속성뿐만 아니라 여러 특징들을 동시에 예측하도록 훈련
- 새로운 논문 연구를 위한 좋은 주제
1. 새로운 data를 얻기 위한 능동적 실험 및 알고리즘 개발
2. 학습 알고리즘 + data 시각화
3. 여러 DB에 걸친 학습
- 필자가 좋아하는 연구 주제
1. Learning from mixed-media data
2. 개인 및 internet data

### Learning from mixed-media data
- 임산부 data의 경우 여러 유형의 data(image, 음성 등)을 가지고 있지만 기계 학습 방법이 부족함

### Learning using private data plut internet accessible data
- ex) 대학은 몇 년에 걸쳐 학생에 대한 data를 수집하고 규칙 학습 방법을 적용할 수 있음
- 위와 같은 1세대 학습 방법은 충분히 큰 훈련 data가 있으면 잘 작동
- Web에는 학생에 대한 보다 자세한 정보를 얻을 수 있음 -> 방대한 data
- Internet data가 효과적으로 사용될 수 있다면 학습된 규칙의 정확도를 향상시킬 수 있는 중요한 추가 기능 제공
- Web의 상당 부분은 text, 관련되지 않은 정보도 많이 포함되거나 사실이 아닌 정보도 있을 수 잇음
- 잠재력이 매우 높은 data

## Learning to Perceive: Face Recognition
- 기계학습의 두 번째 틈새 시장은 단순히 손으로 프로그래밍하기 너무 어려운 컴퓨터 프로그램을 만드는 곳
- 많은 sensor 문제가 하나의 범주
- 음성 인식 문제, image classification

![캡처](https://user-images.githubusercontent.com/80622859/189297441-60787db2-39ac-44c2-b066-6f884d0b3304.PNG)

- 역전파로 훈련
- MLP의 특성 : 훈련 중에 입력 이미지의 중요한 특징을 추출. Input image의 새로운 표현을 발견
- 양의 가중치 : 밝은 흰색, 음의 가중치 : 어두은 검은색, 0에 가까운 값 : 회색
- pixel의 값을 통해 밝기 파악. ex) 어두운 색은 배경
- 아직은 발전이 필요. ex) 베이지안 + 신경망, Long-term learning

## A Self-Customizing News Reader
- 추천시스템
- ex) NEWS WEEDER 
- 사용자를 대신하여 온라인 뉴스 기사의 범람을 filterling. 1~5점 점수를 통해 관심도 파악
- 특정 텍스트 문서 집합에서 사용자 관심을 어떻게 파악할 수 있는가? 어떤 알고리즘으로 파악해야 하는가?
- 나이브 베이지안 학습 방법 + 정보 검색의 초기 방법
- 텍스트 기사는 하나의 긴 특징 vector로 표현(각 값은 단어의 빈도 수,BOW)
- 베이지안 추론으로 조건부 확률을 구한 후 선형 조합을 사용하여 최종 예측
- 사용자가 읽지 않은 기사는 건너뜀

![캡처](https://user-images.githubusercontent.com/80622859/189299391-d62db9d1-6bae-4ea2-86ec-0f60cddefb2d.PNG)

- BOW 방법을 넘어서 명사 구절과 text 의미 부분 해석과 같은 더 많은 연구가 진행

## Where Next?
- 기계 학습은 컴퓨터 과학 내의 여러 틈새 시장에 영향을 주고 있음
- 더 많은 data가 online에 나타나게 되면서 ML의 영향은 점점 더 커질 것임
- 역사를 길게 봤을 때, 아직 컴퓨터는 50년밖에 안 된 젊은 분야. 앞으로 기대가 되는 분야

### Incorporation of prior knowledge with training data
- 앞에서 설명한 기계학습의 두드러진 특징은 초기 지식이 없으며 많은 양의 훈련데이터로부터만 학습해야 한다고 가정
- 사전 지식은 샘플 추출과 학습 정확도를 높이는데 영향을 줌
- 사전 지식 + data

### Lifelong learning
- 현재 학습 시스템은 한 가지 작업만 다룸
- 축적된 지식을 후속 학습을 하는데 이용(재사용)하는 기술 개발 + 스스로 새로운 표현
- ex) 로봇 학습, 자율 소프트웨어

### Machine learning embedded in programming languages
- ML이 소프트웨어에서 쉽게 작동하기 위한 새로운 프로그래밍 언어 또는 개발 환경 필요

### Machine learning for natural language
- 텍스트에 많은 영향을 미칠 것
