# !pip install sklearn graphviz
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
# import graphviz
import matplotlib.pylab as plt


iris = load_iris()

df = pd.DataFrame(data=iris.data, columns= iris['feature_names'])
label = pd.DataFrame(data = iris.target, columns=['label'])

print(df)
print(label)

# 데이터 순서를 섞은 뒤에 80퍼센트를 추출, 학습 
X_train, X_test,Y_train, Y_test = train_test_split(df,label,train_size = 0.8)

print(X_train[:10])
print(Y_train[:10])

# decition tree 모델로 만드는 방법 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

# X_test 값을 가지고 Y값 예측 
Y_pred = clf.predict(X_test)

# 예측한 값과 비교
print("accuracy:", metrics.accuracy_score(Y_test,Y_pred))

# tree 반환 
# tree.plot_tree(clf.fit(iris.data, iris.target))

# dot_data = tree.export_graphviz(
#     clf, out_file=None,
#     feature_names=iris.feature_names,
#     class_names=iris.target_names,
#     filled=True, rounded=True,
#     special_characters=True
# )
# graph = graphviz.Source(dot_data)
# print(graph)

# 차트를 그리기 위한 코드
# 중요하게 작용된 요소들의 퍼센테이지를 보여줌 
def plot_feature_importances(model):
    n_features = iris.data.shape[1]
    plt.barh(range(n_features),model.feature_importances_, align="center")
    plt.yticks(np.arange(n_features), iris.feature_names)
    plt.xlabel("importance_value")
    plt.ylabel("feature")
    plt.ylim(-1,n_features)

plot_feature_importances(clf)
plt.show()