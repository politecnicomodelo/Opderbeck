from Clases_Trabajo_Practico.Vuelos_Clases import *

tripulantes = []
pasajeros = []
aviones = []
vuelos = []

pasajero = Pasajero ()
tripulacion = Tripulacion()
avion = Aviones()
vuelo = Vuelos()


def RecuperarDatos ():

    archivo = open("personas.dat", "r")
    for line in archivo:
        lista = line.split("|")
        if lista [0] == 'Pasajero':
            pasajero = Pasajero ()
            pasajero.setNombre (lista [1])
            pasajero.setApellido (lista [2])
            pasajero.setFechaNacimiento (lista [3])
            pasajero.setDni (lista [4])
            pasajero.setPasajeroVip (lista [5])
            listaaux = lista[6]
            #if lista [6] == '\n' or listaaux [-1] == '\n':
             #   listaaux [-1] = ' '
            pasajero.setNecesidadEspecial (listaaux)
            pasajeros.append (pasajero)
        else:
            tripulacion = Tripulacion()
            tripulacion.setNombre(lista[1])
            tripulacion.setApellido (lista [2])
            tripulacion.setFechaNacimiento (lista [3])
            tripulacion.setDni (lista [4])
            listaaux = lista[5].split(",")
            for item in listaaux:
                #if item == '\n' or item[-1] == '\n':
                 #   item[-1] = ""
                tripulacion.setModeloPermitido (item)
            if lista[0] == 'Servicio':
                listaaux = lista[6]
                #if listaaux == '\n' or listaaux[-1] == '\n':
                 #    listaaux[-1] = ""
                tripulacion.setIdiomas (listaaux)
            tripulantes.append (tripulacion)
    archivo.close ()

    archivo = open("aviones.dat", "r")
    for line in archivo:

        lista = line.split("|")
        avion = Aviones()
        avion.setModeloAvion (lista [0])
        avion.setCantidadPasajeros (lista [1])
        avion.setCantidadTripulacion (lista [2])
        aviones.append (avion)
    archivo.close ()

    archivo = open("vuelos.dat", "r")
    for line in archivo:
        lista = line.split("|")
        vuelo = Vuelos()
        vuelo.setAvion (lista [0])
        vuelo.FechaSalida (lista [1])
        vuelo.HoraSalida (lista [2])
        vuelo.Origen (lista [3])
        vuelo.Destino (lista [4])
        listaaux = lista [5].split(",")
        for item in listaaux:
            for item2 in pasajeros:
                if item2.DNI == item:
                    vuelo.setPasajeros (item2)
        listaaux = lista [6].split(",")
        for item in listaaux:
            for item2 in tripulantes:
                if item2.DNI == item:
                    vuelo.setTripulantes (item2)
        # if item [-1] == '\n':
        #   item [-1] = ""
        vuelo.CodigoVuelo(lista [7])
        vuelos.append (vuelo)
    archivo.close ()


def NominaPersonas ():
    for item in vuelos:
        print ("VUELO", item.codigo_vuelo)
        for item2 in item.pasajeros:
            print ("PASAJERO", item2)

def PasajeroMasJoven ():
    for vuelo in vuelos:
        lista = []
        for persona in vuelo.pasajeros:
            lista.append(persona.CalcularEdad())
        print(min(lista))

def VuelosSinTripulacion ():
    for item in vuelos:
        for item2 in item.avion:
            if item2.cant_tripulacion > len(item.tripulantes):
                print ("vuelo ", item.codigo_vuelo)

def PasajerosEspeciales ():
    for item in vuelos:
        for item2 in item.pasajeros:
            if item2.necesidades_especiales != None:
                if item2.pasajero_vip != 0:
                    print("PASAJERO VIP: ", item2.DNI)
                else :
                    print ("PASAJERO: ", item2.DNI)
                print ("NECESIDAD: ", item2.necesidades_especiales)
            elif item2.pasajero_vip != 0:
                print("PASAJERO VIP: ", item2.DNI)

def TripulacionNoAutorizada ():
    for item in vuelos:
        print ("VUELO:", item.codigo_vuelo)
        for item2 in item.tripulantes:
            if item2.modelo_permitido not in item.avion:
                print ("TRIPULANTE", item2.DNI)

def TripulacionRompeRegla ():
    lista = []
    for item in vuelos:
        for item2 in vuelos:
            if item.fecha == item2.fecha:
                for item3 in item.tripulantes:
                    for item4 in item2.tripulantes:
                        if item3.DNI == item4.DNI:
                            lista.append(item3.DNI)
    print (lista)

RecuperarDatos ()
#NominaPersonas ()
PasajeroMasJoven ()
#VuelosSinTripulacion ()
#TripulacionNoAutorizada ()
#TripulacionRompeRegla ()
