from random import *

class Pieza:
    x = 0
    y = 0

    piezas = [
        [[4, 5, 6, 7], [1, 5, 9, 13]], #vStick, hStick
        [[0, 1, 4, 5]], #square
        [[0, 5, 9,  10], [4, 0, 1, 2], [0, 1, 5, 9], [4, 5, 6, 2]] #normalL, hDownL, primeL, hUpL
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pieza = randint(0, len(self.piezas) - 1)
        self.posicion = 0

    def aparecePieza(self):
        return self.piezas[self.pieza][self.posicion]

    def girar(self):
        if self.posicion + 1 == len(self.piezas):
            self.posicion = 0;
        else:
            self.posicion = self.posicion + 1
