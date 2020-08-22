# http://docs.sympy.org/0.7.5/modules/physics/mechanics/index.html

from sympy import init_session
init_session(use_latex=True)

from sympy import init_printing
init_printing()

from sympy import symbols

# SISTEMAS DE REFERENCIA
from sympy.physics.mechanics import ReferenceFrame
A = ReferenceFrame("A")
# Consola: 'A.x'

# Para definir vectores, hay que multiplicar cada componente por su versor
# Consola: '2 * A.x - 1 * A.y'

# Forma de proceder: 
# -Definir un sistema inercial 1 del que partir, para asi poder referir todos los demas sistemas a este
# -Los versores del sistema han de ser i, j, k

B = ReferenceFrame("1", latexs=['\mathbf{i}', '\mathbf{j}', '\mathbf{k}'])
# Consola: 'B.x + B.y + B.z'

# Para evitar hacerlo siempre, se puede crear una clase para que los versores sean i, j, k
class IJKReferenceFrame(ReferenceFrame):
    def __init__(self, name):
        super().__init__(name, latexs=['\mathbf{%s}_{%s}' % (idx, name) for idx in ("i", "j", "k")])
        self.i = self.x
        self.j = self.y
        self.k = self.z

C = IJKReferenceFrame("1")
# Consola: 'C.i + C.j + C.k'


# ALGEBRA VECTORIAL
R, V = symbols('R, V', positive=True)
r1 = R * (C.x + C.y + C.z)
v1 = V * (C.x - 2 * C.z)

# Consola: 'r1'
# Consola: 'v1'

from sympy.physics.mechanics import dot, cross

r1.dot(v1)
dot(r1, v1)

# Consola: 'r1 & v1' -> -RV

r1.cross(v1)
cross(r1, v1)

# Consola: 'r1 ^ v1'


# Obtener la norma de los vectores con 'magnitude' y normalizalos con 'normalize'
# Consola: '(r1 ^ v1).magnitude()'
# Consola: '(r1 ^ v1).normalize()'


# MOVIMIENTO RELATIVO

A1 = IJKReferenceFrame("1")
A0 = IJKReferenceFrame("0")

phi = symbols('phi')
A0.orient(A1, 'Axis', [phi, A1.z])                                             # Rotacion phi alrededor del eje A1*z. 'orient' especifica la orientacion de los sistemas de referencia
# Consola: 'A0.dcm(A1)' -> 'dcm' recupera la matriz de cosenos directores

# Con el argumento 'Axis' se ha especificado que se rota el sistema un angulo especificado alrededor de un eje. Otros metodos son:
# -Body: se especifican los tres angulos de Euler
# -Space: igual que 'Body', pero las rotaciones se aplican en orden inverso
# -Quaternion: utilizando cuaternios, rotacion alrededor de un vector unitario λ una cantidad θ

# Consola: 'A0.x.express(A1)' -> 'express' o 'to_matrix' para expresar un vector en otro sistema de referencia
# Consola: 'A0.x.to_matrix(A1)'

# Simbolos dinamicos. Si un simbolo varia con el tiempo, utilizar 'dynamicsymbols'
from sympy.physics.mechanics import dynamicsymbols
alphat = dynamicsymbols('alpha')
# Consola: 'alphat'
# Consola: 'alphat.diff()' -> Pide su derivada


# DERIVADA EN EJES MOVILES

A2 = IJKReferenceFrame("A2")
psi = dynamicsymbols('psi')
A2.orient(A, 'Axis', [psi, A.z])

v1m = A2.x

#v1.diff(dynamicsymbols._t, A2)
dv1m = v1m.diff(symbols('t'), A2)
# Consola: 'dv1m'
# Consola: 'dv1m.to_matrix(A2)'
# Consola: '(dv1m & A2.i).simplify()'


# PUNTOS Y VELOCIDADES
from sympy.physics.mechanics import Point                                      # Posibilidad de definir puntos en solidos y aplicar su campo de velocidades

O = Point("O")
O.set_vel(A2, 0)

e_b = symbols('e_b')
E_b = O.locatenew('E_b', e_b * A1.x)                                           # 'locatenew' para colocar nuevos puntos
# Consola: E_b.pos_from(O) -> Obtener vectores de un punto a otro

# La notacion de este paquete esta influenciada por el libro: Kane, T. R. & Levinson, D. A. "Dynamics, Theory and Applications"
