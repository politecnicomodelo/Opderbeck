#:::::::::::::::::CODIGOS DE MESES::::::::::::::::::::::::::::::
#EN...enero          MY...mayo       SE...septiembre
#FE...febrero        JN...junio      OC...octubre
#MZ...marzo         JL...julio      NO...noviembre
#AB...abril         AG...agosto     DI...diciembre
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


#IMPORTANDO CLASES:::::::::::::::::::::::::::::::::::::::::::::
from Clases.Empresa_Clases import *


#CREANDO EMPLEADO::::::::::::::::::::::::::::::::::::::::::::::
empleado1 = Empleado()

#CREANDO EMPRESA:::::::::::::::::::::::::::::::::::::::::::::::
empresa1 = Empresa()

#ASIGNANDO DATOS AL EMPLEADO:::::::::::::::::::::::::::::::::::
empleado1.setNombre ("nico")
empleado1.setApellido ("prusci")
empleado1.setTelefono (1178213792)
empleado1.setAsistenciaDia ("AB")   #abril
empleado1.setAsistenciaDia ("101010") #lunes si  martes no  miercoles si  jueves no  viernes si  sabado no
empleado1.setAsistenciaDia ("AB")   #abril
empleado1.setAsistenciaDia ("011111")

#INGRESANDO EMPLEADO A LA EMPRESA:::::::::::::::::::::::::::::
empresa1.ingresar_Empleado(empleado1)
empresa1.existe_Empleado ("nico")           #devuelve un true o un false (Existe o no existe)
print (empresa1.existe_Empleado ("nico"))   #muestra si existe el empleado


#CONSULTAR DIAS DE INGRESO::::::::::::::::::::::::::::::::::::
empleado1.dias_Trabajados("AB", "nico")         #Dias que trabajo en abril nico
print (empleado1.dias_Trabajados ("AB", "nico")) #muestar el total de dias que trabajo en abril usuario nico

