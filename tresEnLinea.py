matrizCoord=[['(0, 0)','(0, 1)','(0, 2)'], ['(1, 0)','(1, 1)','(1, 2)'], ['(2, 0)','(2, 1)','(2, 2)']]
matrizTab=[['_','_','_'], ['_','_','_'], ['_','_','_']]

#jugador1
#jugador2


######Funciones######


"""def MostrarMatriz():
    print("La matriz es la siguiente: ")
    for fila in matrizCoord:
        for valor in fila:
            print("\t", valor, end=" ")
        print()"""

def ElegirLado():
    jugador1=input("Selecciona tu simbolo para jugar X/O: ")
    #jugador2
    if jugador1 == 'x' or jugador1 == 'X':
        jugador2 = 'O'
        return False, jugador1, jugador2
    elif jugador1 == 'o' or jugador1 == 'O':
        jugador2 = 'X'
        return False, jugador1, jugador2
    else:
        print("Elige la ficha correcta X/O")
        return True, ' ', ' '


def TiraFicha():
    coordenadax = input("Jugador 1, ingrese la coordenada de su ficha (X): ")
    coordenadax = int(coordenadax)
    coordenaday = input("Jugador 1, ingrese la coordenada de su ficha (Y): ")
    coordenaday = int(coordenaday)
    if (coordenadax >= 0 and coordenadax <= 2) and (coordenaday >= 0 and coordenaday <= 2):
        return False, coordenadax, coordenaday
    else:
        print("Ingresa una coordenada valida para el tablero")
        return True, None, None





######Invocacion a funciones#######


#MostrarMatriz()
"""estadoFicha = True
while(estadoFicha):
    estadoFicha, jugador1, jugador2 = ElegirLado()
    print(jugador1)
    print(jugador2)"""

estadoCoord = True
while(estadoCoord):
    estadoCoord, coordenadax, coordenaday = TiraFicha()
    print(coordenadax)
    print(coordenaday)
