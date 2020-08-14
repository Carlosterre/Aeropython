import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize                                                     # Incluye multitud de metodos para optimizacion, ajuste de curvas y busqueda de raices

# La funcion 'root' se utiliza para hallar soluciones de sistemas de ecuaciones no lineales, por lo que funciona para ecuaciones escalares.
# No obstante, se van a utilizar las funciones 'brentq' y 'newton' para que el metodo utilizado quede mas claro

# Tipos de algoritmos para hallar raices de ecuaciones no lineales:
# -Aquellos que operan en un intervalo [a,b] tal que f(a)*f(b)<0. Mas lentos, convergencia asegurada -> Funciones 'brentq' y 'bisect'
# -Aquellos que operan dando una condicion inicial x0 mas o menos cerca de la solucion. Más rápidos, convergencia condicionada -> Funcion 'newton' que engloba los metodos de Newton y de la secante


# Ejemplo:
# lnx = senx -> F(x)=lnx-senx=0

def F(x):
    return np.log(x) - np.sin(x)

x = np.linspace(0, 10, num=100)
plt.plot(x, F(x), 'k', lw=2, label="$F(x)$")
plt.plot(x, np.log(x), label="$\log{x}$")
plt.plot(x, np.sin(x), label="$\sin{x}$")
plt.plot(x, np.zeros_like(x), 'k--')
plt.legend(loc=4)
plt.show()

print(optimize.brentq(F, 0, 3))                                                # 2.219107148913746

# Manejando arrays de NumPy las operaciones siguen las reglas dadas en el estandar de punto flotante (IEEE 754): Divisiones por cero resultan en infinito, 0/0 resulta en NaN, etc.
# Se puede controlar si se quieren warnings o errores con la función 'np.seterr'


# Ecuacion que depende de un parametro:
# sqrt(x)+logx=C

# Las funciones tienen que tomar como primer argumento la incognita (el valor que la hace cero). Si se desean incluir mas, se tiene que usar el argumento 'args' de la funciones de busqueda de raices

def G(x, C):                                                                   # La incognita es la x, por lo que debe ir en primer lugar. El resto de parametros van a continuacion, y sus valores se especifican a la hora de resolver la ecuacion usando 'args'
    return C - np.sqrt(x) - np.log(x)

print(optimize.newton(G, 2.0, args=(2,)))                                      # 1.8773216666875552


# FLUJO COMPRESIBLE
# Hallar el numero de Mach en la seccion x=0.9

def A(x):
    return 3 - 2 * x

x = np.linspace(0, 1)
area = A(x)
r = np.sqrt(area / np.pi)
plt.fill_between(x, r, -r, color="#ffcc00")
plt.show()

# 2 opciones: definir una funcion F0.9(M) que da el numero de Mach en la seccion 0.9 o una funcion F(M;x) con la que se puede hallar el numero de Mach en cualquier seccion

def F(M, x, g):
    return A(x) - (1 / M) * ((2 / (1 + g)) * (1 + (g - 1) / 2 * M ** 2)) ** ((g + 1) / (2 * (g - 1))) 

print(optimize.brentq(F, 0.01, 1, args=(0.9, 1.4)))                            # 0.5902487609888621


# ECUACION DE KEPLER (Metodo de Newton)
# 1.- Definir la funcion correspondiente a la ecuacion de Kepler, que no solo es una ecuacion implicita, sino que ademas depende de un parametro

def F(E, e, M):
    return M - E + e * np.sin(E)

# 2.- Resolverla para la excentricidad terrerestre y anomalia media M=0.3

print(optimize.newton(F, 0.3, args=(0.0167, 0.3)))                             # 0.3050151371487578

# 3.- Crear un dominio (linspace) de anomalias medias entre 0 y 2*π.
#     Resolver la ecuacion de Kepler con excentricidad terrestre para todos esos valores. Se necesita un array donde almacenar las soluciones. Representar la curva resultante

N = 500

M = np.linspace(0, 2 * np.pi, N)
sol = np.zeros_like(M)

for ii in range(N):
    sol[ii] = optimize.newton(F, sol[ii - 1], args=(0.249, M[ii]))

plt.plot(M, sol)
plt.show()

# 4.- Como ultimo paso, solo hay que meter parte del codigo ya escrito en un bucle que cambie el valor de la excentricidad 5 veces. Es aconsejable tener todo ese código en una unica celda

M = np.linspace(0, 2 * np.pi, N)
sol = np.zeros_like(M)

plt.figure(figsize=(6, 6))

for ee in 0.0167, 0.249, 0.432, 0.775, 0.967:
    # Para cada valor de excentricidad sobreescribimos el array sol
    for ii in range(N):
        sol[ii] = optimize.newton(F, sol[ii - 1], args=(ee, M[ii]))
    plt.plot(M, sol)

plt.xlim(0, 2 * np.pi)
plt.ylim(0, 2 * np.pi)
plt.xlabel("$M$", fontsize=15)
plt.ylabel("$E$", fontsize=15)
plt.gca().set_aspect(1)
plt.grid(True)
plt.legend(["Earth", "Pluto", "Comet Holmes", "28P/Neujmin", "Halley's Comet"], loc=2)
plt.title("Soluciones de la ecuacion de Kepler")
