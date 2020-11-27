# https://github.com/PyDataMadrid2016/Conference-Info/tree/master/workshops_materials/20160408_1100_Pandas_for_beginners/tutorial

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

model = pd.read_csv(
    "model.txt", delim_whitespace=True, skiprows = 3,
    parse_dates = {'Timestamp': [0, 1]}, index_col = 'Timestamp'
)

print(model.head())

# EJERCICIOS
# 1.Representar la matriz scatter de la velocidad y orientacion del viento de los primeros mil registros.
# 2.Misma matriz scatter para los 1000 registros con mayor velocidad, ordenados.
# 3.Histograma de la velocidad del viento con 36 particiones.
# 4.Historico de la velocidad media, con los datos agrupados por años y meses.
# 5.Tabla de velocidades medias en funcion del año (filas) y del mes (columnas).
# 6.Grafica con los historicos de cada año, agrupados por meses, superpuestos.

pd.plotting.scatter_matrix(model.iloc[0:1000, 0:2])                            # Matriz scatter de la velocidad y orientacion del viento de los primeros mil registros

pd.plotting.scatter_matrix(                                                    # Matriz scatter para los 1000 registros con mayor velocidad
    model.sort_values('M(m/s)', ascending=False).iloc[0:1000, 0:2]
)

plt.show()
plt.hist(model.loc[:, 'M(m/s)'], bins=np.arange(0, 35))

model['month'] = model.index.month                                             # Historico de la velocidad media
model['year'] = model.index.year

print(model.groupby(by = ['year', 'month']).mean().head(24))

model.groupby(by=['year', 'month']).mean().plot(y='M(m/s)', figsize=(15, 5))

monthly = model.groupby(by=['year', 'month']).mean()                           # Media movil de los datos agrupados por mes y año
monthly['ma'] = monthly.loc[:, 'M(m/s)'].rolling(5, center=True).mean()

print(monthly.head())

monthly.loc[:, ['M(m/s)', 'ma']].plot(figsize=(15, 6))

print(monthly.loc[:, 'M(m/s)'].reset_index().pivot(index='year', columns='month'))

monthly.loc[:, 'M(m/s)'].reset_index().pivot(
    index='year', columns='month'
).T.loc['M(m/s)'].plot(
    figsize=(15, 5), legend=False
)

