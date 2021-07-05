def leer_info(archivo, separacion=' '):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').replace('--', ' ').split(separacion)
    else:
        registro = False
    return registro


SIGNO_PREGUNTA = "?"
MENSAJE_INICIAL = "Palabra a adivinar"
MENSAJE_ACIERTO = "Muy bien!!!"
MENSAJE_DESACIERTO = "Lo siento!!!"
MENSAJE_LETRA_INGRESADA = "Letra ya ingresada"
MENSAJE_INGRESO_INVALIDO = "Ingreso inválido"
MENSAJE_DESPEDIDA = "Gracias por jugar!!!"
MENSAJE_INPUT_LETRA = "Ingrese letra (0 o FIN para abandonar): "
SEGUIR_JUGANDO = "Desea seguir jugando (si o no): "
DESEA_LETRAS = '¿Desea una cantidad de letras específica? (si/no): '
INTRODUZCA_COMANDO_DE_NUEVO = "No entiendo su respuesta, introduzca si o no: "

MAX_USUARIOS = 5
LONG_PALABRA_MIN = 5
LONG_PALABRA_MAX = 18
MAX_DESACIERTOS = 7
PUNTOS_ACIERTOS = 2
PUNTOS_DESACIERTOS = 1
PUNTOS_ADIVINA_PALABRA = 10
PUNTOS_RESTA_GANA_PROGRAMA = 5
INDICE_CLAVE = 0

LETRAS_FIN = ["FIN", "0"]

# Indices diccionario estadísticas jugadores
EST_JUGADOR_INDICE_PALABRA = 0
EST_JUGADOR_INDICE_PUNTAJE = 1
EST_JUGADOR_INDICE_LETRAS_ADIVINADAS = 2
EST_JUGADOR_INDICE_LETRAS_ERRONEAS = 3
EST_JUGADOR_INDICE_GANO = 4

# Indices diccionario estadísticas acumuladas
EST_ACUM_INDICE_PUNTAJE = 0
EST_ACUM_INDICE_CANT_ACIERTOS = 1
EST_ACUM_INDICE_CANT_DESACIERTOS = 2
EST_ACUM_INDICE_CANT_VICTORIAS = 3

with open('configuracion.csv', 'r') as config:
    linea = leer_info(config, ',')
    while linea:
        constante = linea[0]
        valor = linea[1]
        dicc_ctes = locals()
        if constante in dicc_ctes:
            if valor.isnumeric():
                valor = int(valor)
            dicc_ctes[constante] = valor
        linea = leer_info(config, ',')
