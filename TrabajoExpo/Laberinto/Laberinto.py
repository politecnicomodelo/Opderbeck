import pygame
pygame.init()


def removeBackground(image):
    image = image.convert()
    color = image.get_at((0, 0))
    image.set_colorkey(color)
    return image


class Menu(object):
    def InitializeMenu(self, width, height):
        self.start = pygame.Rect(width/2, height/2, width/2, height/10)
        self.save = pygame.Rect(width/2.2, height/2.2, width/2, height/10)
        self.button = [self.start, self.save]
        return self.button

    def ShowMenu(self, screen, color, button):
        pygame.draw.rect(screen, color, button[0])
        pygame.draw.rect(screen, color, button[1])

    def StartGame(self):
        pass

    def SaveGame(self):
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

    def newMap(self, lvl, width, height):
        if lvl == 3:
            self.rect1 = pygame.Rect(width/4, height/4, width/2, height/2)
            self.rect2 = pygame.Rect(width/4, height/12, width/14, height/6)
            self.rect3 = pygame.Rect(width/15, height/1.5, width/4, height/12)
            self.rect4 = pygame.Rect(width/100, height/1.9, width/5, height/12)
            self.rect5 = pygame.Rect(width/15, height/2.5, width/5, height/12)
            self.rect6 = pygame.Rect(width/100, height/3.5, width/5, height/12)
            self.rect7 = pygame.Rect(width/15, height/6.0, width/5, height/12)
            self.rect8 = pygame.Rect(width/2.7, height/70, width/12, height/5)
            self.rect9 = pygame.Rect(width/2, height/6.7, width/12, height/7)
            self.rect10 = pygame.Rect(width/1.6, height/70, width/12, height/5)
            self.rect11 = pygame.Rect(width/2, height/70, width/12, height/10)
            self.rectfinal = pygame.Rect(width-50, height-50, 25, 25)
            self.listrec = [self.rect1, self.rect2, self.rect3, self.rect4, self.rect5, self.rect6, self.rect7, self.rect8, self.rect9, self.rect10, self.rect11, self.rectfinal]
        elif lvl == 2:
            self.rect1 = pygame.Rect(width/25.5, height/10, width/1.2, height/10)
            self.rect2 = pygame.Rect(width/10, height/3.8, width/1.1, height/15)
            self.rect3 = pygame.Rect(width/25, height/2.3, width/1.2, height/10)
            self.rect4 = pygame.Rect(width/10, height/1.6, width/1.1, height/15)
            self.rect5 = pygame.Rect(width/2, height/1.6, width/9, height/3)
            self.rectfinal = pygame.Rect(width - 50, height - 50, 25, 25)
            self.listrec = [self.rect1, self.rect2, self.rect3, self.rect4, self.rect5, self.rectfinal]
        elif lvl == 1:
            self.rect1 = pygame.Rect(width/2, height/18, width/8, height/1.05)
            self.rect2 = pygame.Rect(width/3.2, height/20, width/8, height/1.15)
            self.rect3 = pygame.Rect(width/10, height/4, width/38, height/1.50)
            self.rect4 = pygame.Rect(width/35, height/4, width/38, height/1.50)
            self.rect5 = pygame.Rect(width/6, height/4, width/38, height/1.50)
            self.rect6 = pygame.Rect(width/4.5, height/4, width/38, height/1.50)
            self.rect7 = pygame.Rect(width/3.4, height/4, width/1000, height/1000)
            self.rect8 = pygame.Rect(width/3.8, height/4, width/1000, height/1000)
            self.rect9 = pygame.Rect(width/12, height/4, width/1000, height/1000)
            self.rect10 = pygame.Rect(width/1.45, height/5, width/4, height/20)
            self.rectfinal = pygame.Rect(width - 50, height - 50, 25, 25)
            self.listrec = [self.rect1, self.rect2, self.rect3, self.rect4, self.rect5, self.rect6, self.rect7, self.rect8, self.rect9, self.rect10, self.rectfinal]

        return self.listrec

    def paintMap(self, screen, color, color1, map):
        for item in map:
            pygame.draw.rect (screen, color, item)
            if item == map[-1]:
                pygame.draw.rect(screen, color1, item)

class Player (object):

    def createPlayer(self):
        self.player = pygame.Rect(25, 25, 25, 25)
        return self.player

    def movePlayer(self, player, x, y):
        player.move_ip(x, y)

    def update(self, screen, color, player):
        pygame.draw.rect(screen, color, player)

    def detectCollision(self, screen, player, map):
        self.colision = 1
        for item in map:
            if player.colliderect(item):
                if item == map[-1]:
                    pygame.draw.rect(screen, (0, 255, 0), player)
                    self.colision = 2
                else:
                    pygame.draw.rect(screen, (255, 0, 0), player)
                    self.colision = True
                return self.colision

    def detectLimit(self, player, listborders):
        for item in listborders:
            if player.colliderect(item):
                return True


def main ():

    pygame.display.set_caption("MAZE")
    (width, height) = (1000, 900)
    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    fps = 30

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (155, 155, 155)

    velocidad = 10
    vx, vy = (0, 0)
    restartX, restartY = (25, 25)


    up, down, left, right = False, False, False, False

    finish = False
    nextlevel = True

    player = Player()
    player1 = player.createPlayer()
    background = Background()
    listborders = background.CreateBorders(width, height)
    level = 1
    mode = 0

    if mode == 1:
        pygame.mouse.set_pos(restartX, restartY)

    while finish != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if mode == 1:
                (player1.x, player1.y) = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finish = True
                    if event.key == pygame.K_UP:
                        vy = -velocidad
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


        if nextlevel:
            map = background.newMap(level, width, height)

        (oldx, oldy) = (player1.x, player1.y)

        clock.tick(fps)
        screen.fill(white)
        background.PaintBorders(screen, grey, listborders)
        background.paintMap(screen, grey, blue, map)
        if mode == 1:
            collision = player.detectCollision(screen, player1, map)
            if collision == 2:
                (player1.x, player1.y) = (restartX, restartY)
                pygame.mouse.set_pos((restartX, restartY))
                level += 1
                nextlevel = True
            elif collision:
                (player1.x, player1.y) = (restartX, restartY)
                pygame.mouse.set_pos((restartX, restartY))
                nextlevel = False
            else:
                player.movePlayer(player1, vx, vy)
                nextlevel = False
        else:
            collision = player.detectCollision(screen, player1, map)
            if collision == 2:
                (player1.x, player1.y) = (restartX, restartY)
                level += 1
                nextlevel = True
            elif collision:
                (player1.x, player1.y) = (restartX, restartY)
                nextlevel = False
            else:
                player.movePlayer(player1, vx, vy)
                nextlevel = False

            limit = player.detectLimit(player1, listborders)
            if limit:
                if mode == 1:
                    (player1.x, player1.y) = (oldx, oldy)
                    pygame.mouse.set_pos((oldx, oldy))
                else:(player1.x, player1.y) = (oldx, oldy)


        player.update(screen, black, player1)
        pygame.display.update()


main()
pygame.quit()


