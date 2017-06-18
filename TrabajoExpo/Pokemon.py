import pygame
pygame.init()

class Fondo(pygame.sprite.Sprite):

    def __init__(self):
        self.fondo = pygame.image.load("imagenes/FondoPueblo.png").convert_alpha()
        self.rect = self.fondo.get_rect()

    def update(self, screen, velocidadx, velocidady):
        self.rect.move_ip(-velocidadx, -velocidady)
        screen.blit(self.fondo, self.rect)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        # cargado de imagenes___________________________________________________________________________________________
        self.PersonajeFrente = pygame.image.load("imagenes/PersonajeFrente.png").convert_alpha()
        self.PersonajeFrente = self.SacarFondo(self.PersonajeFrente)
        self.PersonajeFrenteCaminando1 = pygame.image.load("imagenes/PersonajeFrenteCaminando1.png").convert_alpha()
        self.PersonajeFrenteCaminando1 = self.SacarFondo(self.PersonajeFrenteCaminando1)
        self.PersonajeFrenteCaminando2 = pygame.image.load("imagenes/PersonajeFrenteCaminando2.png").convert_alpha()
        self.PersonajeFrenteCaminando2 = self.SacarFondo(self.PersonajeFrenteCaminando2)
        self.PersonajeEspalda = pygame.image.load("imagenes/PersonajeEspalda.png").convert_alpha()
        self.PersonajeEspalda = self.SacarFondo(self.PersonajeEspalda)
        self.PersonajeEspaldaCaminando1 = pygame.image.load("imagenes/PersonajeEspaldaCaminando1.png").convert_alpha()
        self.PersonajeEspaldaCaminando1 = self.SacarFondo(self.PersonajeEspaldaCaminando1)
        self.PersonajeEspaldaCaminando2 = pygame.image.load("imagenes/PersonajeEspaldaCaminando2.png").convert_alpha()
        self.PersonajeEspaldaCaminando2 = self.SacarFondo(self.PersonajeEspaldaCaminando2)
        self.PersonajeDerecha = pygame.image.load("imagenes/PersonajeDerecha.png").convert_alpha()
        self.PersonajeDerecha = self.SacarFondo(self.PersonajeDerecha)
        self.PersonajeDerechaCaminando1 = pygame.image.load("imagenes/PersonajeDerechaCaminando1.png").convert_alpha()
        self.PersonajeDerechaCaminando1 = self.SacarFondo(self.PersonajeDerechaCaminando1)
        self.PersonajeDerechaCaminando2 = pygame.image.load("imagenes/PersonajeDerechaCaminando2.png").convert_alpha()
        self.PersonajeDerechaCaminando2 = self.SacarFondo(self.PersonajeDerechaCaminando2)
        self.PersonajeIzquierda = pygame.image.load("imagenes/PersonajeIzquierda.png").convert_alpha()
        self.PersonajeIzquierda = self.SacarFondo(self.PersonajeIzquierda)
        self.PersonajeIzquierdaCaminando1 = pygame.image.load("imagenes/PersonajeIzquierdaCaminando1.png").convert_alpha()
        self.PersonajeIzquierdaCaminando1 = self.SacarFondo(self.PersonajeIzquierdaCaminando1)
        self.PersonajeIzquierdaCaminando2 = pygame.image.load("imagenes/PersonajeIzquierdaCaminando2.png").convert_alpha()
        self.PersonajeIzquierdaCaminando2 = self.SacarFondo(self.PersonajeIzquierdaCaminando2)

        self.listImages = [[self.PersonajeFrente, self.PersonajeFrenteCaminando1, self.PersonajeFrenteCaminando2],
                            [self.PersonajeEspalda, self.PersonajeEspaldaCaminando1, self.PersonajeEspaldaCaminando2],
                            [self.PersonajeDerecha, self.PersonajeDerechaCaminando1, self.PersonajeDerechaCaminando2],
                            [self.PersonajeIzquierda, self.PersonajeIzquierdaCaminando1, self.PersonajeIzquierdaCaminando2]]

        self.currentImage = 0
        self.image = self.listImages[0][self.currentImage]

        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = (50, 50)

        self.motion = False
        self.orientation = 0

    def SacarFondo(self, image):
        image = image.convert()
        color = image.get_at((0, 0))
        image.set_colorkey(color)
        return image

    def MovePJ(self, velocidadx, velocidady):
        self.rect.move_ip(velocidadx, velocidady)

    def Update(self, screen, velocidadx, velocidady):
        screen.blit(self.image, self.rect)
        if (velocidadx, velocidady) == (0, 0):
            self.motion = False
            self.currentImage = 0
        else: self.motion = True
        if velocidady > 0:
            self.orientation = 0
            if self.motion:
                if self.currentImage == 0 or self.currentImage > 3: self.currentImage = 1
                elif self.currentImage == 1: self.currentImage = 2
                elif self.currentImage == 2: self.currentImage = 1
        elif velocidady < 0:
            self.orientation = 1
            if self.motion:
                if self.currentImage == 0 or self.currentImage > 3: self.currentImage = 1
                elif self.currentImage == 1: self.currentImage = 2
                elif self.currentImage == 2: self.currentImage = 1
        if velocidadx > 0:
            self.orientation = 2
            if self.motion:
                if self.currentImage == 0 or self.currentImage > 3:self.currentImage = 1
                elif self.currentImage == 1: self.currentImage = 2
                elif self.currentImage == 2: self.currentImage = 1
                if self.currentImage > 2: self.currentImage = 0
        elif velocidadx < 0:
            self.orientation = 3
            if self.motion:
                if self.currentImage == 0 or self.currentImage > 3: self.currentImage = 1
                elif self.currentImage == 1: self.currentImage = 2
                elif self.currentImage == 2: self.currentImage = 1
                if self.currentImage > 2: self.currentImage = 0

        (velocidadx, velocidady) = (0, 0)
        self.MovePJ(velocidadx, velocidady)
        self.image = self.listImages[self.orientation][self.currentImage]
        screen.blit(self.image, self.rect)


def main():
    pygame.display.set_caption("JUEGUITO")
    displaySize = (1000, 1000)
    screen = pygame.display.set_mode(displaySize)

    clock = pygame.time.Clock()
    fps = 20

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    finish = False

    fondo = Fondo()
    player = Player()
    velocidad = 10
    (vx, vy) = (0, 0)

    left, right, up, down = False, False, False, False

    while finish != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                    vx = -velocidad
                if event.key == pygame.K_RIGHT:
                    vx = velocidad
                    right = True
                if event.key == pygame.K_DOWN:
                    down = True
                    vy = velocidad
                if event.key == pygame.K_UP:
                    up = True
                    vy = -velocidad
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

        clock.tick(fps)
        screen.fill(white)
        fondo.update(screen, vx, vy)
        player.update(screen, vx, vy)
        pygame.display.update()

main()
pygame.quit()