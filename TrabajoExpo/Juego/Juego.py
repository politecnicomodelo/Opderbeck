import pygame
pygame.init()



def confirmGame(matriz, font):
    total = 0
    for f in xrange(3):
        for c in xrange(3):
            total += matriz[f][c]
        break

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
    cantidad = 0
    for f1 in xrange(3):
        for c1 in xrange(3):
            for f in xrange(3):
                for c in xrange(3):
                    if matriz[f][c] == matriz[f1][c1]:
                        cantidad += 1


    col = font.render("Esta mal una COLUMNA", 0, (0,0,0))
    fil = font.render("Esta mal una FILA", 0, (0, 0, 0))
    diag = font.render("Esta mal una DIAGONAL", 0, (0, 0, 0))

    mal = font.render("ALGO ESTA MAL, PRUEBA DENUEVO", 0, (0, 0, 0))
    bien = font.render("GANASTE!  FELICITACIONES!", 0, (0, 0, 0))

    #if columna != total or columna1 != total or columna2 != total:
      #  return col
    #elif fila != total or fila1 != total or fila2 != total:
      #  return fil
    #elif diagonal != total or diagonal1 != total:
     #   return diag
    if cantidad > 9:
        return mal
    if columna != total or columna1 != total or columna2 != total or fila != total or \
                    fila1 != total or fila2 != total or diagonal != total or diagonal1 != total:
        return mal
    else:
        return bien

