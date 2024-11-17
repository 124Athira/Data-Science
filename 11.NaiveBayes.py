import numpy as np
import pandas as pd
dataset = pd.read_csv('iris.csv')
X = dataset.iloc[:,:4].values
y = dataset['variety'].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("\n",y_pred,"\n")
from sklearn.metrics import accuracy_score
print ("\n Accuracy : ", accuracy_score(y_test, y_pred))
mislabeled_count = (y_test != y_pred).sum()
print(f"\n Number of mislabeled points: {mislabeled_count} out of
{len(y_test)}")
mismatches = (y_test != y_pred)
print("\n Mismatching records (Actual vs Predicted):")
for actual, predicted in zip(y_test[mismatches], y_pred[mismatches]):
print(f"Actual: {actual}, Predicted: {predicted}")

OUTPUT:
C:\Users\LENOVO\PycharmProject\ds\venv\Scripts\python.exe C:/Users/LENOVO/PycharmProject/ds/naivebayes.py

 ['Setosa' 'Setosa' 'Virginica' 'Setosa' 'Versicolor' 'Virginica' 'Setosa'
 'Setosa' 'Virginica' 'Versicolor' 'Virginica' 'Setosa' 'Setosa'
 'Virginica' 'Versicolor' 'Versicolor' 'Versicolor' 'Versicolor' 'Setosa'
 'Virginica' 'Virginica' 'Setosa' 'Setosa' 'Virginica' 'Setosa' 'Setosa'
 'Virginica' 'Virginica' 'Versicolor' 'Virginica'] 


 Accuracy :  0.9666666666666667

 Number of mislabeled points: 1 out of30

 Mismatching records (Actual vs Predicted):
Actual: Versicolor, Predicted: Virginica

Process finished with exit code 0









