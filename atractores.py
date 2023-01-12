import numpy as np
from life import *
from progress.bar import ChargingBar
import sys


def main():
    if len(sys.argv) == 3:
        nombre_archivo = sys.argv[1]
        N = int(sys.argv[2])
    else:
        return

    f = open(nombre_archivo+"_nodos.csv", 'w')
    f2 = open(nombre_archivo+"_aristas.csv", 'w')
    f.write("ID,Label\n")
    f2.write("Source,Target\n")

    combinaciones = 2**(N*N)  # Total de combinaciones en el tablero
    bar = ChargingBar('Calculando Atractores:', max=combinaciones)
    # Calcula la funcion de transicion
    for estado in range(0, combinaciones):
        tablero = numToMatriz(estado, N)
        nextGen(tablero)
        estadoSig = matrizToNum(tablero, N)
        f.write("{},{}\n".format(estado, estado))
        f2.write("{},{}\n".format(estado, estadoSig))
        bar.next()
    f.close()
    f2.close()

    print("")


def estaEnLista(lista, val):
    pos = 0
    flag = False
    for i in lista:
        if i == val:
            flag = True
            break
        pos = pos + 1
    return pos if flag is True else -1


main()
