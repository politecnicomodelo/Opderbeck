class Empleado (object):
    nombre = ""
    apellido = ""
    telefono = 0
    asistencia_dia = []


    def __init__(self):
        asistencia_dia = []

    def setNombre (self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str(apellido)

    def setTelefono (self, telefono):
        self.telefono = str(telefono)

    def setAsistenciaDia (self, mes_dia):
        self.asistencia_dia.append(mes_dia)



class Empresa (object):
    asistencia_total = 0
    dias = 0
    item2 = 0
    def __init__(self):
        lista_empleados = []

    def Ingresar_Empleado (self, empleado):
        self.lista_empleados.append(empleado)

    def existeEmpleado (self, nombre):
        for empleado in self.lista_empleados:
            if nombre == empleado:
                return True
        return False

    def diasTrabajados (self, mes, nombre):
        existeEmpleado(nombre)
        if existeEmpleado(nombre) == true:
            for item in asistencia_dia:
                self.item2 += 1
                if item == mes:
                    self.dias = asitencia_dia [self.item2+1]
                    for numero in self.dias[0:5]:
                        asistencia_total += numero

        return asistencia_total


    #def diasTrabajados (self, mes):
     #   for item in range:
      #      for item2 in range:
       #         if asistencia_mes_dia[item][none]== mes:
    #             self.Asistencia_dias += asistencia_mes_dia[none][item2]
    #                for item3 in range (self.asistencia_dias):
     #                   if self.asistencia_dias[item] == 1:
      #                      asistencia_total += 1
       # return asistencia_total
