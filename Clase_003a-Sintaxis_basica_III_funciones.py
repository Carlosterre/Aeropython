def fahr_to_kelvin(temp):                                                      # Funcion:  'def' seguido del 'nombre_de_la_funcion' y, entre parentesis, los argumentos de entrada. La cabercera de la función termina con ':'
    return ((temp - 32) * (5/9)) + 273.15                                      # Cuerpo de la funcion, indentado con cuatro espacios. Escribir 'return' y los argumentos de salida. Si la funcion no devuelve nada, no hace falta usar 'return'. La definicion de la funcion termina cuando la indentacion vuelve a su nivel inicial

print('freezing point of water:', fahr_to_kelvin(32))                          # Punto de congelacion del agua en Kelvin (32 F)
print('boiling point of water:', fahr_to_kelvin(212))                          # Pnto de ebullicion del agua en Kelvin (212 F)

def kelvin_to_celsius(temp):                                                   # Funcion que llama a otra funcion
    return temp - 273.15

print('absolute zero in Celsius:', kelvin_to_celsius(0.0))                     # Cero absoluto en Celsius

def fahr_to_celsius(temp):                                                     # Convertir de Fahrenheit a Celsius
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

print('freezing point of water in Celsius:', fahr_to_celsius(32.0))            # Punto de congelacion del agua en Celsius (32 F)

import numpy as np                                                             # Importar numpy

def span(a):                                                                   # Definir funcion span (rango)
    diff = a.max() - a.min()                                                   # diff: variable creada no accesible
    return diff

data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')                  # Cargar los datos
# 'span(data)' muestra el rango: 20
diff = span(data)                                                              # Se define la variable 'diff' fuera de la funcion
print(diff)


x = 1
def add_one():
    print('x before: ', x)
    print('x after: ', x + 1)                                                  # x = x + 1
    
add_one()

# La documentacion de una funcion se almacena en el llamado docstring. Esta cadena de documentacoón va justo despues de la cabecera y se define entre comillas triples
def center(data, desired):                                                     # Funcion que centre los datos en torno a un valor que se pase por cabecera  
   
    """Return a new array containing the original data centered around the desired value
    Example: center([1, 2, 3], 0) => [-1, 0, 1]"""
    
    return (data - data.mean()) + desired

help(center)

# 'np.loadtxt('../data/swc/inflammation-01.csv', delimiter=',')': array(...)

def center(data, desired=0.0):                                                 # Funcion definida con valores por defecto para algunos de sus argumentos, de modo que pueden ser llamadas sin especificar el valor de esos argumentos cada vez

    '''Return a new array containing the original data centered around the desired value (0 by default)
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    
    return print((data - data.mean()) + desired)

test_data = np.zeros((2, 2))                                                   # Array de ceros para probar
center(test_data)                                                              # Sin especificar desired
center(test_data, desired=0)                                                   # Especificando el argumento con su nombre
center(test_data, 0)                                                           # Especificando el argumento en su posicion

def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

display()
display(10)
display(10, 20, 30)
display(b=50)
