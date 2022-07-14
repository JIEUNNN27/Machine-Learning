[TOC]

## **머신러닝의 종류**

- 지도학습 (Supervised Learning)
- 비지도학습 (Unsupervised Learning)
- 강화학습 (Reinforcement Learning)

 





## **머신러닝의 목적**

이미 알고 있는 데이터 (관측 데이터)를 학습해서 알지 못했던 사실을 추론하는 것
(Inferring unknows from knowns.)

 





## **머신러닝의 지도학습 방법론**
### 분류 (Classification)
	데이터의 target이 class나 label 혹은 category (0, 1, 2와 같은)로 구성되어 있는 경우
### 회귀 (Regression)
	Target이 실수 값 (2.3, 5.8, 4.0과 같은)으로 구성되어 있는 경우
### 군집화 (Clustering)

 





## **머신러닝의 지도학습을 위한 데이터**
- Feature: 각 샘플의 특징을 모아 놓은 부분
- Target: 알아내려는 목적
- 머신러닝의 지도학습은 이미 관측된 데이터의 feature와 target의 관계를 학습한 후, 새로 관측된 데이터의 feature에 대한 미지의 target을 추정하는 것
- 분석할 데이터는 학습용 (train), 평가용 (evaluation), 시험용 (test)으로 분리해서 분석

 





## **과잉적합 (overfitting)과 과소적합 (underfitting) 현상**
### 과잉적합 (overfitting)
- 분석 모델이 학습용 데이터는 잘 설명하지만 평가용이나 시험용 데이터는 잘 설명하지 못하는 현상
- 데이터의 양이 적거나 모델이 복잡한 경우 과잉적합 (overfitting) 현상이 발생할 수 있음
### 과소적합 (underfitting)
- 모델이 너무 단순하면 과소적합 (underfitting) 현상이 발생할 수 있다.

 





## **데이터 전처리 (data preprocessing) 과정**
전처리 과정에서는 데이터 표준화, 결측치 처리 (missing value), categorical feature의 수치화 작업 등을 수행

 





## **데이터 표준화 (normalization)**
- Feature 값들의 scale이 다를 때에는 데이터를 표준화 (normalization)한다.
- 특히, 거리나 마진 (margin) 등을 계산하는 알고리즘들과 나중에 배울 딥러닝 등에서는 데이터의 scale을 맞추는 것이 매우 중요.
- 단, tree 계열의 알고리즘은 데이터 표준화 안 해도 된다.
### 데이터 표준화 방법
- Z-score 방법
	-  평균과 분산 (표쥰편차)을 이용
	-  sklearn에서 “StandardScaler” 함수를 이용
- Min_max 표준화 방법
	- 데이터를 0과 1 사이 값으로 맞춤
	- sklearn에서 “MinMaxScaler” 함수를 이용

 





## **categorical data의 수치화 작업**

- Feature 데이터는 실수 값이나 categorical data로 구성.
- 대부분의 알고리즘들은 수치 데이터를 요구하므로 categorical data들은 수치로 변환해야 함

### Categorical Data

#### Ordinal data
- 순서에 의미가 있다 (예: small, mid, large)
- 수치화: 0, 1, 2와 같이 순서대로 번호 부여
- sklearn에서 “LabelEncoder”함수를 이용
#### Nominal data
- 순서에 의미가 없다 (예: red, green, blue)
- 수치화: one-hot encoding을 사용 (예: (1 ,0, 0), (0, 1, 0), (0, 0, 1))
- sklearn에서 “OneHotEncoder”를 이용
- 단, Tree 계열의 알고리즘에서는 nominal data도 ordinal처럼 취급해도 된다.
	(Feature 값을 Tree 분기용으로 사용하기 때문에 순서에 영향을 받지 않기 때문)



 