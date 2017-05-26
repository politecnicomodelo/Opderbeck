from Clases_Trabajo_Practico.Vuelos_Clases import *
from datetime import datetime, date, time, timedelta
import calendar

tripulantes = []
pasajeros = []
aviones = []
vuelos = []

pasajero = Pasajero ()
tripulacion = Tripulacion()
avion = Aviones()
vuelo = Vuelos()
#print ("{: >10} {: >10} {: >10}".format(*lista_datos))


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
    for vuelo1 in vuelos:
        print("VUELO:", vuelo1.codigo_vuelo)
        for pasajero2 in pasajeros:
            if pasajero2.DNI not in  vuelo1.pasajeros:
                print("PASAJERO", pasajero2.DNI)


def PasajeroMasJoven ():
    for vuelo in vuelos:
        lista = []
        for persona2 in pasajeros:
            if persona2.DNI not in vuelo.pasajeros:
                lista.append(persona2.CalcularEdad())
        print (min(lista))


def VuelosSinTripulacion ():
    numero = 0
    for vuelo in vuelos:
        for avion in aviones:
            if avion.modelo not in vuelo.avion:
                if int(avion.cant_tripulacion) > len(vuelo.tripulantes):
                    print ("VUELO:", vuelo.codigo_vuelo)


def PasajerosEspeciales ():
    for item in vuelos:
        for item2 in pasajeros:
            if item2 not in item.pasajeros:
                if item2.necesidades_especiales != None:
                    if item2.pasajero_vip != 0:
                        print("PASAJERO VIP: ", item2.DNI)
                    else :
                        print ("PASAJERO: ", item2.DNI)
                    print ("NECESIDAD: ", item2.necesidades_especiales)
                elif item2.pasajero_vip != 0:
                    print("PASAJERO VIP: ", item2.DNI)


def TripulacionNoAutorizada ():
    for vuelo in vuelos:
        print ("VUELO:", vuelo.codigo_vuelo)
        for tripulante in tripulantes:
            if tripulante.DNI not in vuelo.tripulantes:
                for modelo in tripulante.modelo_permitido:
                    if vuelo.avion == modelo:
                        print ("TRIPULANTE", tripulante.DNI)


def TripulacionRompeRegla ():

    for vuelo1 in vuelos:
        lista = []
        for vuelo2 in vuelos:
            if vuelo1.fecha == vuelo2.fecha:
                if vuelo1.codigo_vuelo != vuelo2.codigo_vuelo:
                    for tripulante1 in vuelo1.tripulantes:
                        for tripulante2 in vuelo2.tripulantes:
                            if tripulante1.DNI == tripulante2.DNI:
                                lista.append(tripulante1.DNI)

        print("VUELO:", vuelo1.codigo_vuelo)
        for item in lista:
            print ("TRIPULANTE: ", item)



RecuperarDatos ()

#NominaPersonas ()
#PasajeroMasJoven ()
#VuelosSinTripulacion ()
PasajerosEspeciales ()
#TripulacionNoAutorizada ()
#TripulacionRompeRegla ()
