from Clases_Trabajo_Practico.Vuelos_Clases import *
from datetime import datetime, date, time, timedelta
import calendar

lista_tripulantes = []
lista_pasajeros = []
lista_aviones = []
lista_vuelos = []

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
            lista_pasajeros.append (pasajero)
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
                listaaux = lista[6].split(",")
                for item in listaaux:
                    tripulacion.setIdiomas (listaaux)
            lista_tripulantes.append (tripulacion)
    archivo.close ()

    archivo = open("aviones.dat", "r")
    for line in archivo:

        lista = line.split("|")
        avion = Aviones()
        avion.setModeloAvion (lista [0])
        avion.setCantidadPasajeros (lista [1])
        avion.setCantidadTripulacion (lista [2])
        lista_aviones.append (avion)
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
        listaaux = lista [6].split(",")
        for item in listaaux:
            for item2 in lista_pasajeros:
                if item2.DNI == int(item):
                    vuelo.setPasajeros (item2)
        listaaux = lista [5].split(",")
        for item in listaaux:
            for item2 in lista_tripulantes:
                if int (item2.DNI) == int(item):
                    vuelo.setTripulantes(item2)
        # if item [-1] == '\n':
        #   item [-1] = ""
        vuelo.CodigoVuelo(lista [7])
        lista_vuelos.append (vuelo)
    archivo.close ()


def PasajerosEspeciales ():
    listavip = []
    lista = []
    for item in lista_vuelos:
        for item2 in lista_pasajeros:
            if item2 not in item.lista_pasajeros:
                if item2.pasajero_vip != 0:
                    if item2.necesidades_especiales != None:
                        print ("NECESIDAD: ", item2.necesidades_especiales)
                        listavip.append (item2.necesidades_especiales)
                    print("PASAJERO VIP: ", item2.DNI)
                    listavip.append(item2.DNI)
                else :
                    if item2.necesidades_especiales != None:
                        print ("NECESIDAD: ", item2.necesidades_especiales)
                        lista.append (item2.necesidades_especiales)
                    print ("PASAJERO: ", item2.DNI)
                    lista.append (item2.DNI)


def TripulacionNoAutorizada ():
    lista = []
    for vuelo in lista_vuelos:
        print ("VUELO:", vuelo.codigo_vuelo)
        lista.append (vuelo.codigo_vuelo)
        for tripulante in lista_tripulantes:
            if tripulante.DNI not in vuelo.lista_tripulantes:
                if vuelo.avion not in tripulante.modelo_permitido:
                    print ("TRIPULANTE", tripulante.DNI)
                    lista.append(tripulante.DNI)

def TripulacionRompeRegla ():

    for vuelo1 in lista_vuelos:
        lista = []
        for vuelo2 in lista_vuelos:
            if vuelo1.fecha == vuelo2.fecha:
                if vuelo1.codigo_vuelo != vuelo2.codigo_vuelo:
                    for tripulante1 in vuelo1.lista_tripulantes:
                        for tripulante2 in vuelo2.lista_tripulantes:
                            if tripulante1.DNI == tripulante2.DNI:
                                if tripulante1.DNI not in lista:
                                    lista.append(tripulante1.DNI)

        print("VUELO:", vuelo1.codigo_vuelo)
        for item in lista:
            print ("TRIPULANTE: ", item)

RecuperarDatos ()



#vuelo.PasajeroMasJoven()
vuelo.NominaPersonas()

for item in lista_vuelos:

    for item2 in lista_aviones:
        if item.avion == item2.modelo:
            if int (item2.cant_tripulacion) < item.VuelosSinTripulacion ():
                break

#PasajerosEspeciales ()
#TripulacionNoAutorizada ()
#TripulacionRompeRegla ()
