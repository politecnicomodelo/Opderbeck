

class Empresa (object):
    lista_autos = []
    lista_camionetas = []

    def __init__(self):
        listas_autos = []
        lista_camionetas =  []

    def agregarAuto (self, auto):
        self.lista_autos.append (auto)

    def agregarCamioneta (self, camioneta):
        self.lista_camionetas.append (camioneta)


class Veiculo (object):
    patente = ""
    ruedas = 0
    año_fabricacion = None

    def setPatente (self, patente):
        self.patente = patente

    def setRuedas (self, ruedas):
        self.ruedas = ruedas

    def setAñoFabricacion (self, año):
        self.año_fabricacion = año


class Auto (veiculo):
    descapotable = ""

    def setDescapotable (self, sino):
        self.descapotable = str(sino)


class Camioneta (veiculo):
    capacidad = 0

    def setCapacidad (self, carga):
        self.capacidad = carga
