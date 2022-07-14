
# EL CODIGO YA CUENTA CON UNA CONSOLA, PARA PROBARLO SOLO EJECUTELO.

def cargar_datos(nombre_archivo:str)->dict:

    archivo = open(nombre_archivo, "r", encoding="utf-8")
    columna = archivo.readline().replace("\n", "").split(",")
    linea = archivo.readline()

    dic_principal = {}
    dic_congresista = {}

    while len(linea) > 0:
        linea = linea.replace("\n", "").split(",")
        partido = linea[1]

        if partido not in dic_principal:
            dic_principal[partido] = []

        linea = archivo.readline()

    archivo.close()

    archivo = open("Data.csv", "r", encoding="utf-8")
    columna = archivo.readline().replace("\n", "").split(",")
    linea = archivo.readline()

    while len(linea) > 0:

        linea = linea.replace("\n", "").split(",")
        nombre = linea[0]
        partido = linea[1]
        votos = linea[2]
        puntaje = linea[3]

        for i in dic_principal:
            partido_i = i

            if partido == partido_i:
                dic_congresista = {"nombre": nombre, "votos": votos, "puntaje": puntaje}
                lista = dic_principal[partido]
                lista.append(dic_congresista)
                dic_congresista = {}

        linea = archivo.readline()

    return dic_principal

def promedio_corrupcion(datos:dict)->dict:

    dic_puntajes = {}
    puntajes_totales = 0
    cuenta = 0
    promedio = 0
    puntaje_total = 0

    for i in datos:
        dic_puntajes[i] = 0

    for i in datos:
        partido = i
        lista_partido = datos[partido]

        for l in lista_partido:
            dic_congresista = l
            puntaje = int(dic_congresista["puntaje"])
            puntajes_totales += 1
            puntaje_total += puntaje
        promedio = round((puntaje_total / puntajes_totales), 1)
        dic_puntajes[partido] = promedio
        puntajes_totales = 0
        puntaje_total = 0
        promedio = 0


    return "\n"+str(dic_puntajes)

def top_5_corruptos(datos:dict)->str:

    puntajes = {}
    maximo = 0

    for i in datos:
        lista = datos[i]
        
        for l in lista:
            dic_congresista = l
            nombre = dic_congresista["nombre"]
            puntaje = dic_congresista["puntaje"]
            puntajes[nombre] = puntaje

    valores = []

    for i in puntajes.values():
        valores.append(int(i))

    for i in valores:
        if i > maximo:
            maximo = i

    personas = []
    minimo = maximo
    diccionario = {}

    for i in datos:    
        for i in datos:
            lista = datos[i]
            for l in lista:
                dic_congresista = l
                nombre = dic_congresista["nombre"]
                puntaje = int(dic_congresista["puntaje"])
                votos = dic_congresista["votos"]
                if puntaje == maximo:
                    diccionario["nombre"] = nombre
                    diccionario["puntaje"] = puntaje
                    diccionario["votos"] = votos
                    personas.append(diccionario)
                    diccionario = {}

    personas = personas[0:5]

    cadena = "+-------------------------------------------------------+\n|\tNombres\t\t\t\t|Votos\t|Puntaje|\n+-------------------------------------------------------+\n|\t{}\t|{}\t|{}\t|\n+-------------------------------------------------------+\n|\t{}\t\t|{}\t|{}\t|\n+-------------------------------------------------------+\n|\t{}\t\t|{}\t|{}\t|\n+-------------------------------------------------------+\n|\t{}\t|{}\t|{}\t|\n+-------------------------------------------------------+\n|\t{}\t\t|{}\t|{}\t|\n+-------------------------------------------------------+"

    cadena = cadena.format(personas[0]["nombre"], personas[0]["votos"], personas[0]["puntaje"], personas[1]["nombre"], personas[1]["votos"], personas[1]["puntaje"], personas[2]["nombre"], personas[2]["votos"], personas[2]["puntaje"], personas[3]["nombre"], personas[3]["votos"], personas[3]["puntaje"], personas[4]["nombre"], personas[4]["votos"], personas[4]["puntaje"])

    return "\n"+cadena

print("\n¡Bienvenido al detector de corrupcion en el Congreso!\nTenemos 2 posibles datos para ti, esoce el que quieras.\n\n1. Promedio de corrupcion en los partidos.\n2. ¡TOP 5 corruptos!\n")

opcion = 0

while opcion != 3:

    opcion = int(input("\nInserte la opcion que desees ejecutar, si quieres salir del programa inserta el numero 3: "))

    if opcion == 1:
        print(promedio_corrupcion(cargar_datos("Data.csv")))
    elif opcion == 2:
        print(top_5_corruptos(cargar_datos("Data.csv")))
    elif opcion == 3:
        opcion = 3
    else: 
        print("Ha insertado una opcion no valida.")