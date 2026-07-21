import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import datasets

dataset = load_iris()
# print(dataset)
df = pd.DataFrame([dataset])
print(df.head(2))

hello = load_iris()
df = pd.DataFrame(hello.data, columns = hello.feature_names)
print(df.head(2))
df['target'] = hello.target
print(df.columns)


plt.scatter(df['petal length (cm)'],df['petal width (cm)'], c= df['target'], cmap = 'rainbow')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.colorbar()
plt.show()
