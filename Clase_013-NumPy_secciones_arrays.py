import numpy as np

# Arrays en 1D
arr = np.arange(10)
print(arr)

print(arr[0])                                                                  # Acceder al primer elemento
print(arr[-1])                                                                 # Acceder al ultimo elementoç


arr = np.arange(10)                                                            # NumPy devuelve vistas, no copias 
a = arr[5:]

print(arr)
print(a)

arr[5] = 999

print(arr)
print(a)


arr = np.arange(10)                                                            # Ocurre lo mismo al reves. 'a' apunta a las direcciones de memoria donde se guardan los elementos de 'arr' seleccionados
a = arr[5:]

print(arr)
print(a)

a[-1] = 999

print(arr)
print(a)


arr = np.arange(10)                                                            # Forma de copiar sus valores
a = arr[5:].copy()

print(arr)
print(a)

arr[5] = 999

print(arr)
print(a)


# Arrays en 2D
arr = np.arange(9).reshape([3, 3])
print(arr)
print(arr[0, -1])
print(arr[2, 2])

# Seleccion de arrays
M = np.arange(36, dtype=float).reshape(4, 9)
print(M)
print(M[1:3])                                                                  # De la segunda a la tercera fila, incluidas
print(M[:2, 1:5:2])                                                            # Hasta la tercera fila sin incluir y de la segunda a la quinta columnas saltando 2
#print(M[1:2:1, 1:5:2])                                                        # Equivalente
