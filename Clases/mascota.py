class Mascota (object):
    nombre = ""
    tipo = ""

    def setNombre(self , n):
        self.Nombre = str(n)

    def setTipo (self , t):
        self.Tipo = str(t)

    def quienSoy (self):
        return "soy " + self.Nombre + " un " + self.Tipo

