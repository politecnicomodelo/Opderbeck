#IMPORTANDO CLASES::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from Clases.Automovil_Clases import *

#CREANDO UN NUEVO VEICULO:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
vehiculo1 = Autos()
vehiculo2 = Camioneta()

#CREANDO UNA NUEVA EMPRESA::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
empresa1 = Empresa()

#AGREGANDO DATOS A LOS VEICULOS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
vehiculo1.setPatente ("123ASD")
vehiculo1.setRuedas (2)
vehiculo1.setAñoFabricacion ("2016-06-12")
vehiculo1.setDescapotable ("si")

vehiculo2.setPatente ("456QWE")
vehiculo2.setRuedas (4)
vehiculo2.setAñoFabricacion ("2016-08-2")
vehiculo2.setCapacidad (40)

#INGRESANDO VEHICULOS A LA EMPRESA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
empresa1.AgregarAuto (vehiculo1)
empresa1.AgregarCamioneta (vehiculo2)



#SETEANDO INTERFAZ DEL USUARIO
cantidad_vehiculos = ""
numero = 0
datos = ""
lista_vehiculos = []

print("Ingrese la cantidad de vehiculos que tiene su empresa: ")
cantidad_vehiculos = input(cantidad_vehiculos)

for vehiculos in range(int(cantidad_vehiculos)):
    numero += 1
    #INGRESA LA PATENTE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    print ("Ingrese el numero de patente que posee el vehiculo ", numero)
    lista_vehiculos.append (input(datos))
    #INGRESA LA CANTIDAD DE RUEDAS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    print ("Ingrese la cantidad de ruedas que posee el veiculo", numero)
    lista_vehiculos.append (input(datos))
    #INGRESA EL AÑO DE FABRICACION :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    print ("Ingrese el año de fabricacion del veiculo", numero)
    lista_vehiculos.append(input(datos))
    #INGRESA SI ES UN AUTO O CAMIONETA::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    print ("Ingrese si el vehiculo", numero, "es auto o camioneta")
    lista_vehiculos.append (input(datos))
    datos = lista_vehiculos[-1]
    if datos == "auto":#SI EL VEHICULO ES UN AUTO INGRESA SI ES DESCAPOTABLE O NO
        #INGRESA SI ES DESCAPOTABLE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        datos = ""
        print ("Ingrese si el veiculo", numero, "es descapotable (si o no)")
        lista_vehiculos.append (input(datos))
    else:                                 #SINO , ES CAMIONETA E INGRESA CUANTA CARGA SOPORTA EL VEHICULO
        #INGRESA CUANTA CARGA SOPORTA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        datos = ""
        print ("Ingrese la capacidad que tiene el veiculo", numero)
        lista_vehiculos.append (input(datos))





