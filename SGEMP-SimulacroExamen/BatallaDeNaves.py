"""
BATALLA DE NAVES

- Dos naves
- Dos campos
- Cada nave se controla con keys diferentes
- Cada jugador dispara con una tecla
"""

import time
import turtle

PUTOFF = 0.1
SPEED = 1.7

wn = turtle.Screen()
wn.title("Batalla de naves")
wn.bgcolor("hotpink")
wn.setup(width=600, height=600)
wn.tracer(0)

leftShip = turtle.Turtle()
leftShip.speed(0)
leftShip.shape("square")
leftShip.color("black")
leftShip.penup()
leftShip.goto(-150, 0)

rightShip = turtle.Turtle()
rightShip.speed(0)
rightShip.shape("square")
rightShip.color("black")
rightShip.penup()
rightShip.goto(-150, 0)

contScore = 0
leftScore = turtle.Turtle()
leftScore.shape("square")
leftScore.color("white")
leftScore.penup()
leftScore.hideturtle()
leftScore.goto(-280, -280)
leftScore.write(contScore, align="center", font=("Cournier", 24, "normal"))

def upLeftShip():
    leftShip.direction = "up"
def downLeftShip():
    leftShip.direction = "down"
def upRightShip():
    rightShip.direction = "up"
def downRightShip():
    rightShip.direction = "down"

def rightMov():
    if rightShip.direction == "up":
        y = rightShip.ycor()
        rightShip.sety(y + SPEED)
    else:
        if rightShip.direction == "down":
            y = rightShip.ycor()
            rightShip.sety(y - SPEED)
def leftMov():
    if leftShip.direction == "up":
        y = leftShip.ycor()
        leftShip.sety(y + SPEED)
    else:
        if leftShip.direction == "down":
            y = leftShip.ycor()
            leftShip.sety(y - SPEED)

wn.listen()
wn.onkeypress(upRightShip, "Up")
wn.onkeypress(downRightShip, "Down")
wn.onkeypress(upRightShip, "W")
wn.onkeypress(downRightShip, "S")

while True:
    wn.update()

    if rightShip.xcor() > 280 or rightShip.xcor() < -280 or rightShip.ycor() > 280 or rightShip.ycor() < -280:
        time.sleep(1)
        rightShip.goto(0, 0)
        rightShip.direction = "stop"

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