def main():
    WIDTH = 1000
    HEIGHT = 600
    FPS = 60

    TABLE = (252, 239, 176)
    BLACK = (0, 0, 0)
    BACKGROUND = (250, 246, 222)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cuadrado Magico")

    clock = pygame.time.Clock()
    finish = True

    check = False

    font = pygame.font.SysFont("Arial", 48, True, False)

    confirm = pygame.image.load("images/Confirm.png").convert_alpha()
    help = pygame.image.load("images/Help.png").convert_alpha()
    reset = pygame.image.load("images/Reset.png").convert_alpha()

    confirm1 = pygame.sprite.Sprite()
    confirm1.image = confirm
    confirm1.rect = confirm.get_rect()
    confirm1.rect.top = 400
    confirm1.rect.left = 750

    help1 = pygame.sprite.Sprite()
    help1.image = help
    help1.rect = help.get_rect()
    help1.rect.top = 250
    help1.rect.left = 750

    reset1 = pygame.sprite.Sprite()
    reset1.image = reset
    reset1.rect = reset.get_rect()
    reset1.rect.top = 100
    reset1.rect.left = 750


    p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0, 0, 0, 0, 0, 0, 0, 0, 0


    mouse = pygame.Rect(0, 0, 1, 1)

    r1 = pygame.Rect(250, 100, 130, 130)
    r2 = pygame.Rect(380, 100, 130, 130)
    r3 = pygame.Rect(510, 100, 130, 130)
    r4 = pygame.Rect(250, 230, 130, 130)
    r5 = pygame.Rect(380, 230, 130, 130)
    r6 = pygame.Rect(510, 230, 130, 130)
    r7 = pygame.Rect(250, 360, 130, 130)
    r8 = pygame.Rect(380, 360, 130, 130)
    r9 = pygame.Rect(510, 360, 130, 130)

    div1 = pygame.Rect(380, 100, 5, 395)
    div2 = pygame.Rect(510, 100, 5, 395)
    div3 = pygame.Rect(250, 230, 395, 5)
    div4 = pygame.Rect(250, 360, 395, 5)

    border1 = pygame.Rect(250, 100, 395, 5)
    border2 = pygame.Rect(250, 100, 5, 395)
    border3 = pygame.Rect(640, 100, 5, 395)
    border4 = pygame.Rect(250, 490, 395, 5)


    #matriz = [
     #       [4, 9, 2],
      #      [3, 5, 7],
       #     [8, 1, 6]
        #    ]

    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check = False
                if mouse.colliderect(r1):
                    p1 += 1
                    if p1 > 9:
                        p1 = 0
                elif mouse.colliderect(r2):
                    p2 += 1
                    if p2 > 9:
                        p2 = 0
                elif mouse.colliderect(r3):
                    p3 += 1
                    if p3 > 9:
                        p3 = 0
                elif mouse.colliderect(r4):
                    p4 += 1
                    if p4 > 9:
                        p4 = 0
                elif mouse.colliderect(r5):
                    p5 += 1
                    if p5 > 9:
                        p5 = 0
                elif mouse.colliderect(r6):
                    p6 += 1
                    if p6 > 9:
                        p6 = 0
                elif mouse.colliderect(r7):
                    p7 += 1
                    if p7 > 9:
                        p7 = 0
                elif mouse.colliderect(r8):
                    p8 += 1
                    if p8 > 9:
                        p8 = 0
                elif mouse.colliderect(r9):
                    p9 += 1
                    if p9 > 9:
                        p9 = 0
                elif mouse.colliderect(help1):
                    pass
                elif mouse.colliderect(confirm1):
                    check = True
                    matriz = [
                        [p1, p2, p3],
                        [p4, p5, p6],
                        [p7, p8, p9]
                    ]
                    result = confirmGame(matriz, font)
                elif mouse.colliderect(reset1):
                    p1, p2, p3, p4, p5, p6, p7, p8, p9 = \
                        0, 0, 0, 0, 0, 0, 0, 0, 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finish = False

        punto1 = font.render(str(p1), 0, BLACK)
        punto2 = font.render(str(p2), 0, BLACK)
        punto3 = font.render(str(p3), 0, BLACK)
        punto4 = font.render(str(p4), 0, BLACK)
        punto5 = font.render(str(p5), 0, BLACK)
        punto6 = font.render(str(p6), 0, BLACK)
        punto7 = font.render(str(p7), 0, BLACK)
        punto8 = font.render(str(p8), 0, BLACK)
        punto9 = font.render(str(p9), 0, BLACK)

        clock.tick(FPS)
        mouse.left, mouse.top = pygame.mouse.get_pos()

        screen.fill(BACKGROUND)

        pygame.draw.rect(screen, TABLE, mouse)

        pygame.draw.rect(screen, TABLE, r1)
        pygame.draw.rect(screen, TABLE, r2)
        pygame.draw.rect(screen, TABLE, r3)
        pygame.draw.rect(screen, TABLE, r4)
        pygame.draw.rect(screen, TABLE, r5)
        pygame.draw.rect(screen, TABLE, r6)
        pygame.draw.rect(screen, TABLE, r7)
        pygame.draw.rect(screen, TABLE, r8)
        pygame.draw.rect(screen, TABLE, r9)

        pygame.draw.rect(screen, BLACK, div1)
        pygame.draw.rect(screen, BLACK, div2)
        pygame.draw.rect(screen, BLACK, div3)
        pygame.draw.rect(screen, BLACK, div4)

        pygame.draw.rect(screen, BLACK, border1)
        pygame.draw.rect(screen, BLACK, border2)
        pygame.draw.rect(screen, BLACK, border3)
        pygame.draw.rect(screen, BLACK, border4)

        screen.blit(confirm1.image, confirm1.rect)
        screen.blit(help1.image, help1.rect)
        screen.blit(reset1.image, reset1.rect)

        screen.blit(punto1, (300, 160))
        screen.blit(punto2, (440, 160))
        screen.blit(punto3, (570, 160))
        screen.blit(punto4, (300, 290))
        screen.blit(punto5, (440, 290))
        screen.blit(punto6, (570, 290))
        screen.blit(punto7, (300, 420))
        screen.blit(punto8, (440, 420))
        screen.blit(punto9, (570, 420))

        if check:
            screen.fill(BACKGROUND)
            screen.blit(result, (170, 200))

        pygame.display.update()


main()

