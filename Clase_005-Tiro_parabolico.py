# TIRO PARABOLICO
# Averiguar la velocidad necesaria para lanzar un proyectil con un determinado angulo a una determinada distancia utilizando un metodo numerico

import math

G = 9.81                                                                       # m/(s^2)

# main()
def main(angle=45, rel_tol=1E-3):                                              # 45º
    angle = math.radians(angle)                                                # Convertir el angulo a radianes

    # El metodo se basa en saber donde se acerto la vez anterior y donde se acierta esta, para estimar la velocidad para la siguiente
    # Por tanto, se necesitan unas condiciones iniciales
    
    v0, d0, v1, d1 = init(angle)                                               # Hay que implementar la funcion init()

    d = float(input('Where is the target? (m): '))                              # Pedir la distancia por teclado
  
    while abs(d1 - d) / d > rel_tol:                                           # Iterar hasta encontrar una solucion
        v0, d0, v1, d1 = bissection(v0, d0, v1, d1, angle, d)                  # Hay que implementar la funcion bissection()
    
    print('v = {} m/s, d = {} m'.format(v1, d1))                               # Se imprimen
    
# init()
def init(angle):
    v0, d0 = 0.0, 0.0                                                          # El primer tiro puede ser, sencillamente, no ir a ninguna parte
    v1 = 1.0                                                                   # El segundo tiro a 1 m/s
    d1 = shot(angle, v1)                                                       # Hay que implementar la funcion shot()
    
    return v0, d0, v1, d1

# shot()
def shot(angle, v):
    vx, vy = v * math.cos(angle), v * math.sin(angle)                          # Lo primero es obtener las componentes x e y de la velocidad
    t = 2 * vy / G                                                             # Con ellas, se saca el tiempo de vuelo
   
    return vx * t                                                              # Con lo anterior, se obtiene el alcance

# bissection()
def bissection(x_a, f_a, x_b, f_b, angle, f):
    if f_a > f_b:                                                              # Reordenar si es necesario
        x_a, f_a, x_b, f_b = x_b, f_b, x_a, f_a
    
    if f_a < f < f_b:                                                          # Obtener una nueva aproximacion para la velocidad
        x_c = 0.5 * (x_a + x_b)
        
    else:
        x_c = 2.0 * x_b
    
    f_c = shot(angle, x_c)                                                     # El alcance correspondiente

    if f_c > f:                                                                # Comprobar en que subintervalo esta
        return x_a, f_a, x_c, f_c
    return x_b, f_b, x_c, f_c

main()                                                                         # 20: v = 14.0078125 m/s, d = 20.001917536713176 m
