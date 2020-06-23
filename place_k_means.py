from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

wine = datasets.load_wine()

labels = pd.DataFrame(wine.target)
labels.columns=['labels']

data = pd.DataFrame(wine.data)
data.columns = wine.feature_names
data = pd.concat([data,labels],axis=1)

feature = data[wine.feature_names[:2]]

# k 값 = 3
model = KMeans(n_clusters=3)
model.fit(feature)
predict = pd.DataFrame(model.predict(feature))
predict.columns=['predict']

r = pd.concat([feature,predict], axis=1)
print('graph: 3')
print(r)

centers = pd.DataFrame(model.cluster_centers_, columns=['alcohol','malic_acid'])
center_x = centers['alcohol']
center_y = centers['malic_acid']

plt.scatter(r['alcohol'], r['malic_acid'], c=r['predict'], s=90, alpha=0.5)
plt.scatter(center_x, center_y, s=30, marker='D', c='red')
print('k =',3)
plt.show()

r.to_csv('wine.csv')