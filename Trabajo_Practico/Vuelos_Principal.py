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
            if lista[4] not in lista_pasajeros:
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
            if lista[4] not in lista_tripulantes:
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
                if item2.DNI == item:
                    vuelo.setPasajeros (item2)
        listaaux = lista [5].split(",")
        for item in listaaux:
            for item2 in lista_tripulantes:
                if int (item2.DNI) == int(item):
                    vuelo.setTripulantes(item2)
        # if item [-1] == '\n':
        #   item [-1] = ""
        vuelo.CodigoVuelo(lista[7])
        lista_vuelos.append (vuelo)
    archivo.close ()
########################################################################################################################

def PasajerosEspeciales ():
    listavip = []
    lista = []
    for item in lista_vuelos:
        for item2 in lista_pasajeros:
            if item2 not in item.lista_pasajeros:
                if item2.pasajero_vip != 0:
                    if item2.necesidades_especiales != None:
                        #print ("NECESIDAD: ", item2.necesidades_especiales)
                        listavip.append (item2.necesidades_especiales)
                    #print("PASAJERO VIP: ", item2.DNI)
                    listavip.append(item2.DNI)
                else :
                    if item2.necesidades_especiales != None:
                        #print ("NECESIDAD: ", item2.necesidades_especiales)
                        lista.append (item2.necesidades_especiales)
                    #print ("PASAJERO: ", item2.DNI)
                    lista.append (item2.DNI)
    return lista, listavip#hay dos listas el vip y el normal con cada lista tambien estan las nececidades de cada persona
########################################################################################################################

def TripulacionNoAutorizada ():
    lista = []
    for vuelo in lista_vuelos:
        #print ("VUELO:", vuelo.codigo_vuelo)
        lista.append (vuelo.codigo_vuelo)
        for tripulante in lista_tripulantes:
            if tripulante.DNI not in vuelo.lista_tripulantes:
                if vuelo.avion not in tripulante.modelo_permitido:
                    #print ("TRIPULANTE", tripulante.DNI)
                    lista.append(tripulante.DNI)
    print (lista)
    return lista#devuelve el codigo del vuelo y los tripulantes no autorizados
########################################################################################################################

def TripulacionRompeRegla ():
    lista = []
    for vuelo1 in lista_vuelos:
        for vuelo2 in lista_vuelos:
            if vuelo1.fecha == vuelo2.fecha:
                if vuelo1.codigo_vuelo != vuelo2.codigo_vuelo:
                    for tripulante1 in vuelo1.lista_tripulantes:
                        for tripulante2 in vuelo2.lista_tripulantes:
                            if tripulante1.DNI == tripulante2.DNI:
                                if tripulante1.DNI not in lista:
                                    lista.append(tripulante1.DNI)

        #print("VUELO:", vuelo1.codigo_vuelo)
        #for item in lista:
            #print ("TRIPULANTE: ", item)
    return lista #devuelve los tripulantes que vuelan dos veces en el mismo dia
########################################################################################################################

def PasajeroMasJoven():
    listaaux = []
    for pasajero in lista_vuelos:
        lista = []
        for pasajero2 in pasajero.lista_pasajeros:
            edad = pasajero2.CalcularEdad()
            lista.append(edad)
        listaaux.append(min(lista))
    return listaaux#te devuelve las edades minimas de cada vuelo
########################################################################################################################

def VuelosSinTripulantes():
    lista = []
    for item in lista_vuelos:
        for item2 in lista_aviones:
            if item.avion == item2.modelo:
                if int (item2.cant_tripulacion) > item.VuelosSinTripulacion():
                    lista.append(item.codigo_vuelo)
    return lista#devuelve los vuelos en los cuales no hay tripulacion suficiente(codigo vuelo)
########################################################################################################################

def NominaPersonas ():
    lista = []
    for vuelo in lista_vuelos:
        lista.append(vuelo.codigo_vuelo)
        for pasajero in vuelo.lista_pasajeros:
            lista.append(pasajero.DNI)
    return lista
########################################################################################################################

########################################################################################################################
def MostrarTodoHermoso ():
    codigos = ""
    lista_dni = ""
    lista_cabecera = []
    lista = NominaPersonas()
    #print ("{: >10} {: >10} {: >10}".format(*))
