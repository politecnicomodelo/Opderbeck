class Materia (object):
    nombre = ""
    lista_notas = []


    def setNombre (self , a):
        self.nombre = str (a)

    def setNotas (self , b):
        (self.lista_notas).append(b)

    def setPromedio_nota(self):
        return sum(self.lista_notas)/len(self.lista_notas)

