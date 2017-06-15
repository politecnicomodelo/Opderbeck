import pygame
import pymysql

database = pymysql.connect(host = "localhost", user = "root", passwd = "",
                           database = "expo_modelo_2017_computacion", autocommit = True)

cursor = database.cursor()

pygame.init()
#titulo de la pantalla
pygame.display.set_caption("EXPO MODELO 2017")

#tamaño de la pantalla
screen = (1350,735)

#superficie principal
pantalla = pygame.display.set_mode(screen)

#superficies de cada proyecto
superficie_titulo = pygame.Surface((750,200))
superficie_descripcion = pygame.Surface((750,530))
superficie_estadisticas = pygame.Surface((600,230))
superficie_fotos = pygame.Surface((600,500))

#velocidad de refresco
clock = pygame.time.Clock()
fps = 20

#colores
blanco = (255,255,255)
rojo = (255,0,0)
azul = (0,0,255)
negro = (0,0,0)
verde = (0,255,0)

#nombre de proyectos
texto_Titulo_stopMotion = cursor.execute()
texto_Titulo_chicas = cursor.execute()
texto_Titulo_megaman = cursor.execute()
texto_Titulo_mario = cursor.execute()
texto_Titulo_maquinaEnigma = cursor.execute()
texto_Titulo_scorpion = cursor.execute()
texto_Titulo_juli = cursor.execute()

#descripcion de los proshectos


#Proyectos bool
proyecto_stopMotion = False
proyecto_chicas = False
proyecto_megaman = False
proyecto_mario = False
proyecto_maquinaEnigma = False
proyecto_scorpion = False
proyecto_pong = False

#esto es un bool!!
fin = False

#loop principal
while fin != True:
    #recorrido de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key_UP:
                proyecto_fiori = True
    clock.tick(fps)

    if proyecto_stopMotion:
        pass
        superficie_titulo.blit(texto_Titulo_stopMotion)
    elif proyecto_pong:
        pass
    elif proyecto_maquinaEnigma:
        pass
    elif proyecto_mario:
        pass
    elif proyecto_stopMotion:
        pass
    elif proyecto_chicas:
        pass

    #color de las superficies
    superficie_titulo.fill(blanco)
    superficie_descripcion.fill(rojo)
    superficie_estadisticas.fill(azul)
    superficie_fotos.fill(verde)

    #colocado de superficies dentro de la pantalla
    pantalla.blit(superficie_titulo,(0,0))
    pantalla.blit(superficie_descripcion, (0, 201))
    pantalla.blit(superficie_estadisticas, (751, 0))
    pantalla.blit(superficie_fotos, (751, 231))

    pygame.display.update()

database.close()
pygame.quit()