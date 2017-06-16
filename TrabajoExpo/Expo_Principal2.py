import pygame
#import pymysql

""""database = pymysql.connect(host = "localhost", user = "root", passwd = "",
                            database = "expo_modelo_2017_computacion", autocommit = True)"""""

#cursor = database.cursor()

pygame.init()
#titulo de la pantalla__________________________________________________________________________________________________
pygame.display.set_caption("EXPO MODELO 2017")

#tamaño de la pantalla__________________________________________________________________________________________________
screen = (1350,735)

#superficie principal__________________________________________________________________________________________________
pantalla = pygame.display.set_mode(screen)

#superficies de cada proyecto__________________________________________________________________________________________________
superficie_titulo = pygame.Surface((750,400))
superficie_descripcion = pygame.Surface((750,330))
superficie_estadisticas = pygame.Surface((600,330))
superficie_fotos = pygame.Surface((600,400))

#velocidad de refresco__________________________________________________________________________________________________
clock = pygame.time.Clock()
fps = 20

#colores__________________________________________________________________________________________________
blanco = (255,255,255)
rojo = (255,0,0)
azul = (0,0,255)
negro = (0,0,0)
verde = (0,255,0)

#creacion de una fuente__________________________________________________________________________________________________
fuente = pygame.font.SysFont("Arial", 50, True, True)

#LISTA DE IMAGENES DE CADA GRUPO________________________________________________________________________________________
lista_imagen_stopMotion = []
lista_imagen_chicas = []
lista_imagen_megaman = []
lista_imagen_mario = []
lista_imagen_maquinaEnigma = []
lista_imagen_scorpion = []
lista_imagen_juli = []



#nombre de proyectos__________________________________________________________________________________________________
#titulo_stopMotion = cursor.execute(select nombre from proyectos where id_grupo = 1;)
#titulo_chicas = cursor.execute(select nombre from proyectos where id_grupo = 2;)
#titulo_megaman = cursor.executeselect nombre from proyectos where id_grupo = 3;)
#titulo_mario = cursor.execute(select nombre from proyectos where id_grupo = 4;)
#titulo_maquinaEnigma = cursor.execute(select nombre from proyectos where id_grupo = 5;)
#titulo_scorpion = cursor.execute(select nombre from proyectos where id_grupo = 6;)
#titulo_juli = cursor.execute(select nombre from proyectos where id_grupo = 7;)
titulo_stopMotion = "StopMotion"

#MOSTRAR EN PANTALLA__________________________________________________________________________________________________
titulo_stopMotion_mostrar = fuente.render(titulo_stopMotion, 0, negro)
#titulo_chicas_mostrar = fuente.render(titulo_chicas, 0, negro)
#titulo_megaman_mostrar = fuente.render(titulo_megaman, 0, negro)
#titulo_mario_mostrar = fuente.render(titulo_mario, 0, negro)
#titulo_maquinaEnigma_mostrar = fuente.render(titulo_maquinaEnigma, 0, negro)
#titulo_scorpion_mostrar = fuente.render(titulo_scorpion, 0, negro)
#titulo_juli_mostrar = fuente.render(titulo_juli, 0, negro)

#descripcion de los proshectos__________________________________________________________________________________________________
#descripcion_stopMotion = cursor.execute(select descripcion from proyectos where id_grupo = 1;)
#descripcion_chicas = cursor.execute(select descripcion from proyectos where id_grupo = 2;)
#descripcion_megaman = cursor.executeselect descripcion from proyectos where id_grupo = 3;)
#descripcion_mario = cursor.execute(select descripcion from proyectos where id_grupo = 4;)
#descripcion_maquinaEnigma = cursor.execute(select descripcion from proyectos where id_grupo = 5;)
#descripcion_scorpion = cursor.execute(select descripcion from proyectos where id_grupo = 6;)
#descripcion_juli = cursor.execute(select descripcion from proyectos where id_grupo = 7;)

#fotos de los proyectos__________________________________________________________________________________________________
#fotos_StopMotion = cursor.execute(select imagen from imagen where id_grupo = 1;)
#fotos_chicas = cursor.execute(select imagen from imagen where id_grupo = 2;)
#fotos_megaman = cursor.executeselect imagen from imagen where id_grupo = 3;)
#fotos_mario = cursor.execute(select imagen from imagen where id_grupo = 4;)
#fotos_maquinaEnigma = cursor.execute(select imagen from imagen where id_grupo = 5;)
#fotos_scorpion = cursor.execute(select imagen from imagen where id_grupo = 6;)
#fotos_juli = cursor.execute(select imagen from imagen where id_grupo = 7;)

#descripcion de la foto__________________________________________________________________________________________________
#descripcion_fotos_StopMotion = cursor.execute(select descripcion from imagen where id_grupo = 1;)
#descripcion_fotos_chicas = cursor.execute(select descripcion from imagen where id_grupo = 2;)
#descripcion_fotos_megaman = cursor.executeselect descripcion from imagen where id_grupo = 3;)
#descripcion_fotos_mario = cursor.execute(select descripcion from imagen where id_grupo = 4;)
#descripcion_fotos_maquinaEnigma = cursor.execute(select descripcion from imagen where id_grupo = 5;)
#descripcion_fotos_scorpion = cursor.execute(select descripcion from imagen where id_grupo = 6;)
#descripcion_fotos_juli = cursor.execute(select descripcion from imagen where id_grupo = 7;)

