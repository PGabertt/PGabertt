"""

En el segundo avance del proyecto, se espera que se desarrolle una funcionalidad
clave. Esta consiste en la lectura de los datos de cada partido a partir de un archivo
en formato CSV que se les proporcionará. A través de esta funcionalidad, se
calcularán las puntuaciones correspondientes a cada equipo involucrado en los
partidos según las reglas de puntuación.
Se deberá ir acumulando la cantidad de puntos, goles y tarjetas de cada equipo.
El programa debe imprimir el total de goles,puntaje y tarjetas obtenido por
cada equipo



"""









import csv

#Crear diccionarios para almacenar las puntuaciones, goles y tarjetas de cada equipo
puntuaciones = {}
goles = {}
tarjetas = {}

#Leer el archivo CSV
with open("C:\\Users\\pgabe\\OneDrive\\Documentos\\Copa_Mundial_2023.csv") as per:
    reader = csv.reader(per)
    header = next(reader)  #Leer la primera fila que contiene los encabezados
    
    row = next(reader, None)  #Leer la primera fila de datos
    
    while row is not None:
        equipo_casa = row[0]
        equipo_visita = row[1]
        goles_casa = int(row[2])
        goles_visita = int(row[3])
        tarjetas_casa = int(row[4])
        tarjetas_visita = int(row[5])

        #Actualizar las puntuaciones, goles y tarjetas de los equipos
        if equipo_casa not in puntuaciones:
            puntuaciones[equipo_casa] = 0
            goles[equipo_casa] = 0
            tarjetas[equipo_casa] = 0
        if equipo_visita not in puntuaciones:
            puntuaciones[equipo_visita] = 0
            goles[equipo_visita] = 0
            tarjetas[equipo_visita] = 0

        #Calcular puntuaciones, goles y tarjetas
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
        
        row = next(reader, None)  #Leer la siguiente fila de datos

#Imprimir los resultados en formato de columnas
print(f"{'Equipo':<20}{'Puntuación':<15}{'Total de Goles':<15}{'Total de Tarjetas'}")
for equipo in puntuaciones:
    print(f"{equipo:<20}{puntuaciones[equipo]:<15}{goles[equipo]:<15}{tarjetas[equipo]}")
