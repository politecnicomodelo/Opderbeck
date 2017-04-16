class Empleado (object):
    nombre = ""
    apellido = ""
    telefono = 0
    asistencia_mes_dia = [[],[]]
    mes = ""
    dia = 0


    def __init__(self):
        asistencia_dia = []

    def setNombre (self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str(apellido)

    def setTelefono (self, telefono):
        self.telefono = str(telefono)

    def setAsistenciaDia (self,mes,dia):
        for item in range(mes):
            for item2 in range(dia):
                self.asistencia_mes_dia.append(mes, dia)



class Empresa (object):
    asistencia_dias = 0
    asistencia_total = 0
    def __init__(self):
        lista_empleados = []

    def Ingresar_Empleado (self, empleado):
        self.lista_empleados.append(empleado)

    def existeEmpleado (self, nombre):
        for self.lista_empleados in range:
            if self.nombre == self.lista_empledos:
                return True
        return False

    def diasTrabajados (self, mes):
        for item in range:
            for item2 in range:
                if asistencia_mes_dia[item][none]== mes:
                    self.Asistencia_dias += asistencia_mes_dia[none][item2]
                    for item3 in range (self.asistencia_dias):
                        if self.asistencia_dias[item] == 1:
                            asistencia_total += 1
        return asistencia_total
