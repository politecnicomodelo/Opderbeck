class Torneo (object):
    lista_partidos = []
    lista_equipos = []

    def __init__(self):
        lista_partidos = []
        lista_equipos = []

    def equipos (self, lista_equipos):

        for equipoActual in lista_equipos :
            if equipoActual.nombre == lista_equipos.nombre :
                return False
        self.lista_equipos.append (lista_equipos)

    def partidos (self, lista_partidos):
        self.lista_partidos.append (lista_partidos)


class Jugador (object):
    nombre = ""
    numero = ""
    apellido = ""
    fecha_nacimiento = None

    def setNombre (self, n):
        self.nombre = str(n)

    def setApellido (self , apellido):
        self.apellido = str (apellido)

    def setNumero (self, num):
        self.numero = str(num)

    def setNacimiento (self , fecha_nacimiento):
        self.nacimiento = fecha_nacimiento


class Equipo(object):
    nombre = ""
    disponibilidad = []
    jugadores = []
    barrio = ""
    partidosJugados = []

    def __init__(self):
        self.disponibilidad = []
        self.jugadores = []

    def setNombre (self, nombre):
        self.nombre = str(nombre)

    def a_disponibilidad (self, turno):
        self.disponibilidad.append(turno)

    def Jugadores (self, jugador):
        for jugadorActual in jugadores :
            if jugadorActual.numero == jugador.numero :
                return False
        self.jugadores.append (jugador)

    def setCapitan (self, jugador):
        self.capitan = jugador.numero

    def setBarrio (self, barrio):
        self.barrio = barrio

    def partidoJugado (self):
        self.partidosJugados.append (equiporival)


class Partido (object):

    equipo = []
    turno = ""
    dia = None

    def __init__(self):
        self.equipo = []

    def equipo1 (self, equipo):
        self.equipo.append(equipo)

    def turno (self , turno):
        self.turno = turno

    def dia (self , dia):
        self.dia = dia