import pygame
from random import *
import time

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ejemplo 3")
speed = [randint(3, 6), randint(3, 6)]
fuente = pygame.font.Font(None, 36)

ball = pygame.image.load("../assets/ball.png")
ball = pygame.transform.scale(ball, (17, 17))
ballrect = ball.get_rect()
#speed = [4, 4]
ballrect.move_ip(0, 0)

zapato = pygame.image.load("../assets/zapato.png")
zapato = pygame.transform.scale(zapato, (57, 27))
zapatorect = zapato.get_rect()
zapatorect.move_ip(320, 450)

texto = ""
textoRect = None

jugando = True

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        zapatorect = zapatorect.move(-7, 0)
    if keys [pygame.K_RIGHT]:
        zapatorect = zapatorect.move(7, 0)
    if zapatorect.colliderect(ballrect):
        speed[1] = -speed[1]

        if speed[1] < 0:
            speed[1] = speed[1] - 0.5
        else:
            speed[1] = speed[1] + 0.5

    ballrect = ballrect.move(speed)
    if ballrect.left <= 0 or ballrect.right >= ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top <= 0:
        speed[1] = -speed[1]
    if ballrect.bottom >= ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 125, 125))
        textoRect = texto.get_rect()
        textoX = ventana.get_width() / 2 - textoRect.width / 2
        textoY = ventana.get_height() / 2 - textoRect.height / 2

        textoRect.center = (textoX, textoY)

        ventana.fill((252, 243, 207))
        ventana.blit(texto, textoRect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

        jugando = False
        time.sleep(5)
    else:
        ventana.fill((252, 243, 207))

        ventana.blit(ball, ballrect)
        ventana.blit(zapato, zapatorect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

pygame.quit()