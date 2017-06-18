import pygame
pygame.init()


"""def CargarImagenes():
    # cargado de imagenes_______________________________________________________________________________________________
    PersonajeFrente = pygame.image.load("PersonajeFrente.png").convert_alpha()
    PersonajeFrenteCaminando1 = pygame.image.load("PersonajeFrenteCaminando1.png").convert_alpha()
    PersonajeFrenteCaminando2 = pygame.image.load("PersonajeFrenteCaminando2.png").convert_alpha()
    PersonajeEspalda = pygame.image.load("PersonajeEspalda.png").convert_alpha()
    PersonajeEspaldaCaminando1 = pygame.image.load("PersonajeEspaldaCaminando1.png").convert_alpha()
    PersonajeEspaldaCaminando2 = pygame.image.load("PersonajeEspaldaCaminando2.png").convert_alpha()
    PersonajeDerecha = pygame.image.load("PersonajeDerecha.png").convert_alpha()
    PersonajeDerechaCaminando1 = pygame.image.load("PersonajeDerechaCaminando1.png").convert_alpha()
    PersonajeDerechaCaminando2 = pygame.image.load("PersonajeDerechaCaminando2.png").convert_alpha()
    PersonajeIzquierda = pygame.image.load("PersonajeIzquierda.png").convert_alpha()
    PersonajeIzquierdaCaminando1 = pygame.image.load("PersonajeIzquierdaCaminando1.png").convert_alpha()
    PersonajeIzquierdaCaminando2 = pygame.image.load("PersonajeIzquierdaCaminando2.png").convert_alpha()

    #fondo = pygame.image.load("").convert_alpha()

    lista = [[PersonajeFrente, PersonajeFrenteCaminando1, PersonajeFrenteCaminando2],
            [PersonajeEspalda, PersonajeEspaldaCaminando1, PersonajeEspaldaCaminando2],
            [PersonajeDerecha, PersonajeDerechaCaminando1, PersonajeDerechaCaminando2],
            [PersonajeIzquierda, PersonajeIzquierdaCaminando1, PersonajeIzquierdaCaminando2]]
    return lista"""""

class Fondo(pygame.sprite.Sprite):

    def __init__(self):
        self.fondo = pygame.image.load("FondoPueblo.png").convert_alpha()
        self.rect = self.fondo.get_rect()

    def update(self, screen, velocidadx, velocidady):
        self.rect.move_ip(-velocidadx, -velocidady)
        screen.blit(self.fondo, self.rect)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        # cargado de imagenes___________________________________________________________________________________________
        self.PersonajeFrente = pygame.image.load("PersonajeFrente.png").convert_alpha()
        self.PersonajeFrenteCaminando1 = pygame.image.load("PersonajeFrenteCaminando1.png").convert_alpha()
        self.PersonajeFrenteCaminando2 = pygame.image.load("PersonajeFrenteCaminando2.png").convert_alpha()
        self.PersonajeEspalda = pygame.image.load("PersonajeEspalda.png").convert_alpha()
        self.PersonajeEspaldaCaminando1 = pygame.image.load("PersonajeEspaldaCaminando1.png").convert_alpha()
        self.PersonajeEspaldaCaminando2 = pygame.image.load("PersonajeEspaldaCaminando2.png").convert_alpha()
        self.PersonajeDerecha = pygame.image.load("PersonajeDerecha.png").convert_alpha()
        self.PersonajeDerechaCaminando1 = pygame.image.load("PersonajeDerechaCaminando1.png").convert_alpha()
        self.PersonajeDerechaCaminando2 = pygame.image.load("PersonajeDerechaCaminando2.png").convert_alpha()
        self.PersonajeIzquierda = pygame.image.load("PersonajeIzquierda.png").convert_alpha()
        self.PersonajeIzquierdaCaminando1 = pygame.image.load("PersonajeIzquierdaCaminando1.png").convert_alpha()
        self.PersonajeIzquierdaCaminando2 = pygame.image.load("PersonajeIzquierdaCaminando2.png").convert_alpha()

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

    def MovePJ(self, velocidadx, velocidady):
        self.rect.move_ip(velocidadx, velocidady)

    def Update(self, screen, velocidadx, velocidady):
        if (velocidadx, velocidady) == (0, 0):
            self.motion = False
            self.currentImage = 0
        else:
            self.motion = True
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
        fondo.update(screen, vx, vy)
        player.update(screen, vx, vy)
        pygame.display.update()

main()
pygame.quit()