from Clases.Bufes_Clases import *

opcion = ""
opcion1 = ""

dato = ""
dato1 = ""
dato2 = ""
dato3 = ""
dato4 = ""
dato5 = ""
dato6 = ""
precio = 0
lista = []

alumno = Alumno ()
profesor = Profesor ()
plato = Plato ()
pedido = Pedido ()
buffet = Buffet ()

def GuardarPersona (alumno = None, profesor = None):
    if profesor != None:
        archivo = open ("profesor.txt", "a")
        for item in buffet.profesores:
            archivo.write (item.nombre + "|" + item.apellido + "|" + item.descuento +'\n')
        archivo.close ()
    if alumno != None:
        archivo = open ("alumno.txt", "a")
        for item in buffet.alumnos:
            archivo.write (item.nombre + "|" + item.apellido + "|" + item.division + '\n')
        archivo.close ()

def GuardarPlato ():
    archivo = open ("plato.txt", "a")
    for item in buffet.platos:
        archivo.write (item.nombre + "|" + item.precio + '\n')
    archivo.close ()

def GuardarPedido ():
    archivo = open ("pedido.txt", "a")
    for item in buffet.pedidos:
        archivo.write (item.nombre + "|" + item.fecha_creacion+ "|" + item.fecha_entrega + "|" + item.entregado + "|" + item.platos+ "|" + item.persona +'\n')
    archivo.close ()

def GuardarTodo ():
    GuardarPedido ()
    GuardarPlato ()
    GuardarPersona (alumno = 1, profesor = 1)

def RecuperarDatos ():
    archivo3 = open("pedido.txt", "r")
    for line in archivo3:
        pedido = Pedido()
        lista = line.split("|")
        pedido.setCreacion(lista[1])
        pedido.setEntrega(lista[2])
        pedido.Entregado(lista[3])
        pedido.Plato(lista[4])
        pedido.Persona(lista[5])
        pedido.Pedido(lista[0])
        buffet.AgregarPedido(pedido)
    archivo3.close()

    archivo2 = open("plato.txt", "r")
    for line in archivo2:
        plato = Plato()
        lista = line.split("|")
        plato.setPlatoNombre(lista[0])
        plato.setPlatoPrecio(lista[1])
        buffet.AgregarPlato(plato)
    archivo2.close()

    archivo1 = open("alumno.txt", "r")
    for line in archivo1:
        alumno = Alumno()
        lista = line.split("|")
        alumno.setDivision(lista[2])
        alumno.setNombre(lista[0])
        alumno.setApellido(lista[1])
        buffet.AgregarAlumno(alumno)
    archivo1.close()

    archivo = open("profesor.txt", "r")
    for line in archivo:
        profesor = Profesor()
        lista = line.split("|")
        profesor.setDescuento(lista[2])
        profesor.setNombre(lista[0])
        profesor.setApellido(lista[1])
        buffet.AgregarProfesor(profesor)
    archivo.close()


