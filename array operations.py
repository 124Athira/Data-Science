import numpy as np
ar1=np.array([[1,2],[3,4]])
ar2=np.array([[2,3],[2,1]])
print("matrix addition")
print(np.add(ar1,ar2))
print("matrix subtraction")
print(np.subtract(ar1,ar2))
print("multiplication of individual elements of matrix")
print(np.multiply(ar1,ar2))
print("divide matrix elements")
print(np.divide(ar1,ar2))
print("matrix multiplication")
print(np.dot(ar1,ar2))
print("transpose of matrix")
print(ar1.transpose())
print("sum of diagonal elements")
print(np.trace(ar1))

--------------------------------------------------------
output:
matrix addition
[[3 5]
 [5 5]]
matrix subtraction
[[-1 -1]
 [ 1  3]]
multiplication of individual elements of matrix
[[2 6]
 [6 4]]
divide matrix elements
[[0.5        0.66666667]
 [1.5        4.        ]]
matrix multiplication
[[ 6  5]
 [14 13]]
transpose of matrix
[[1 3]
 [2 4]]
sum of diagonal elements
5
