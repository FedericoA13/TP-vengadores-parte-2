def leer_info(archivo, separacion=' '):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').replace('--', ' ').split(separacion)
    else:
        registro = False
    return registro


# Mensajes y simbolos
CARACTER_OCULTO = "?"
MENSAJE_INICIAL = "Palabra a adivinar"
MENSAJE_ACIERTO = "Muy bien!!!"
MENSAJE_DESACIERTO = "Lo siento!!!"
MENSAJE_LETRA_INGRESADA = "Letra ya ingresada"
MENSAJE_INGRESO_INVALIDO = "Ingreso inválido"
MENSAJE_DESPEDIDA = "Gracias por jugar!!!"
MENSAJE_INPUT_LETRA = "Ingrese letra (0 o FIN para abandonar): "
SEGUIR_JUGANDO = "Desea seguir jugando (si o no): "
DESEA_LETRAS = "¿Desea una cantidad de letras específica? (si/no): "
CUANTAS_LETRAS = "Cuantas letras?: "
MENSAJE_DE_VALIDACION = "No entiendo su respuesta, introduzca si o no: "
MENSAJE_DE_COMPROBACION = "Ingrese si o no: "
MENSAJE_DE_RECREACION_ARCHIVO = "Hemos recreado el archivo de palabras!"
MENSAJE_CREACION_ARCHIVO = "El archivo de palabras no existia y lo hemos creado!"
MENSAJE_RECARGA_ARCHIVO = "Desea recargar el archivo de palabras?: "
CANTIDAD_VALIDA_LETRAS = "Ingrese cantidad de letras correcta: "
LONGITUD_INEXISTENTE = "No hay palabras con esa longitud"
AFIRMACION = "si"
NEGACION = "no"
MENSAJE_VICTORIA = "Ganaste! "
MENSAJE_DERROTA = "Perdiste :("
MENSAJE_FELICIDADES = "Felicitaciones!"
MENSAJE_NUEVO_JUGADOR = "Nuevo Jugador (Max 5 jugadores): "
MENSAJE_DEJAR_DE_INGRESAR_NOMBRES = "Presionar enter para dejar de ingresar nombres"
INGRESO_MINIMO_JUGADORES = "Ingresar al menos a un jugador"
NOMBRE_YA_INGRESADO = "Nombre ya ingresado"
TURNOS_JUGADORES = "Turnos de los jugadores: "

# Ahorcado: Longitudes y puntajes
MAX_USUARIOS = 5
LONG_PALABRA_MIN = 5
LONG_PALABRA_MAX = 18
MAX_DESACIERTOS_PERMITIDOS = 7
PUNTOS_ACIERTO_LETRA = 2
PUNTOS_DESACIERTOS_LETRA = 1
PUNTAJE_ACIERTO_PALABRA = 10
PUNTAJE_PERDIDA_PARTIDA = 5
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
