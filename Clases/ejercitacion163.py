from .ejercitacion2163 import Materia

class Alumno (object):
    nombre = ""
    apellido = ""
    fecha_nacimiento = None
    materias = []

    def __init__(self):
        self.materias = []

    def setNombre(self, nombre):
        self.nombre = str(nombre)

    def setApellido (self , apellido):
        self.apellido = str (apellido)

    def setNacimiento (self , fecha_nacimiento):
        self.nacimiento = fecha_nacimiento

    def setMateria (self , n):
        (self.materias).append(n)

        def Menor(self):
            return min(self.)

        def Mayor(self):
            return max(self.)

    def PromedioMateria (self , k):
        #return [item.promedio() for item in self.materias]       version loca
        suma = 0
        for item in Materia:
            suma += Materia.Promedio_nota()
        return suma/len (self.materias)

    def MaximoProm (self):
        return max([item.promedio() for item in self.materias])

    def MinimoProm (self):
        return min([item.promedio() for item in self.materias])



