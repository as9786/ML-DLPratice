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

