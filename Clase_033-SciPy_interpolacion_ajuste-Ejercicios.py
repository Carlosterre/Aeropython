# %% 1.-
print("1.-")
# Crear una funcion interpolante CD=f(CL) usando splines de grado 2 y representarla. Utilizar solo los datos que resultan de haber eliminado la region de entrada en perdida.
# Tener en cuenta que la x y la y para este caso estan cambiadas de sitio

# 1.- Crear un polinomio interpolante usando los valores que encajan en el modelo parabolico
# 2.- Crear un dominio de  CL entre 'C_L.min()' y 'C_L.max()'
# 3.- Hallar los valores interpolados de CD en ese dominio
# 4.- Representar la funcion y los puntos

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Ver 'Clase_033'
datos = np.loadtxt("polar.dat")
C_L = datos[0]
C_D = datos[1]

plt.plot(C_D, C_L, 'x', mew=2, label="Datos reales")
plt.xlabel("$C_D$")
plt.ylabel("$C_L$")
plt.legend()
plt.show()

idx_stall = np.argmax(C_L)
C_L[idx_stall]

plt.plot(C_D[:idx_stall + 1], C_L[:idx_stall + 1], 'x', mew=2, label="Datos reales")
plt.plot(C_D[idx_stall + 1:], C_L[idx_stall + 1:], 'o', mfc='none', label="Fuera del modelo")
plt.xlabel("$C_D$")
plt.ylabel("$C_L$")
plt.legend(loc=4)
plt.show()


# Polinomio interpolante
f_C_D = interpolate.InterpolatedUnivariateSpline(C_L[:idx_stall + 1], C_D[:idx_stall + 1], k=2)

C_L_domain = np.linspace(C_L.min(), C_L.max())
C_D_interp = f_C_D(C_L_domain)

plt.plot(C_D_interp, C_L_domain)
plt.plot(C_D, C_L, 'x', mew=2)
plt.show()


# %% 2.-
print("2.-")
# Modelizar la polar como CD=CD0+k*CL^2
# Obtener CD0 y k

def model(x, A, C):
    return A*x**2 + C
print(C_L)
print(C_D)

from scipy.optimize import curve_fit
popt, _ = curve_fit(model, C_L[:idx_stall+1], C_D[:idx_stall+1])
A, B = popt
x = np.linspace(-1.5, 1.5, 50)
y = model(x, A, B)

plt.plot(y, x)
plt.plot(C_D[:idx_stall + 1], C_L[:idx_stall + 1], 'x', mew=2, label="Datos reales")
plt.plot(C_D[idx_stall + 1:], C_L[idx_stall + 1:], 'o', mfc='none', label="Fuera del modelo")
plt.xlabel("$C_D$")
plt.ylabel("$C_L$")
plt.legend(loc=4)
