# 1.- Crear una grafica que muestre la desviacion tipica de los datos cada dia para todos los pacientes
# 2.- Crear una grafica que muestre a la vez la inflamacion maxima, media y minima para cada dia

import numpy as np
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

import matplotlib.pyplot as plt

plt.plot(data.std(axis=0))                                                     # Desviacion tipica por dia
plt.show()

plt.plot(data.max(axis=0))                                                     # Inflamacion maxima, media y minima para cada dia
plt.plot(data.mean(axis=0))
plt.plot(data.min(axis=0))
plt.show()
