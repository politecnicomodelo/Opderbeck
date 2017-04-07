class Empleado (object):
    nombre = ""
    apellido = ""
    telefono = 0
    asistencia = []

    def setNombre (self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str(apellido)

    def setTelefono (self, telefono):
        self.telefono = str(telefono)

    def setAsitencia (self, asistencia):
        self.asistencia = str(asistencia)


class Empresa (object):

    def __init__(self):
        lista_empleados = []

    def Ingresar_Empleado (self, empleado):
        self.lista_empleados.append(empleado)

