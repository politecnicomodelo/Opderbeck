import pygame
from random import randint
pygame.init()

def CrearCuadrados(lista):
    for cuadrado in range(randint(0, 10)):
        x = randint(5, 20)
        cuadrado = pygame.Rect(randint(0, 1200), randint(0, 700), x, x)
        lista.append (cuadrado)
    return lista

def pintarEnemigos(lista, screen):
    for cuadrado in lista:
        pygame.draw.rect(screen, (240, 240, 240), cuadrado)

def detectar(mouse, lista, mouserect):
    for cuadrado in lista:
        if mouse.colliderect(cuadrado) or mouserect.colliderect(cuadrado): return 0

def mover(lista):
    for cuadrado in lista:
        cuadrado.move_ip(randint(-5, 5), randint(-5, 5))

def main():
    lista = []
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("JUEGO")

    clock = pygame.time.Clock()

    finish = True
    mouse = pygame.Rect(0, 0, 1, 1)
    mouserect = pygame.Rect(0, 0, 10, 10)
    up, down, right, left = False, True, True, False

    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
                if event.key == pygame.K_UP: up, down, right, left  = True, False, False, False
                if event.key == pygame.K_DOWN:up, down, right, left  = False, True, False, False
                if event.key == pygame.K_RIGHT: up, down, right, left  = False, False, True, False
                if event.key == pygame.K_LEFT: up, down, right, left  = False, False, False, True

        resultado = detectar(mouse, lista, mouserect)
        if up: mouserect.move_ip(0, -5)
        if down: mouserect.move_ip(0, +5)
        if right: mouserect.move_ip(+5, 0)
        if left: mouserect.move_ip(-5, 0)
        if randint(0, 20) == 10: lista = CrearCuadrados(lista)

        clock.tick(20)
        mouse.left, mouse.top = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (240, 0, 0), mouse)
        pygame.draw.rect(screen, (240, 0, 0), mouserect)
        pygame.draw.aaline(screen, (240, 0, 0), (mouserect.x, mouserect.y), (mouse.x, mouse.y), 2)

        mover(lista)
        pintarEnemigos(lista, screen)
        pygame.display.update()

        if resultado == 0: finish = False

main ()
