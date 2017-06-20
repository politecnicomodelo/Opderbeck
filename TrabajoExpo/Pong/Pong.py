import pygame

pygame.init()
pygame.display.set_caption("PONG")
screen = (500,500)
pantalla = pygame.display.set_mode(screen)

fin = False

clock = pygame.time.Clock()
fps = 20

blanco = (255,255,255)
rojo = (255,0,0)
azul = (0,0,255)
negro = (0,0,0)

jugador1 = pygame.Rect (25,150,10,50)
jugador2 = pygame.Rect (290,150,10,50)
pelota = pygame.Rect (15,15,10,10)

abajo = pygame.Rect (5,310,315,15)
arriba = pygame.Rect (5,5,310,15)
izquierda = pygame.Rect (5,5,10,310)
derecha = pygame.Rect (310,5,10,310)

sentido = True
sentido1 = True

vy1 = 0
vy2 = 0
vx = 5
vy = 5

puntos1 = "0"
puntos2 = "0"

fuente = pygame.font.SysFont("Arial", 20, True, False)
texto1 = fuente.render(puntos1, 0, negro)
texto2 = fuente.render(puntos2, 0, negro)
texto3 = fuente.render("Puntos:", 0, negro)

velocidad = 10
up, down, w, s = False, False, False, False

while fin != True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vy1 -= velocidad
                up = True

            if event.key == pygame.K_DOWN:
                vy1 = velocidad
                down = True

            if event.key == pygame.K_w:
                vy2 -= velocidad
                w = True
            if event.key == pygame.K_s:
                vy2 = velocidad
                s = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if down: vy1 = velocidad
                else: vy1 = 0
                up = False
            if event.key == pygame.K_DOWN:
                if up: vy1 = velocidad
                else: vy1 = 0
                down = False
            if event.key == pygame.K_w:
                if s: vy1 = velocidad
                else: vy2 = 0
                w = False
            if event.key == pygame.K_s:
                if w: vy1 = velocidad
                else: vy2 = 0
                s = False


    oldy1 = jugador1.y
    oldy2 = jugador2.y
    jugador1.move_ip(0, vy1)
    jugador2.move_ip(0, vy2)
    pelota.move_ip (vx, vy)


    if pelota.colliderect (izquierda):
        pelota.y = 150
        pelota.x = 150

    if pelota.colliderect (derecha):
        pelota.y = 50
        pelota.x = 50

    if pelota.colliderect(abajo):
        if sentido == True:
            vx = 5
            vy =-5
            sentido = False
        else :
            vx = -5
            vy = -5
            sentido = True
    elif pelota.colliderect(arriba):
        if sentido == True:
            vx = 5
            vy = 5
            sentido = False
        else :
            vx = -5
            vy = 5
            sentido = True
    elif pelota.colliderect(jugador2):
        if sentido1 == True:
            vx = -5
            vy = -5
            sentido1 = False
        else :
            vx = -5
            vy = 5
            sentido1 = True
    elif pelota.colliderect(jugador1):
        if sentido1 == True:
            vx = 5
            vy =-5
        else :
            vx = 5
            vy = 5

    if jugador1.colliderect(abajo) or jugador1.colliderect(arriba):
        jugador1.y = oldy1
    if jugador2.colliderect(abajo) or jugador2.colliderect(arriba):
        jugador2.y = oldy2

    pelota.move_ip(vx, vy)
    clock.tick(fps)

    pantalla.fill(blanco)

    pantalla.blit(texto3, (230, 350))
    pantalla.blit(texto3, (0, 350))
    pantalla.blit(texto1, (300, 350))
    pantalla.blit(texto2, (70, 350))
    pygame.draw.rect(pantalla, rojo, jugador1)
    pygame.draw.rect(pantalla, azul, jugador2)
    pygame.draw.rect(pantalla, negro, abajo)
    pygame.draw.rect(pantalla, negro, arriba)
    pygame.draw.rect(pantalla, negro, izquierda)
    pygame.draw.rect(pantalla, negro, derecha)
    pygame.draw.rect(pantalla, negro, pelota)

    pygame.display.update()


pygame.quit()