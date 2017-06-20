import pygame
pygame.init()


def removeBackground(image):
    image = image.convert()
    color = image.get_at((30, 0))
    image.set_colorkey(color)
    return image

class Menu():
    pass

class Background (pygame.sprite.Sprite):
    def UpdateMap(self, lvl):
        if lvl == 1:
            self.background = pygame.image.load("Imagenes/Niveles/mapaGrandeNivel1.png")
            self.background = removeBackground(self.background)
            #self.rect = self.background.get_rect()
        elif lvl == 2:
            pass
        elif lvl == 3:
            pass
        return self.background

class Enemy (pygame.sprite.Sprite):
    pass

class Player (pygame.sprite.Sprite):
    pass

class Arms (pygame.sprite.Sprite):
    def UploadImages(self):
        self.arma1 = pygame.image.load("Imagenes/Armas/Arma1Grande.png")
        self.arma1 = removeBackground(self.arma1)
        self.arma2 = pygame.image.load("Imagenes/Armas/Arma2Grande.png")
        self.arma2 = removeBackground(self.arma2)
        self.arma3 = pygame.image.load("Imagenes/Armas/Arma3Grande.png")
        self.arma3 = removeBackground(self.arma3)
        self.arma4 = pygame.image.load("Imagenes/Armas/Arma4Grande.png")
        self.arma4 = removeBackground(self.arma4)

    def ShowArms(self, screen):
        screen.blit(self.arma1, (100, 800))
        screen.blit(self.arma2, (250, 800))
        screen.blit(self.arma3, (400, 800))
        screen.blit(self.arma4, (520, 810))


def main ():

    pygame.display.set_caption("JUEGUITO")
    displaySize = (1500, 950)
    screen = pygame.display.set_mode(displaySize)

    clock = pygame.time.Clock()
    fps = 20

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (155,155,155)
    finish = False
    finishlvl = True


    background = Background()
    enemy = Enemy()
    player = Player()
    arms = Arms()
    arms.UploadImages()

    level = 1
    lowmenu = pygame.Rect(60, 770, 600, 140)

    while finish != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass


        if finishlvl:
            newbackground = background.UpdateMap(level)
        clock.tick(fps)
        screen.fill(white)
        screen.blit(newbackground, (0,0))
        pygame.draw.rect(screen, grey, lowmenu)
        arms.ShowArms(screen)
        pygame.display.update()


main()
pygame.quit()


