#Equipo local

Nombre_Local = input('Nombre del equipo local: ')
Goles_Equipo_Local = int(input('Goles anotados por el equipo local: '))
Tarjetas_Local = int(input('Tarjetas recibidas por el equipo local: '))
 
#Informacion del equipo visitante
Nombre_Visitante = input('Nombre del equipo visitante: ')
Goles_Equipo_Visitante = int(input('Goles anotados por el equipo visitante: '))
Tarjetas_Visitante = int(input('Tarjetas recibidas por el equipo visitante: '))

#Quien gana el partido

if Goles_Equipo_Local > Goles_Equipo_Local:
    Ganador = Goles_Equipo_Local
    puntos_ganador = 3
elif Goles_Equipo_Visitante > Goles_Equipo_Local: 
    ganador= Nombre_Visitante
    puntos_ganador = 3
else:
    ganador = "Mierda"
    puntos_ganador =1

#Imprimir el enfrentamiento


#Equipo ganador y si hubo empate
if ganador == "Empate":
    print('El enfrentamiento termino en empate. Ambos equipos ganan 1 punto')
else:
    print(f'El equipo ganador es {ganador} con {puntos_ganador} puntos')

#Ver si hay un desempate basado en los goles y tarjetas
if Goles_Equipo_Local == Goles_Equipo_Visitante and ganador == "empate":
    if Tarjetas_Local < Tarjetas_Visitante:
        ganador = Nombre_Local
elif Tarjetas_Visitante < Tarjetas_Local:
    ganador = Nombre_Visitante
    
#Ahora si los resultados del desempate
if ganador != "empate":
    print(f'Despues del desempate el equipo ganador es {ganador} ')