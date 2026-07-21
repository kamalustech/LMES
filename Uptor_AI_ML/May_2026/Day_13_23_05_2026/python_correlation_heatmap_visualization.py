import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

df = pd.DataFrame(load_iris().data,columns = ['a','b','c','d'])
correlation_output = df.corr()

print(correlation_output)



sns.heatmap(correlation_output,
                     annot= True,
                     cmap='magma',
                     fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