# eliminar alumno y profesor platos y pedidos
# agregar alumno y profesor platos y pedidos
# modificar alumno y profesor platos y pedidos
while True:
#:::::::::::::::::::::::::::::::::::::::::::::::MENU::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    print ("::::::::::::::::::MENU:::::::::::::::::::::::::::::::")
    print (":::::::::::::INGRESA UNA OPCION::::::::::::::::::::::")
    print ("A)...........................................Agregar ")
    print ("B)..........................................Eliminar ")
    print ("C).........................................Modificar ")
    print ("D)...........................................Mostrar ")
    print ("E)..................................Lista de pedidos ")
    print ("F)...........................................Guardar ")
    print ("G)...................................Recuperar datos ")

    opcion = input ("OPCION: ")

    if opcion == "e" or opcion == "E":
        print("INGRESE LA FECHA DE LOS PEDIDOS DEL DIA: ")
        dato = input("FECHA: ")
        buffet.PlatosDelDia(dato)
        for item in buffet.platosdia:
            for item3 in plato:
                if item.plato == item3.nombre:
                    precio = plato.precio

            for item2 in item.persona:
                if item2 == profesor.nombre:
                     precio -= profesor.descuento*100/precio
                if item2 == alumno.nombre:
                    precio = precio

            print ("PLATO:", item.plato)
            print ("NOMBRE:", item.persona)
            print ("PRECIO:", precio)

    if opcion == "g" or opcion == "G":
        RecuperarDatos()

    else:
        print (":::::::::::::INGRESA UNA OPCION::::::::::::::::::::::")
        print ("A)..........................................Profesor ")
        print ("B).............................................Plato ")
        print ("C)............................................Pedido ")
        print ("D)............................................Alumno ")

        opcion1 = input ("OPCION: ")

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    if opcion == "a" and opcion1 == "a":
        profesor = Profesor()
        print ("INGRESE EL DESCUENTO DEL PROFESOR: ")
        dato = input ("DESCUENTO: ")
        profesor.setDescuento (dato)
        print ("INGRESE EL NOMBRE DE LA PERSONA: ")
        dato = input ("NOMBRE: ")
        profesor.setNombre (dato)
        print ("INGRESE EL APELLIDO DE LA PERSONA: ")
        dato = input ("APELLIDO: ")
        profesor.setApellido (dato)
        buffet.AgregarProfesor (profesor)

    elif opcion == "a" and opcion1 == "b":
        plato = Plato()
        print ("INGRESE EL NOMBRE DEL PLATO: ")
        dato = input ("NOMBRE: ")
        plato.setPlatoNombre (dato)
        print ("INGRESE EL PRECIO DEL PLATO: ")
        dato = input ("PRECIO: ")
        plato.setPlatoPrecio (dato)
        buffet.AgregarPlato (plato)

    elif opcion == "a" and opcion1 == "c":
        pedido = Pedido ()
        print ("INGRESE EL NOMBRE DEL PEDIDO: ")
        dato = input ("NOMBRE: ")
        pedido.Pedido (dato)
        print ("INGRESE LA FECHA DE CREACION: ")
        dato = input ("CREACION: ")
        pedido.setCreacion (dato)
        print ("INGRESE LA FECHA DE ENTREGA: ")
        dato = input ("ENTREGA: ")
        pedido.setEntrega (dato)
        print ("INGRESE SI EL PEDIDO YA FUE ENTREGADO(1) O NO(0): ")
        dato = input ("ENTREGADO: ")
        pedido.Entregado (dato)
        print ("INGRESE EL NOMBRE DEL PLATO: ")
        dato = input ("PLATO: ")
        pedido.Plato (dato)
        print ("INGRESE EL NOMBRE DE LA PERSONA: ")
        dato = input ("PERSONA: ")
        pedido.Persona (dato)
        buffet.AgregarPedido (pedido)

    elif opcion == "a" and opcion1 == "d":
        alumno = Alumno()
        print("INGRESE LA DIVISION DEL ALUMNO: ")
        dato = input("DIVISION: ")
        alumno.setDivision(dato)
        print("INGRESE EL NOMBRE DE LA PERSONA: ")
        dato = input("NOMBRE: ")
        alumno.setNombre(dato)
        print("INGRESE EL APELLIDO DE LA PERSONA: ")
        alumno.setApellido(input("APELLIDO: "))
        buffet.AgregarAlumno(alumno)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    elif opcion == "b" and opcion1 == "a":
        print ("INGRESE EL NOMBRE DEL PROFESOR QUE DESEA ELIMINAR:")
        dato = input ("PROFESOR: ")
        buffet.EliminarProfesor (dato)

    elif opcion == "b" and opcion1 == "b":
        print ("INGRESE EL NOMBRE DEL PLATO QUE DESEA ELIMINAR:")
        dato = input("PLATO: ")
        buffet.EliminarPlato (dato)

    elif opcion == "b" and opcion1 == "c":
        print("INGRESE EL NOMBRE DEL PEDIDO QUE DESEA ELIMINAR:")
        dato = input("PEDIDO: ")
        buffet.EliminarPedido(dato)

    elif opcion == "b" and opcion1 == "d":
        print("INGRESE EL NOMBRE DEL ALUMNO QUE DESEA ELIMINAR:")
        dato = input("ALUMNO: ")
        buffet.EliminarAlumno(dato)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    elif opcion == "c" and opcion1 == "a":
        print ("INGRESE EL NOMBRE DEL PROFESOR QUE DESEA MODIFICAR:")
        dato = input ("PROFESOR: ")

        print("INGRESE EL NUEVO NOMBRE DE LA PERSONA: ")
        dato1 = input("NOMBRE: ")

        print("INGRESE EL NUEVO APELLIDO DE LA PERSONA: ")
        dato2 = input ("APELLIDO: ")

        print("INGRESE EL NEUVO DESCUENTO DEL PROFESOR: ")
        dato3 = input ("DESCUENTO: ")

        buffet.ModificarProfesor(dato, dato1, dato2, dato3)

    elif opcion == "c" and opcion1 == "b":
        print ("INGRESE EL NOMBRE DEL PLATO QUE DESEA CAMBIAR: ")
        dato = input ("PLATO: ")

        print ("INGRESE EL NUEVO NOMBRE DEL PLATO: ")
        dato1 = input ("NOMBRE: ")

        print ("INGRESE EL NUEVO PRECIO DEL PLATO: ")
        dato2 = input ("PRECIO: ")

        buffet.ModificarPlato (dato, dato1, dato2)

    elif opcion == "c" and opcion1 == "c":
        print ("INGRESE EL NOMBRE DEL PEDIDO QUE DESEA MODIFICAR:")
        dato = input("PEDIDO: ")

        print ("INGRESE LA NUEVA FECHA DE CREACION: ")
        dato1 = input ("CREACION: ")

        print ("INGRESE LA NUEVA FECHA DE ENTREGA: ")
        dato2 = input ("ENTREGA: ")

        print ("INGRESE SI EL NUEVO PEDIDO YA FUE ENTREGADO O NO: ")
        dato3 = input ("ENTREGADO: ")

        print ("INGRESE EL NUEVO NOMBRE DEL PLATO: ")
        dato6 = input ()

        print ("INGRESE EL NUEVO NOMBRE DE LA PERSONA: ")
        dato5 = input ("PLATO:")

        print("INGRESE SI ESA PERSONA ES ALUMNO(1) O PROFESOR(0): ")
        dato4 = input("PERSONA")

        buffet.AgregarPedido (dato, dato6, dato5, dato4, dato3, dato2, dato1)

    elif opcion == "c" and opcion1 == "d":
        print("INGRESE EL NOMBRE DEL ALUMNO QUE DESEA MODIFICAR:")
        dato = input("ALUMNO: ")

        print("INGRESE EL NUEVO NOMBRE DE LA PERSONA: ")
        dato1 = input("NOMBRE: ")

        print("INGRESE EL NUEVO APELLIDO DE LA PERSONA: ")
        dato2 = input("APELLIDO: ")

        print("INGRESE EL NEUVO DESCUENTO DEL PROFESOR: ")
        dato3 = input("DESCUENTO: ")
        buffet.ModificarAlumno(dato, dato1, dato2, dato3)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    elif opcion == "d" and opcion1 == "a":
        for item in buffet.profesores:
            print ("PROFESOR: ", item.nombre)

    elif opcion == "d" and opcion1 == "b":
        for item in buffet.platos:
            print ("PLATO:", item.nombre)

    elif opcion == "d" and opcion1 == "c":
        for item in buffet.pedidos:
            print ("PEDIDO:", item.nombre)

    elif opcion == "d" and opcion1 == "d":
        for item in buffet.alumnos:
            print("ALUMNO: ", item.nombre)

    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    elif opcion == "f" and opcion1 == "a":
        GuardarPersona (profesor = 1)

    elif opcion == "f" and opcion1 == "b":
        GuardarPlato ()

    elif opcion == "f" and opcion1 == "c":
        GuardarPedido ()

    elif opcion == "f" and opcion1 == "d":
        GuardarPersona (alumno = 1)

    elif opcion == "f" and opcion1 == "e":
        GuardarTodo ()






