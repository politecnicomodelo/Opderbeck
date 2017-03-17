from Clases.ejercitacion163 import Alumno
from datetime import date
from Clases.ejercitacion2163 import Materia


a = Alumno ()
a.setNombre ("chuman")
a.setApellido ("fiori")
a.setNacimiento (date(2017,3,4))
print (a.nombre , a.apellido, a.setMayor, a.setMenor)
mate = Materia()

mate.nombre = "tincho"
mate.setNotas (5)

a.materias.append (mate)
for item in a.materias:
    print (str (item.nombre) , str (item.lista_notas) , str (item.setPromedio_nota()))











