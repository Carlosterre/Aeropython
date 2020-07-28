# Pintar un tablero de ajedrez usando la funcion 'plt.matshow'

import numpy as np

tablero = np.zeros([8, 8], dtype=int)

tablero[0::2, 1::2] = 1
tablero[1::2, 0::2] = 1

print(tablero)


import matplotlib.pyplot as plt

plt.matshow(tablero, cmap=plt.cm.gray_r)