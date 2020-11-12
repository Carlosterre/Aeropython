ºimport numpy as np
print(np.__version__)                                                          # Muestra la version instalada

mi_primer_array = np.array([1, 2, 3, 4])
print(mi_primer_array)

print(mi_primer_array.dtype)                                                   # Tipo de datos que contiene el array

mi_segundo_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])                 # Array 2D, lista de listas
print(mi_segundo_array)

mi_segundo_array = np.array([                                                  # Para continuar en la siguiente linea no es necesario utilizar '\' dentro de parentesis o corchetes. Se utiliza indentacion
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])
print(mi_segundo_array)

print(np.sum(mi_primer_array))                                                 # Funcion suma incorporada en numpy
print(np.max(mi_primer_array))                                                 # Funcion maximo incorporada en numpy
print(np.sin(mi_segundo_array))                                                # Funcion seno incorporada en numpy
print(np.pi, np.e)                                                             # Constantes 'pi' y 'e' incluidas en numpy

print(np.zeros(100))                                                           # Vector de ceros en 1D
print(np.zeros([100])) 
print(np.zeros([10, 10]))                                                      # En 2D

print(np.identity(4))                                                          # Array identidad

a = np.arange(0, 5)                                                            # Rango, array que va de 0 a 5
print(a)                                                                       # Va de 0 a 4

print(np.arange(0, 11, 3))                                                     # Array que va de 0 a 10 de 3 en 3

print(np.linspace(0, 10, 21))                                                  # Si icluye el ultimo elemento

a = np.arange(1, 10)                                                           # Se parte de un vector 1D
M = np.reshape(a, [3, 3])                                                      # Se le da forma de array en 2D

# Metodo: son funciones especiales en las que el argumento mas importante (sobre el que se realiza la accion) se escribe delante seguido de un punto. Por ejemplo '.metodo(argumentos)'
N = a.reshape([3,3])                                                           # Metodo: Programacion orientada a objetos. En Python, todo es un objeto
print(N)

arr = np.arange(11)                                                            # Crear un array y sumarle un numero
print (arr + 55)

print(arr * 2)                                                                 # Multiplicarlo por 2
print(arr ** 2)                                                                # Elevarlo al cuadrado
print(np.tanh(arr))                                                            # Calcular la funcion tangente

arr1 = np.arange(0, 11)                                                        # Crear 2 arrays
arr2 = np.arange(20, 31)

print(arr1 + arr2)                                                             # Suma
print(arr1 * arr2)                                                             # Producto
print(arr1 > arr2)                                                             # Comparacion, array booleano
print(arr1 == arr2)                                                            # Los arrays soy de enteros, no de flotantes. Array booleano
