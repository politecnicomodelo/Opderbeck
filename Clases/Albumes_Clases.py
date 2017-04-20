class Albumes_Totales (object):
    album = []
    artistas_album = []

    def __init__(self):
        album = []
        artistas_album = []

    def agregar_Album (self, album):
        self.album.append (album)

    def autores_Totales (self, nombre):
        for item in self.album:
            if nombre == item.setTitulo_Album:
                for item2 in self.album.canciones:
                    for item3 in self.album.canciones.artistas:
                        if item3 not in artistas_album:
                            self.artistas_album.append (self.album.canciones.artistas.nombre)
        return self.artistas_album




class Albumes (object):
    titulo = ""
    canciones = []
    maximo = 0
    cant = 0

    def __init__(self):
        canciones = []

    def setTitulo_Album (self, titulo):
        self.titulo = str(titulo)

    def agregar_Cancion (self, cancion):
        self.canciones.append (cancion)

    def mas_Influyente (self):
        for item in canciones2.artistas.personas.nombre:
            for item2 in self.canciones.artistas.nombre:
                if item == item2:
                    maximo += 1
            if self.maximo > self.cant:
                self.cant = self.maximo
        for item in self.canciones.artistas.nombre:
            for item2 in self.canciones.artistas.nombre:
                if item == item2:
                    self.maximo += 1
            if self.maximo == self.cant:
                return item



class Canciones (object):
    titulo = ""
    artistas = []
    autores = []

    def __init__(self):
        artistas = []
        autores = []

    def setTitulo_Cancion (self, titulo):
        self.titulo = str(titulo)

    def agregar_Artistas(self, artistas):
        self.artistas.append(artistas)

    def agregar_Autores(self, autores):
        self.autores.append(autores)




class Personas (object):
    nombre = ""
    apellido = ""

    def setNombre (self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str (apellido)

