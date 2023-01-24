import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ejemplo 2")

ball = pygame.image.load("../assets/ball.png")
ball = pygame.transform.scale(ball, (17, 17))
ballrect = ball.get_rect()
speed = [4, 4]
ballrect.move_ip(0, 0)

jugando = True

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    ballrect = ballrect.move(speed)

    if ballrect.left <= 0 or ballrect.right >= ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top <= 0 or ballrect.bottom >= ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((252, 243, 207))

    ventana.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()