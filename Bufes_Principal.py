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

alumno = Alumno ()
profesor = Profesor ()
plato = Plato ()
pedido = Pedido ()
buffet = Buffet ()


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
    print ("D)...........................................Mostrar")
    print ("E)..................................Lista de pedidos")

    opcion = input ()

    if opcion == "e" or opcion == "E":
        print("INGRESE LA FECHA DE LOS PEDIDOS DEL DIA: ")
        dato = input()
        buffet.PlatosDelDia(dato)
        for item in buffet.platosdia:
            for item3 in item.plato:
                if item3 == plato.nombre:
                     precio = plato.precio
            for item2 in item.persona:
                if item2 == profesor.nombre:
                     precio -= profesor.descuento*100/precio
                if item2 == alumno.nombre:
                    precio = precio

            print ("PLATO:", item.plato)
            print ("NOMBRE:", item.nombre)
            print ("PRECIO:", precio)

    else:
        print (":::::::::::::INGRESA UNA OPCION::::::::::::::::::::::")
        print ("A)..........................................Profesor ")
        print ("B).............................................Plato ")
        print ("C)............................................Pedido ")
        print ("D)............................................Alumno ")

        opcion1 = input ()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    if opcion == "a" and opcion1 == "a":
        profesor = Profesor()
        print ("INGRESE EL DESCUENTO DEL PROFESOR: ")
        dato = input ()
        profesor.setDescuento (dato)
        print ("INGRESE EL NOMBRE DE LA PERSONA: ")
        dato = input ()
        profesor.setNombre (dato)
        print ("INGRESE EL APELLIDO DE LA PERSONA: ")
        dato = input ()
        profesor.setApellido (dato)
        buffet.AgregarProfesor (profesor)

    elif opcion == "a" and opcion1 == "b":
        print ("INGRESE EL NOMBRE DEL PLATO: ")
        dato = input ()
        plato.setPlatoNombre (dato)
        print ("INGRESE EL PRECIO DEL PLATO: ")
        dato = input ()
        plato.setPlatoPrecio (dato)
        buffet.AgregarPlato (plato)

    elif opcion == "a" and opcion1 == "c":
        print ("INGRESE LA FECHA DE CREACION: ")
        dato = input ()
        pedido.setCreacion (dato)
        print ("INGRESE LA FECHA DE ENTREGA: ")
        dato = input ()
        pedido.setEntrega (dato)
        print ("INGRESE SI EL PEDIDO YA FUE ENTREGADO(1) O NO(0): ")
        dato = input ()
        pedido.Entregado (dato)
        print ("INGRESE EL NOMBRE DEL PLATO: ")
        dato = input ()
        pedido.Plato (dato)
        print ("INGRESE EL NOMBRE DE LA PERSONA: ")
        dato = input ()
        pedido.Persona (dato)
        buffet.AgregarPedido (pedido)

    elif opcion == "a" and opcion1 == "d":
        alumno = Alumno()
        print("INGRESE LA DIVISION DEL ALUMNO: ")
        dato = input()
        alumno.setDivision(dato)
        print("INGRESE EL NOMBRE DE LA PERSONA: ")
        dato = input()
        alumno.setNombre(dato)
        print("INGRESE EL APELLIDO DE LA PERSONA: ")
        alumno.setApellido(input())
        buffet.AgregarAlumno(alumno)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    elif opcion == "b" and opcion1 == "a":
        print ("INGRESE EL NOMBRE DEL PROFESOR QUE DESEA ELIMINAR:")
        dato = input ()
        buffet.EliminarProfesor (dato)

    elif opcion == "b" and opcion1 == "b":
        print ("INGRESE EL NOMBRE DEL PLATO QUE DESEA ELIMINAR:")
        dato = input()
        buffet.EliminarPlato (dato)

    elif opcion == "b" and opcion1 == "c":
        print("INGRESE EL NOMBRE DEL PEDIDO QUE DESEA ELIMINAR:")
        dato = input()
        buffet.EliminarPedido(dato)

    elif opcion == "b" and opcion1 == "d":
        print("INGRESE EL NOMBRE DEL ALUMNO QUE DESEA ELIMINAR:")
        dato = input()
        buffet.EliminarAlumno(dato)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    elif opcion == "c" and opcion1 == "a":
        print ("INGRESE EL NOMBRE DEL PROFESOR QUE DESEA MODIFICAR:")
        dato = input ()

        print("INGRESE EL NUEVO NOMBRE DE LA PERSONA: ")
        dato1 = input()

        print("INGRESE EL NUEVO APELLIDO DE LA PERSONA: ")
        dato2 = input ()

        print("INGRESE EL NEUVO DESCUENTO DEL PROFESOR: ")
        dato3 = input ()

        buffet.ModificarProfesor(dato, dato1, dato2, dato3)

    elif opcion == "c" and opcion1 == "b":
        print ("INGRESE EL NOMBRE DEL PLATO QUE DESEA CAMBIAR: ")
        dato = input ()

        print ("INGRESE EL NUEVO NOMBRE DEL PLATO: ")
        dato1 = input ()

        print ("INGRESE EL NUEVO PRECIO DEL PLATO: ")
        dato2 = input ()

        buffet.ModificarPlato (dato, dato1, dato2)

    elif opcion == "c" and opcion1 == "c":
        print ("INGRESE EL NOMBRE DEL PEDIDO QUE DESEA MODIFICAR:")
        dato = input()

        print ("INGRESE LA NUEVA FECHA DE CREACION: ")
        dato1 = input ()

        print ("INGRESE LA NUEVA FECHA DE ENTREGA: ")
        dato2 = input ()

        print ("INGRESE SI EL NUEVO PEDIDO YA FUE ENTREGADO O NO: ")
        dato3 = input ()

        print ("INGRESE EL NUEVO NOMBRE DEL PLATO: ")
        dato6 = input ()

        print ("INGRESE EL NUEVO NOMBRE DE LA PERSONA: ")
        dato5 = input ()

        print("INGRESE SI ESA PERSONA ES ALUMNO(1) O PROFESOR(0): ")
        dato4 = input()

        buffet.AgregarPedido (dato, dato6, dato5, dato4, dato3, dato2, dato1)

    elif opcion == "c" and opcion1 == "d":
        print("INGRESE EL NOMBRE DEL ALUMNO QUE DESEA MODIFICAR:")
        dato = input()

        print("INGRESE EL NUEVO NOMBRE DE LA PERSONA: ")
        dato1 = input()

        print("INGRESE EL NUEVO APELLIDO DE LA PERSONA: ")
        dato2 = input()

        print("INGRESE EL NEUVO DESCUENTO DEL PROFESOR: ")
        dato3 = input()
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





















































