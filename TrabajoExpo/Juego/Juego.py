import pygame
pygame.init()



def confirmGame(matriz, font, COLOR):
    total = 0
    for f in range(3):
        for c in range(3):
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
    for f1 in range(3):
        for c1 in range(3):
            for f in range(3):
                for c in range(3):
                    if matriz[f][c] == matriz[f1][c1]:
                        cantidad += 1


    col = font.render("Esta mal una COLUMNA", 0, COLOR)
    fil = font.render("Esta mal una FILA", 0, COLOR)
    diag = font.render("Esta mal una DIAGONAL", 0, COLOR)

    mal = font.render("ALGO ESTA MAL", 0, COLOR)
    bien = font.render("GANASTE!  FELICITACIONES!", 0, COLOR)

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


def Help(screen, COLOR, matriz, font):
    f1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
    f2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    f3 = matriz[2][0] + matriz[2][1] + matriz[2][2]


    c1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
    c2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
    c3 = matriz[0][2] + matriz[1][2] + matriz[2][2]


    d1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    d2 = matriz[0][2] + matriz[1][1] + matriz[2][0]

    fila1 = font.render(str(f1), 0, COLOR)
    fila2 = font.render(str(f2), 0, COLOR)
    fila3 = font.render(str(f3), 0, COLOR)

    columna1 = font.render(str(c1), 0, COLOR)
    columna2 = font.render(str(c2), 0, COLOR)
    columna3 = font.render(str(c3), 0, COLOR)

    diag1 = font.render(str(d1), 0, COLOR)
    diag2 = font.render(str(d2), 0, COLOR)

    screen.blit(fila1, (200, 160))
    screen.blit(fila2, (200, 290))
    screen.blit(fila3, (200, 420))
    screen.blit(columna1, (300, 60))
    screen.blit(columna2, (440, 60))
    screen.blit(columna3, (570, 60))
    screen.blit(diag1, (200, 60))
    screen.blit(diag2, (200, 510))
    #pygame.draw.line(screen, COLOR, (220, 175), (590, 175))


def menu(font, COLOR, screen, BACKGROUND):
    finish = True
    level1 = font.render("NIVEL 1", 0, COLOR)
    level2 = font.render("NIVEL 2", 0, COLOR)

    level3 = pygame.Rect(380, 245, 145, 40)
    level4 = pygame.Rect(380, 305, 145, 40)

    clock = pygame.time.Clock()

    mouse = pygame.Rect(0, 0, 1, 1)

    while finish:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse.colliderect(level3):
                    level = 1
                    finish = False
                if mouse.colliderect(level4):
                    level = 2
                    finish = False

        mouse.left, mouse.top = pygame.mouse.get_pos()
        clock.tick(20)

        screen.fill(BACKGROUND)

        pygame.draw.rect(screen, BACKGROUND, mouse)
        pygame.draw.rect(screen, BACKGROUND, level3)
        pygame.draw.rect(screen, BACKGROUND, level4)

        screen.blit(level1, (380, 235))
        screen.blit(level2, (380, 300))

        pygame.display.update()

    return level3, level4, level

