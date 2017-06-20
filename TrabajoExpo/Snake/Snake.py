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

class Snake(object):
    def CreateSnake(self):
        self.snake = pygame.Rect(50, 60, 15, 15)
        return self.snake

    def PaintSnake(self, screen, color, listsnake):
        for item in listsnake:
            pygame.draw.rect(screen, color, item)

    def AddSnake(self, listsnake, x, y):
        self.snake = pygame.Rect(x, y, 15, 15)
        listsnake.append (self.snake)
        return listsnake

    def Getpos (self, listsnake):
        for item in listsnake:
            self.lastitem = item
        return (self.lastitem.x , self.lastitem.y)

    def MoveSnake(self, listsnake, x, y):
        for item in listsnake:
            self.item2 = (item.x, item.y)
            item.move_ip (x, y)


    def DetectChanges(self, x, y):
        self.lastchage.append(x, y)
        return self.lastchange


def main ():

    pygame.display.set_caption("JUEGUITO")
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

    finish = False

    background = Background()
    listborders = background.CreateBorders(width, height)


    while finish != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass



        clock.tick(fps)
        screen.fill(white)
        background.PaintBorders(screen, grey, listborders)
        pygame.display.update()


main()
pygame.quit()


