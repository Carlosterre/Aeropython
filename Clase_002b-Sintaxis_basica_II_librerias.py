import numpy as np                                                             # Importar la libreria NumPy
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')                  # Llamada a la funcion 'loadtxt' que pertenece a numpy
print(data)

# Tipo de data 'type(data)': numpy.ndarray
# Tipo de valores de data 'data.dtype': dtype('float64')
# Numero de elementos 'data.size': 2400
# Numero de elementos por dimension 'data.shape': (60, 40)

print('first value in data:', data[0, 0])                                      # La indexacion comienza en 0
print('middle value in data:', data[30, 20])

print(data[0:4, 0:10])                                                         # Primeros diez dias para los primeros cuatro pacientes
print(data[:4, :10])                                                           # No hace falta poner el valor inicial si es 0
print(data[5:10, 0:10])                                                        # Acceder a cualquier otra seccion
print(data[0:10:3, 0:10:2])                                                    # Saltar elementos (ultimo no incluido)

small = data[:3, 36:]                                                          # Tomando una seccion mas pequeña
small

# 'data.mean()' para obtener la inflamacion media
print('maximum inflammation:', data.max())                                     # Maximo: 20.0
print('minimum inflammation:', data.min())                                     # Minimo: 0.0
print('standard deviation:', data.std())                                       # Desviacion standard

patient_0 = data[0, :]                                                         # Seleccionando el primer paciente
print('maximum inflammation for patient 0:', patient_0.max())                  # Calculando su maximo

# 'data.mean(axis=1)' media a lo largo de las filas. 'axis=0' para calcular a lo largo de las columnas
# 'data.mean(axis=1).shape' para ver el tamaño del array: (60,)

element = 'oxygen'                                                             # String
# 'element[:4]' slicing del string: 'oxyg'
# 'element[4:]': 'en'
# 'element[:]': 'oxygen'
# 'element[-1]': 'n'
# 'element[-2]': 'e'
# 'element[1:-1]': 'xyge'
# 'element[3:3]': '' cadena vacia

# 'data[3:3, 4:4]': array([], shape=(0, 0), dtype=float64)
# 'data[3:3, :]': array([], shape=(0, 40), dtype=float64)

import matplotlib.pyplot as plt                                                # Modulo PyPlot de matplotlib

plt.matshow(data)                                                              # Las regiones azules corresponden a valores bajos de inflamacion, mientras que las amarillas indican valores mas altos. Se puede ver como a lo largo de los cuarenta dias la inflamacion aumenta y luego disminuye en todos los pacientes
plt.show()

ave_inflammation = data.mean(axis=0)                                           # Inflamacion media de todos los pacientes para cada día
plt.plot(ave_inflammation)
plt.show()

print('maximum inflammation per day')                                          # Inflamacion maxima por dia
plt.plot(data.max(axis=0))
plt.show()

print('minimum inflammation per day')                                          # Inflamacion minima por dia
plt.plot(data.min(axis=0))
