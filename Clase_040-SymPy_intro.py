# SymPy es una biblioteca de Python para matematica simbolica. Apunta a convertirse en un sistema de algebra computacional (CAS) con todas sus prestaciones, manteniendo el codigo tan simple como sea posible para manterlo comprensible y facilmente extensible.
# Esta escrito totalmente en Python y no requiere bibliotecas adicionales. Este proyecto comenzo en 2005, fue lanzado al publico en 2007 y a el han contribuido durante estos años cientos de personas.
# https://www.sympy.org/en/index.html

from sympy import init_session                                                 # Se encarga de importar todas las funciones básicas y preparar las salidas gráficas.
init_session(use_latex=True)                                                   # 'init_session lleva' a cabo algunas acciones por el usuario: Gracias a 'use_latex=True' se obtiene la salida en LATTEX

from sympy import init_printing
init_printing()

# Importar funciones utiles necesarias

from sympy import (symbols, pi, I, E, cos, sin, exp, tan, simplify, expand, factor, collect,
                   apart, cancel, expand_trig, diff, Derivative, Function, integrate, limit,
                   series, Eq, solve, dsolve, Matrix, N)

# Importar todo, pero se debe usar con cuidado:
#from sympy import *

a = symbols('a')
# Consola: 'a'
# Consola: '(a + pi) ** 2'
# Consola: 'E'
print(type(a))

b = 2 * a
# Consola: 'b'
print(type(b))

a2 = symbols('a')
a2 = 2.26492
print(type(a2))

# -Si se desesa usar una variable como simbolo debe ser creada previamente
# -Las operaciones con simbolos devuelven simbolos
# -Si una variable que almacenaba un simbolo recibe otra asignacion, cambia de tipo


# Creacion de simbolos
coef_traccion = symbols('c_T')
# Consola: 'coef_traccion'

c = symbols('b')
# Consola: 'c'

x, y, z, t = symbols('x y z t')                                                # Creacion de varios simbolos a la vez
# Consola: 'x'
# Consola: 't'

w = symbols('omega')                                                           # Simbolos griegos
W = symbols('Omega')
# Consola: 'w, W'


f, g, h, i = symbols('f g h i', real=True)                                     # Simbolos reales
print(f.assumptions0)                                                          # Asunciones de un simbolo -> Son numeros complejos


expr = cos(x)**2 + sin(x)**2
# Consola: 'expr'
# Consola: 'simplify(expr)' -> 1
# Consola: 'expr.subs(x, y**2)' -> Sustituir x por y -> sen^2(y^2)+cos^2(y^2)
# Consola: 'expr' -> La expresion no cambia

expr_2 = expr.subs(x, y**2)
# Consola: 'expr_2' -> La expresion se almacena
# Consola: 'expr.subs(sin(x), exp(x))' -> Cambia el sen(x) por exp(x)

# Consola: '(sin(x) + 3 * x).subs(x, pi)' -> Particulariza la expresion "sin(x) + 3 * x" en x=pi
# Consola: '(sin(x) + 3 * x).subs(x, pi).evalf(25)' -> Da el valor numerico


# Pi con 25 decimales
# Consola: 'pi.evalf(25)'
# Consola: 'N(pi, 25)'


# Funciones utiles:
# expand()
# factor()
# collect()
# apart()
# cancel()


# DERIVADAS E INTEGRALES
expr_3 = cos(x)
# Consola: 'diff(expr_3, x)' -> Derivada primera
# Consola: 'expr_3.diff(x)'

# Consola: 'expr_3.diff(x, x, x)' -> Derivada tercera

expr_xy = y ** 3 * sin(x) ** 2 + x ** 2 * cos(y)
# Consola: 'Derivative(expr_xy, x, 2, y)' -> Deja la expresion indicada


# Regla de la cadena
F = Function('F')                                                              # Creacion de la funcion F
# Consola: 'F(x)'
G = Function('G')                                                              # Creacion de la funcion G
# Consola: 'G(x)'

# Consola: 'F(G(x)).diff(x)'

f1 = 2 * y * exp(x)
g1 = f1 **2 * cos(x) + f1

# Consola: 'diff(g1,x)'


# Integrales
int1 = cos(x) ** 2
# Consola: 'integrate(int1)'

int2 =  1 / sin(x)
# Consola: 'integrate(int2)'

xi, ai = symbols('x a', real=True)
int3 = 1 / (xi ** 2 + ai ** 2) ** 2
# Consola: 'integrate(int3, xi)'


# LIMITES
xl = symbols('x', real=True)
expr_lim = (xl / tan(xl)) ** (1 / xl ** 2)                                     # Consola: 'expr_lim'
# Consola: 'limit(expr_lim, xl, 0)'


# SERIES
expr_ser = exp(x)                                                              # Consola: 'expr_ser'

# Consola: 'series(expr_ser)'
# Consola: 'series(expr_ser, n=10)' -> Indicar numero de terminos
# Consola: 'series(expr_ser, n=10).removeO()' -> Quita el orden superior
# Consola: 'series(sin(x), n=8, x0=pi/3).removeO().subs(x, x-pi/3)'


# ECUACIONES
ecuacion = Eq(x ** 2 - x, 3)                                                   # Consola: 'ecuacion'
# Consola: solve(equacion)

ae, xe, te, Ce = symbols('a, x, t, C', real=True)
ecuacion_2 = Eq(ae * exp(xe/te), Ce)
# Consola: 'solve(ecuacion_2, xe)'


# ECUACIONES DIFERENCIALES: y"=y
td = symbols("t")
yd = Function("y")(td)
yd_ = Derivative(yd, td)

sol = dsolve(yd_ - yd, yd)                                                     # Consola: 'dsolve(yd_ - yd, yd)'
def f(td_):
    return sol.args[1].subs([(td, td_)])

print(sol)
print(f(0))


# MATRICES

am, bm, cm, dm = symbols('a b c d')                                            # Matriz llena de simbolos
A = Matrix([
            [am, bm],
            [cm, dm]
    ])

# Consola: 'A.eigenvals()' -> Obtener autovalores
# Consola: 'A.inv()' -> Obtener la inversa
# Consola: 'A ** 2' -> Elevar al cuadrado la matriz
