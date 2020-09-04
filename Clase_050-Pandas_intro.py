import pandas as pd
import matplotlib.pyplot as plt

# Datos de https://www.juntadeandalucia.es/agriculturaypesca/ifapa/riaweb/web/

#pd.read_csv('tabernas_meteo_data.txt').head(5)                                 # No funciona, pues el archivo no tiene formato csv

# Cambios a realizar:
# -Separar los campos por un numero arbitrario de espacios en blanco
# -Saltar las primeras lineas
# -Dar nombres nuevos a las columnas
# -Descartar la columna del dia del año (Se puede calcular luego)
# -Parsear las fechas en el formato correcto

data = pd.read_csv(
    "../data/tabernas_meteo_data.txt",
    delim_whitespace=True,                                                     # Delimitado por espacios en blanco
    usecols=(0, 2, 3, 4, 5),                                                   # Columnas que se desean usar
    skiprows=2,                                                                # Saltar las dos primeras lineas
    names=['DATE', 'TMAX', 'TMIN', 'TMED', 'PRECIP'],
    parse_dates=['DATE'],
    #date_parser=lambda x: pd.datetime.strptime(x, '%d-%m-%y'),                 # Parseo manual
    dayfirst=True,                                                             # Importante
    index_col=["DATE"]                                                         # Si se quiere indexar por fechas
)

# Ordenando de mas antigua a mas moderna
data.sort_index(inplace=True)

# Mostrando solo las primeras o las ultimas lineas
data.head()

print(data.dtypes)                                                             # Tipo de datos
print(data.info())                                                             # Informacion general del dataset
print(data.describe())                                                         # Informacion estadistica

print(data.index.dayofweek)


# ACCESO A LOS DATOS
print(data['TMAX'].head())                                                     # Como clave
print(data.TMIN.head())                                                        # Como atributo
print(data[['TMAX', 'TMIN']].head())                                           # Acceder a varias columnas a la vez
print(data[['TMAX', 'TMIN']] / 10)                                             # Modificar valores de columnas


import numpy as np
print(np.mean(data.TMAX))                                                      # Funcion media a una columna entera
print(data.TMAX.mean())                                                        # Media con pandas

print(data.iloc[1])                                                            # Accediendo a una fila por indices
print(data.loc["2016-09-02"])                                                  # Accediendo a una fila por etiqueda

print(data.loc["2016-12-01":])                                                 # Secciones basadas en fechas

print(data.loc[data.TMIN.isnull()])                                            # Busqueda de valores nulos

# Agrupar datos: 'groupby'
data['year'] = data.index.year
data['month'] = data.index.month
monthly = data.groupby(by=['year', 'month'])

print(monthly.groups.keys())                                                   # Ver grupos creados

print(monthly.get_group((2016,3)).head())                                      # Acceder a un grupo

# Agregacion de datos
monthly_mean = monthly.mean()
monthly_mean.head(24)

print(monthly_mean.reset_index().pivot(index='year', columns='month'))         # Dejar los años como indices y ver la media mensual en cada columna

print(monthly.TMAX.mean().head(15))                                            # Media de la columna TMAX

print(monthly_mean.TMAX.rolling(3, center=True).mean().head(15))               # Media mensual cerrada


# GRAFICAS
data.plot(y=["TMAX", "TMIN", "TMED"])                                          # Pintar la temperatura max, min, med
plt.title("Temperaturas")
plt.show()

# Cajas
data.loc[:, 'TMAX':'PRECIP'].plot.box()
plt.show()

# Temperatura maxima de las maximas, minima de las minimas, media de las medias para cada año disponible
group_daily = data.groupby(['month', data.index.day])
daily_agg = group_daily.agg({'TMED': 'mean', 'TMAX': 'max', 'TMIN': 'min', 'PRECIP': 'mean'})

print(daily_agg.head())

daily_agg.plot(y=['TMED', 'TMAX', 'TMIN'])
plt.show()
