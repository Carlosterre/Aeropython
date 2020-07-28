import numpy

print(numpy.sin(5))
print(numpy.linspace(0,100,50))
print(numpy.sin(numpy.pi))


import numpy as np

print(np.sin(5))
print(np.linspace(0,100,50))
print(np.sin(np.pi))


from numpy import linspace, sin

print(linspace(0,100,50))
print(sin(np.pi))


# Para importar TODO (no recomendado el uso de '*')
from numpy import *

a = [1,2,3,4,5]
print(sin(a))


from math import *

#print(sin(a))                                                                  # Da error, la funcion seno incorporada en NumPy no es la misma que incorpora Math. Esta ultima no admite listas, pero sobreescribe a la de NumPy
