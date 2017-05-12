class Persona(Registro):
    nombre = ""
    apellido = ""
    fecha_nac = None
    registro = []

    pesopromedio = 0
    alturapromedio = 0
    contador = 0
    pesototal = 0
    alturatotal = 0
    añomod = None        #el año siguiente al peido

    altura_año = []     #se utilizan para calcular el altura de un año a otro
    porcentaje = 0


    def __init__(self):
        registro = []
        altura_año = []

    def setNombre (self, nombre):
        self.nombre = str(nombre)

    def setApellido (self, apellido):
        self.apellido = str(apellido)

    def setFecha_nac (self, fecha_nac):
        self.fecha_nac = fecha_nac

    def Resgistro (self, registro):
        self.registro.append (registro)

    def Consultar (self, fecha):
        for item in self.registro:
            if item == fecha:
                return item.peso, item.altura

    def promedioPesoAltura (self, año):
        self.añomod = año + "1.0.0"     #le suma 1 año 0 meses y 0 dias para saber cuando seria el año siguiente
        self.fecha_registro.sort()  # ordena los registros de menor a mayor en base a la fecha de registros

        for item in self.registro:
            if item > self.añomod:
                break
            self.pesototal += item.peso         #peso total
            self.alturatotal += item.altura     #altura total
            self.contador += 1              #cantidad de veces que el usuario ingrteso un registro

        self.pesopromedio = self.pesototal / self.contador            #peso total dividido por la cantidad de registros que tomo dentro de la fecha indicada
        self.alturapromedio = self.alturatotal / self.contador        #altura total dividido por la cantidad de registros que tomo dentro de la fecha indicada
        return self.pesopromedio, self.alturatotal




    def promedioAltura(self, año1, año2):           # ultimo eje
        self.fecha_registro.sort()

        for item in self.registro:              #comprueba que las fechas que dio el usuario esten en la lista de registros
            if item == año1:
                for item2 in self.registro:
                    if item2 == año2:
                        break       #si encontro los dos años continua con el programa
                return False        #sino devuelve false y termina el programa

        for item in self.registro:
            if año1 < año2:
                if item == año2:
                    self.altura_año[2] = item.altura #si el año 1 era mas chico guarda la altura mas grande(año mas reciente) en la segunda posicion de la lista
                if item == año1:
                    self.altura_año[1] = item.altura #
            else :
                if item == año2:
                    self.altura_año[1] = item.altura #siempre guarda la altura mas grande(el año mas reciente) en la ultima posicion
                if item == año1:
                    self.altura_año[2] = item.altura


        self.porcentaje = (self.altura_año[2]*100)/self.altura_año[1] #regla de 3 para calcular el porcentaje de crecimiento
        return self.porcentaje



class Registro (object):
    peso = 0
    altura = 0
    fecha_registro = None


    def setPeso (self, peso):
        self.peso = peso

    def setAltura (self, altura):
        self.altura = altura

    def fechaRegistro (self, fecha_registro):
        self.fecha_registro = fecha_registro
