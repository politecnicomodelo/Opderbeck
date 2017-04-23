class Vehiculo (object):
    patente = ""
    cantidad_ruedas = 0
    año_fabricacion = ""

    def setPatente (self, patente):
        self.patente = patente

    def setRuedas (self, ruedas):
        self.cantidad_ruedas = ruedas

    def setAñoFabricacion (self, año):
        self.año_fabricacion = año


class CamionetaAutos (Vehiculo):
    capacidad_carga = 0
    descapotable = ""

    def setCapacidad (self, carga):
        self.capacidad_carga = carga

    def setDescapotable (self, desc):
        self.descapotable = str(desc)


class Empresa (object):
    lista_autos = []
    lista_camionetas = []

    def __init__(self):
        lista_autos = []
        lista_camionetas = []

    def AgregarCamioneta (self, camioneta):
        self.lista_camionetas.append(camioneta)

    def AgregarAuto (self, auto):
        self.lista_autos.append(auto)











