import pandas as pd
from sklearn.linear_model import LinearRegression

"""pip install scikit-learn"""

data1 = {
    "Year":[2000, 2001, 2002, 2003, 2004],
    "Price":[10000,20000,30000,40000,50000]

}
df = pd.DataFrame(data1)
#print(df)

# data = [2000,2001,2002,2003,2004]
# df = pd.DataFrame(data,columns=["Year"],index=["a","b","c","d","e"])
# print(df)
# print(df["Year"])
# print(df["Year"]["a"])

"""
Pandas - Series (normal list into kind of array) - Single Dimension
Pandas - Data Frame (Normal list into kind of array with double dimension)
Pandas - Panels (Normal list into kind of array with 3 dimension)
"""

# series1 =  pd.Series(data1)
# print(series1)
df["Country"] = ['India','SA','Kenya','Libya','Iran']
print(df)
x = df[["Year"]] #input or independent data or feature data or x data
y = df["Price"] #inpur of dependent data or target data or y data

model_obj = LinearRegression() # inbuilt class name for model (algoritm)
model_obj.fit(x,y) #training data

prediction_data_input = pd.DataFrame({"Year":[2005,2006]}) #prediction data input
print(prediction_data_input)
output_prediction = model_obj.predict(prediction_data_input)
prediction_data_input['Price'] = output_prediction
prediction_data_input['Country'] = ['Myanmar','Loas']
print(prediction_data_input)
finaloutput  =  pd.concat([df, prediction_data_input])
print(finaloutput)