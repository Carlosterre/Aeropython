import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate                                                    # Paquete integrador

#print(help(integrate))

from scipy.integrate import quad                                               # Integracion numerica de una funcion de una variable

#print(help(quad))

# f(x)=x*sen(x)
def fun(x):
    return x * np.sin(x)

x = np.linspace(0, 10, 100)
y = fun(x)

plt.title('$y = x sin(x)$', fontsize = 25)

plt.plot(x, y, linewidth = 2)                                                  # Linea

x_fill = np.linspace(2, 9, 100)                                                # Relleno
y_fill = fun(x_fill)
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.5)

plt.grid()

value, err = quad(fun, 2, 9)
print("El resultado es:", value, "con un error de:", err)


# Trapecio de Simpson
x = np.linspace(2, 9, 100)

value = integrate.trapz(fun(x), x)

print("El resultado es:", value)


x = np.linspace(2, 9, 100)

value = integrate.simps(fun(x), x)

print("El resultado es:", value)