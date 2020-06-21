import csv
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('weather2.csv', sep=',', dtype='unicode')

print(data)

# print(data)

k_data = data[["Avg_temp", "Rain"]]


k_arr = np.array(k_data, dtype=np.float64)
print(k_arr)

model = KMeans(n_clusters=3)
model.fit(k_arr)

y_predict = model.predict(k_arr)

print(y_predict)
k_data['cluster'] = y_predict

print(k_data)

# plt.scatter(data["Avg_temp"], data["Rain"], s=10)


plt.scatter(k_arr[:, 0], k_arr[:, 1], c=y_predict, s=30, cmap='viridis')
plt.title('Weather Clustering')
plt.show()
