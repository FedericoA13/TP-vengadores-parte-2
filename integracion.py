import palabrasmenos
import ahorcado
import constantes as const
import os


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


def seleccion_palabra(lista_palabras, cant_letras=0):

    if cant_letras != 0:
        palabra_adivinar = palabrasmenos.elegir_palabra(lista_palabras, cant_letras)

    else:
        palabra_adivinar = palabrasmenos.elegir_palabra(lista_palabras)

    return palabra_adivinar


def quiere_letras():

    desea_letras = input(const.DESEA_LETRAS)
    while desea_letras.lower() not in ('no', 'si'):
        desea_letras = input(const.INTRODUZCA_COMANDO_DE_NUEVO)

    return desea_letras


def jugar_una_partida(lista_palabras):

    desea_letras = quiere_letras()
    if desea_letras == "si":
        cant_letras = verificar_cant_letras(lista_palabras)
        palabra_adivinar = seleccion_palabra(lista_palabras, cant_letras)
    else:
        palabra_adivinar = seleccion_palabra(lista_palabras)

    return ahorcado.jugar_ahorcado(palabra_adivinar)


def jugar_multiples_partidas():
    archivo_palabras = open('palabras.csv', 'r')
    lista_palabras = palabrasmenos.generar_palabras_candidatas(archivo_palabras)

    puntaje = jugar_una_partida(lista_palabras)

    seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    while seguir_jugando.lower() == "si":
        puntaje += jugar_una_partida(lista_palabras)
        seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    print(f"\nPuntaje total = {puntaje}")
    print(const.MENSAJE_DESPEDIDA)

    archivo_palabras.close()


preguntar_recarga_csv()
