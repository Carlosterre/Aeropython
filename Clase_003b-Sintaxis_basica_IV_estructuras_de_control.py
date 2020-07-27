# En Python los bloques se delimitan por sangrado, utilizando siempre cuatro espacios por indentacion
# Al colocar ':' al final de la primera linea del condicional, todo lo que vaya a continuación con un nivel de sangrado superior se considera dentro del condicional
# Al escribir la primera línea con un nivel de sangrado inferior, se cierra el condicional

x = 3                                                                          # Se definen dos variables
y = 1
print(x,y)

if x > y:                                                                      # If simple x > y
    print("x es mayor que y")
    
# Para añadir ramas adicionales al condicional, se puede emplear la sentencia 'elif' (abreviatura de else if). Para la parte final, que debe ejecutarse si ninguna de las condiciones anteriores se ha cumplido, se usa la sentencia 'else'
x = 0                                                                          # Se le asigna un nuevo valor a x
print(x,y)

if x > y:                                                                      # else
    print("x es mayor que y")
else:
    print("x es menor que y")
    
y = 0                                                                          # Se le asigna un nuevo valor a y
print(x, y)

if x < y:                                                                      # else if
    print("x es menor que y")
elif x == y:
    print("x es igual a y")
else:
    print("x no es ni menor ni igual que y")
    
ii = -2
while ii < 5:                                                                  # Los bucles 'while' repetiran las sentencias anidadas en el mientras se cumpla una condicion
    print(ii)
    ii += 1                                                                    # Como en el caso de los condicionales, los bloques se separan por indentacion sin necesidad de sentencias del tipo 'end'
    
# `ii += 1` equivale a `ii = ii + 1`. En el segundo, Python realiza la operación 'ii + 1' creando un nuevo objeto con ese valor y luego lo asigna a la variable 'ii'. Existe una reasignación. En el primero, sin embargo, el incremento se produce sobre la propia variable. Esto puede conducirnos a mejoras en velocidad
# Otros operadores in-place son: '-=', '*=', '/='

ii = 0                                                                         # 'break' interrumpe el bucle
while ii < 5:
    print(ii)
    ii += 1
    if ii == 3:
        break
    
ii = 0                                                                         # Un bloque else justo después del bucle se ejecuta si este no ha sido interrumpido
while ii < 5:
    print(ii)
    ii += 1
    if ii == 3:
        break
else:
    print("El bucle ha terminado")
    
ii = 0
while ii < 5:
    print(ii)
    ii += 1
    #if ii == 3:
        #break
else:
    print("El bucle ha terminado")
    
for ii in (1,2,3,4,5):                                                         # Bucle 'for'
    print(ii)
    
for nombre in "Juan", "Luis", "Carlos":
    print(nombre)

for ii in range(3):
    print(ii)
    
for jj in range(2, 5):
    print(jj)

import glob                                                                    # Importar la libreria glob

print(glob.glob('*.ipynb'))                                                    # Funcion glob dentro de la libreria glob: encuentra todos los nombres que cumplen un patron mediante una expresion regular
print(glob.glob('*.csv'))
# El resultado es una lista de strings y por lo tanto, se pude iterar a lo largo de ella y aplicar a cada fichero una funcion para analizarlo

import numpy as np
from matplotlib import pyplot as plt

def analyze(filename):                                                         # Funcion analize para explorar cada archivo
    data = np.loadtxt(fname=filename, delimiter=',')
    plt.plot(data.mean(axis=0))   
    plt.show()

analyze('inflammation-01.csv')
analyze('inflammation-02.csv')
analyze('inflammation-09.csv')

filenames = glob.glob('*.csv')
filenames = filenames[0:3]
for f in filenames:
    print(f)
    analyze(f)
