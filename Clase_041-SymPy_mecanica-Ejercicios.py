from sympy import init_session
init_session(use_latex=True)

from sympy import init_printing
init_printing()

from sympy import symbols

from sympy.physics.mechanics import ReferenceFrame

class IJKReferenceFrame(ReferenceFrame):
    def __init__(self, name):
        super().__init__(name, latexs=['\mathbf{%s}_{%s}' % (idx, name) for idx in ("i", "j", "k")])
        self.i = self.x
        self.j = self.y
        self.k = self.z


# 1.-
print("1.-")

R, Omega = symbols('R, Omega', positive=True)
A0 = IJKReferenceFrame('0')

a = R * A0.i
omega01 = Omega * A0.k
da = omega01 ^ a                                                               # Consola: 'da'


# 2.-
print("2.-")

from sympy.physics.mechanics import dynamicsymbols
init_printing(pretty_print=False)                                              # La representacion grafica puede fallar, pero se puede volver a desactivar y activar llamando a la funcion 'init_printing(pretty_print=True)' con diferentes valores True/False

A = IJKReferenceFrame("A")

A1 = IJKReferenceFrame("A1")
psi = dynamicsymbols('psi')
A1.orient(A, 'Axis', [psi, A.z])                                               # Consola: 'A1.dcm(A)' -> T_{A1A}


A2 = IJKReferenceFrame("A2")
beta = dynamicsymbols('beta')
A2.orient(A1, 'Axis', [beta, -A1.y])                                           # Consola: 'A2.dcm(A1)' -> T_{A2A1}

A3 = IJKReferenceFrame("A3")
zeta = dynamicsymbols('zeta')
A3.orient(A2, 'Axis', [zeta, A2.z])                                            # Consola: 'A3.dcm(A1)' -> T_{A3A1}

B = IJKReferenceFrame("B")
theta = dynamicsymbols('theta')
B.orient(A3, 'Axis', [theta, A3.x])                                            # Consola: 'B.dcm(A3)' -> T_{BA3}
                                                                               #          'B.dcm(A2)'
                                                                               #          'B.dcm(A1)'
                                                                               

# 3.- DISCO QUE RUEDA SIN DESLIZAR
print("3.-")

from sympy.physics.mechanics import Point
init_printing(pretty_print=True)        

A1r = IJKReferenceFrame('1')                                                   # Crear sistema de referencia
A0r = IJKReferenceFrame('0')
A2r = IJKReferenceFrame('2')

xi, theta = dynamicsymbols('xi, theta')                                        # Crear simbolos necesarios -> Consola: 'xi, theta'

A0r.orient(A1r, 'Axis', [0, A1r.k])                                            # Orientar sistemas de referencia, A0 no gira respecto a A1
A2r.orient(A0r, 'Axis', [theta, A0r.k])
# Consola: 'A2r.dcm(A1r)'
 
C = Point('C')                                                                 # Crear punto del disco y especificar velocidad respecto a A1
C.set_vel(A1r, xi.diff() * A1r.x)

R = symbols('R')                                                               # Localizar el punto P, punto fijo del disco, respecto a C en sistema A2 (que gira solidariamente con el disco)
P = C.locatenew('P', -R * A2r.j)
# Consola: 'P.pos_from(C)'

# Hallar la velocidad de P en A1, expresada en A0. Con esta llamada ya se esta diciendo que C y P son fijos en A2
# Consola: 'P.v2pt_theory(C, A1r, A2r).express(A0r)'
