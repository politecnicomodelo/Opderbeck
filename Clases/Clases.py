
class Lugar(object):
    nombre = ""
    codigo = None
    lista_coordenadas = []

    listaContinente = []
    listaLugar = []

    def __init__(self):
        self.lista_coordenadas = []
        self.listaContinente = []
        self.listaLugar = []

    def SetNombre(self, nombre): self.nombre = nombre

    def SetCodigo(self, codigo): self.codigo = codigo

    def SetCoordenadas(self, coordenadas): self.lista_coordenadas = coordenadas

    def AgregarContinente(self, continente):
        for kontinente in self.listaContinente:
            if kontinente.codigo == continente.codigo:
                self.listaLugar.append(continente)

class Continente (Lugar):

    listaContinente = []
    listaPais = []
    poblacionContinente = None

    def __init__(self):
        self.listaContinente = []
        self.listaPais = []

    def CrearContinente (self, nombre, codigo, coordenadas):
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetCoordenadas(coordenadas)

    def AgregarPais (self, pais):
        for paises in self.listaPais:
            if paises.codigo == pais.codigo:
                self.listaContinente.append(pais)

    def ConsultarContinente(self, codigo):
        for kontinente in self.listaContinente:
            if kontinente.codigo == codigo:
                return kontinente

    def SetPoblacionContinente(self, poblacion):
        self.poblacionContinente = poblacion

    def PoblacionContinente(self, codigo):
        for continente in self.listaContinente:
            if continente.codigo == codigo:
                for pais in continente.listaPais:
                    self.poblacionContinente += pais.PoblacionProvincia
        self.SetPoblacionContinente(self.poblacionContinente)

    def ContinenteMayorPoblacion(self):
        max = max(self.listaContinente.poblacionContinente)
        for continente in self.listaContinente:
            if continente.poblacionContinente == max:
                return continente

    def ContinenteMenorPoblacion(self):
        min = min(self.listaContinente.poblacionContinente)
        for continente in self.listaContinente:
            if continente.poblacionContinente == min:
                return continente

    def EliminarContinente(self, codigo):
        for continente in self.listaContinente:
            if continente.codigo == codigo:
                for pais in continente.listaPais:
                    for provincia in pais.listaProvincia:
                        for ciudad in provincia.listaCiudad:
                            for barrio in ciudad.listaBarrio:
                                ciudad.listaBarrio.remove(barrio)
                            provincia.listaCiudad(ciudad)
                        pais.listaProvincia(provincia)
                    continente.listaPais(pais)
                self.listaContinente.remove(continente)

    def ModificarContinente(self, codigo):
        for continente in self.listaContinente:
            continente

class Pais (Lugar):

    listaPais = []
    listaProvincia = []

    poblacionPais = None

    def __init__(self):
        self.listaPais = []
        self.listaProvincia = []

    def CrearPais (self, nombre, codigo, coordenadas):
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetCoordenadas(coordenadas)

    def AgregarProvincia(self, provincia):
        for provinsia in self.listaProvincia:
            if provinsia.codigo == provincia.codigo:
                self.listaPais.append(provincia)

    def ConsultarPais(self, codigo):
        for pais in self.listaPais:
            if pais.codigo == codigo:
                return pais

    def SetPoblacionPais(self, poblacion):
        self.poblacionPais = poblacion

    def PoblacionPais(self, codigo):
        for pais in self.listaPais:
            if pais.codigo == codigo:
                for provincia in pais.listaProvincia:
                    self.poblacionPais += provincia.PoblacionProvincia
        self.SetPoblacionPais(self.poblacionPais)

    def PaisMayorPoblacion(self):
        max = max(self.listaPais.poblacionPais)
        for pais in self.listaPais:
            if pais.poblacionPais == max:
                return pais

    def PaisMenorPoblacion(self):
        min = min(self.listaPais.poblacionPais)
        for pais in self.listaPais:
            if pais.poblacionPais == min:
                return pais

    def EliminarPais(self, codigo):
        for pais in self.listaPais:
            if pais.codigo == codigo:
                for provincia in pais.listaProvincia:
                    for ciudad in provincia.listaCiudad:
                        for barrio in ciudad.listaBarrio:
                            ciudad.listaBarrio.remove(barrio)
                        provincia.listaCiudad(ciudad)
                    pais.listaProvincia(provincia)
                self.listaPais.remove(pais)

