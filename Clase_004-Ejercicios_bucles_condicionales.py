# 1.- Escribir una funcion que sume los n primeros numeros naturales
print('EJERCICIO 1.-')

def sumatorio(num):
    
    """Suma los n primeros numeros
    Ejemplo: sumatorio(4) = 10"""
    
    suma = 0                                                                   # Suma se inicializa en 0
    for nn in range(1, num + 1):
        suma = nn + suma                                                       # Se acumulan los num primeros numeros naturales
    return print(suma)

help(sumatorio)
sumatorio(4)

list(range(1, 4 + 1))                                                          # Comprobar el resultado correcto con la funcion 'sum' de Python, que suma los elementos introducidos
print(sum(range(1, 4 + 1)))


# 2.- Escribir una funcion que sume numeros naturales consecutivos y no se pase de un determinado limite. Ademas, debe mostrar el valor de la suma
print('EJERCICIO 2.-')

def suma_tope(tope):
    
    """Suma numeros naturales consecutivos hasta un tope"""
    
    suma = 0
    nn = 1
    while suma + nn <= tope:
        suma = suma + nn
        nn += 1
    return print(suma)

help(suma_tope)

suma_tope(9)
suma_tope(10)


# 3.- "Si un examen dura mas de 3 horas, entonces debe tener un descanso". Los argumentos de la funcion son el tiempo en horas y un valor True o False que indica si hay descanso o no
print('EJERCICIO 3.-')

def cumple_normativa(tiempo, descanso):
    
    """Comprueba si un examen cumple la normativa de la UPM"""
    
    if tiempo <= 3:
        return True
    else:
        #if descanso:
        #    return True
        #else:
        #    return False
        return descanso                                                        # Equivalente

help(cumple_normativa)

print(cumple_normativa(2, False))

if not cumple_normativa(5, descanso=False):
    print("No cumple normativa")

    
# 4.- Hallar x = sqrt(S)
# 1. x -> S/2
# 2. x -> 1/2*(x+S/2)
# 3. Repetir 2. hasta que se alcance un limite de iteraciones o un criterio de convergencia
print('EJERCICIO 4.-')

def raiz(S):                                                                   # Truco de la aritmetica en punto flotante: como la convergencia se alcanza rapidamente, llega un momento en que el error es menor que la precision de la maquina y el valor no cambia de un paso a otro
    x = S / 2
    while True:
        temp = x
        x = (x + S / x) / 2
        if temp == x:
            return print(x)

raiz(10)

import math

print(math.sqrt(10))
print(math.sqrt(10) ** 2)                                                      # Ver: puntoflotante.org


# 5.- Secuencia de Fibonacci: Fn = Fn+1 + Fn-2, con F0 = 0 y F1 = 1
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
print('EJERCICIO 5.-')

def fib(n):
    a, b = 0, 1                                                                # Asignacion multiple
    for i in range(n):
        a, b = b, a + b
    return print(a)

fib(0)
fib(3)
fib(10)

def fib_recursivo(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib_recursivo(n - 1) + fib_recursivo(n - 2)
    return res

def n_primeros(n):
    F = fib_recursivo
    lista = []
    for ii in range(n):
        lista.append(F(ii))
    return print(lista)

n_primeros(10)


# 6.- Ley D'Hont
# El sistema se basa en ir repartiendo escaños consecutivamente al partido con el maximo coeficiente: Ci=Vi/(Si+1) donde Vi es el numero total de votos obtenido por del partido i, mientras que Si es el numero de escaños asignados dicho partido (0 al comenzar el reparto)
print('EJERCICIO 6.-')

def hondt(votos, n):
    s = [0] * len(votos)
    for i in range(n):
        c = [v[j] / (s[j] + 1) for j in range(len(s))]
        s[c.index(max(c))] += 1
    return print(s)

v = [340000, 280000, 160000, 60000, 15000]                                     # Numero de votos
n = 7                                                                          # Numero de escaños
hondt(v, n)
