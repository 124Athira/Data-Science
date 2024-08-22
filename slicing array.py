import numpy as np
arr1=np.array([[3,4,2,1],[1,4,7,7],[9,3,9,12],[1,6,8,7]])
print(arr1[ : , : ])
print(arr1[1: , : ])
print(arr1[ : , :3])
print(arr1[1:3,0:2])
print(arr1[ : ,1:3])
print(arr1[ :1,1:3])

------------------------------------
output:
1)[[ 3  4  2  1]
 [ 1  4  7  7]
 [ 9  3  9 12]
 [ 1  6  8  7]]
2)[[ 1  4  7  7]
 [ 9  3  9 12]
 [ 1  6  8  7]]
3)[[3 4 2]
 [1 4 7]
 [9 3 9]
 [1 6 8]]
4)[[1 4]
 [9 3]]
5)[[4 2]
 [4 7]
 [3 9]
 [6 8]]
6)[[4 2]]
