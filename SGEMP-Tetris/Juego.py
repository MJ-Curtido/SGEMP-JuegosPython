import Pieza

class Juego:
    level = 2
    puntuacion = 0
    modo = 1
    filas = []
    alto = 0
    ancho = 0
    x = 100
    y = 60
    zoom = 20
    pieza = None

    def __init__(self):
        self.alto = 20
        self.ancho = 10
        self.filas = []
        self.puntuacion = 0
        self.modo = 1

        for i in range(self.alto):
            linea = []

            for j in range(self.ancho):
                linea.append(0)

            self.filas.append(linea)

    def crearFigura(self):
        self.pieza = Pieza(3, 0)

    def dentroDeLimite(self):
        dentro = False
        for i in range(4):
            for j in range(4):
                if (i * 4 + j in self.pieza.limitePieza()) and (i + self.pieza.y > self.alto - 1 or j + self.pieza.x > self.ancho - 1 or j + self.pieza.x < 0 or self.filas[i + self.pieza.y][j + self.pieza.x] > 0):
                    dentro = True
        return dentro

    def go_down(self):
        self.pieza.y += 1
        if self.intersects():
            self.pieza.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.pieza.image():
                    self.filas[i + self.pieza.y][j + self.pieza.x] = self.pieza.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.modo = 0

    def movLateral(self, nuevaX):
        antiguaX = self.pieza.x
        self.pieza.x += nuevaPos
        if self.dentroDeLimite():
            self.pieza.x = antiguaX

    def rotate(self):
        old_rotation = self.pieza.rotation
        self.pieza.rotate()
        if self.intersects():
            self.pieza.rotation = old_rotation
