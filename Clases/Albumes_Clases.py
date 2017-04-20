class Albumes (object):
    titulo = ""
    canciones = []

    def __init__(self):
        canciones = []

    def setTitulo_Album (self, titulo):
        self.titulo = str(titulo)

    def agregar_Cancion (self, cancion):
        self.canciones.append (cancion)




class Canciones (object):
    titulo = ""
    artitas = []
    autores = []

    def setTitulo_Cancion (self, titulo):
        self.titulo = str(titulo)

    def agregar_Artistas(self, artistas):
        self.artitas.append(artistas)

    def agregar_Autores(self, autores):
        self.autores.append(autores)


class Personas (object):
    nombre = ""
    apellido = ''
