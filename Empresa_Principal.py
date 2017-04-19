#:::::::::::::::::CODIGOS DE MESES::::::::::::::::::::::::::::::
#EN...enero          MY...mayo       SE...septiembre
#FE...febrero        JN...junio      OC...octubre
#MZ...marzo         JL...julio      NO...noviembre
#AB...abril         AG...agosto     DI...diciembre
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


#IMPORTANDO CLASES:::::::::::::::::::::::::::::::::::::::::::::
from Clases.Empresa_Clases import *


#CREANDO EMPLEADO::::::::::::::::::::::::::::::::::::::::::::::
empleado1= Empleado


#ASIGNANDO DATOS AL EMPLEADO:::::::::::::::::::::::::::::::::::
empleado1.nombre = "Nico"
empleado1.apellido = "Prusci"
empleado1.telefono = 1178213792
empleado1.setAsistenciaDia ("AB")
empleado1.setAsistenciaDia(101010)#Abril lunes si  martes no  miercoles si  jueves no  viernes si  sabado no

#INGRESANDO EMPLEADO A LA EMPRESA:::::::::::::::::::::::::::::
Empresa.Ingresar_Empleado(empleado1)
Empresa.existeEmpleado ("nico")    #devuelve un true o un false (Existe o no existe)
print (Empresa.existeEmpleado ("nico"))

#CONSULTAR DIAS DE INGRESO
Empresa.diasTrabajados (AB)   #Dias que trabajo en abril
print (Empresa.diasTrabajados (AB, "nico")