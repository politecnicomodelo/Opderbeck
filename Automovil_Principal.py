#IMPORTANDO CLASES::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from Clases.Automovil_Clases import *

#CREANDO UN NUEVO VEICULO:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
vehiculo1 = CamionetaAutos()

#CREANDO UNA NUEVA EMPRESA::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
empresa1 = Empresa()

#AGREGANDO DATOS A LOS VEICULOS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
vehiculo1.setPatente ("123ASD")
vehiculo1.setRuedas (2)
vehiculo1.setAñoFabricacion ("2016-06-12")
vehiculo1.setDescapotable ("si")

#AGREGANDO LOS VEHICULOS A LA EMPRESA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
empresa1.AgregarAuto (vehiculo1)

#AGREGANDO DATOS A LOS VEICULOS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
vehiculo1.setPatente ("456QWE")
vehiculo1.setRuedas (4)
vehiculo1.setAñoFabricacion ("2016-08-2")
vehiculo1.setCapacidad (40)

#AGREGANDO LOS VEHICULOS A LA EMPRESA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
empresa1.AgregarCamioneta (vehiculo1)





#SETEANDO INTERFAZ DEL USUARIO
datos = ""
opcion = ""
numero = 0
fin = False
while fin != True:
    #SETEANDO MENU::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    print ("::::::::::::::::ELIJA UNA OPCION:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    print ("1)              VER DATOS DE LA EMPRESA")
    print ("2)              INGRESAR DATOS DE UN AUTO")
    print ("3)              INGRESAR DATOS DE UNA CAMIONETA")
    print ("4)              SALIR")

    opcion = int (input (opcion))


    if opcion == 1:
        print ("AUTOS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        for auto in empresa1.lista_autos:
            numero += 1
            print ("Patente del auto", numero, ":", vehiculo1.patente)
            print ("Cantidad de ruedas del auto", numero, " :", vehiculo1.cantidad_ruedas)
            print ("Fecha de fabricacion del auto", numero, ":", vehiculo1.año_fabricacion)
            print ("Descapotable", vehiculo1.descapotable)

        numero = 0
        print ("CAMIONETAS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        for camioneta in empresa1.lista_camionetas:
            numero += 1
            print("Patente de la camioneta", numero, ":", vehiculo1.patente)
            print("Cantidad de ruedas de la camioneta", numero, ":", vehiculo1.cantidad_ruedas)
            print("Fecha de fabricacion de la camioneta", numero, ":", vehiculo1.año_fabricacion)
            print ("La capacidad maxima es ", vehiculo1.capacidad_carga)

    elif opcion == 2 or opcion == 3:
        # INGRESA LA PATENTE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        print("Ingrese el numero de patente que posee el vehiculo ")
        vehiculo1.setPatente (input(datos))

        # INGRESA LA CANTIDAD DE RUEDAS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        print("Ingrese la cantidad de ruedas que posee el veiculo")
        vehiculo1.setRuedas (input(datos))

        # INGRESA EL AÑO DE FABRICACION :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        print("Ingrese el año de fabricacion del veiculo")
        vehiculo1.setAñoFabricacion (input(datos))

        if opcion == 2:
            #INGRESA SI ES DESCAPOTABLE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            print ("Ingrese si el veiculo es descapotable (si o no)")
            vehiculo1.setDescapotable (input(datos))
            empresa1.AgregarAuto (vehiculo1)


        elif opcion == 3:
            #INGRESA CUANTA CARGA SOPORTA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            print ("Ingrese la capacidad que tiene el veiculo")
            vehiculo1.setCapacidad (input(datos))
            empresa1.AgregarCamioneta (vehiculo1)

        elif opcion == 4:
            print ("PCIHI EL QUE LEE")
            fin = True
        else:
            print ("ERROR, EL VEHICULO INGRESADO NO ES CORRECTO...")








