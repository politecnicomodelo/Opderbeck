import pygame



class Fondo(pygame.sprite.Sprite):


    def __init__(self):
        self.fono = pygame.image.load("Imagenes/Pasto_Grande.png").convert_alpha()
        self.rect = self.fondo.get_rect()

    def update(self, pantalla, vx, vy):
        self.rect.move_ip(-vx, -vy)
        pantalla.blit(self.fondo, self.rect)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.imagenes = [[self.personaje, self.personaje_frente_caminando, self.personaje_frente_caminando2],
        [self.personaje2, self.personaje_espalda_caminando, self.personaje_espalda_caminando2],
        [self.personaje_derecha, self.personaje_derecha_caminando],
        [self.personaje_izquierda, self.personaje_izquierda_caminando]]


        self.imagen_actual = 0
        self.imagen = self.imagenes[0][self.imagen_actual]
        self.rect = self.imagen.get_rect()
        self.rect.top, self.rect.left = (100, 200)
        self.estamoviendo = False
        self.orientacion = 0





    def Mover(self, vx, vy):
        self.rect.move_ip(vx, vy)


    def update(self, pantalla, vx, vy, orientacion):

        if (vx, vy) == (0, 0):
            self.estamoviendo = False
            self.imagen_actual = 0
        else:
            self.estamoviendo = True

        if vy > 0:
            self.orientacion = 0

        if self.imagen_actual == 0 and self.estamoviendo == True:
            self.imagen_actual = 1
        elif self.imagen_actual == 1 and self.estamoviendo == True:
            self.imagen_actual = 2
        elif self.imagen_actual == 2 and self.estamoviendo == True:
            self.imagen_actual = 1
        if self.imagen_actual > 3 and self.estamoviendo == True:
            self.imagen_actual = 1


        if vy < 0:
            self.orientacion = 1

        if self.imagen_actual == 0 and self.estamoviendo == True:
            self.imagen_actual = 1
        elif self.imagen_actual == 1 and self.estamoviendo == True:
            self.imagen_actual = 2
        elif self.imagen_actual == 2 and self.estamoviendo == True:
            self.imagen_actual = 1
        if self.imagen_actual > 3 and self.estamoviendo == True:
            self.imagen_actual = 1



        if vx > 0:
            self.orientacion = 2

        if self.imagen_actual == 0 and self.estamoviendo == True:
            self.imagen_actual = 1
        elif self.imagen_actual == 1 and self.estamoviendo == True:
            self.imagen_actual = 2
        elif self.imagen_actual == 2 and self.estamoviendo == True:
            self.imagen_actual = 1

        if self.imagen_actual > 1 and self.estamoviendo == True:
            self.imagen_actual = 0


        if vx < 0:
            self.orientacion = 3

        if self.imagen_actual == 0 and self.estamoviendo == True:
            self.imagen_actual = 1
        elif self.imagen_actual == 1 and self.estamoviendo == True:
            self.imagen_actual = 2
        elif self.imagen_actual == 2 and self.estamoviendo == True:
            self.imagen_actual = 1

        if self.imagen_actual > 1 and self.estamoviendo == True:
            self.imagen_actual = 0
            vx = 0
            vy = 0
            self.Mover(vx, vy)
            self.imagen = self.imagenes[self.orientacion][self.imagen_actual]
            pantalla.blit(self.imagen, self.rect)



def main():



    pygame.init()

    pantalla = pygame.display.set_mode([1800, 900])
    pygame.display.set_caption("SEB'S")
    salir = False

    reloj = pygame.time.Clock()
    (x, y) = (100, 100)

    fondo = pygame.image.load("Imagenes/Pasto.jpg")
    personaje = pygame.image.load("Imagenes/Persona_Frente.png")
    personaje1 = pygame.sprite.Sprite()
    personaje1.image = personaje
    personaje1.rect = personaje.get_rect()
    personaje1.rect.top = 50
    personaje1.rect.left = 50

    r1 = pygame.Rect(150, 15, 15, 200)

    player = Player()
    fondo = Fondo()

    vx, vy = 0, 0
    velocidad = 7
    orientacion = 0
    leftapretada, rightapretada, upapretada, downapretada = False, False, False, False

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx -= 5
                vx = -velocidad
                leftapretada = True
            if event.key == pygame.K_RIGHT:
                vx += 5
                vx = velocidad
                rightapretada = True
            if event.key == pygame.K_DOWN:
                vy += 5
                downapretada = True
                vy = velocidad
            if event.key == pygame.K_UP:
                vy -= 5
                upapretada = True
                vy = -velocidad

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 vy = 0
                oldx = personaje1.rect.left
                personaje1.rect.move_ip(vx, vy)
            if personaje1.rect.colliderect(r1):
                    personaje1.rect.left = oldx
                    reloj.tick(30)
                    pantalla.blit(fondo, (0, 0))
                    pantalla.blit(personaje1.image, personaje1.rect)
                    pygame.draw.rect(pantalla, (0, 0, 0), r1)

            if event.key == pygame.K_LEFT:
                    leftapretada = False

            if rightapretada: vx = velocidad
            else: vx = 0

            if event.key == pygame.K_RIGHT:
                rightapretada = False

            if leftapretada: vx = -velocidad
            else: vx = 0

            if event.key == pygame.K_UP:
                upapretada = False

            if downapretada: vy = velocidad
            else: vy = 0

            if event.key == pygame.K_DOWN:
                downapretada = False

            if upapretada: vy = -velocidad
            else: vy = 0


        reloj.tick(30)
        fondo.update(pantalla, vx, vy)
        player.update(pantalla, vx, vy, orientacion)
        pygame.display.update()


    pygame.quit()

main()