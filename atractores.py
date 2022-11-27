import numpy as np
from life import *
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
    # Calcula la funcion de transicion
    for estado in range(0, combinaciones):
        tablero = numToMatriz(estado, N)
        nextGen(tablero)
        estadoSig = matrizToNum(tablero, N)
        # tuplas.append((estado,estadoSig))
        f.write("{},{}\n".format(estado, estado))
        f2.write("{},{}\n".format(estado, estadoSig))

    # for tupla in tuplas:
     #   f.write("{} {}\n".format(tupla[0], tupla[1]))
    f.close()


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
