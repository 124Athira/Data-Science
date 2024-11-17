import numpy as np
ar1=np.array([[1,2],[3,4]])
ar2=np.array([[5,6],[7,8]])
print("Add two Matrices")
print(np.add(ar1,ar2))
print("Subtract two matrices")
print(np.subtract(ar1,ar2))
print("Multiply individual elements of the matrices")
print(np.multiply(ar1,ar2))
print("Divide the elements of the matrices")
print(np.divide(ar1,ar2))
print("Perform matrix Multiplication")
print(np.dot(ar1,ar2))
print("Display the transpose of the matrices")
print(ar1.transpose())
print(ar2.transpose())
print("Sum of diagonal elements of the matrices")
print(np.trace(ar1))
print(np.trace(ar2))

OUTPUT:
C:\Users\LENOVO\PycharmProject\ds\venv\Scripts\python.exe C:/Users/LENOVO/PycharmProject/ds/arithmetic.py
Add two Matrices
[[ 6  8]
 [10 12]]
Subtract two matrices
[[-4 -4]
 [-4 -4]]
Multiply individual elements of the matrices
[[ 5 12]
 [21 32]]
Divide the elements of the matrices
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
Perform matrix Multiplication
[[19 22]
 [43 50]]
Display the transpose of the matrices
[[1 3]
 [2 4]]
[[5 7]
 [6 8]]
Sum of diagonal elements of the matrices
5
13

Process finished with exit code 0

