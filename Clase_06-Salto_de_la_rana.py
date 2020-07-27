# SALTO DE LA RANA
# Un tablero con 7 huecos, en los que los 3 huecos de la izquierda contienen fichas rojas, mientras que los 3 huecos de la derecha contienen fichas azules. En el centro hay un hueco vaci≠o
# El objetivo del juego es conseguir que todas las fichas rojas ocupen las posiciones de las fichas azules, y viceversa
# Para alcanzar el objetivo las fichas rojas solo pueden moverse hacia la derecha mientras que las fichas azules solo pueden moverse hacia la izquierda
# Los movimientos permitidos son los siguientes:
# -Se puede mover una ficha una unica casilla hasta el hueco, que por supuesto debera ser contiguo
# -Se permite avanzar dos casillas con una ficha, saltando otra ficha del color contrario

# La forma de proceder es la siguiente
# -Primero hay que actuar como usuario de libreria, es decir, programar aquello que se desea, sin preocuparse de si realmente se dispone de todas las funciones a las que se est√° llamando
# -Recolectar y listar todas las funciones que se necesitan y que no esten implementadas
# -Empezar por la mas sencilla e ir una por una implementandolas (volviendo al principio de esta lista)

# main()
def main():                                                                    # Crear el tablero de juego
    board = init()
    target = board[::-1]
    
    while can_move_something(board):                                           # Ir pasando turnos hasta que no se pueda continuar
        show(board)                                                            # Pintar el tablero
        pos = int(input('Select a token to move (by its position): '))         # Pide por teclado una ficha para mover
        
        if not can_move(board, pos):                                           # Asegurarse de que se puede mover la ficha
            print('The token cannot move')
            continue
        
        board = move(board,pos)                                                # La ficha se mueve
        
        if board == target:                                                    # Comprobar si ha ganado
            print('You win')
        else:
            print('Keep moving')
            
# init()
# Creacion del tablero: Crear una lista con 7 numeros enteros, en el que el '0' representa el hueco vacio, el '1' las fichas rojas, y el '-1' las fichas azules (de paso permite saber la direccion en la que avanzan)
def init():
    return [1] * 3 + [0] + [-1] * 3

# show()
def show(board):
    print(board)
    
# can_move_something()
# Esta funcion solo debe recorrer la lista, y preguntar si alguien puede moverse. En caso de encontrar alguna ficha que pueda moverse, devolverera una respuesta afirmativa
def can_move_something(board):
    for i in range(len(board)):
        if can_move(board, i):
            return True
    return False

# move()
# Esta funcion debe intercambiar los valores de la posicion elegida y del hueco
def move(board, token):
    hole = get_hole(board)
    board[token], board[hole] = board[hole], board[token]
    return board

# get_hole()
# Debe buscar donde se encuentra el 0 en la lista, unico
def get_hole(board):
    for i, token in enumerate(board):
        if not token:
            return i

# can_move()
def can_move(board, token):
    if not -1 < token < len(board):                                            # Excluir fichas fuera del tablero
        return False
    if not board[token]:                                                       # Excluir el hueco
        return False
    hole = get_hole(board)                                                     # Localizar el hueco
    if token + board[token] == hole:                                           # Si el hueco es contiguo, y esta en el lado correcto, se puede mover
        return True
    
    # Si no es el caso, la ficha esta obligada a saltar
    if (token + 2 * board[token] == hole) and (board[token + board[token]]) != board[token]:
        return True
    return False                                                               # Si la ficha no puede avanzar o saltar, no se puede mover

main()
 