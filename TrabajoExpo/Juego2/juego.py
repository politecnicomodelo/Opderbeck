import pygame
pygame.init()



def main():

    WIDTH = 1000
    HEIGHT = 600
    FPS = 60

    ORANGE = (252, 239, 176)
    BLACK = (0, 0, 0)
    BACKGROUND = (250, 246, 222)


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("JUEGO")

    clock = pygame.time.Clock()

    finish = True

    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: finish = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: finish = False

    clock.tick(FPS)

    screen.fill(BACKGROUND)

    pygame.display.update()

main()




