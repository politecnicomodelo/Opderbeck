from .ejercitacion2163 import Materia

class Alumno (object):
    nombre = ""
    apellido = ""
    fecha_nacimiento = None
    materias = []

    def __init__(self):
        self.materias

    def setNombre(self, a):
        self.nombre = str(a)

    def setApellido (self , b):
        self.apellido = str (b)

    def setNacimiento (self , c):
        self.nacimiento = c

    def setMenor (self):
        return min(self.notas)

    def setMayor (self):
        return max(self.notas)

    def seMateria (self , n):
        (self.materias).append(n)

    def setPromedioMateria (self , k):
        suma = 0
        for item in Materia:
            suma += Materia.setPromedio_nota()
        return suma/len (self.materias)

    def setMaximoProm (self):
        return max (materias.setPromedio_nota())# porque en materias en el principal tenes que igualar a la clase

    def setMinimoProm (self):
        return min (materias.setPromedio_nota())




