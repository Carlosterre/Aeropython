# Forzar que la division sea entera en con el operador '//'
# Elevar un numero a otro con el operador '**'
# Valor absoluto del numero complejo (2+3j) con 'abs(2 + 3j)'
# '_1' recupera el Out[1] como variable
# 'int(18.6)' convierte el numero 18.6 en entero: 18
# 'round(18.6)' redondea el numero 18.6: 19
# 'float(1)' convierte el numero 1 en flotante: 1.0
# 'complex(2)' convierte el numero 2 en complejo: (2+0j)
# 'str(256568)': 256568

a = 2.                                                                         # 'type(a)' comprueba el tipo de la variable a
                                                                               # 'isinstance(a, float)' compara el tipo de la variable a con el solicitado. Booleano
                                                                               
x, y = 1, 2                                                                    # Asignacion multiple

# 'x == y': False. Operadores de comparacion: '==' igual a, '!=' distinto de, '<' menor que, '<=' menor o igual que. Booleanos
                                                                              
print(x != y)                                                                  # Booleanos
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)

b = 5.                                                                         # '6. < b < 8.': False
                                                                               
print('hola mundo')                                                            # Imprime en pantalla el texto entrecomillado

# 'max(1,5,8,7)': 8
# 'min(-1,1,0)': -1
                                                                           
lista = [1, 2, 3.0, 4 + 0j, "5"]                                               # Lista entre corchetes
tupla = (1, 2, 3.0, 4 + 0j, "5")                                               # Tupla entre parentesis
print(lista)                                                                   # 'print(lista)' para mostrar la lista en pantalla
print(tupla)
print(lista == tupla)                                                          # Booleano

tupla_dos = 2, 5, 6, 9, 7                                                      # En las tuplas se pueden obviar los parentesis
                                                                               
# '2 in lista' para comprobar si la lista contiene un 2. Booleano
# 'len(lista)' para saber cuantos elementos tiene la lista
                                                                               
print(lista[0])                                                                # Primer elemento de la lista: 1
print(tupla[1])                                                                # Segundo elemento de la tupla: 2
print(lista[0:2])                                                              # Desde el primero hasta el tercero de la lista, excluyendo este: [1, 2]
print(tupla[:3])                                                               # Desde el primero hasta el cuarto de la tupla, excluyendo este: (1, 2, 3.0)
print(lista[-1])                                                               # El ultimo de la lista: 5
print(tupla[:])                                                                # Desde el primero hasta el ultimo de la tupla
print(lista[::2])                                                              # Desde el primero hasta el ultimo de la lista, saltando 2: [1, 3.0, '5']
                                                                               # La indexacion empieza por 0
                                                                               