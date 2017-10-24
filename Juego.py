import pygame
pygame.init()



def confirmGame(matriz, screen):

    Win = pygame.image.load("images/Win.png")
    Lose = pygame.image.load("images/Lose.png")

    total = 0
    for f in range(3):
        for c in range(3):
            total += matriz[f][c]
        break

    columna = matriz[0][0] + matriz[0][1] + matriz[0][2]
    columna1 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    columna2 = matriz[2][0] + matriz[2][1] + matriz[2][2]

    fila = matriz[0][0] + matriz[1][0] + matriz[2][0]
    fila1 = matriz[0][1] + matriz[1][1] + matriz[2][1]
    fila2 = matriz[0][2] + matriz[1][2] + matriz[2][2]

    diagonal = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diagonal1 = matriz[0][2] + matriz[1][1] + matriz[2][0]

    total = 15

    cantidad = 0
    for f1 in range(3):
        for c1 in range(3):
            for f in range(3):
                for c in range(3):
                    if matriz[f][c] == matriz[f1][c1]:
                        cantidad += 1

    if cantidad > 9:
        Confirm(screen, Lose)
    elif columna != total or columna1 != total or columna2 != total or fila != total or \
                    fila1 != total or fila2 != total or diagonal != total or diagonal1 != total:
        Confirm(screen, Lose)
    else:
        Confirm(screen, Win)

def Confirm(screen, result):
    Background = pygame.image.load("images/Background.png")
    finish = True
    clock = pygame.time.Clock()
    mouse = pygame.Rect(0, 0, 1, 1)
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    finish = False

        mouse.left, mouse.top = pygame.mouse.get_pos()
        clock.tick(20)
        screen.blit(Background, (0, 0))
        screen.blit(result, (0, 0))
        pygame.display.update()

def Help(screen):
    Help = pygame.image.load("images/Help.png")
    Background = pygame.image.load("images/Background.png")
    finish = True
    clock = pygame.time.Clock()
    mouse = pygame.Rect(0, 0, 1, 1)
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    finish = False

        mouse.left, mouse.top = pygame.mouse.get_pos()
        clock.tick(20)
        screen.blit(Background, (0, 0))
        screen.blit(Help, (0, 0))
        pygame.display.update()

def menu(screen):
    Tutorial = pygame.image.load("images/Tutorial.png")
    Background = pygame.image.load("images/Background.png")
    finish = True
    clock = pygame.time.Clock()
    mouse = pygame.Rect(0, 0, 1, 1)
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    finish = False

        mouse.left, mouse.top = pygame.mouse.get_pos()
        clock.tick(20)
        screen.blit(Background, (0, 0))
        screen.blit(Tutorial, (0, 0))
        pygame.display.update()