########################################################################################################################
    print("###########################################################################################################")
    print ("mostrar nomina de los pasajeros por vuelo")
#mostrar nomina de los pasajeros por vuelo
    lista_cabecera.append("CODIGO VUELO")
    lista_cabecera.append("DNI ")
    print("{: >5} {: >12}".format(*lista_cabecera))
    for vuelo in lista_vuelos:
        lista_dni = ""
        for pasajero in vuelo.lista_pasajeros:
            codigos = vuelo.codigo_vuelo
            lista_dni = pasajero.DNI
            print("{: >5} {: >20}".format(*codigos, lista_dni))

########################################################################################################################
    print ("###########################################################################################################")
    print ("mostar el pasajeros jovenes")
#mostar el pasajeros jovenes
    lista_cabecera = []
    lista_dni = []
    lista_cabecera.append ("CODIGO VUELO")
    lista_cabecera.append ("EDADES")
    #lista_cabecera.append ("DNI")
    print ("{: >5} {: >10}".format(*lista_cabecera))
    lista = PasajeroMasJoven()
    for item in lista_vuelos:
        for item2 in item.lista_pasajeros:
            edad = item2.CalcularEdad()
            for item3 in lista:
                if edad == item3:
                    lista_dni.append (item2.DNI)
    for item in lista_vuelos:
        for lista2 in lista:
            for lista_dni2 in lista_dni:
                lista_Todo = [item.codigo_vuelo, lista2]
        print("{: >6} {: >13}".format(*lista_Todo))

########################################################################################################################
    print("###########################################################################################################")
    print ("mostra pasajeros especiales")
#mostrat pasajeros especiales
    novip = []
    vip = []
    novip, vip = PasajerosEspeciales()
    lista = VuelosSinTripulantes()

    lista_cabecera = []
    lista_cabecera.append("PASAJERO VIP")
    lista_cabecera.append("NECESIDAD")
    print("{: >5}, {: >15}".format(*lista_cabecera))
    #for item in vip:
        #if item != '\n':
            #print("{: >5} {: >15}".format(*))
    lista_cabecera = []
    lista_cabecera.append("PASAJERO NO VIP")
    lista_cabecera.append("NECESIDAD")
    print("{: >5}, {: >15}".format(*lista_cabecera))
    #for item in novip:
        #if item != '\n':
            #print("{: >5}, {: >15}".format(*item))
########################################################################################################################
    print ("###########################################################################################################")
    print ("mostrar tripulacion insuficiente")
#mostrar tripulacion insuficiente
    lista_cabecera = []
    lista = VuelosSinTripulantes()
    lista_cabecera.append("CODIGO VUELO")
    print("{: >5}".format(*lista_cabecera))
    for item in lista:
        print ("{: >5}".format(*item))

########################################################################################################################

#mostrar tripulacion que no esta autorizada a volar
    print("###########################################################################################################")
    print("mostrar tripulacion que no esta autorizada a volar")
    lista = TripulacionNoAutorizada()
    codigos = []
    for item in lista_vuelos:
        codigos.append(item.codigo_vuelo)
    lista_cabecera = []
    lista_cabecera.append("CODIGO VUELO")
    lista_cabecera.append("TRIPULANTES")
    print("{: >5} {: >15}".format(*lista_cabecera))
    for item in lista:
        if item not in codigos:
            print("{: >25}".format(item))
        else:
            print(":::::{: >0}:::::::::::::::::::".format(item))
########################################################################################################################
    print("###########################################################################################################")
    print ("#mostrar tripulacion que rompe las reglas")
#mostrar tripulacion que rompe las reglas
    lista_cabecera = []
    lista = TripulacionRompeRegla()
    lista_cabecera.append("TRIPULANTE")
    print("{: >5} ".format(*lista_cabecera))

    for item in lista:
        print(" {: >5}".format(item))


########################################################################################################################

RecuperarDatos ()

NominaPersonas()

PasajeroMasJoven()

PasajerosEspeciales ()

TripulacionNoAutorizada ()

TripulacionRompeRegla ()

MostrarTodoHermoso()
########################################################################################################################