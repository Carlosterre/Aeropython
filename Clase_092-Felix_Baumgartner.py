# FELIX BAUMGARTNER

import numpy as np
import matplotlib.pyplot as plt

def T_ISA_1(h):
    """Temperature depending on height according to ISA model
    
    Parameters
    ----------
    h : Height in meters

    Returns
    -------
    T : Temperature in Kelvin

    """
    T0 = 288.16                                                                # K
    ll = -6.5e-3                                                               # Lambda, adimensional
    if 0 <= h <= 11000:
        T = T0 + ll * h
    elif 11000 < h:
        T = T0 + ll * 11000
    return T                                                                   # Es preferible que la funcion tenga un solo return


print(help(T_ISA_1))


from numpy.testing import assert_almost_equal

assert_almost_equal(T_ISA_1(0), 288.16)                                          # Tests que comprueban de que las funciones funcionan
assert_almost_equal(T_ISA_1(11000), 216.66)


# Si se utilizan condicionales para comprobar las capas de la atmosfera, seguramente as funciones fallaran si se quieren representar utilizando un 'linspace'. Para estos casos es mejor utilizar la funcion 'np.select'
def T_ISA_2(h):
    """Temperature depending on height according to ISA model
    
    Parameters
    ----------
    h : Height in meters

    Returns
    -------
    T : Temperature in Kelvin

    """    
    h = np.asarray(h)                                                          # Convierte la entrada en un array
    
    T0 = 288.16                                                                # K
    ll = -6.5e-3                                                               # Lambda. K/m
    
    T1 = T0 + ll * h
    T2 = T0 + ll * 11000
    
#   if 0 <= h <= 11000:                                                        # No funciona para arrays
#       T = T0 + ll * h
#   elif 11000 < h:
#       T = T0 + ll * 11000

    T = np.select([(0 <= h)&(h <= 11000), 11000 < h], [T1, T2])    
    return T


print(T_ISA_2(0))
print(T_ISA_2(np.array([0, 11000, 20000])))
print(T_ISA_2([0, 11000, 20000]))                                              # Gracias a que se ha utilizado 'asarray'


# Forma alternativa
def T_ISA_3(h):
    """Temperature depending on height according to ISA model
    
    Parameters
    ----------
    h : Height in meters

    Returns
    -------
    T : Temperature in Kelvin

    """
    h = np.atleast_1d(h)                                                       # Convierte la entrada a un array

    T0 = 288.16                                                                # K
    ll = -6.5e-3                                                               # K/m

    T = np.zeros_like(h, dtype=float)

    T[(0 <= h) & (h <= 11000)] = T0 + ll * h[(0 <= h) & (h <= 11000)]
    T[11000 < h] = T0 + ll * 11000
    return T


print(T_ISA_3(0))
print(T_ISA_3([0, 11000, 20000]))


def rho_ISA(h):
    h = np.asarray(h)

    T0 = 288.16                                                                # K
    ll = -6.5e-3                                                               # K/m
    g = 9.8                                                                    # m/s^2
    rho0 = 1.225                                                               # kg/m^3
    R = 287.0                                                                  # [SI]

    rho1 = rho0 * (T_ISA_2(h) / T0) ** (-g / (ll * R) - 1)
    
    rho2 = rho0 * (T_ISA_2(11000) / T0) ** (-g / (ll * R) - 1) * np.exp(-g * (h - 11000) / (R * T_ISA_2(h)))

    rho = np.select([(0 <= h) & (h <= 11000), 11000 < h], [rho1, rho2])
    return rho

print(rho_ISA([0, 11000, 20000]))


# 'integrate.odeint' resuelve ecuaciones del tipo:
# dy/dt=f(y,t) con condiciones iniciales y(0)=y0.
# Al tratarse de una ecuación en derivada segunda, hay que hacer una reduccion de orden

from scipy import integrate
import matplotlib.pyplot as plt

def f(y, t):                                                                   # Funcion del sistema
    g = 9.8                                                                    # m/s^2
    C_D = 0.4
    A = 1.0                                                                    # m^2
    m = 80                                                                     # kg
    return np.array([
        y[1],
        -g + rho_ISA(y[0]) * y[1] ** 2 * C_D * A / (2 * m)
    ])


y0 = np.array([39000, 0])                                                      # Condiciones iniciales
t = np.linspace(0, 250)                                                        # Vector de tiempos
sol = integrate.odeint(f, y0, t)                                               # Integra la ecuacion

pos = sol[:, 0]                                                                # Primera columna: posicion
vel = sol[:, 1]                                                                # Segunda columna: velocidad

# Representacion de la solucion
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6, 6))
line, = axes[0].plot(t, pos / 1e3, label="Position $y$")
axes[0].set_ylabel("Position (km)")
axes[1].plot(t, vel, '--', color=line.get_color(), label="Velocity $\dot{y}$")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].set_xlabel("Time (s)")
axes[0].legend()
axes[1].legend()
axes[0].set_title("Felix Baumgartner free fall")
fig.tight_layout()
plt.show()

# Barrera del sonido
gamma = 1.4
R = 287.0                                                                      # [SI]
c = np.sqrt(gamma * R * T_ISA_2(pos))

M = np.abs(vel) / c

plt.plot(t, M)
plt.plot(t, np.ones_like(t), 'k--')
plt.ylabel('Mach number')
plt.xlabel('Time (s)')
plt.title("Mach number")
plt.show()