def main():
    WIDTH = 1280
    HEIGHT = 720
    FPS = 60

    TABLE = (60, 216, 255)
    BLACK = (0,0, 0)
    BACKGROUND = (222, 252, 255)
    WHITE = (255, 255, 255)

    LIMITLEVE1 = 9

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Cuadrado Magico")

    clock = pygame.time.Clock()

    finish = True
    font = pygame.font.SysFont("Arial", 54, True, False)

    Background = pygame.image.load("images/Background.png")
    Error = pygame.image.load("images/Error.png")

    reset = pygame.Rect(1075, 100, 130, 130)
    confirm = pygame.Rect(1075, 490, 130, 130)
    help = pygame.Rect(1075, 290, 130, 130)
    tutorial = pygame.Rect(80, 276, 130, 130)

    p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

    mouse = pygame.Rect(0, 0, 1, 1)

    r1 = pygame.Rect(395, 110, 160, 160)
    r2 = pygame.Rect(560, 110, 160, 160)
    r3 = pygame.Rect(725, 110, 160, 160)
    r4 = pygame.Rect(395, 270, 160, 160)
    r5 = pygame.Rect(560, 270, 160, 160)
    r6 = pygame.Rect(725, 270, 160, 160)
    r7 = pygame.Rect(395, 430, 160, 160)
    r8 = pygame.Rect(560, 430, 160, 160)
    r9 = pygame.Rect(725, 430, 160, 160)

    listTable = [mouse, r1, r2, r3, r4, r5, r6, r7, r8, r9]

    #matriz = [
     #       [4, 9, 2],
      #      [3, 5, 7],
       #     [8, 1, 6]
        #    ]

    time = 0
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                time = 0

                if mouse.colliderect(r1):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p1 == 0: p1 = LIMITLEVE1
                        else: p1 -= 1
                    elif pygame.mouse.get_pressed() == (1,0,0):
                        p1 += 1
                        if p1 > LIMITLEVE1: p1 = 0
                elif mouse.colliderect(r2):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p2 == 0:p2 = LIMITLEVE1
                        else: p2 -= 1
                    else:
                        p2 += 1
                        if p2 > LIMITLEVE1: p2 = 0
                elif mouse.colliderect(r3):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p3 == 0:p3 = LIMITLEVE1
                        else: p3 -= 1
                    else:
                        p3 += 1
                        if p3 > LIMITLEVE1: p3 = 0
                elif mouse.colliderect(r4):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p4 == 0:p4 = LIMITLEVE1
                        else: p4 -= 1
                    else:
                        p4 += 1
                        if p4 > LIMITLEVE1: p4 = 0
                elif mouse.colliderect(r5):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p5 == 0: p5 = LIMITLEVE1
                        else: p5 -= 1
                    else:
                        p5 += 1
                        if p5 > LIMITLEVE1: p5 = 0
                elif mouse.colliderect(r6):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p6 == 0:p6 = LIMITLEVE1
                        else: p6 -= 1
                    else:
                        p6 += 1
                        if p6 > LIMITLEVE1: p6 = 0
                elif mouse.colliderect(r7):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p7 == 0: p7 = LIMITLEVE1
                        else: p7 -= 1
                    else:
                        p7 += 1
                        if p7 > LIMITLEVE1: p7 = 0
                elif mouse.colliderect(r8):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p8 == 0:p8 = LIMITLEVE1
                        else: p8 -= 1
                    else:
                        p8+= 1
                        if p8 > LIMITLEVE1: p8 = 0
                elif mouse.colliderect(r9):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if p9 == 0: p9 = LIMITLEVE1
                        else: p9 -= 1
                    else:
                        p9 += 1
                        if p9 > LIMITLEVE1: p9 = 0
                elif mouse.colliderect(confirm):
                    matriz = [
                        [p1, p2, p3],
                        [p4, p5, p6],
                        [p7, p8, p9]
                    ]
                    confirmGame(matriz, screen)
                elif mouse.colliderect(help): Help(screen)
                elif mouse.colliderect(tutorial): menu(screen)
                elif mouse.colliderect(reset): p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

        time += 1
        punto1 = font.render(str(p1), 1, BLACK)
        punto2 = font.render(str(p2), 1, BLACK)
        punto3 = font.render(str(p3), 1, BLACK)
        punto4 = font.render(str(p4), 1, BLACK)
        punto5 = font.render(str(p5), 1, BLACK)
        punto6 = font.render(str(p6), 1, BLACK)
        punto7 = font.render(str(p7), 1, BLACK)
        punto8 = font.render(str(p8), 1, BLACK)
        punto9 = font.render(str(p9), 1, BLACK)

        clock.tick(FPS)

        screen.blit(Background, (0, 0))

        mouse.left, mouse.top = pygame.mouse.get_pos()

        screen.blit(punto1, (465, 160))
        screen.blit(punto2, (625, 160))
        screen.blit(punto3, (785, 160))
        screen.blit(punto4, (465, 320))
        screen.blit(punto5, (630, 320))
        screen.blit(punto6, (785, 320))
        screen.blit(punto7, (465, 480))
        screen.blit(punto8, (625, 480))
        screen.blit(punto9, (785, 480))



        if time == 1500:
            p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
            menu(screen)
        elif time == 4500: screen.blit(Error, (0, 0))

        pygame.display.update()


main()

