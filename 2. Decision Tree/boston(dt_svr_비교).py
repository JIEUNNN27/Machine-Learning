import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR, LinearSVR
from sklearn.model_selection import train_test_split

# Boston house dataset을 읽어온다.
boston = load_boston()

# 데이터 프레임 형태로 저장한다.
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['PRICE'] = boston.target

df.head()

# 데이터 스케일 조정
# 이 부분은 금요일 다시 설명 드리겠습니다.
df['AGE'] /= 10
df['TAX'] /= 100
df['PTRATIO'] /= 10
df['B'] /= 100
df['PRICE'] /= 10

# 학습 데이터와 시험 데이터로 분리한다.
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size = 0.2)
x_train.shape, x_test.shape

# Decision Regression Tree 분석
# Tree의 최적 depth를 찾고 시험 데이터의 R2 score를 측정한다.
d_max = 20
r2 = []
for depth in range(1, d_max):
    dt = DecisionTreeRegressor(max_depth=depth)
    dt.fit(x_train, y_train)

    r2.append(dt.score(x_test, y_test))

opt_depth = np.argmax(r2) + 1
print("optimal depth = ", opt_depth)

# 최종 모델
final_dt = DecisionTreeRegressor(max_depth=opt_depth)
final_dt.fit(x_train, y_train)

# Support Vector Regression (SVR) 분석
# gamma와 C의 조합을 바꿔가면서 학습 데이터의 R2가 최대인 조합을 찾는다
opt_acc = -999
opt_ep = 0
opt_c = 0

# 이 부분도 금요일 다시 설명 드리겠습니다.
EP = [0.5, 1, 5]
C = [10000, 11000, 12000, 20000, 50000, 100000]

for ep in EP:
    for c in C:
        # print(ep, c)
        model = SVR(kernel='rbf', C=c, epsilon=ep)
        model.fit(x_train, y_train)
        acc = model.score(x_test, y_test)
        
        if acc > opt_acc:
            opt_ep = ep
            opt_c = c
            opt_acc = acc

print('opt_ep = %.3f' % opt_ep)
print('opt_c = %.3f' % opt_c)
print('opt_acc = %.3f' % opt_acc)

# 최종 SVR 모델을 생성한다.
final_svr = SVR(kernel='rbf', C=opt_c, epsilon=opt_ep)
final_svr.fit(x_train, y_train)

# R2 score를 측정한다.
print(" DT의 R2 = {:.3f}".format(final_dt.score(x_test, y_test)))
print("SVR의 R2 = {:.3f}".format(final_svr.score(x_test, y_test)))

