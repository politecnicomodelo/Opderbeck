from Clases.Bufes_Clases import *

opcion = ""
opcion1 = ""
# eliminar alumno y profesor platos y pedidos
# agregar alumno y profesor platos y pedidos
# modificar alumno y profesor platos y pedidos
#:::::::::::::::::::::::::::::::::::::::::::::::MENU::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print("::::::::::::::::::MENU:::::::::::::::::::::::::::::::")
print(":::::::::::::INGRESA UNA OPCION::::::::::::::::::::::")
print("1)...........................................Agregar ")
print("2)..........................................Eliminar ")
print("3).........................................Modificar ")
input (opcion)
print(":::::::::::::INGRESA UNA OPCION::::::::::::::::::::::")
print("1)...........................................Persona ")
print("2).............................................Plato ")
print("3)............................................Pedido ")
input (opcion1)

# print ("1)....................................Agregar Persona")
# print ("2)...................................Eliminar Persona")
# print ("3)..................................Modificar Persona")

# print ("4)......................................Agregar Plato")
# print ("5).....................................Eliminar Plato")
# print ("6)....................................Modificar Plato")

# print ("7).....................................Agregar Pedido")
#  print ("8)....................................ELiminar Pedido")
# print ("9)...................................Modificar pedido")



alumno = Alumno ()
profesor = Profesor ()
plato = Plato ()
pedido = Pedido ()
buffet = Buffet ()

dato = ""


if opcion == 1 and opcion1 == 1:
    print ("INGRESE SI LA PERSONA ES ALUMNO O PROFESOR: ")
    input (dato)
    if dato == "profesor" or dato == "PROFESOR":
        print ("INGRESE EL DESCUENTO DEL PROFESOR: ")
        input (dato)
        profesor.setDescuento (dato)
        print ("INGRESE EL NOMBRE DE LA PERSONA: ")
        input (dato)
        profesor.setNombre (dato)
        print ("INGRESE EL APELLIDO DE LA PERSONA: ")
        input (dato)
        profesor.setApellido (dato)
        buffet.AgregarProfesor (profesor)

    elif dato == "alumno" or dato == "ALUMNO":
        print ("INGRESE LA DIVISION DEL ALUMNO: ")
        input (dato)
        alumno.setDivision (dato)
        print ("INGRESE EL NOMBRE DE LA PERSONA: ")
        input (dato)
        alumno.setNombre (dato)
        print ("INGRESE EL APELLIDO DE LA PERSONA: ")
        input (dato)
        alumno.setApellido (dato)
        buffet.AgregarAlumno (alumno)


elif opcion == 1 and opcion1 == 2:
    print ("INGRESE EL NOMBRE DEL PLATO: ")
    input (dato)
    plato.setPlatoNombre (dato)
    print ("INGRESE EL PRECIO DEL PLATO: ")
    input (dato)
    plato.setPlatoPrecio (dato)
    buffet.AgregarPlato (plato)

elif opcion == 1 and opcion1 == 3:
    print ("INGRESE LA FECHA DE CREACION: ")
    input (dato)
    pedido.setCreacion (dato)
    print ("INGRESE LA FECHA DE ENTREGA: ")
    input (dato)
    pedido.setEntrega (dato)
    print ("INGRESE SI EL PEDIDO YA FUE ENTREGADO O NO: ")
    input (dato)
    pedido.Entregado (dato)
    print ("INGRESE EL NOMBRE DEL PLATO: ")
    input (dato)
    pedido.Plato (dato)
    print ("INGRESE EL NOMBRE DE LA PERSONA: ")
    input (dato)
    pedido.Persona (dato)
    buffet.AgregarPedido (pedido)

elif opcion == 2 and opcion1 == 1:

elif opcion == 2 and opcion1 == 2:

elif opcion == 2 and opcion1 == 3:

elif opcion == 3 and opcion1 == 1:
    dato1 = ""
    dato2 = ""
    dato3 = ""
    print("INGRESE SI LA PERSONA ES ALUMNO O PROFESOR: ")
    input (dato)
    if dato == "profesor" or dato == "PROFESOR":
        print ("INGRESE EL NOMBRE DEL PROFESOR QUE DESEA MODIFICAR:")
        input (dato)
        print("INGRESE EL DESCUENTO DEL PROFESOR: ")
        input(dato3)
        profesor.setDescuento(dato3)
        print("INGRESE EL NOMBRE DE LA PERSONA: ")
        input(dato1)
        profesor.setNombre(dato1)
        print("INGRESE EL APELLIDO DE LA PERSONA: ")
        input(dato2)
        profesor.setApellido(dato2)
        buffet.ModificarProfesor(dato, dato1, dato2, dato3)

    elif dato == "alumno" or dato == "ALUMNO":
        print ("INGRESE EL NOMBRE DEL ALUMNO QUE DESEA MODIFICAR")
        input (dato)
        print("INGRESE LA DIVISION DEL ALUMNO: ")
        input(dato3)
        alumno.setDivision(dato3)
        print("INGRESE EL NOMBRE DE LA PERSONA: ")
        input(dato1)
        alumno.setNombre(dato1)
        print("INGRESE EL APELLIDO DE LA PERSONA: ")
        input(dato2)
        alumno.setApellido(dato2)
        buffet.ModificarAlumno(dato, dato1, dato2, dato3)


elif opcion == 3 and opcion1 == 2:

elif opcion == 3 and opcion1 == 3:

























































