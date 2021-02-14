import numpy as np
import numpy as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()

import pandas as pd

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
pd.plotting.scatter_matrix(iris_df, c=iris.target, s=60, alpha=0.8, figsize=[12,12])
print('')

col1 = 0
col2 = 3

X = iris.data[:,[col1,col2]]
y = iris.target # y 값은 군집에서 사용하지 않는다

from sklearn.cluster import KMeans

model = KMeans(3)
model.fit(X)

labels = model.labels_
labels

# labels = np.where(model.labels_==1, 0, np.where(model.labels_==0, 1, model.labels_))
# labels = model.labels_.copy()
# labels[labels==1]=999
# labels[labels==0]=1
# labels[labels==999]=0

# plt.figure(figsize=[12,8])
plt.title('Iris Clustering', fontsize=20)
plt.scatter(X[:,0], X[:,1], c=labels, s=60)
plt.colorbar()

plt.figure(figsize=[12,8])
plt.title('Iris Clustering', fontsize=20)
plt.scatter(X[:,0], X[:,1], c=labels, marker='s', s=150)
CS = plt.scatter(X[:,0], X[:,1], c=y, s=60)
plt.legend(['Clustering', 'Original'])
plt.colorbar(CS)

from sklearn.datasets import make_blobs

X, y = make_blobs()

X.shape, y.shape

y

plt.scatter(X[:,0], X[:,1], c=y)

model = KMeans(3)
model.fit(X)

plt.scatter(X[:,0],X[:,1],c=model.labels_)
plt.colorbar()

model.cluster_centers_

plt.scatter(X[:,0],X[:,1],c=model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], marker='^', c='r', s=200)

model.predict([[0, -5]])

X = iris.data[:,[col1,col2]]

model = KMeans(2)
model.fit(X)

plt.figure(figsize=[12,8])
plt.title('Iris Clustering', fontsize=20)
plt.scatter(X[:,0], X[:,1], c=model.labels_, s=60)
plt.colorbar(shrink=0.5)

model.cluster_centers_ # 중심점 위치들

model.predict([[6, 1]]) # 결과를 해석하려면 위의 colorbar 를 확인해야 한다.

model.transform([[6, 1]]) # 각 중심점 까지의 거리 벡터

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target)

kmeans10 = KMeans(10)
X_train_10 = kmeans10.fit_transform(X_train)
X_test_10 = kmeans10.transform(X_test)

lr = LogisticRegression()
lr.fit(X_train_10, y_train)

train_score = lr.score(X_train_10, y_train)
test_score = lr.score(X_test_10, y_test)

train_score, test_score

from sklearn.datasets import make_blobs, make_circles, make_moons

X, y = make_circles(factor=0.5, noise=0.1) # factor = R1/R2, noise: svd
print(X.shape, y)

plt.scatter(X[:,0], X[:,1], c=y, cmap='autumn')
plt.colorbar(shrink=0.7)

X, y = make_moons(noise=0.1)
plt.show()
plt.savefig("X.png")

plt.scatter(X[:,0], X[:,1], c=y, cmap='autumn')
plt.colorbar(shrink=0.7)


