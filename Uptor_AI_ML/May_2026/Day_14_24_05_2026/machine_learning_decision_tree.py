from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

x = load_iris().data
y = load_iris().target

# print(x,y)
x_train, x_test, y_train,y_test = train_test_split(x,y,random_state=42, train_size=0.8)
# print(x_test,y_test)
#
model_ds = DecisionTreeClassifier(criterion = 'gini')
model_ds.fit(x_train,y_train)
y_predict = model_ds.predict(x_test)
cm = confusion_matrix(y_test,y_predict)
#
print(cm)
# print(y_test, y_predict)

plt.figure(figsize =(100,100))
plot_tree(
    model_ds,
    feature_names = load_iris().feature_names,
    class_names = load_iris().target_names,
    filled = True,
    rounded = True,
    fontsize = 10

)
plt.show()