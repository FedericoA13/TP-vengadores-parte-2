import random
import constantes as const


def leer_info(archivo, separacion=' '):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').replace('--', ' ').split(separacion)
    else:
        registro = False
    return registro


def quitar_tildes(palabra):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """

    cambios = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for vocal_con_tilde, vocal_sin_tilde in cambios:
        palabra = palabra.replace(vocal_con_tilde, vocal_sin_tilde).replace(
            vocal_con_tilde.upper(), vocal_sin_tilde.upper())
    return palabra


def limpiar_palabra(palabra):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """

    palabra_limpia = "".join(caracter.lower() if caracter.isalpha()
                             else "" for caracter in palabra)
    palabra_sin_tildes = quitar_tildes(palabra_limpia)

    return palabra_sin_tildes


def creacion_de_dicc(lista_archivos):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """
    diccionario = {}
    num_archivo = 0

    for archivo in lista_archivos:
        renglon = const.leer_info(archivo)
        contador_lineas_vacias = 0
        while contador_lineas_vacias < 20:
            if not renglon:
                contador_lineas_vacias += 1
            else:
                contador_lineas_vacias = 0
                for palabra in renglon:
                    palabra = limpiar_palabra(palabra)
                    if palabra not in diccionario and len(palabra) > 0:
                        diccionario[palabra] = [0, 0, 0]
                        diccionario[palabra][num_archivo] = 1
                    elif len(palabra) > 0:
                        diccionario[palabra][num_archivo] += 1
            renglon = leer_info(archivo)
        num_archivo += 1

    return diccionario


def ordenar_dicc(dicc):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """

    return dict(sorted(dicc.items(), key=lambda i: i[0]))


def creacion_texto(dicc):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """
    archivo_palabras = open('palabras.csv', 'w')
    for palabra, apariciones in dicc.items():
        archivo_palabras.write(
            f'{palabra},{apariciones[0]},{apariciones[1]},{apariciones[2]} \n')

    archivo_palabras.close()


def generar_palabras_candidatas(archivo):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """

    lista_palabras_candidatas = []
    renglon = leer_info(archivo, ',')

    while renglon:
        palabra = renglon[0]
        if const.LONG_PALABRA_MAX >= len(palabra) >= const.LONG_PALABRA_MIN:
            lista_palabras_candidatas.append(palabra)
        renglon = leer_info(archivo, ',')

    return lista_palabras_candidatas


def elegir_palabra(lista_palabras, cant_letras):
    """
    Autores: Joaquin Mendaña, Martin Morono, Federico Aldrighetti
    """

    lista_palabras = list(filter(lambda palabra: len(palabra) == cant_letras, lista_palabras))

    return random.choice(lista_palabras) if len(lista_palabras) > 0 else None
