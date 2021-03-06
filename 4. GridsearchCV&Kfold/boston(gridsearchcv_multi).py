# -*- coding: utf-8 -*-
"""Boston(GridSearchCV_multi).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10rzdjr7FDbDfnKFnixjpGtY5-5VTQs8z
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as  plt

# Boston house dataset을 읽어온다.
boston = load_boston()

# 데이터 프레임 형태로 저장한다.
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['PRICE'] = boston.target

# 데이터 스케일 조정. 데이터 표준화에 대해서는 추후 정리할 예정임.
df[['ZN', 'AGE', 'PTRATIO', 'PRICE']] /= 10
df[['TAX', 'B']] /= 100

df.head()

# 학습 데이터와 시험 데이터로 분리한다.
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size = 0.15)
x_train.shape, x_test.shape

pipe = Pipeline(steps=[('model', SVR())])  # 임의 model로 pip를 초기화한다.
grid_params = [{'model':[SVR()],
                'model__kernel':['rbf'],
                'model__C':[0.1, 1.0, 10.0],
                'model__epsilon':[0.1, 1.0, 2.0]},
               
               {'model':[DecisionTreeRegressor()],
                'model__max_depth':np.arange(1, 20)}]

grid = GridSearchCV(estimator=pipe, param_grid=grid_params, cv=10, refit=True)
grid.fit(x_train, y_train)

# grid.cv_results_     : K-fold cross validation test 결과 dictionary
# grid.best_params_    : best parameter ==> {'max_depth': 5}
# grid.best_model_ : best parameter로 생성한 tree

best_model = grid.best_estimator_

print("Best parameter = ", grid.best_params_)
print("Best test score = ", best_model.score(x_test, y_test))

# test data의 추정 결과를 육안으로 확인한다.
y_pred = best_model.predict(x_test)

# 원래 스케일로 환원한다.
d_test = y_test * 10
d_pred = y_pred * 10

# 데이터 프레임으로 변환한다
df_pred = pd.DataFrame(np.c_[d_test, d_pred], columns=['price', 'prediction'])
df_pred.head()

# 추정 결과를 시각화 한다.
plt.figure(figsize=(6, 6))
plt.scatter(d_test, d_pred, c='red', s=30, alpha=0.5)
plt.xlabel("house price")
plt.ylabel("predicted price")
plt.show()

