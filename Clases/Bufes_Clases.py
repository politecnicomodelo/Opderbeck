class Persona(object):
    nombre = ""
    apellido = ""

    def setNombre(self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str(apellido)

    def setDescuento (self, descuento):
        self.descuento = descuento


class Profesor(Persona):
    descuento = 0

    def setDescuento (self, descuento):
        self.descuento = descuento


class Alumno(Persona):
    division = ""

    def setDivision (self, division):
        self.division = division


class Plato (object):
    nombre = ""
    precio = 0

    def setPlatoNombre(self, nombre):
        self.nombre = nombre

    def setPlatoPrecio(self, precio):
        self.precio = precio


class Pedido (object):
    fecha_creacion = ""
    fecha_entrega = ""
    entregado = 0
    platos = ""
    persona = ""
    nombre = ""

    def setCreacion (self, fecha_creacion):
        self.fecha_creacion = fecha_creacion

    def setEntrega (self, fecha_entrega):
        self.fecha_entrega = fecha_entrega

    def Entregado (self, entregado):
        self.entregado = entregado

    def Plato (self, platos):
        self.platos = platos

    def Persona (self, persona):
        self.persona = persona

    def Pedido(self, nombre):
         self.nombre = str(nombre)


class Buffet (object):
    #eliminar alumno y profesor platos y pedidos
    #agregar alumno y profesor platos y pedidos
    #modificar alumno y profesor platos y pedidos
    alumnos = []
    profesores = []
    platos = []
    pedidos = []
    platosdia = []

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self):
        self.alumnos = []
        self.profesores = []
        self.platos = []
        self.pedidos = []
        self.platosdia = []

    def AgregarAlumno (self, alumno):
        self.alumnos.append(alumno)

    def EliminarAlumno (self, alumno):
        for item in self.alumnos:
            if item.nombre == alumno:
                self.alumnos.remove(alumno)

    def ModificarAlumno (self, alumno, nombre, apellido, division):
        for item in self.alumnos.nombre:
            if item == alumno:
                self.alumnos.nombre = nombre
                self.alumnos.apellido = apellido
                self.alumnos.division = division

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def AgregarProfesor(self, profesor):
        self.profesores.append(profesor)

    def EliminarProfesor(self, profesor):
        for item in self.profesores:
            if item.nombre == profesor:
                 self.profesores.remove(profesor)

    def ModificarProfesor (self, profesor, nombre, apellido, descuento):
        for item in self.profesores:
            if item.nombre == profesor:
                self.profesores.nombre = nombre
                self.profesores.apellido = apellido
                self.profesores.descuento = descuento
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def AgregarPlato(self, plato):
        self.platos.append(plato)

    def EliminarPlato(self, plato):
        for item in self.platos:
           if item.nombre == plato:
                self.platos.remove(plato)

    def ModificarPlato (self, plato, nombre, precio):
        for item in self.platos:
            if item.nombre == plato:
                self.platos.nombre = nombre
                self.platos.precio = precio

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def AgregarPedido(self, plato):
        self.pedidos.append(plato)

    def EliminarPedido(self, pedido):
        for item in self.pedidos:
            if item.nombre == pedido:
                self.pedidos.remove(pedido)

    def ModificarPedido(self, pedido, plato, persona, profesor = 0,  entregado = None, hora_entrega = None, fecha_creacion = None):
        for item in self.pedidos:
            if pedido not in item.nombre:
                return False

        for item in self.platos:
            if plato not in item.nombre:
                return False

        if profesor != 0:
            for item in self.profesores:
                 if persona not in item.nombre:
                    return False
        else:
            for item in self.alumnos:
                if persona not in item.nombre:
                    return False

        self.pedidos.entregado = entregado
        self.pedidos.fecha_entrega = hora_entrega
        self.pedidos.fecha_creacion = fecha_creacion

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def PlatosDelDia(self, fecha):
        for item in self.pedidos:
            if fecha == item.fecha_entrega:
                if item.entregado == 0:
                    self.platosdia.append (self.pedidos)
        return self.platosdia
