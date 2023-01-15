from life import *
from progress.bar import ChargingBar
import sys

# Reglas de LIFE
sMin = 2
sMax = 3
bMin = 3
bMax = 3

def main():
    if len(sys.argv) == 3:
        nombre_archivo = sys.argv[1]
        N = int(sys.argv[2])
    else:
        print("uso: python atractores.py <nombre_archivo> <N>")
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
        nextGen(tablero, sMin, sMax, bMin, bMax)
        estadoSig = matrizToNum(tablero, N)
        f.write("{},{}\n".format(estado, estado))
        f2.write("{},{}\n".format(estado, estadoSig))
        bar.next()
    f.close()
    f2.close()

    print("")

main()
