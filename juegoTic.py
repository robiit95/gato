def muestra_tablero(tablero):
    tableroNuevo="""
    | 7 | 8 | 9 |
    | 4 | 5 | 6 |
    | 1 | 2 | 3 |
    """
    for i in range(1,10):
        if (tablero[i] == 'O' or tablero[i] == 'X'):
            tableroNuevo = tableroNuevo.replace(str(i), tablero[i])
        else:
            tableroNuevo = tableroNuevo.replace(str(i), ' ')
    print(tableroNuevo)


def entrada_jugador():
    jugador1 = input("Ingresa tu ficha 'X' o 'O': ")
    while True:
        if jugador1.upper() == 'X':
            jugador2 = 'O'
            print("Elegiste " + jugador1 + ". El jugador 2 sera " + jugador2)
            return jugador1.upper(), jugador2
        elif jugador1.upper() == 'O':
            jugador2 = 'X'
            print("Elegiste " + jugador1 + ". El jugador 2 sera " + jugador2)
            return jugador1.upper(), jugador2
        else:
            jugador1 = input("Ingresa tu ficha 'X' o 'O': ")
    

def lugar_ficha(tablero, marca, posicion):
    tablero[posicion] = marca
    return tablero


def verifica_espacio(tablero, posicion):
    return tablero[posicion] == '#'


def verifica_tablero_lleno(tablero):
    return len([x for x in tablero if x == '#']) == 1


def verifica_ganador(tablero, marca):
    if tablero[1] == tablero[2] == tablero[3] == marca:
        return True
    if tablero[4] == tablero[5] == tablero[6] == marca:
        return True
    if tablero[7] == tablero[8] == tablero[9] == marca:
        return True
    if tablero[1] == tablero[4] == tablero[7] == marca:
        return True
    if tablero[2] == tablero[5] == tablero[8] == marca:
        return True
    if tablero[3] == tablero[6] == tablero[9] == marca:
        return True
    if tablero[1] == tablero[5] == tablero[9] == marca:
        return True
    if tablero[3] == tablero[5] == tablero[7] == marca:
        return True
    return False


def opcion_jugador(tablero):
    opcion = input("Ingresa un espacio vacio entre 1 y 9: ")
    while not verifica_espacio(tablero, int(opcion)):
        opcion = input("Este espacio no esta vacio, ingresa uno vacio entre 1 y 9: ")
    return opcion


def reiniciar():
    jugar = input("¿Quieres jugar de nuevo (s/n)? ")
    if jugar.lower() == 'y':
        return True
    if jugar.lower() == 'n':
        return False


print("Juego de Gato/Tic Tac Toe!")
i=1
#seleccionar ficha
jugadores = entrada_jugador()
#tablero vacio
tablero = ['#'] * 10
while True:
    #inicia juego
    inicia_juego = verifica_tablero_lleno(tablero)
    while not inicia_juego:
        #elegir donde poner la marca
        posicion = opcion_jugador(tablero)
        #quien estara jugando?
        if i % 2 == 0:
            marca = jugadores[1]
        else:
            marca = jugadores[0]
        #juega
        lugar_ficha(tablero, marca, int(posicion))
        #revisando el tablero
        muestra_tablero(tablero)
        i += 1
        if verifica_ganador(tablero, marca):
            print("Ganaste!")
            break
        inicia_juego = verifica_tablero_lleno(tablero)
    if not reiniciar():
        break
    else:
        i = 1
        #selecciona el lado
        jugadores=entrada_jugador()
        #tablero vacio
        tablero = ['#'] * 10
