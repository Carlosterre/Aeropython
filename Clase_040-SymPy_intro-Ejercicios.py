# EJERCICIOS

from sympy import init_session
init_session(use_latex=True) 

from sympy import init_printing
init_printing()

from sympy import (symbols, sin, expand, expand_trig)

#%% 1.-
print('1.-')

x, y = symbols('x y')                                                          # Consola: 'expr1'
expr1 = (x ** 3 + 3 * y + 2) ** 2
sol1 = expr1.expand()                                                          # Consola: 'sol1'


#%% 2.-
print('2.-')

expr2 = (3 * x ** 2 - 2 * x + 1) / (x - 1) ** 2                                # Consola: 'expr2'
sol2 = expr2.apart()                                                           # Consola: 'sol2'


#%% 3.-
print('3.-')

expr3 = x ** 3 + 9 * x ** 2 + 27 * x + 27                                      # Consola: 'expr3'
sol3 = expr3.factor()                                                          # Consola: 'sol3'


#%% 4.-
print('4.-')

expr4 = sin(x + 2 * y)                                                         # Consola: 'expr4'
expr4_exp = expand(expr4)
expr4_exp2 = expand_trig(expr4)
sol4 = expand(expr4, trig=True)                                                # Consola: 'sol4'
