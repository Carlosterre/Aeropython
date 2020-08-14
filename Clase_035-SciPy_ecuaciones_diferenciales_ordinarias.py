import numpy as np
import matplotlib.pyplot as plt

# Para integrar EDOs se va a usar la funcion 'odeint' del paquete 'integrate', que permite integrar sistemas del tipo:
# dy/dt=f(y,t) con condiciones iniciales y(0)=y0
#  La funcion del sistema recibe como primer argumento "y" (un array) y como segundo argumento el instante "t" (un escalar). Esta convencion va exactamente al reves que en MATLAB

from scipy.integrate import solve_ivp

# EDO ELEMENTAL con solucion conocida
# y'+y=0
# f(y,t)=dy/dt=-y

def f(t, y):
    return np.array([-y])

y0 = np.array([1])                                                             # Condiciones iniciales

tini = 0
tfin = 3

sol = solve_ivp(f, (tini, tfin), y0)                                           # Integracion y resolucion

plt.plot(sol.t, sol.y[0, :], 'o-')
plt.show()

# El solver ha seleccionado los puntos en los que se calcula la solucions. Si se desea tener control sobre estos puntos, se puede pasar de manera explicita el vector de tiempos

time = np.linspace(tini, tfin, 30)
sol_2 = solve_ivp(f, (tini, tfin), y0, t_eval=time)

plt.plot(sol_2.t, sol_2.y[0, :], 'o-')
plt.show()

plt.plot(sol_2.t, sol_2.y[0, :], 'o-')
plt.plot(sol.t, sol.y[0, :], 'o-')
plt.show()

print(f"Evaluaciones de la funcion en la solucion 1: {sol.nfev}")              # El solver siempre da los pasos que considere necesarios para calcular la solucion, pero solo guarda los que se le indican
print(f"Evaluaciones de la funcion en la solucion 2: {sol_2.nfev}")

# Se puede usar la salida densa para obtener la solucion en un punto cualquiera
sol_3 = solve_ivp(f, (tini, tfin), y0, dense_output=True)
sol_3.sol(1.14567)
t = np.linspace(tini, tfin, 45)
y = sol_3.sol(t)
plt.plot(t, y[0, :], 'o-')
plt.show()

plt.plot(t, y[0, :], '^-')
plt.plot(sol_2.t, sol_2.y[0, :], 'x-')
plt.plot(sol.t, sol.y[0, :], 'o-')
plt.show()


# EDOS DE ORDEN SUPERIOR
# y+y"=0

def f(t, y):
    return np.array([y[1], -y[0]])

t0 = 0
t1 = 10

t = np.linspace(t0, t1)
y0 = np.array([1.0, 0.0])

sol = solve_ivp(f, (t0, t1), y0, t_eval=t)

plt.plot(t, sol.y[0, :], label='$y$')
plt.plot(t, sol.y[1, :], '--k', label='$\dot{y}$')
plt.legend()
