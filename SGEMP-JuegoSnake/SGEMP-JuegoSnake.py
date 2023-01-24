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
manzana.shape("turtle")
manzana.color("white")
manzana.penup()
manzana.goto(randint(-280, 280), randint(-280, 280))

contPuntuacion = 0

puntuacion = turtle.Turtle()
puntuacion.speed(0)
puntuacion.shape("square")
puntuacion.color("white")
puntuacion.penup()
puntuacion.hideturtle()
puntuacion.goto(-280, -280)
puntuacion.write(contPuntuacion, align="center", font=("Cournier", 24, "normal"))

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
        contPuntuacion = 0
        puntuacion.write(contPuntuacion, align="center", font=("Cournier", 24, "normal"))

    if cabeza.distance(manzana) < 20:
        manzana.goto(randint(-280, 280), randint(-280, 280))

        puntuacion.clear()
        contPuntuacion += 1
        puntuacion.write(contPuntuacion, align="center", font=("Cournier", 24, "normal"))

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
            contPuntuacion = 0
            puntuacion.write(contPuntuacion, align="center", font=("Cournier", 24, "normal"))

    time.sleep(POSPONER)
