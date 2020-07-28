import numpy as np

# Paquete de algebra 'linalg' de Numpy. Tambien puede usarse la libreria SciPy
help(np.linalg)

from numpy.linalg import norm, det

M = np.array([
    [1, 2],
    [3, 4]
])

v = np.array([1, -1])
print(v)

print(v.T)                                                                     # Calculo de la traspuesta

u = np.dot(M, v)                                                               # Producto matricial usual de algebra lineal
print(u)

print(u, v)


# Comparaciones entre arrays de punto flotante
print(np.allclose(u, v))                                                       # Comprueba si todos los elementos de los arrays son iguales dentro de una tolerancia. Booleano
print(np.isclose(0.0, 1e-8, atol=1e-10))                                       # Compara elemento a elemento y devuelve un array de valores True y False

u = M @ v                                                                      # Multiplicacion de matrices de forma  mas legible
print(u)


mat = np.array([[1, 5, 8, 5],
                [0, 6, 4, 2],
                [9, 3, 1, 6]])

vec1 = np.array([5, 6, 2])

print(vec1 @ mat)

# Autovalores
A = np.array([
    [1, 0, 0],
    [2, 1, 1],
    [-1, 0, 1]
])

print(np.linalg.eig(A))