#foto de cada grupo__________________________________________________________________________________________________
#foto_principal_stopMotion =  cursor.execute(select imagen from integrante where id_grupo = 1;)
#foto_principal_chicas = cursor.execute(select imagen from integrante where id_grupo = 2;)
#foto_principal_megaman = cursor.executeselect imagen from integrante where id_grupo = 3;)
#fotos_principal_mario = cursor.execute(select imagen from integrante where id_grupo = 4;)
#fotos_principal_maquinaEnigma = cursor.execute(select imagen from integrante where id_grupo = 5;)
#fotos_principal_scorpion = cursor.execute(select imagen from integrante where id_grupo = 6;)
#fotos_principal_juli = cursor.execute(select imagen from integrante where id_grupo = 7;)


#CARGADO DE IMAGENES PRINCIPALES________________________________________________________________________________________
#imagen_principal_stopMotion = pygame.image.load(foto_principal_stopMotion)
#imagen_principal_chicas = pygame.image.load(foto_principal_chicas)
#imagen_principal_megaman = pygame.image.load(foto_principal_megaman)
#imagen_principal_mario = pygame.image.load(foto_principal_mario)
#imagen_principal_maquinaEnigma = pygame.image.load(foto_principal_maquinaEnigma)
#imagen_principal_scorpion = pygame.image.load(foto_principal_scorpion)
#imagen_principal_juli = pygame.image.load(foto_principal_juli)

#CARGADO DE IMAGENES____________________________________________________________________________________________________
#imagen = fotos_StopMotion.split(",")
#lista_imagen_stopMotion.append(pygame.image.load(imagen[0]))
#lista_imagen_stopMotion.append(pygame.image.load(imagen[1]))
#lista_imagen_stopMotion.append(pygame.image.load(imagen[2]))
#lista_imagen_stopMotion.append(pygame.image.load(imagen[3]))
#lista_imagen_stopMotion.append(pygame.image.load(imagen[4]))

#imagen = fotos_chicas.split(",")
#lista_imagen_chicas.append(pygame.image.load(imagen[0]))
#lista_imagen_chicas.append(pygame.image.load(imagen[1]))
#lista_imagen_chicas.append(pygame.image.load(imagen[2]))
#lista_imagen_chicas.append(pygame.image.load(imagen[3]))
#lista_imagen_chicas.append(pygame.image.load(imagen[4]))

#imagen = fotos_megaman.split(",")
#lista_imagen_megaman.append(pygame.image.load(imagen[0]))
#lista_imagen_megaman.append(pygame.image.load(imagen[1]))
#lista_imagen_megaman.append(pygame.image.load(imagen[2]))
#lista_imagen_megaman.append(pygame.image.load(imagen[3]))
#lista_imagen_megaman.append(pygame.image.load(imagen[4]))

#imagen = fotos_mario.split(",")
#lista_imagen_mario.append(pygame.image.load(imagen[0]))
#lista_imagen_mario.append(pygame.image.load(imagen[1]))
#lista_imagen_mario.append(pygame.image.load(imagen[2]))
#lista_imagen_mario.append(pygame.image.load(imagen[3]))
#lista_imagen_mario.append(pygame.image.load(imagen[4]))

#imagen = fotos_maquinaEnigma.split(",")
#lista_imagen_maquinaEnigma.append(pygame.image.load(imagen[0]))
#lista_imagen_maquinaEnigma.append(pygame.image.load(imagen[1]))
#lista_imagen_maquinaEnigma.append(pygame.image.load(imagen[2]))
#lista_imagen_maquinaEnigma.append(pygame.image.load(imagen[3]))
#lista_imagen_maquinaEnigma.append(pygame.image.load(imagen[4]))

#imagen = fotos_scorpion.split(",")
#lista_imagen_scorpion.append(pygame.image.load(imagen[0]))
#lista_imagen_scorpion.append(pygame.image.load(imagen[1]))
#lista_imagen_scorpion.append(pygame.image.load(imagen[2]))
#lista_imagen_scorpion.append(pygame.image.load(imagen[3]))
#lista_imagen_scorpion.append(pygame.image.load(imagen[4]))

#imagen = fotos_juli.split(",")
#lista_imagen_juli.append(pygame.image.load(imagen[0]))
#lista_imagen_juli.append(pygame.image.load(imagen[1]))
#lista_imagen_juli.append(pygame.image.load(imagen[2]))
#lista_imagen_juli.append(pygame.image.load(imagen[3]))
#lista_imagen_juli.append(pygame.image.load(imagen[4]))







#Proyectos bool__________________________________________________________________________________________________
proyecto_stopMotion = False
proyecto_chicas = False
proyecto_megaman = False
proyecto_mario = False
proyecto_maquinaEnigma = False
proyecto_scorpion = False
proyecto_pong = False

#esto es un bool!!
fin = False

#loop principal_________________________________________________________________________________________________________
while fin != True:
    #recorrido de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                proyecto_stopMotion = True
    clock.tick(fps)

    if proyecto_stopMotion:

        #superficie_titulo.blit(texto_Titulo_stopMotion)

        #color de las superficies
        superficie_titulo.fill(blanco)
        superficie_titulo.blit(titulo_stopMotion_mostrar, (200, 300))

        superficie_descripcion.fill(rojo)

        superficie_estadisticas.fill(azul)

        superficie_fotos.fill(verde)
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


    #colocado de superficies dentro de la pantalla______________________________________________________________________
    pantalla.blit(superficie_titulo,(0,0))
    pantalla.blit(superficie_descripcion, (0, 401))
    pantalla.blit(superficie_estadisticas, (751, 0))
    pantalla.blit(superficie_fotos, (751, 331))

    pygame.display.update()

#database.close()
pygame.quit()