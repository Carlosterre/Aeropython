import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("polar.dat")
C_L = data[0]
C_D = data[1]

plt.plot(C_D, C_L, 'x', mew=2, label="Datos reales")
plt.xlabel("$C_D$")
plt.ylabel("$C_L$")
plt.legend()
plt.show()


idx_stall = np.argmax(C_L)                                                     # Indice del maximo valor de C_L para descartar datos fuera de la region de entrada en perdida
print(idx_stall)
print(C_L[idx_stall])                                                          # C_L max

# Representar datos dentro y fuera del modelo
plt.plot(C_D[:idx_stall + 1], C_L[:idx_stall + 1], 'x', mew=2, label="Datos reales")
plt.plot(C_D[idx_stall + 1:], C_L[idx_stall + 1:], 'o', mfc='none', label="Fuera del modelo")
plt.xlabel("$C_D$")
plt.ylabel("$C_L$")
plt.legend(loc=4)
plt.show()

from scipy import interpolate

x_i = [0.0, 0.9, 1.8, 2.7, 3.6, 4.4, 5.3, 6.2, 7.1, 8.0]
y_i = [0.0, 0.8, 1.0, 0.5, -0.4, -1.0, -0.8, -0.1, 0.7, 1.0]
plt.plot(x_i, y_i, 'x', mew=2)
plt.show()

f_interp = interpolate.InterpolatedUnivariateSpline(x_i, y_i, k=1)             # Funcion interpolante. Admite 'x' como argumento

x = np.linspace(0, 8)
y_interp = f_interp(x)

plt.plot(x_i, y_i, 'x', mew=2)
plt.plot(x, y_interp)
plt.show()

# FENOMENO DE RUNGE
def runge(x):
    return 1 / (1 + x ** 2)

N = 11                                                                         # Nodos de interpolacion

xp = np.linspace(-5, 5, N)                                                     # Seleccionar los nodos: -5, -4, -3, ..., 3, 4, 5
fp = runge(xp)

x = np.linspace(-5, 5, 200)                                                    # Seleccionar la x para interpolar

lag_pol = interpolate.lagrange(xp, fp)                                         # Polinomio de Lagrange para interpolar
y = lag_pol(x)

plt.plot(x, y, label='Interpolation')
plt.plot(xp, fp, 'o', label='Muestras')
plt.plot(x, runge(x), label='Real')
plt.legend(loc='upper center')
plt.show()

from numpy.polynomial import chebyshev                                         # Importar polinomio de Chebyshev

N = 11                                                                         # Nodos de interpolacion

coeffs_cheb = [0] * N + [1]                                                    # Tomar el elemento 11 de la serie
print(coeffs_cheb)

T11 = chebyshev.Chebyshev(coeffs_cheb, [-5, 5])
xp_ch = T11.roots()

xp_ch

fp = runge(xp_ch)

x = np.linspace(-5, 5, 200)

lag_pol = interpolate.lagrange(xp_ch, fp)

y = lag_pol(x)

plt.plot(x, y, label='Interpolacion')
plt.plot(xp_ch, fp, 'o', label='Muestras')
plt.plot(x, runge(x), label='Real')
plt.legend()
plt.show()


# Ajuste -> Curva que no tiene por que pasar por ninguno de los puntos originales, pero que a cambio tendra una expresión analitica simple
from scipy.optimize import curve_fit

x_i = np.linspace(-2, 3, num=10)
y_i = x_i ** 2 - x_i + 1 + 0.5 * np.random.randn(10)                           # Funcion tipo y(x)=x^2-x+1+Ruido
plt.plot(x_i, y_i, 'x', mew=2)
plt.show()

def poldeg2(x, a, b, c):                                                       # Funcion 'polynomial.polyfit': Recibe los puntos de interpolacion y el grado del polinomio. El resultado seran los coeficientes del mismo, en orden de potencias crecientes
    return a * x**2 + b * x + c
val, cov = curve_fit(poldeg2, x_i, y_i)
a, b, c= val

print(a, b, c)

x = np.linspace(-2, 3)

y_fit = poldeg2(x, a, b, c)

l, = plt.plot(x, y_fit)
plt.plot(x_i, y_i, 'x', mew=2, c=l.get_color())
