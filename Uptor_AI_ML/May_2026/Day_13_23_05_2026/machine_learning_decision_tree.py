from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

load_iris_input = load_iris()
# print(load_iris_input)
x = load_iris_input.data
y = load_iris_input.target
print(x,y)
x_train,x_test, y_train,y_test = train_test_split(x,y, train_size=0.8,random_state= 42)
model_decision_tree = DecisionTreeClassifier()
model_decision_tree.fit(x_train,y_train)
prediction = model_decision_tree.predict(x_test)
print(prediction)

confusion_metrics_metric = confusion_matrix(y_test, prediction)
print(confusion_metrics_metric)