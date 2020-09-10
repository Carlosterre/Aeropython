import numpy as np
import matplotlib.pyplot as plt                                                # http://matplotlib.org/gallery.html#pylab_examples

plt.plot([0.0, 0.1, 0.2, 0.7, 0.9], [1, -2, 3, 4, 1])
plt.show()
#plt.figure(figsize=(16,9))                                                     # En lugar de 'plt.show()'. Permite cambiar la resolucion


# Representar la funcion f(x)=e^(-x^2)
def f(x):
    return np.exp(-x ** 2)

x = np.linspace(-1, 3, 100)                                                    # Vector de puntos equiespaciados

plt.plot(x, f(x), label="Funcion f(x)")
plt.xlabel("Eje $x$")                                                          # Escribir LATEX encerrando entre $$
plt.ylabel("$f(x)$")
plt.legend()
plt.title("Funcion $f(x)$")
plt.show()

plt.plot(x, f(x), color='red', linestyle='', marker='o')
plt.plot(x, 1 - f(x), c='g', ls='--')
plt.show()

# Codigos abreviados
plt.plot(x, f(x), 'ro')
plt.plot(x, 1 - f(x), 'g--')
plt.show()

# Personalizacion
with plt.style.context('ggplot'):
    plt.plot(x, f(x))
    plt.plot(x, 1 - f(x))
plt.show()

with plt.xkcd():
    plt.plot(x, f(x))
    plt.plot(x, 1 - f(x))
    plt.xlabel("Eje x")
plt.show()


# Otro tipo de graficas
N = 100
x = np.random.randn(N)
y = np.random.randn(N)

plt.scatter(x, y)
plt.show()

s = np.abs(50 + 50 * np.random.randn(N))                                       # 's', 'c' modifican tamaño y color.  A cada valor numerico se le asigna un color a traves de un mapa de colores; ese mapa se puede cambiar con el argumento 'cmap'. Esa correspondencia se puede visualizar llamando a la funcion 'colorbar'
c = np.random.randn(N)

plt.scatter(x, y, s=s, c=c, cmap=plt.cm.Blues)
plt.colorbar()
plt.show()

plt.scatter(x, y, s=s, c=c, cmap=plt.cm.Oranges)                               # http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html#colormaps
plt.colorbar()
plt.show()


# Curvas de nivel de la funcion f(x)=x^2-y^2
def f(x, y):
    return x ** 2 - y ** 2

x = np.linspace(-2, 2)
y = np.linspace(-2, 2)
xx, yy = np.meshgrid(x, y)
zz = f(xx, yy)

plt.contour(xx, yy, zz)                                                        # 'contour' se utiliza para visualizar las curvas de nivel de funciones de dos variables y esta muy ligada a la función 'np.meshgrid'
plt.colorbar()
plt.show()

plt.contourf(xx, yy, zz, np.linspace(-4, 4, 100))                              # 'contourf' es casi idé'entica pero rellena el espacio entre niveles. Se pueden especificar manualmente estos niveles usando el cuarto argumento
plt.colorbar()
plt.show()


# Varias figuras
x = np.linspace(-1, 7, 1000)

fig = plt.figure()
plt.subplot(211)
plt.plot(x, np.sin(x))
plt.grid(False)
plt.title("Funcion seno")

plt.subplot(212)
plt.plot(x, np.cos(x))
plt.grid(False)
plt.title("Funcion coseno")
plt.show()

# Separar graficas: http://stackoverflow.com/a/9827848
x = np.linspace(-1, 7, 1000)

fig = plt.figure()
plt.subplot(211)
plt.plot(x, np.sin(x))
plt.grid(False)
plt.title("Funcion seno")

plt.subplot(212)
plt.plot(x, np.cos(x))
plt.grid(False)
plt.title("Funcion coseno")

fig.tight_layout()
print(fig)
