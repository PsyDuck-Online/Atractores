from Cell import Cell


# Funciones

def printMatriz(matriz):
    for y in range(0, len(matriz)):
        for x in range(0, len(matriz)):
            print(matriz[y][x].estado, end=" ")
        print("")


def nextGen(matriz, sMin, sMax, bMin, bMax):
    for y in range(0, len(matriz)):
        for x in range(0, len(matriz)):
            # Calculamos el siguiente estado de las celulas
            suma = matriz[y][x].sumarVecinos()
            if (suma < sMin) or (suma > sMax):
                matriz[y][x].estadoSig = 0
            if (suma >= bMin) and (suma <= bMax):
                matriz[y][x].estadoSig = 1

    for y in range(0, len(matriz)):
        for x in range(0, len(matriz)):
            matriz[y][x].mutar()


def numToMatriz(num, n):
    matriz = []
    exp = 2**((n*n)-1)
    for y in range(n-1, -1, -1):
        aux = []
        for x in range(n-1, -1, -1):
            if ((num % exp) != num):
                aux.insert(0, Cell(x, y, 1))
                num = num - exp
            else:
                aux.insert(0, Cell(x, y, 0))
            exp = exp / 2
        matriz.insert(0, aux)

    for y in range(0, n):
        for x in range(0, n):
            matriz[x][y].agregarVecinos(matriz)
    return matriz


def matrizToNum(matriz, n):
    exp = 1
    num = 0
    for y in range(0, n):
        for x in range(0, n):
            num = num + (matriz[y][x].estado * exp)
            exp = exp * 2
    return num
