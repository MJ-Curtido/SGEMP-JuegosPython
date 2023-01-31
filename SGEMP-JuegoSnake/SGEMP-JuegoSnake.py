import time
import turtle
from random import *

segmentos = []
POSPONER = 0.1
VELOCIDAD = 20

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("hotpink")
wn.setup(width=600, height=600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("black")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "up"

manzana = turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.color("white")
manzana.penup()
manzana.goto(randint(-280, 280), randint(-280, 280))

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.shape("turtle")
tortuga.color("white")
tortuga.penup()
tortuga.goto(randint(-280, 280), randint(-280, 280))

contPuntuacionTemp = 0
contPuntuacion = 0
contManzanas = 0
contTortugas = 0

puntuacion = turtle.Turtle()
puntuacion.speed(0)
puntuacion.shape("square")
puntuacion.color("white")
puntuacion.penup()
puntuacion.hideturtle()
puntuacion.goto(180, -280)
puntuacion.write("TOTAL: " + str(contPuntuacion), align="center", font=("Cournier", 24, "normal"))

puntuacionManzana = turtle.Turtle()
puntuacionManzana.speed(0)
puntuacionManzana.shape("square")
puntuacionManzana.color("white")
puntuacionManzana.penup()
puntuacionManzana.hideturtle()
puntuacionManzana.goto(-200, -280)
puntuacionManzana.write("Manzanas: " + str(contManzanas), align="center", font=("Cournier", 24, "normal"))

puntuacionTortuga = turtle.Turtle()
puntuacionTortuga.speed(0)
puntuacionTortuga.shape("square")
puntuacionTortuga.color("white")
puntuacionTortuga.penup()
puntuacionTortuga.hideturtle()
puntuacionTortuga.goto(0, -280)
puntuacionTortuga.write("Tortugas: " + str(contTortugas), align="center", font=("Cournier", 24, "normal"))

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izq():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + VELOCIDAD)
    else:
        if cabeza.direction == "down":
            y = cabeza.ycor()
            cabeza.sety(y - VELOCIDAD)
        else:
            if cabeza.direction == "left":
                x = cabeza.xcor()
                cabeza.setx(x - VELOCIDAD)
            else:
                if cabeza.direction == "right":
                    x = cabeza.xcor()
                    cabeza.setx(x + VELOCIDAD)

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izq, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for elem in segmentos:
            elem.goto(1000, 1000)

        segmentos.clear()
        puntuacion.clear()

        if contPuntuacionTemp > contPuntuacion:
            contPuntuacion = contPuntuacionTemp

        contPuntuacionTemp = 0
        contManzanas = 0
        contTortugas = 0

        puntuacionManzana.clear()
        puntuacionTortuga.clear()

        puntuacionManzana.write("Manzanas: " + str(contManzanas), align="center", font=("Cournier", 24, "normal"))
        puntuacionTortuga.write("Tortugas: " + str(contTortugas), align="center", font=("Cournier", 24, "normal"))
        puntuacion.write("TOTAL: " + str(contPuntuacion), align="center", font=("Cournier", 24, "normal"))

    if cabeza.distance(manzana) < 20:
        manzana.goto(randint(-280, 280), randint(-280, 280))

        puntuacion.clear()
        contPuntuacionTemp += 1

        puntuacionManzana.clear()
        contManzanas += 1

        puntuacionManzana.write("Manzanas: " + str(contManzanas), align="center", font=("Cournier", 24, "normal"))

        if contPuntuacionTemp > contPuntuacion:
            puntuacion.write("TOTAL: " + str(contPuntuacionTemp), align="center", font=("Cournier", 24, "normal"))
        else:
            puntuacion.write("TOTAL: " + str(contPuntuacion), align="center", font=("Cournier", 24, "normal"))

        nuevoSegmento = turtle.Turtle()
        nuevoSegmento.speed(0)
        nuevoSegmento.shape("square")
        nuevoSegmento.color("grey")
        nuevoSegmento.penup()
        segmentos.append(nuevoSegmento)

    if cabeza.distance(tortuga) < 20:
        tortuga.goto(randint(-280, 280), randint(-280, 280))

        puntuacion.clear()
        contPuntuacionTemp += 1

        puntuacionTortuga.clear()
        contTortugas += 1

        puntuacionTortuga.write("Tortugas: " + str(contTortugas), align="center", font=("Cournier", 24, "normal"))

        if contPuntuacionTemp > contPuntuacion:
            puntuacion.write("TOTAL: " + str(contPuntuacionTemp), align="center", font=("Cournier", 24, "normal"))
        else:
            puntuacion.write("TOTAL: " + str(contPuntuacion), align="center", font=("Cournier", 24, "normal"))

        nuevoSegmento = turtle.Turtle()
        nuevoSegmento.speed(0)
        nuevoSegmento.shape("square")
        nuevoSegmento.color("grey")
        nuevoSegmento.penup()
        segmentos.append(nuevoSegmento)

    totalSeg = len(segmentos)
    for i in range(totalSeg - 1, 0, -1):
        segmentos[i].goto(segmentos[i - 1].xcor(), segmentos[i - 1].ycor())

    if totalSeg > 0:
        segmentos[0].goto(cabeza.xcor(), cabeza.ycor())

    mov()

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            for element in segmentos:
                element.goto(1000, 1000)

            segmentos.clear()
            puntuacion.clear()

            if contPuntuacionTemp > contPuntuacion:
                contPuntuacion = contPuntuacionTemp

            contPuntuacionTemp = 0
            contManzanas = 0
            contTortugas = 0

            puntuacionManzana.clear()
            puntuacionTortuga.clear()

            puntuacionManzana.write("Manzanas: " + str(contManzanas), align="center", font=("Cournier", 24, "normal"))
            puntuacionTortuga.write("Tortugas: " + str(contTortugas), align="center", font=("Cournier", 24, "normal"))
            puntuacion.write("TOTAL:" + str(contPuntuacion), align="center", font=("Cournier", 24, "normal"))

    time.sleep(POSPONER)
