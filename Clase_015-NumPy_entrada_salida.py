# Entrada/Salida ("I/O")

import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('barrio_del_pilar-20160322.csv', skiprows=3, delimiter=';', usecols=(2,3,4))
print(data1[:10,:])

# El archivo que contiene los datos de 2015 tiene algunos agujeros por errores de medida. Como alternativa a 'loadtxt', se puede usar la función 'genfromtxt', teniendo teniendo en cuenta que el argumento opcional de saltar lineas pasa a llamarse 'skip_header'
data2 = np.genfromtxt('../data/barrio_del_pilar-20151222.csv', skip_header=3, delimiter=';', usecols=(2,3,4))
print(data2[:10,:])

print(np.mean(data2, axis=0))                                                  # Comprobar como afecta la existencia de estos valores a 'np.mean'
print(np.nanmean(data2, axis=0))                                               # Utilizando 'np.nanmean'

data_dif = data1 - data2                                                       # Diferencia entre ambos años
print(data_dif[:10,:])

# Guardar datos nuevos
np.savetxt('diferencia_interanual.txt', data_dif, fmt='%9.3f', newline = '\r\n')


# NO2. Valores maximos obtenidos de  http://www.mambiente.munimadrid.es/opencms/export/sites/default/calaire/Anexos/valores_limite_1.pdf
# Media anual: 40 µg/(m^3)
# Media horaria: 200 µg/(m^3)

plt.plot(data1[:, 1], label='2016')
plt.plot(data2[:, 1], label='2015')

plt.legend()

plt.hlines(200, 0, 200, linestyles='--')
plt.hlines(40, 0, 200, linestyles='--')
plt.ylim(0, 220)
plt.show()


# CO
# Maxima diaria de las medias moviles octohorarias: 10 mg/(m^3)

def moving_average(x, N=8):
    return np.convolve(x, np.ones(N)/N, mode='same')

plt.plot(moving_average(data1[:, 0]), label='2016')

plt.plot(moving_average(data2[:, 0]), label='2015')

plt.hlines(10, 0, 250, linestyles='--')
plt.ylim(0, 11)

plt.legend()
plt.show()


# O3
# Maxima diaria de las medias moviles octohorarias: 120 µg/(m^3)
# Umbral de información. 180 µg/(m^3)
# Media horaria. Umbral de alerta: 240 µg/(m^3)

plt.plot(moving_average(data1[:, 2]), label='2016')
#plt.plot(data1[:, 2])

plt.plot(moving_average(data2[:, 2]), label='2015')
#plt.plot(data2[:, 2])

plt.hlines(180, 0, 250, linestyles='--')
plt.ylim(0, 190)

plt.legend()


# Leer un archivo sin usar NumPy
data_file = 'barrio_del_pilar-20151222.csv'

data = []

with open(data_file) as f:
    for ii in range(3):                                                        # Saltar las 3 primeras lineas
        f.readline()
    
    for line in f:
        line_string = line
        line_list = line.split(';')
        
        date = line_list[0]
        hour = line_list[1]
        
        components_data = []
        for c in line_list[2:]:
            if '-' not in c:
                components_data.append(float(c))
            else:
                components_data.append(np.nan)
        data.append(components_data)
        
print(np.array(data))