def main():
    WIDTH = 1000
    HEIGHT = 600
    FPS = 60

    TABLE = (252, 239, 176)
    BLACK = (0, 0, 0)
    BACKGROUND = (250, 246, 222)

    LIMITLEVE1 = 9
    LIMITLEVE2 = 15

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
    confirm1.rect.top, confirm1.rect.left = (400, 750)

    help1 = pygame.sprite.Sprite()
    help1.image = help
    help1.rect = help.get_rect()
    help1.rect.top, help1.rect.left = (250, 750)

    reset1 = pygame.sprite.Sprite()
    reset1.image = reset
    reset1.rect = reset.get_rect()
    reset1.rect.top, reset1.rect.left = (100, 750)

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

    listBlack = [div1, div2, div3, div4, border1, border2, border3, border4]
    listTable = [mouse, r1, r2, r3, r4, r5, r6, r7, r8, r9]

    #matriz = [
     #       [4, 9, 2],
      #      [3, 5, 7],
       #     [8, 1, 6]
        #    ]

    helpT = False
    level = 1

    level1, level2, level = menu(font, BLACK, screen, BACKGROUND)

    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check = False
                if mouse.colliderect(r1):
                    p1 += 1
                    if level == 1:
                        if p1 > LIMITLEVE1: p1 = 0
                    else:
                        if p1 > LIMITLEVE2: p1 = 0
                elif mouse.colliderect(r2):
                    p2 += 1
                    if level == 1:
                        if p2 > LIMITLEVE1: p2 = 0
                    else:
                        if p2 > LIMITLEVE2: p2 = 0
                elif mouse.colliderect(r3):
                    p3 += 1
                    if level == 1:
                        if p3 > LIMITLEVE1: p3 = 0
                    else:
                        if p3 > LIMITLEVE2: p3 = 0
                elif mouse.colliderect(r4):
                    p4 += 1
                    if level == 1:
                        if p4 > LIMITLEVE1: p4 = 0
                    else:
                        if p4 > LIMITLEVE2: p4 = 0
                elif mouse.colliderect(r5):
                    p5 += 1
                    if level == 1:
                        if p5 > LIMITLEVE1: p5 = 0
                    else:
                        if p5 > LIMITLEVE2: p5 = 0
                elif mouse.colliderect(r6):
                    p6 += 1
                    if level == 1:
                        if p6 > LIMITLEVE1: p6 = 0
                    else:
                        if p6 > LIMITLEVE2: p6 = 0
                elif mouse.colliderect(r7):
                    p7 += 1
                    if level == 1:
                        if p7 > LIMITLEVE1: p7 = 0
                    else:
                        if p7 > LIMITLEVE2: p7 = 0
                elif mouse.colliderect(r8):
                    p8 += 1
                    if level == 1:
                        if p8 > LIMITLEVE1: p8 = 0
                    else:
                        if p8 > LIMITLEVE2: p8 = 0
                elif mouse.colliderect(r9):
                    p9 += 1
                    if level == 1:
                        if p9 > LIMITLEVE1: p9 = 0
                    else:
                        if p9 > LIMITLEVE2: p9 = 0
                elif mouse.colliderect(help1):
                    if helpT: helpT = False
                    else: helpT = True
                elif mouse.colliderect(confirm1):
                    check = True
                    matriz = [
                        [p1, p2, p3],
                        [p4, p5, p6],
                        [p7, p8, p9]
                    ]
                    result = confirmGame(matriz, font, BLACK)
                elif mouse.colliderect(reset1): p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0, 0, 0, 0, 0, 0, 0, 0, 0



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

        screen.fill(BACKGROUND)

        mouse.left, mouse.top = pygame.mouse.get_pos()

        for rect in listTable: pygame.draw.rect(screen, TABLE, rect)

        for rect in listBlack: pygame.draw.rect(screen, BLACK, rect)

        screen.blit(confirm1.image, confirm1.rect)
        screen.blit(help1.image, help1.rect)
        screen.blit(reset1.image, reset1.rect)

        if p1 > 9: screen.blit(punto1, (290, 140))
        else: screen.blit(punto1, (300, 140))
        if p2 > 9: screen.blit(punto2, (430, 140))
        else: screen.blit(punto2, (440, 140))
        if p3 > 9: screen.blit(punto3, (560, 140))
        else: screen.blit(punto3, (570, 140))
        if p4 > 9: screen.blit(punto4, (290, 270))
        else: screen.blit(punto4, (300, 270))
        if p5 > 9: screen.blit(punto5, (430, 270))
        else: screen.blit(punto5, (440, 270))
        if p6 > 9: screen.blit(punto6, (560, 270))
        else: screen.blit(punto6, (570, 270))
        if p7 > 9: screen.blit(punto7, (290, 400))
        else: screen.blit(punto7, (300, 400))
        if p8 > 9: screen.blit(punto8, (430, 400))
        else: screen.blit(punto8, (440, 400))
        if p9 > 9: screen.blit(punto9, (560, 400))
        else: screen.blit(punto9, (570, 400))


        #if levelT: level1, level2 = menu(font, BLACK, screen, BACKGROUND)
        if check:
            screen.fill(BACKGROUND)
            screen.blit(result, (170, 200))
        if helpT:
            matriz = [
                [p1, p2, p3],
                [p4, p5, p6],
                [p7, p8, p9]
            ]
            Help(screen, BLACK, matriz, font)

        pygame.display.update()


main()

