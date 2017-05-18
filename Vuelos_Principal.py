from Clases.Vuelos_Clases import *

tripulantes = []
pasajeros = []
aviones = []
vuelos = []

def RecuperarDatos ():
    lista = []

    archivo = open("personas.dat", "r+")
    for line in archivo:
        lista.append(line.split("|"))
        if lista [0] == "Pasajero":
            pasajero = Pasajero ()
            pasajero.setNombre (lista [1])
            pasajero.setApellido (lista [2])
            pasajero.setFechaNacimiento (lista [3])
            pasajero.setDni (lista [4])
            pasajero.setPasajeroVip (lista [5])
            if lista [6] != "":
                pasajero.setNecesidadEspecial (lista [6])
            pasajeros.append (pasajero)
        else:
            tripulacion = Tripulacion()
            tripulacion.setNombre (lista [1])
            tripulacion.setApellido (lista [2])
            tripulacion.setFechaNacimiento (lista [3])
            tripulacion.setDni (lista [4])
            tripulacion.setModeloPermitido (lista [5])
            if lista[0] == "Servicio":
                tripulacion.setIdiomas (lista [6])
            tripulantes.append (tripulacion)
    archivo.close ()

    archivo = open("aviones.dat", "r+")
    for line in archivo:
        lista.append(line.split("|"))
        avion = Aviones()
        avion.setModeloAvion (lista [0])
        avion.setCantidadPasajeros (lista [1])
        avion.setCantidadTripulacion (lista [2])
        aviones.append (avion)
    archivo.close ()

    archivo = open("vuelos.dat", "r+")
    for line in archivo:
        lista.append(line.split("|"))
        vuelo = Vuelos()
        vuelo.setAvion (lista [0])
        vuelo.FechaSalida (lista [1])
        vuelo.HoraSalida (lista [2])
        vuelo.Origen (lista [3])
        vuelo.Destino (lista [4])
        vuelo.setPasajeros (lista [5])
        vuelo.setTripulantes (lista [6])
        vuelos.append (vuelo)
    archivo.close ()