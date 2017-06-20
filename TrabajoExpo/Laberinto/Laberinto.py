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
    def CreateBorders(self, width, height):
        self.right = pygame.Rect(width/width, height/height, width/100, height) # x y width height
        self.top = pygame.Rect(width/width, height/height, width, height/60)
        self.down = pygame.Rect(width/width, height-10, width, height/60)
        self.left = pygame.Rect(width-10, height/height, width/100, height)
        listborders = [self.top, self.down, self.right, self.left]
        return listborders

    def PaintBorders (self, screen, color, listborder):
        pygame.draw.rect(screen, color, listborder[0])
        pygame.draw.rect(screen, color, listborder[1])
        pygame.draw.rect(screen, color, listborder[2])
        pygame.draw.rect(screen, color, listborder[3])

    def newMap(self, lvl):
        if lvl == 1:
            self.rect1 = pygame.Rect(150, 150, 50, 500)
            self.rect2 = pygame.Rect(200, 0, 600, 50)
            self.rect3 = pygame.Rect(1400, 50, 50, 950)
            self.rect4 = pygame.Rect(500, 300, 500, 50)
            self.listrec = [self.rect1, self.rect2, self.rect3, self.rect4]
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

    def detectCollision(self, screen, player, map):
        for item in map:
            if player.colliderect(item):
                pygame.draw.rect(screen, (255,0,0), player)
                return True

    def detectLimit(self, player, listborders):
        for item in listborders:
            if player.colliderect(item):
                return True

def main ():

    pygame.display.set_caption("LABERINTO")
    (width, height) = (1500, 950)
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
    vx, vy = (0, 0)

    up, down, left, right = False, False, False, False

    finish = False
    finishlvl = True

    player = Player()
    player1 = player.createPlayer()
    background = Background()
    listborders = background.CreateBorders(width, height)
    level = 1
    map = background.newMap(level)
    lost = False
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

        (oldx, oldy) = (player1.x, player1.y)

        clock.tick(fps)
        screen.fill(white)
        background.PaintBorders(screen, grey, listborders)
        background.paintMap(screen, grey, map)

        collision = player.detectCollision(screen, player1, map)
        if collision:
            (player1.x, player1.y) = (25, 25)
            collision = False
        else: player.movePlayer(player1, vx, vy)

        limit = player.detectLimit(player1, listborders)
        if limit:
            (player1.x, player1.y) = (oldx, oldy)
            limit = False

        player.update(screen, black, player1)
        pygame.display.update()


main()
pygame.quit()


