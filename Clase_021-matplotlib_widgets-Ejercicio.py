# Crear una función que represente graficamente esta expresion:
# sen(2𝜋f1t)+sen(2𝜋f2t)
# Siendo f1 y f2 argumentos de entrada (por defecto 10 y 100) y t∈[0,0.5]. Ademas, debe mostrar:
# -Leyenda
# -Titulo: "Dos frecuencias"
# -Eje x "Tiempo (t)"
# -Debe usar algun estilo de los disponibles.

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

# Componentes interactivos
from ipywidgets import interact

interact(frecuencias, f1=(10.0, 200.0), f2=(10.0, 200.0))
