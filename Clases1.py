class Lugar(object):
    nombre = None
    codigo = None
    lista = []
    tipo = None

    def __init__(self): self.lista = []

    def SetNombre(self, nombre): self.nombre = nombre

    def SetCodigo(self, codigo): self.codigo = codigo

    def SetTipo(self, tipo): self.tipo = tipo

    def GetPoblacion(self, poblacion):
        for item in self.lista:
            poblacion += item.GetPoblacion()
        return poblacion


    def Agregar(self, lugar): self.lista.append(lugar)

    def Modificar(self, id, nombre = None, tipo = None):
        for item in self.lista:
            if id == item.codigo:
                if nombre != None: item.nombre = nombre
                if tipo != None: item.tipo = tipo
        return item

    def Borrar(self, lugar):
        if lugar.tipo == "continente":
            for item in self.lista:
                if item.codigo == lugar.codigo:
                    for item2 in item.lista:
                        for item3 in item2.lista:
                            for item4 in item3.lista:
                                for item5 in item4.lista:
                                    self.lista.remove(item5)
                                self.lista.remove(item4)
                            self.lista.remove(item3)
                        self.lista.remove(item2)
                    self.lista.remove(item)
        elif lugar.tipo == "pais":
            for item in self.lista:
                if item.codigo == lugar.codigo:
                    for item2 in item.lista:
                        for item3 in item2.lista:
                            for item4 in item3.lista:
                                self.lista.remove(item4)
                            self.lista.remove(item3)
                        self.lista.remove(item2)
                    self.lista.remove(item)
        elif lugar.tipo == "provincia":
            for item in self.lista:
                if item.codigo == lugar.codigo:
                    for item2 in item.lista:
                        for item3 in item2.lista:
                            self.lista.remove(item3)
                        self.lista.remove(item2)
                    self.lista.remove(item)
        elif lugar.tipo == "ciudad":
            for item in self.lista:
                if item.codigo == lugar.codigo:
                    for item2 in item.lista:
                        self.lista.remove(item2)
                    self.lista.remove(item)
        elif lugar.tipo == "barrio":
            self.lista.remove(lugar)


class Barrio(Lugar):
    poblacion = None

    def SetPoblacion (self, poblacion): self.poblacion = poblacion

    def GetPoblacion(self): return self.poblacion

















