# Crear una funcion que reciba el fichero 'inflammation-01.csv' por cabecera y calcule la media, el maximo y el minimo de la inflamacion. Ademas, debe representar la media de la inflamacion diaria para los pacientes

import numpy as np
import matplotlib.pyplot as plt

def analyze(file):
    data = np.loadtxt(file, delimiter=',')

    plt.plot(data.mean(axis=1))                                                # Representacion de la media de la inflamacion diaria
    plt.show()
    
    return print((data.max(), data.mean(), data.min()))                        # (Media, Maximo, Minimo)

analyze("inflammation-01.csv")
