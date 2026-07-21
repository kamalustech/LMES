import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import pandas as pd

x = load_iris().data
y = load_iris().target

x_train,x_test, y_train,y_test = train_test_split(x,y,random_state= 42,
                                                  train_size=0.8)
my_input_parameter = {"criterion":['gini','entropy'],
                      "max_depth":[2,4,5,6],
                      "min_samples_split":[4,8,12]}# to run the program on the cpu core
# -1, split among all cpu, 1 only on 1 cpu, 2 on 2 cpu's

model = DecisionTreeClassifier(random_state= 42)
grid_search = GridSearchCV(estimator=model,param_grid=my_input_parameter,
                           cv=5, scoring='accuracy', n_jobs=-1)

# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
grid_search.fit(x_train,y_train)
best_estimator = grid_search.best_estimator_
y_prediction = best_estimator.predict(x_test)

print(y_prediction,y_test)

