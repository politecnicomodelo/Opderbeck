class Persona(object):
    nombre = ""
    apellido = ""

    def setNombre(self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str(apellido)

    def setDescuento (self, descuento):
        self.descuento = descuento

class Profesores(Persona):
    descuento = 0

    def setDescuento (self, descuento):
        self.descuento = descuento


class Alumno(Persona):
    division = ""

    def setDivision (self, division):
        self.division = division


class Platos (object):
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



class buffet (object):
    #eliminar alumno y profesor platos y pedidos
    #agregar alumno y profesor platos y pedidos
    #modificar alumno y profesor platos y pedidos
    alumnos = []
    profesores = []
    platos = []
    pedidos = []
    platosdia = []

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def AgregarAlumno (self, alumno):
        self.alumnos.append(alumno)

    def EliminarAlumno (self, alumno):
        self.alumnos.remove(alumno)

    def ModificarAlumno (self, alumno, nombre = None, apellido = None, division = None):
        for item in self.alumnos:
            if item == alumno:
                if nombre != None: self.alumnos.nombre = nombre
                if apellido != None: self.alumnos.apellido = apellido
                if division != None: self.alumnos.division = division

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def AgregarProfesor(self, profesor):
        self.profesores.append(profesor)

    def EliminarProfesor(self, profesor):
        self.profesores.remove(profesor)

    def ModificarProfesor (self, profesor, nombre = None, apellido = None, descuento = None):
        for item in self.profesores:
            if item == profesor:
                if nombre != None: self.profesores.nombre = nombre
                if apellido != None: self.profesores.apellido = apellido
                if descuento != None: self.profesores.descuento = descuento
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def AgregarPlato(self, plato):
        self.platos.append(plato)

    def EliminarPlato(self, plato):
        self.platos.remove(plato)

    def ModificarPlato (self, plato, nombre = None, precio = None):
        for item in self.platos:
            if item == plato:
                if nombre != None: self.platos.nombre = nombre
                if precio != None: self.platos.precio = precio

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def AgregarPedido(self, plato):
        self.platos.append(plato)

    def EliminarPedido(self, plato):
        self.platos.remove(plato)

    def ModificarPedido(self, pedido, plato, persona, entregado = None, hora_entrega = None, fecha_creacion = None):
        if pedido not in self.pedidos:
            return False
        if plato not in self.platos:
            return False
        if persona not in self.profesores and persona not in self.profesores:
            return False
        if entregado != None: self.pedidos.entregado = entregado
        if hora_entrega != None: self.pedidos.fecha_entrega = hora_entrega
        if fecha_creacion != None: self.pedidos.fecha_creacion = fecha_creacion

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def PlatosDelDia(self, fecha):
        for item in self.pedidos.fecha_entrega:
            if fecha == item:
                if self.pedidos.entregado == False:
                    self.platosdia.append (self.pedidos)


