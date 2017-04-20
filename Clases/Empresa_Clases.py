class Empleado (object):
    nombre = ""
    apellido = ""
    telefono = 0
    asistencia_dia = []
    asistencia_total = 0
    item2 = 0
    dias = ""
    def __init__(self):
        asistencia_dia = []

    def setNombre (self, nombre):
        self.nombre = str(nombre)          #guarda su nombre

    def setApellido (self, apellido):
        self.apellido = str(apellido)      #guarda su apellido

    def setTelefono (self, telefono):
        self.telefono = str(telefono)      #guarda su telefono

    def setAsistenciaDia (self, mes_dia):
        self.asistencia_dia.append(mes_dia) #guarda en la lista asistencia_dia el mes y los dias que fue en esa semana

    def dias_Trabajados (self, mes, nombre):
        #existe_Empleado (self.nombre)
        #if existe_Empleado (self.nombre) == True:  #pregunta si el empleado existe
        for item in self.asistencia_dia:     #si lo encontro recorre la lista de asistencia(donde se guarda los dias y meses que asiste)
            self.item2 += 1             #item2 se utiliza para saber la posicion en la que estas
            if item == self.mes:
                self.dias = asistencia_dia [self.item2+1]
                for item3 in self.dias [0:5]:
                    self.asistencia_total += int(item3)
        return self.asistencia_total


class Empresa (object):

    lista_empleados = []

    def __init__(self):
        lista_empleados = []

    def ingresar_Empleado (self, empleado):
        self.lista_empleados.append(empleado)   #agrega un empleado a la lista de empleados

    def existe_Empleado (self, nombre):
        for empleado in self.lista_empleados:    #recorre la lista de empleados
            if nombre == empleado.nombre:        #pregunta si el nombre pedido es un empleado
                return True                      #si lo encontro devuelve true sino false
        return False

    #def diasTrabajados (self, mes):
     #   for item in range:
      #      for item2 in range:
       #         if asistencia_mes_dia[item][none]== mes:
    #             self.Asistencia_dias += asistencia_mes_dia[none][item2]
    #                for item3 in range (self.asistencia_dias):
     #                   if self.asistencia_dias[item] == 1:
      #                      asistencia_total += 1
       # return asistencia_total
