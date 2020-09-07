# 1.- Crear una función que represente graficamente esta expresion:
#     sen(2𝜋f1t)+sen(2𝜋f2t)
#     Siendo f1 y f2 argumentos de entrada (por defecto 10 y 100) y t∈[0,0.5]. Ademas, debe mostrar:
#     -Leyenda
#     -Titulo: "Dos frecuencias"
#     -Eje x "Tiempo (t)"
#     -Debe usar algun estilo de los disponibles.

import numpy as np
import matplotlib.pyplot as plt     

def frecuencias(f1=10.0, f2=100.0):
    max_time = 0.5
    times = np.linspace(0, max_time, 1000)
    signal = np.sin(2 * np.pi * f1 * times) + np.sin(2 * np.pi * f2 * times)
    with plt.style.context("ggplot"):
        plt.plot(signal, label="Señal")
        plt.xlabel("Tiempo ($t$)")
        plt.title("Dos frecuencias")
        plt.legend()

frecuencias()


# 2.- Representar las curvas de nivel de esta funcion:
#     g(x,y)=cos(x)+sen^2(y)

def g(x, y):
    return np.cos(x) + np.sin(y) ** 2

x = np.linspace(-2, 3, 1000)                                                   # Se necesitan muchos puntos de la malla, para que al juntarse no se vean irregularidades
y = np.linspace(-2, 3, 1000)

xx, yy = np.meshgrid(x, y)

zz = g(xx, yy)

fig = plt.figure(figsize=(6, 6))                                               # Ajustar el tamaño de la figura con 'figsize'

cs = plt.contourf(xx, yy, zz, np.linspace(-1, 2, 13), cmap=plt.cm.Spectral)    # Ajustar para que tenga 13 niveles y que use el colormap Spectral
                                                                               # Asignar la salida a la variable cs para luego crear el colorbar
plt.colorbar()                                                                 # Crear la barra de colores

cs = plt.contour(xx, yy, zz, np.linspace(-1, 2, 13), colors='k')               # Con colors='k' se dibujan todas las lineas negras
                                                                               # Asignar la salida a la variable cs2 para crear las etiquetas
plt.clabel(cs)                                                                 # Crear las etiquetas sobre las lineas

plt.xlabel("Eje x")                                                            # Poner las etiquetas de los ejes
plt.ylabel("Eje y")
plt.title(r"Funcion $g(x, y) = \cos{x} + \sin^2{y}$")
