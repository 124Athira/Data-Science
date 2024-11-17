import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
advertising = pd.read_csv('company_data.csv')
print(advertising.head())
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(advertising, x_vars=['TV', 'Radio', 'Newspaper'],
y_vars='Sales', height=5, aspect=1, kind='scatter')
plt.show()
X = advertising.drop(columns=['Sales'])
y = advertising['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nMean Squared Error:", mse)
print("R-squared:", r2)
print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_)
y_pred = model.predict(X_test)
for(i,j) in zip(y_test,y_pred):
if i!=j:
print("Actual value :",i,"Predicted value :",j)
print("\nNumber of mislabeled points from test data set :", (y_test !=
y_pred).sum())

OUTPUT:
C:\Users\LENOVO\PycharmProject\ds\venv\Scripts\python.exe C:/Users/LENOVO/PycharmProject/ds/multiplelinear.py
      TV  Radio  Newspaper  Sales
0  230.1   37.8       69.2   22.1
1   44.5   39.3       45.1   10.4
2   17.2   45.9       69.3   12.0
3  151.5   41.3       58.5   16.5
4  180.8   10.8       58.4   17.9
Shape of the Data set : (150, 5)
First five rows
   sepal_length  sepal_width  petal_length  petal_width variety
0           5.1          3.5           1.4          0.2  Setosa
1           4.9          3.0           1.4          0.2  Setosa
2           4.7          3.2           1.3          0.2  Setosa
3           4.6          3.1           1.5          0.2  Setosa
4           5.0          3.6           1.4          0.2  Setosa
***************
Last five rows
     sepal_length  sepal_width  petal_length  petal_width    variety
145           6.7          3.0           5.2          2.3  Virginica
146           6.3          2.5           5.0          1.9  Virginica
147           6.5          3.0           5.2          2.0  Virginica
148           6.2          3.4           5.4          2.3  Virginica
149           5.9          3.0           5.1          1.8  Virginica
Size of the Data Set : 750
Number of samples available for each Variety
variety
Versicolor    54
Virginica     50
Setosa        46
Name: count, dtype: int64
Description of the data set
Traceback (most recent call last):
  File "C:\Users\LENOVO\PycharmProject\ds\multiplelinear.py", line 8, in <module>
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

