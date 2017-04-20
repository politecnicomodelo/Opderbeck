from Clases.Albumes_Clases import *



#CREANDO PERSONAS::::::::::::::::::::::::::::::::::::
persona1 = Personas()
persona2 = Personas()

#CREANDO CANCIONES
cancion1 = Canciones()
cancion2 = Canciones()

#CREANDO ALBUM:::::::::::::::::::::::::::::::::::::::
album = Albumes()

#CREANDO DISCO:::::::::::::::::::::::::::::::::::::::
disco = Albumes_Totales()

#CARGANDO DATOS DE PERSONAS::::::::::::::::::::::::::
persona1.setNombre("Nico")
persona1.setApellido("Prusci")

persona2.setNombre("juan")
persona2.setApellido("Peron")


#CARGANDO DATOS DE CANCIONES:::::::::::::::::::::::::
cancion1.setTitulo_Cancion("ASD")
cancion1.agregar_Artistas(persona1)
cancion1.agregar_Autores(persona2)

cancion2.setTitulo_Cancion("QWERTY")
cancion2.agregar_Artistas(persona2)
cancion2.agregar_Autores(persona1)

#CARGANDO DATOS DE ALBUM:::::::::::::::::::::::::::::
album.setTitulo_Album ("QSY")
album.agregar_Cancion (cancion1)
album.agregar_Cancion (cancion2)
#album.mas_Influyente ()

#CONSULTANDO ALBUM:::::::::::::::::::::::::::::::::::
disco.agregar_Album (album)
disco.autores_Totales ("QSY")


