import numpy as np
matrix=np.random.randint(10,size=(2,2))
print("Random genereated Matrix")
print(matrix)
det=np.linalg.det(matrix)
print("Determinant of matrix: ",det)
inverse=np.linalg.inv(matrix)
print("Inverse of the Matrix:\n",inverse)
rank=np.linalg.matrix_rank(matrix)
print("Rank of the Matrix: ",rank)
EVal,EVect = np.linalg.eig(matrix)
print("Eigen Value:")
print(EVal)
print("Eigen Vector")
print(EVect)
array_1D=matrix.flatten()
print("Transform Matrix in 1_D array: ",array_1D)

OUTPUT:
C:\Users\LENOVO\PycharmProject\ds\venv\Scripts\python.exe C:/Users/LENOVO/PycharmProject/ds/randinteger.py
Random genereated Matrix
[[6 4]
 [9 7]]
Determinant of matrix:  5.999999999999996
Inverse of the Matrix:
 [[ 1.16666667 -0.66666667]
 [-1.5         1.        ]]
Rank of the Matrix:  2
Eigen Value:
[ 0.47920271 12.52079729]
Eigen Vector
[[-0.58671968 -0.52288342]
 [ 0.80979011 -0.8524042 ]]
Transform Matrix in 1_D array:  [6 4 9 7]

Process finished with exit code 0
