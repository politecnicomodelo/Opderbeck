from datetime import date
from Clases.Torneo import *




#TURNOS
TurnoManana = [True, False, False]
TurnoNoche = [False , False , True]
TurnoTarde = [False, True , False]
TurnoMyT = [True, True , False]
TurnoMyN = [True, False , True]
TurnoMTN = [True, True , True]
TurnoTyN = [False , True , True]
TurnoNada = [False , False , False]




#CREA EQUIPOS Y JUGADORES
jugador1 = Jugador ()
equipo1 = Equipo ()

jugador2 = Jugador ()
equipo2 = Equipo ()




#SET DE JUGADORES
jugador1.setNombre = "Nico"
jugador1.setApellido = "Prusci"
jugador1.setNumero = "10"

jugador2.setNombre = "Gonza"
jugador2.setApellido = "Alessa"
jugador2.setNumero = "10"





#SET DE EQUIPOS
equipo1.setNombre = "Los seguidores de prusci"
equipo1.setBarrio = "Pueyrredon"
equipo1.setCapitan = "Prusci"
equipo1.jugadores = jugador1
equipo1.a_disponibilidad (TurnoManana)
equipo1.a_disponibilidad (TurnoTarde) #martes
equipo1.a_disponibilidad (TurnoNoche) #miercoles
equipo1.a_disponibilidad (TurnoMTN) #jueves
equipo1.a_disponibilidad (TurnoManana) #viernes
equipo1.a_disponibilidad (TurnoManana) #sabado


equipo2.setNombre = "Alessa Team "
equipo2.setBarrio = "Urquiza"
equipo2.setCapitan = "Alessa"
equipo2.jugadores = jugador2
equipo2.a_disponibilidad (TurnoManana) #lunes
equipo2.a_disponibilidad (TurnoManana) #martes
equipo2.a_disponibilidad (TurnoNoche) #miercoles
equipo2.a_disponibilidad (TurnoMTN) #jueves
equipo2.a_disponibilidad (TurnoManana) #viernes
equipo2.a_disponibilidad (TurnoNada) #sabado



#CREA TORNEO
torneo = Torneo()
torneo.equipos (equipo1)
torneo.equipos (equipo2)


#SET PARTIDO

for
for item in torneo.lista_equipos:
    equipostotales += 1

numero = equipostotales
partidostotales = 0

for numero in range (partidostotales):
    partidostotales += numero - 1


fecha_partidos = 0

for fecha_partidos in range (partidostotales):














