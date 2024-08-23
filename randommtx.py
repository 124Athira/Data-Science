import numpy as np
matrix = np.random.randint(10,size=(2,2))
print("random matrix is:")
print(matrix)
print("Determinant of the matrix")
print(np.linalg.det(matrix))
print("inverse of the matrix")
print(np.linalg.inv(matrix))
print("rank of the matrix")
print(np.linalg.matrix_rank(matrix))
print("ID array")
print(matrix.flatten())

_______________________________________________________________________________

               OUTPUT
random matrix is:
[[8 2]
 [5 4]]
Determinant of the matrix
21.999999999999996
inverse of the matrix
[[ 0.18181818 -0.09090909]
 [-0.22727273  0.36363636]]
rank of the matrix
2
ID array
[8 2 5 4]
