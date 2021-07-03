import random
import constantes as const
import os

archivo_cuentos = open('Cuentos.txt', 'r')
archivo_noches = open('Las 1000 Noches y 1 Noche.txt', 'r')
archivo_arania = open('La araña negra - tomo 1.txt', 'r')
archivo_palabras = open('palabras.csv', 'a')

lista_archivos = [archivo_cuentos, archivo_noches, archivo_arania]


def leer_info(archivo, separacion=' '):

    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').replace('--', ' ').split(separacion)
    else:
        registro = False
    return registro


def quitar_tildes(palabra):

    cambios = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for vocal_con_tilde, vocal_sin_tilde in cambios:
        palabra = palabra.replace(vocal_con_tilde, vocal_sin_tilde).replace(
            vocal_con_tilde.upper(), vocal_sin_tilde.upper())
    return palabra


def limpiar_palabra(palabra):

    palabra_limpia = "".join(caracter.lower() if caracter.isalpha()
                             else "" for caracter in palabra)
    palabra_sin_tildes = quitar_tildes(palabra_limpia)

    return palabra_sin_tildes


def creacion_de_dicc(lista_archivos):
    diccionario = {}
    num_archivo = 0

    for archivo in lista_archivos:
        renglon = leer_info(archivo)
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


#dicc = creacion_de_dicc(lista_archivos)


def ordenar_dicc(dicc):

    return dict(sorted(dicc.items(), key=lambda i: i[0]))


#dicc_ordenado = ordenar_dicc(dicc)


def creacion_texto(dicc):

    for palabra, apariciones in dicc.items():
        archivo_palabras.write(
            f'{palabra},{apariciones[0]},{apariciones[1]},{apariciones[2]} \n')


# creacion_texto(dicc_ordenado)

archivo_cuentos.close()
archivo_noches.close()
archivo_arania.close()
archivo_palabras.close()

'''def main():
    if not os.isfile('palabras.csv'):
        dicc = creacion_de_dicc(lista_archivos)
        dicc_ordenado = ordenar_dicc(dicc)
        creacion_texto(dicc_ordenado)
    else:'''


def generar_palabras_candidatas(archivo):

    lista_palabras_candidatas = []
    renglon = leer_info(archivo, ',')

    while renglon:
        # print(renglon)
        palabra = renglon[0]
        if const.LONGITUD_MAXIMA_PALABRA >= len(palabra) >= const.LONGITUD_MINIMA_PALABRA:
            lista_palabras_candidatas.append(palabra)
        renglon = leer_info(archivo, ',')

    return lista_palabras_candidatas


'''def devolver_palabras_candidatas(lista_palabras=None):

    if not lista_palabras:
        lista_palabras = generar_palabras_candidatas(archivo, cant_letras)

    return lista_palabras'''


def elegir_palabra(lista_palabras, cant_letras=0):

    if cant_letras != 0:
        lista_palabras = list(filter(lambda palabra: len(palabra) == cant_letras, lista_palabras))

    return random.choice(lista_palabras) if len(lista_palabras) > 0 else None
