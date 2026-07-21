import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# df = pd.DataFrame(load_iris().data)
# df['target'] = load_iris().target
#
# correlation = df.corr()
# print(correlation)
#
# data = {"Year":[2000,2001,2002,2003,2004,2005],
#         "Price":[1000,500,1500,3500,200,800]}
# df = pd.DataFrame(data)
# print(df)
# print(df.corr())

hello = load_iris()
df = pd.DataFrame(hello.data, columns=['a','b','c','d'])
df['e'] =  hello.target
print(df.tail(2))

print(df['d'].corr(df['d']))

