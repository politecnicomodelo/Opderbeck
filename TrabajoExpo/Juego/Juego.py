import pygame
from pygame.locals import *
pygame.init()



def comprobador(matriz):
    total = 0
    for f in xrange(3):
        for c in xrange(3):
            total += matriz[f][c]
        break
    print (total)
    #comprueba las columnas
    columna = matriz[0][0] + matriz[0][1] + matriz[0][2]
    columna1 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    columna2 = matriz[2][0] + matriz[2][1] + matriz[2][2]

    # comprueba las filas
    fila = matriz[0][0] + matriz[1][0] + matriz[2][0]
    fila1 = matriz[0][1] + matriz[1][1] + matriz[2][1]
    fila2 = matriz[0][2] + matriz[1][2] + matriz[2][2]

    # comprueba las diagonales
    diagonal = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diagonal1 = matriz[0][2] + matriz[1][1] + matriz[2][0]

    if columna != total or columna1 != total or columna2 != total:
        print ("esta mal una columna")
    if fila != total or fila1 != total or fila2 != total:
        print ("esta mal una fila")
    if diagonal != total or diagonal1 != total:
        print ("esta mal una diagonal")


def main():
    WIDTH = 640
    HEIGHT = 480
    FPS = 60

    ORANGE = (252, 190, 34)
    BACKGROUND = (250, 243, 210)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cuadrado Magico")

    clock = pygame.time.Clock()
    finish = True

    fuente = pygame.font.SysFont("Arial", 25, True, False)

    r1 = pygame.Rect(WIDTH/2, HEIGHT/2, 10, 10)

    matriz = [
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
            ]

    while finish:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                finish = False

        clock.tick(FPS)
        screen.fill(BACKGROUND)

        pygame.display.update()


main()

