import numpy as np
import pandas as pd
dataset = pd.read_csv("iris.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))
df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
print(df)
new_test_point = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = classifier.predict(new_test_point)
print(f"\n Predicted class: {prediction[0]}")

OUTPUT:
C:\Users\LENOVO\PycharmProject\ds\venv\Scripts\python.exe C:/Users/LENOVO/PycharmProject/ds/knniris.py
              precision    recall  f1-score   support

      Setosa       1.00      1.00      1.00        12
  Versicolor       1.00      0.86      0.92         7
   Virginica       0.92      1.00      0.96        11

    accuracy                           0.97        30
   macro avg       0.97      0.95      0.96        30
weighted avg       0.97      0.97      0.97        30

Accuracy :  0.9666666666666667
   Real Values Predicted Values
0   Versicolor       Versicolor
1       Setosa           Setosa
2    Virginica        Virginica
3       Setosa           Setosa
4       Setosa           Setosa
5       Setosa           Setosa
6   Versicolor       Versicolor
7    Virginica        Virginica
8       Setosa           Setosa
9    Virginica        Virginica
10   Virginica        Virginica
11      Setosa           Setosa
12   Virginica        Virginica
13      Setosa           Setosa
14  Versicolor       Versicolor
15  Versicolor       Versicolor
16   Virginica        Virginica
17  Versicolor        Virginica
18  Versicolor       Versicolor
19      Setosa           Setosa
20   Virginica        Virginica
21      Setosa           Setosa
22   Virginica        Virginica
23      Setosa           Setosa
24   Virginica        Virginica
25   Virginica        Virginica
26      Setosa           Setosa
27   Virginica        Virginica
28  Versicolor       Versicolor
29      Setosa           Setosa

 Predicted class: Setosa

Process finished with exit code 0







