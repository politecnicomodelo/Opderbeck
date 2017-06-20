import pygame
pygame.init()


def removeBackground(image):
    image = image.convert()
    color = image.get_at((0, 0))
    image.set_colorkey(color)
    return image


class Menu():
    pass

class Background (object):
    def newMap(self, lvl):
        if lvl == 1:
            self.rect1 = pygame.Rect(150,150,50,500)
            self.rect2 = pygame.Rect(200, 0, 600, 50)
            self.listrec = [self.rect1, self.rect2]
        elif lvl == 2:
            pass
        return self.listrec

    def paintMap(self, screen, color, map):
        for item in map:
            pygame.draw.rect (screen, color, item)

class Player (object):

    def createPlayer(self):
        self.player = pygame.Rect(100, 100, 25, 25)
        return self.player

    def movePlayer(self, player, x, y):
       player.move_ip(x, y)

    def update(self, screen, color, player):
        pygame.draw.rect(screen, color, player)

def main ():

    pygame.display.set_caption("LABERINTO")
    width, height = 1500, 950
    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    fps = 20

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (155,155,155)

    velocidad = 10
    vx, vy = (0,0)

    up, down, left, right = False, False, False, False

    finish = False
    finishlvl = True

    player = Player()
    player1 = player.createPlayer()
    background = Background()

    level = 1
    while finish != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    vy =-velocidad
                    up = True
                if event.key == pygame.K_DOWN:
                    vy = velocidad
                    down = True
                if event.key == pygame.K_RIGHT:
                    vx = velocidad
                    right = True
                if event.key == pygame.K_LEFT:
                    vx = -velocidad
                    left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                    if right: vx = velocidad
                    else: vx = 0
                if event.key == pygame.K_RIGHT:
                    right = False
                    if left: vx = -velocidad
                    else: vx = 0
                if event.key == pygame.K_UP:
                    up = False
                    if down: vy = velocidad
                    else: vy = 0
                if event.key == pygame.K_DOWN:
                    down = False
                    if up: vy = -velocidad
                    else: vy = 0

        if finishlvl:
            map = background.newMap(level)


        clock.tick(fps)
        screen.fill(white)
        background.paintMap(screen, grey, map)
        player.movePlayer(player1, vx, vy)
        player.update(screen, black, player1)
        pygame.display.update()


main()
pygame.quit()


