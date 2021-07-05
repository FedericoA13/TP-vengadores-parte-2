import ahorcado
import constantes as const
import palabrasmenos
import os
import operator
import random


def recargar_csv():
    archivo_cuentos = open('Cuentos.txt', 'r')
    archivo_noches = open('Las 1000 Noches y 1 Noche.txt', 'r')
    archivo_arania = open('La araña negra - tomo 1.txt', 'r')

    lista_archivos = [archivo_cuentos, archivo_noches, archivo_arania]
    dicc = palabrasmenos.creacion_de_dicc(lista_archivos)
    dicc_ordenado = palabrasmenos.ordenar_dicc(dicc)
    palabrasmenos.creacion_texto(dicc_ordenado)

    archivo_cuentos.close()
    archivo_noches.close()
    archivo_arania.close()


def preguntar_recarga_csv():
    if not os.path.exists("palabras.csv"):
        recargar_csv()
        print("El archivo de palabras no existia y lo hemos creado!")
        jugar_multiples_partidas()
    else:
        recargar_palabras = input("Desea recargar el archivo de palabras?: ")
        while recargar_palabras.lower() not in ("no", "si"):
            recargar_palabras = input("Ingrese SI o NO: ")
        if recargar_palabras.lower() == "si":
            recargar_csv()
            print("Hemos creado el archivo de palabras!")
            jugar_multiples_partidas()
        elif recargar_palabras.lower() == "no":
            jugar_multiples_partidas()


def verificar_cant_letras(lista_palabras):
    cant_letras = input('Cuantas letras? ')

    while not cant_letras.isnumeric() or palabrasmenos.elegir_palabra(lista_palabras, int(cant_letras)) == None:
        if not cant_letras.isnumeric():
            cant_letras = input('Ingrese cantidad de letras correcta: ')

        elif palabrasmenos.elegir_palabra(lista_palabras, int(cant_letras)) == None:
            cant_letras = input(
                f'No hay palabras con esa longitud. Elige una longitud entre {const.LONG_PALABRA_MIN} y {const.LONG_PALABRA_MAX}: ')

    return int(cant_letras)


def seleccion_palabra(lista_palabras, longitud_palabra):
    palabra_adivinar = palabrasmenos.elegir_palabra(lista_palabras, longitud_palabra)

    return palabra_adivinar


def quiere_letras():
    desea_letras = input(const.DESEA_LETRAS)
    while desea_letras.lower() not in ('no', 'si'):
        desea_letras = input(const.INTRODUZCA_COMANDO_DE_NUEVO)

    return desea_letras


def asignar_palabras_jugadores(nombres_jugadores, lista_palabras):
    palabras_asignadas = {}

    desea_letras = quiere_letras()
    if desea_letras == "si":
        longitud_de_palabras = verificar_cant_letras(lista_palabras)

    else:
        longitud_de_palabras = random.randrange(const.LONG_PALABRA_MIN, const.LONG_PALABRA_MAX)

    for jugador in nombres_jugadores:
        palabra_a_adivinar = seleccion_palabra(lista_palabras, longitud_de_palabras)

        palabras_asignadas[jugador] = palabra_a_adivinar
    # print(palabras_asignadas)
    return palabras_asignadas


def actualizar_estadisticas_acumuladas(dicc_estadisticas_acumuladas, dicc_estadisticas_partida):
    for jugador in dicc_estadisticas_partida:
        palabra, puntaje, letras_adivinadas, letras_erroneas, gano = ahorcado.inicializar_variables(
            dicc_estadisticas_partida[jugador])

        resultado = 1 if gano else 0

        if jugador not in dicc_estadisticas_acumuladas:
            puntaje_total = cant_aciertos = cant_desaciertos = cant_victorias = 0

            dicc_estadisticas_acumuladas[jugador] = [puntaje_total, cant_aciertos, cant_desaciertos, cant_victorias]

        dicc_estadisticas_acumuladas[jugador] = [
            dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_PUNTAJE] + puntaje,
            dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_CANT_ACIERTOS] + len(letras_adivinadas),
            dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_CANT_DESACIERTOS] + len(letras_erroneas),
            dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_CANT_VICTORIAS] + resultado,
        ]

    tupla_estadisticas_acumuladas_ordenado = sorted(dicc_estadisticas_acumuladas.items(), key=operator.itemgetter(1),
                                                    reverse=True)
    dicc_estadisticas_acumuladas_ordenado = dict((c, v) for c, v in tupla_estadisticas_acumuladas_ordenado)

    return dicc_estadisticas_acumuladas_ordenado