class Provincia (Lugar):

    listaProvincia = []
    listaCiudad = []
    poblacionProvincia = None

    def __init__(self):
        self.listaProvincia = []
        self.listaCiudad = []

    def CrearProvincia(self, nombre, codigo, coordenadas):
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetCoordenadas(coordenadas)

    def AgregarCiudad(self, ciudad):
        for siudad in self.listaCiudad:
            if siudad.codigo == ciudad.codigo:
                self.listaCiudad.append(ciudad)

    def ConsultarProvincia(self, codigo):
        for provincia in self.listaProvincia:
            if provincia.codigo == codigo:
                return provincia

    def SetPoblacionProvincia(self, poblacion):
        self.poblacionProvincia = poblacion

    def PoblacionProvincia(self, codigo):
        for provincia in self.listaProvincia:
            if provincia.codigo == codigo:
                for ciudad in provincia.listaCiudad:
                    self.poblacionProvincia += ciudad.PoblacionCiudad
        self.SetPoblacionProvincia(self.poblacionProvincia)

    def EliminarProvincia(self, codigo):
        for provincia in self.listaProvincia:
            if provincia.codigo == codigo:
                for ciudad in provincia.listaCiudad:
                    for barrio in ciudad.listaBarrio:
                         ciudad.listaBarrio.remove(barrio)
                    provincia.listaCiudad(ciudad)
                self.listaProvincia.remove(provincia)

class Ciudad (Lugar):

    listaCiudad = []
    listaBarrio = []
    poblacionCiudad = None

    def __init__(self):
        self.listaCiudad = []
        self.listaBarrio = []

    def CrearCiudad(self, nombre, codigo, coordenadas):
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetCoordenadas(coordenadas)

    def AgregarBarrio(self, barrio):
        for varrio in self.listaBarrio:
            if varrio.codigo == barrio.codigo:
                self.listaBarrio.append(barrio)

    def ConsultarCiudad(self, codigo):
        for ciudad in self.listaCiudad:
            if ciudad.codigo == codigo:
                return ciudad

    def SetPoblacionCiudad (self, poblacion):
        self.poblacionCiudad = poblacion

    def PoblacionCiudad(self, codigo):
        for ciudad in self.listaCiudad:
            if ciudad.codigo == codigo:
                for barrio in self.listaBarrio:
                    self.poblacionCiudad += barrio.poblacion
        self.SetPoblacionCiudad(self.poblacionCiudad)

    def EliminarCiudad(self, codigo):
        for ciudad in self.listaCiudad:
            if ciudad.codigo == codigo:
                for barrio in ciudad.listaBarrio:
                    ciudad.listaBarrio.remove(barrio)
                self.listaCiudad.remove(ciudad)

class Barrio (Lugar):
    listaBarrio = []
    listaCiudad = []
    poblacion = None

    def __init__(self):
        self.listaBarrio = []
        self.listaCiudad = []

    def SetPoblacion(self, poblacion):
        self.poblacion = poblacion

    def AgregarBarrio(self, codigo, barrio):
        for ciudad in self.listaCiudad:
            if ciudad.codigo == codigo:
                ciudad.AgregarBarrio(barrio)

    def CrearBarrio(self, nombre, codigo, coordenadas):
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetCoordenadas(coordenadas)
1
    #def ConsultarBarrio (self, codigo):
        #for barrio in self.listaBarrio:
            #if barrio.codigo == codigo:
                #return barrio

    #def ConsultarPoblacion(self, codigo):
        #for barrio in self.listaBarrio:
            #if barrio.codigo == codigo:
                #return barrio.poblacion

    #def EliminarBarrio(self, codigo):
        #for barrio in self.listaBarrio:
            #if barrio.codigo == codigo:
                #barrio.listaBarrio.remove(barrio)