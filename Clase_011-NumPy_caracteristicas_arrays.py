import numpy as np

lista = [1, 1+2j, True, 'aerodinamica', [1, 2, 3]]
print(lista)

array = np.array([ 1, 1+2j, True, 'aerodinamica'])
print(array)

print(id(lista))
lista.append('fluidos')
print(lista)
print(id(lista))

print(id(array))
array = np.append(array, 'fluidos')
print(array)
print(id(array))

help(np.append)

# Funcion 'linspace' usando un bucle, mayor tiempo de ejecucion
def my_linspace_FORTRAN(start, stop, number=50):
    x = np.empty(number)
    step = (stop - start) / (number - 1)
    for ii in range(number):
        x[ii] = ii * step
    x += start
    return x

# Funcion 'linspace' estilo Python, 
def my_linspace_PYTHONIC(start, stop, number=50):
    step = (stop - start) / (number - 1)
    x = np.array([ii * step  for ii in range(number)])                         # "List comprehension"
    x += start
    return x

# Funcion 'linspace' de NumPy, menor tiempo de ejecucion
np.linspace(0,100,1000000)
