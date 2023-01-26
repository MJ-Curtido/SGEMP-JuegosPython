import Pieza

class Tetris:
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

    def new_figure(self):
        self.pieza = Pieza(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.pieza.image():
                    if i + self.pieza.y > self.alto - 1 or \
                            j + self.pieza.x > self.ancho - 1 or \
                            j + self.pieza.x < 0 or \
                            self.filas[i + self.pieza.y][j + self.pieza.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.alto):
            zeros = 0
            for j in range(self.ancho):
                if self.filas[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.ancho):
                        self.filas[i1][j] = self.filas[i1 - 1][j]
        self.puntuacion += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.pieza.y += 1
        self.pieza.y -= 1
        self.freeze()

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
            self.modo = "gameover"

    def go_side(self, dx):
        old_x = self.pieza.x
        self.pieza.x += dx
        if self.intersects():
            self.pieza.x = old_x

    def rotate(self):
        old_rotation = self.pieza.rotation
        self.pieza.rotate()
        if self.intersects():
            self.pieza.rotation = old_rotation
