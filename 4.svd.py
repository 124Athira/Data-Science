import numpy as np
A = np.array([[1, 2],[3, 4],[5,6]])
print(A)
U,s,VT=np.linalg.svd(A)
print("Left Singular Matrix")
print(U)
print("Singular Matrix")
print(s)
print("Right Singular Matrix")
print(VT)
Sigma = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(Sigma, s)
B = U.dot(Sigma.dot(VT))
print("Reconstructed Matrix:\n",B)

OUTPUT:
C:\Users\LENOVO\PycharmProject\ds\venv\Scripts\python.exe C:/Users/LENOVO/PycharmProject/ds/svd.py
[[1 2]
 [3 4]
 [5 6]]
Left Singular Matrix
[[-0.2298477   0.88346102  0.40824829]
 [-0.52474482  0.24078249 -0.81649658]
 [-0.81964194 -0.40189603  0.40824829]]
Singular Matrix
[9.52551809 0.51430058]
Right Singular Matrix
[[-0.61962948 -0.78489445]
 [-0.78489445  0.61962948]]
Reconstructed Matrix:
 [[1. 2.]
 [3. 4.]
 [5. 6.]]

Process finished with exit code 0



