import csv

# Crear diccionarios para almacenar las puntuaciones, goles y tarjetas de cada equipo
puntuaciones = {}
goles = {}
tarjetas = {}
Partidos_por_equipo = {}

# Leer el archivo CSV
with open("C:\\Users\\pgabe\\OneDrive\\Documentos\\Copa_Mundial_2023.csv") as per:
    reader = csv.reader(per)  # Usar la variable 'per' en lugar de 'Copa_Mundial_2023'
    header = next(reader)  # Leer la primera fila que contiene los encabezados
    total_partidos = 0
    row = next(reader, None)  # Leer la primera fila de datos

    while row is not None:
        equipo_casa = row[0]
        equipo_visita = row[1]
        goles_casa = int(row[2])
        goles_visita = int(row[3])
        tarjetas_casa = int(row[4])
        tarjetas_visita = int(row[5])

        # Actualizar las puntuaciones, goles y tarjetas de los equipos
        if equipo_casa not in puntuaciones:
            puntuaciones[equipo_casa] = 0
            goles[equipo_casa] = 0
            tarjetas[equipo_casa] = 0
        if equipo_visita not in puntuaciones:
            puntuaciones[equipo_visita] = 0
            goles[equipo_visita] = 0
            tarjetas[equipo_visita] = 0

        # Calcular puntuaciones, goles y tarjetas
        if goles_casa > goles_visita:
            puntuaciones[equipo_casa] += 3
        elif goles_casa < goles_visita:
            puntuaciones[equipo_visita] += 3
        else:
            puntuaciones[equipo_casa] += 1
            puntuaciones[equipo_visita] += 1

        goles[equipo_casa] += goles_casa
        goles[equipo_visita] += goles_visita

        tarjetas[equipo_casa] += tarjetas_casa
        tarjetas[equipo_visita] += tarjetas_visita

        # Sumar la cantidad de partidos por equipo
        if equipo_casa not in Partidos_por_equipo:
            Partidos_por_equipo[equipo_casa] = 1
        else:
            Partidos_por_equipo[equipo_casa] += 1

        if equipo_visita not in Partidos_por_equipo:
            Partidos_por_equipo[equipo_visita] = 1
        else:
            Partidos_por_equipo[equipo_visita] += 1

        total_partidos += 1  # Contar la cantidad de partidos en todo el torneo
        row = next(reader, None)  # Leer la siguiente fila de datos

# Avance 3

# Ordenar los equipos por puntuación en orden descendente
equipos_ordenados = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)

# Imprimir los primeros tres equipos
print("Equipos en los primeros tres lugares:")
print("")
for i, (equipo, puntuacion) in enumerate(equipos_ordenados[:3], 1):
    print(f"{i}. {equipo}: {puntuacion} puntos")

# Encuentra el equipo que ha anotado la mayor cantidad de goles
equipo_max_goles = max(goles, key=goles.get)

# Encuentra el equipo que ha acumulado más tarjetas
equipo_max_tarjetas = max(tarjetas, key=tarjetas.get)

# Calcula el promedio de goles en el torneo por partidos
total_goles = sum(goles.values())
promedio_goles_por_partido = total_goles / total_partidos

# Imprime el informe detallado
print("               Reporte             ")
print(f"1. Equipo con la mayor cantidad de goles: {equipo_max_goles} ({goles[equipo_max_goles]} goles)")
print(f"2. Equipo con la mayor cantidad de tarjetas: {equipo_max_tarjetas} ({tarjetas[equipo_max_tarjetas]} tarjetas)")
print(f"3. Promedio de goles en el torneo por partido: {promedio_goles_por_partido:.2f} goles")

print("---------------------------------------------------------")

# Calcular el promedio de goles por equipo
promedio_goles_por_equipo = {}

for equipo, total_goles_equipo in goles.items():
    partidos_jugados = Partidos_por_equipo.get(equipo, 0)
    if partidos_jugados > 0:
        promedio_goles = total_goles_equipo / partidos_jugados
        promedio_goles_por_equipo[equipo] = promedio_goles
    else:
        # Manejar el caso en el que un equipo no jugó ningún partido
        promedio_goles_por_equipo[equipo] = 0.0

# Imprimir el promedio de goles por equipo
print("Promedio de goles por equipo:")
for equipo, promedio in promedio_goles_por_equipo.items():
    print(f"{equipo}: {promedio:.2f} goles por partido")
