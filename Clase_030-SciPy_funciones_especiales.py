import numpy as np
import matplotlib.pyplot as plt
from scipy import special

x = np.linspace(0, 20, 100)
for i in range(5):
    plt.plot(x, special.jn(i, x))                                              #  "jn       -- Bessel function of integer order and real argument"
plt.grid(True)
