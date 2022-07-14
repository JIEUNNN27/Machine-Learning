

# **K-Nearest Neighbors (KNN)**

- 알고자 하는 데이터로부터 모든 학습 데이터와의 거리를 측정한 후 가장 가까운 K개의 학습 데이터를 선택하고, K개의 target값 중 다수의 class로 분류 (classification)하는 알고리즘



- 지도학습 방식, 분류 (classification)와 회귀 (regression)에 적용 가능



- 게으른 학습기 (Laze learner)

  - 모델을 미리 학습시켜 놓지 않고 추정할 때마다 모든 학습 데이터와의 거리를 측정하기 때문에 속도가 늦다.
  - (다른 알고리즘들은 모델을 미리 학습시켜 놓고, 추정할 때 학습된 모델을 이용하기 때문에 속도가 빠르다)



- KNN에서 사용하는 거리
  - 맨하탄 거리 (Manhattan distance)
  - 유클리디언 거리 (Euclidean distance)
  - 밍코브스키 거리 (Minkowski distance)



- Feature 부분의 구성에 따라
  - 실수 값으로 구성된 경우
    - 거리 계산이 용이 
  - Class, label, category로 구성된 경우
  	- 거리 계산이 어렵다
  	- 별도의 거리 측정 방법을 설정해서 사용해야 하기 때문에 실수 값이 아닌 feature 데이터를 분석하는 데에는 적합하지 않음

  

- Weighted KNN: 가까운 거리에는 높은 가중치를 부여, 먼 거리에는 낮은 가중치를 부여



- sklearn패키지 이용
  - classification: “KNeighborsClassifier” 이용
  - regression: “KNeighborsRegressor” 이용