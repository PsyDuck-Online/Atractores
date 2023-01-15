class Cell:
    def __init__(self, x, y, estado):
        self.x = x
        self.y = y
        self.estado = estado
        self.estadoSig = self.estado

        self.vecinos = []

    def agregarVecinos(self, tablero):
        N = len(tablero)
        for i in range(-1, 2):
            for j in range(-1,2):
                xVecino = (self.x + j + N) % N
                yVecino = (self.y + i + N) % N

                if i != 0 or j != 0:
                    self.vecinos.append(tablero[yVecino][xVecino])

    def sumarVecinos(self):
        suma = 0
        for vecino in self.vecinos:
            suma = suma + vecino.estado
        return suma
    
    def mutar(self):
        self.estado = self.estadoSig