def mostrar_resultados_acumulados(dicc_estadisticas_acumuladas, cant_partidas):
    """
    Autor: Alejandro Schamun.

    Muestra los resultados totales luego de cada partida.
    """
    print(f"\n====================== Resultados Generales ======================")
    print(f"Cantidad de partidas jugadas: {cant_partidas}")

    for jugador in dicc_estadisticas_acumuladas:
        print(f"\nJugador {jugador}:")
        print(f" - Puntaje Total: {dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_PUNTAJE]}")
        print(f" - Cantidad de aciertos: {dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_CANT_ACIERTOS]}")
        print(
            f" - Cantidad de desaciertos: {dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_CANT_DESACIERTOS]}")
        print(
            f" - Cantidad de victorias: {dicc_estadisticas_acumuladas[jugador][const.EST_ACUM_INDICE_CANT_VICTORIAS]}")

    print(f"\n==================================================================")


def jugar_una_partida(nombres_jugadores, nombre_ultimo_ganador, lista_palabras):
    nombres_jugadores = ahorcado.asignar_turno_jugadores(nombres_jugadores, nombre_ultimo_ganador)
    ahorcado.informar_turnos_jugadores(nombres_jugadores)
    dicc_palabras = asignar_palabras_jugadores(nombres_jugadores, lista_palabras)
    dicc_estadisticas_partida = {}

    for jugador in dicc_palabras:
        dicc_estadisticas_partida[jugador] = [dicc_palabras[jugador], 0, [], [], False]

    existe_ganador = False
    todos_perdieron = False
    cant_perdedores = 0
    nombre_ultimo_ganador = ""
    perdedores = []

    while not existe_ganador and not todos_perdieron:
        i = 0

        while i < len(nombres_jugadores) and not existe_ganador and not todos_perdieron:

            jugador = nombres_jugadores[i]
            letras_erroneas = dicc_estadisticas_partida[jugador][const.EST_JUGADOR_INDICE_LETRAS_ERRONEAS]

            if ahorcado.tiene_intentos(letras_erroneas):
                print(f"\n====================== Turno de {jugador} ======================")
                dicc_estadisticas_partida[jugador] = ahorcado.jugar_ahorcado(dicc_estadisticas_partida[jugador])

                gano = dicc_estadisticas_partida[jugador][const.EST_JUGADOR_INDICE_GANO]
                if gano:
                    existe_ganador = True
                    nombre_ultimo_ganador = jugador
                    dicc_estadisticas_partida[jugador][
                        const.EST_JUGADOR_INDICE_PUNTAJE] += const.PUNTOS_ADIVINA_PALABRA

            else:
                if jugador in perdedores:
                    cant_perdedores += 0
                else:
                    cant_perdedores += 1
                    perdedores.append(jugador)
                    if cant_perdedores == len(nombres_jugadores):
                        todos_perdieron = True

            i += 1

        if todos_perdieron:
            for jugador in dicc_estadisticas_partida:
                dicc_estadisticas_partida[jugador][const.EST_JUGADOR_INDICE_PUNTAJE] -= const.PUNTOS_RESTA_GANA_PROGRAMA

    return dicc_estadisticas_partida, nombre_ultimo_ganador


def jugar_multiples_partidas():
    archivo_palabras = open('palabras.csv', 'r')
    lista_palabras = palabrasmenos.generar_palabras_candidatas(archivo_palabras)

    nombres_jugadores = ahorcado.solicitar_nombres_jugadores()

    cant_partidas = 0
    dicc_estadisticas_acumuladas = {}

    seguir_jugando = "si"
    nombre_ultimo_ganador = ""

    while seguir_jugando.lower() == "si":

        dicc_estadisticas_partida, nombre_ultimo_ganador = jugar_una_partida(nombres_jugadores, nombre_ultimo_ganador,
                                                                             lista_palabras)

        if nombre_ultimo_ganador != "":
            print("Ganaste ", nombre_ultimo_ganador, "felicitaciones!")

        dicc_estadisticas_acumuladas = actualizar_estadisticas_acumuladas(dicc_estadisticas_acumuladas,
                                                                          dicc_estadisticas_partida)

        cant_partidas += 1

        mostrar_resultados_acumulados(dicc_estadisticas_acumuladas, cant_partidas)

        seguir_jugando = ""
        while seguir_jugando.lower() not in ["si", "no"]:
            seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    print(const.MENSAJE_DESPEDIDA)


preguntar_recarga_csv()
