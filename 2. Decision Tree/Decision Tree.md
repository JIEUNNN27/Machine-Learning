[TOC]

# Decision Tree

- DTree 알고리즘에는 ID3/C4.5와 CART 등이 있다
  - ID3/C4.5
    - 트리가 분기할 때 여러 갈래로 분기
  - CART
    - 트리가 분기할 때 두 갈래로 분기
    - 이진 트리(binary-tree)를 만든다



## sklearn 패키지

- classification: DecisionTreeClassifier 이용
- reg ression : DecisionTreeRegressor 이용



## 최적 분기 찾기

- 엔트로피(entropy)나 지니 지수 (Gini index)를 사용
- A: 분기 이전의 엔트로피나 지니 지수를 계산
- B: 분기 이후의 엔트로피나 지니 지수의 가중평균을 계산
- A B: 둘 간의 차이를 정보이득 (information gain), 정보이득이 가장 큰 분기로 트리를 만들어 나감



## Decision Tree의 장점

- 데이터 표준화를 하지 않아도 되고 , nominal feature 를 ordinal feature 처럼 단순히 수치화 하면 된다 .

  `(red, green, blue) -> (0, 1, 2)`

  (다른 알고리즘을 사용하려면 nominal feature 는 순서에 상관이 없으므로 one hot encoding 으로 수치화 한다)



## 과잉적합(overfitting) 방지 - 사전, 사후 가지치기(pruning)

- 사전 가지치기
  - 트리를 생성할 때 트리의 깊이 (depth), 터미널 노드 (leaf 의 최소 데이터 개수 등을 사전에 결정하는 방법
- 사후 가지치기
  - 초기에는 트리를 최대한 복잡하게 구성한 다음 불필요한 분기 가지 를 제거하는 방법
  - Cost Complexity Pruning (CCP)은 CART 에서 제안된 대표적인 사후 가지치기 방법



## 중요하게 취급해야 할 feature 파악하기

- Decision Tree 에서 정보이득이 높았던 feature 들은 target 을 추정하는 데 중요한 (importance) 역할을 수행
- 각 feature 마다 importance score 를 측정하면 어느 feature 를 중요하게 취급해야 할 지를 파악할 수 있음



## Decision Tree를 이용한 앙상블 기법(Tree 계열의 알고리즘)

- Random Forest
- Gradient Boosting
- Extream Gradient Boosting (XGBoost)
- Light GBM (LGBM)