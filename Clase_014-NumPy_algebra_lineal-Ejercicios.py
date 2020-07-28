# 1.- Producto de dos matrices y su determinante

import numpy as np
from numpy.linalg import det

A = np.array([
    [1, 0, 0],
    [2, 1, 1],
    [-1, 0, 1]
])

B = np.array([
    [2, 3, -1],
    [0, -2, 1],
    [0, 0, 3]
])

print(A)
print(B)

C = A @ B
print (C)                                                                      # Producto entre las 2 matrices
print(det(C))                                                                  # Determinante


# 2.- Resolver el sistema

M = (np.array([[2, 0, 0],
               [-1, 1, 0],
               [3, 2, -1]])
     
     @
     
     np.array([[1, 1, 1],
               [0, 1, 2],
               [0, 0, 1]]))

print(M)

x = np.linalg.solve(M, np.array([-1, 3, 0]))
print(x)                                                                       # Solucion del sistema
print(np.allclose(M @ x, np.array([-1, 3, 0])))


# 3.- Hallar la inversa de la matriz H y comprobar que H*H^-1=I  (recordar la función 'np.eye')

A = np.arange(1, 37).reshape(6,6)
A[1, 1::2] = 0
A[3, ::2] = 1
A[4, :] += 30
B = (2 ** np.arange(36)).reshape((6,6))
H = A + B
print(H)

print(np.linalg.det(H))

Hinv = np.linalg.inv(H)
print(Hinv)

print(np.isclose(np.dot(Hinv, H), np.eye(6)))

np.set_printoptions(precision=3)
print(np.dot(Hinv, H))                                                         # No funciona. Los resultados varian de un ordenador a otro. La matriz esta mal condicionada