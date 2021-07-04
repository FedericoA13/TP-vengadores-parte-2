import constantes as const
import random

def ofuscar_palabra(palabra, letras_adivinadas):
    """
    Autor: Joaquin Mendaña.

    Ofusca las letras de la palabra que todavía no han sido adivinadas utilizando signos de pregunta (?)

    Parámetros:
    - palabra: palabra a ofuscar
    - letras_adivinadas: letras que no deben ofuscarse
    """

    return "".join(letra if letra in letras_adivinadas else const.SIGNO_PREGUNTA for letra in palabra)


def mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas):
    """
    Autor: Joaquin Mendaña.

    Informa sobre el progreso de juego
    """

    palabra = ofuscar_palabra(palabra, letras_adivinadas)
    print(f"\n{mensaje} → {palabra}  Aciertos: {len(letras_adivinadas)}  Desaciertos: {len(letras_erroneas)} - {letras_erroneas}")


def pedir_letra(letras_usadas):
    """
    Autor: Joaquin Mendaña.

    Solicita una letra al usuario realizando las siguientes validaciones:
    - Se ingresó un único caracter válido (no numérico o especial)
    - La letra no se utilizó en intentos anteriores
    - La letra no es un caracter utilizado para finalizar el juego.

    Devuelve la letra ingresada por el usuario en minúscula.

    Parámetros:
    - letras_usadas: Lista de letras ya utilizadas
    """

    letra_valida = False
    letra = input(const.MENSAJE_INPUT_LETRA)

    while not letra_valida and not finalizar_juego(letra):
        if len(letra) != 1 or not letra.isalpha():
            print(f"\n{const.MENSAJE_INGRESO_INVALIDO}")

        elif letra.lower() in letras_usadas or letra.upper() in letras_usadas:
            print(f"\n{const.MENSAJE_LETRA_INGRESADA}")

        else:
            letra_valida = True

        if not letra_valida:
            letra = input(const.MENSAJE_INPUT_LETRA)

    if not finalizar_juego(letra):
        letra = letra.lower()

    return letra


def tiene_intentos(letras_erroneas):
    """
    Autor: Joaquin Mendaña.

    Devuelve True si el usuario cuenta con intentos disponibles, es decir,
    si la cantidad de letras erróneas ingresadas es menor a la cantidad máxima de desaciertos permitidos.
    """
    return len(letras_erroneas) < const.MAXIMOS_DESACIERTOS_PERMITIDOS


def finalizar_juego(letra):
    """
    Autor: Alejandro Schamun.

    Devuelve True si la letra ingresada por el usuario es una letra de fin utilizada para finalizar el juego.
    """
    return letra in const.LETRAS_FIN


def juego_ganado(palabra, letras_adivinadas):
    """
    Autor: Alejandro Schamun.

    Devuelve True si el jugador adivinó todas las letras de la palabra.
    """
    return len(set(palabra)) == len(letras_adivinadas)


def mostrar_mensaje_final(palabra, letras_adivinadas, letra):
    """
    Autor: Alejandro Schamun.

    Se ejecuta al final de la partida.
    Devuelve "¡Ganaste!" si el usuario encontró todas las letras, llamando a la función juego_ganado.
    Devuelve "Gracias por participar" y la palabra que el usuario debía adivinar en caso de agotar los intentos.

    Parámetros:
    - palabra: La palabra que el usuario debe adivinar.
    - letras_adivinadas: Cantidad de letras que el usuario acertó durante la partida.
    - letra: Es el intento del usuario por adivinar ingresando una letra. Si es 0 o FIN, termina la partida.
    """

    if juego_ganado(palabra, letras_adivinadas):
        mensaje = "¡Ganaste!"

    elif letra in const.LETRAS_FIN:
        mensaje = "Gracias por participar"
    
    else:
        mensaje = f"Perdiste :(, la palabra era: {palabra}"
    
    print(mensaje)

def solicitar_nombres_jugadores():
    """
    Autor: Facundo Sanso.
    
    """
    nombres_jugadores = []
    print ("Presionar enter para dejar de ingresar nombres")
    jugador = input("Nuevo Jugador (Max 5 jugadores): ")
    while len (nombres_jugadores) < 5 and jugador != "":
        if jugador.lower() not in nombres_jugadores:
            nombres_jugadores.append(jugador)
            if len (nombres_jugadores) < 5:
                print ("Presionar enter para dejar de ingresar nombres")
                jugador = input("Nuevo Jugador (Max 5 jugadores): ")
        else:
            print ("El nombre ya fue ingresado")
            print ("Presionar enter para dejar de ingresar nombres")
            jugador = input("Nuevo Jugador (Max 5 jugadores): ")
             
        
    return nombres_jugadores

def asignar_turno_jugadores(nombres_jugadores, ganador):
    """
    Autor: Facundo Sanso.
    
    Ordena al azar los turnos de los jugadores.
    Si se jugaron partidas anteriores asigna el primer turno al último ganador.
    """
    random.shuffle(nombres_jugadores)

    if ganador != "":
        nombres_jugadores.remove(ganador)
        nombres_jugadores = [ganador] + nombres_jugadores

    return nombres_jugadores

#print(asignar_turno_jugadores(["carlos", "olivia", "fede", "jose", "victor"], "fede"))


def informar_turnos_jugadores(nombres_jugadores):
    """
    Autor: Facundo Sanso.
    
    Muestra cual es el turno de cada jugador.
    """
    print("\nTurnos de los jugadores:")
    print("")
    for i in range(len(nombres_jugadores)):
        print(f"Turno {i + 1}: {nombres_jugadores[i]}")
    print("")

def inicializar_variables(lista_estadisticas_jugador):
    """
    Autor: Alejandro Schamun.
    
    La funcion recibe una lista y agarra cada uno de los elementos"
    """
    # lista completa para no pasar las variables por separado. Esta asociada a un dicc_estadisticas_jugador donde la
    # clave es el jugador
    palabra = lista_estadisticas_jugador[const.EST_JUGADOR_INDICE_PALABRA]
    puntaje = lista_estadisticas_jugador[const.EST_JUGADOR_INDICE_PUNTAJE]
    letras_adivinadas = lista_estadisticas_jugador[const.EST_JUGADOR_INDICE_LETRAS_ADIVINADAS]
    letras_erroneas = lista_estadisticas_jugador[const.EST_JUGADOR_INDICE_LETRAS_ERRONEAS]
    gano = lista_estadisticas_jugador[const.EST_JUGADOR_INDICE_GANO]

    return palabra, puntaje, letras_adivinadas, letras_erroneas, gano


def jugar_ahorcado(lista_estadisticas_jugador):
    """
    Autor: Alejandro Schamun.

    Esta función concreta la partida del juego del ahorcado.
    Al usuario se le da la palabra encriptada, y debe adivinar las letras, con el sistema avisando si
    acertó en su intento o no.
    Devuelve el puntaje obtenido al terminar de jugar.
    """

    palabra, puntaje, letras_adivinadas, letras_erroneas, gano = inicializar_variables(lista_estadisticas_jugador)
    #convertimos la lista en variables para usarlas directamente

    mostrar_informacion(const.MENSAJE_INICIAL, palabra, letras_adivinadas, letras_erroneas)
    letra = pedir_letra(letras_adivinadas + letras_erroneas)

    tuvo_errores = False

    while not finalizar_juego(letra) and tiene_intentos(letras_erroneas) and not gano and not tuvo_errores:

        if letra in palabra:
            letras_adivinadas.append(letra)
            mensaje = const.MENSAJE_ACIERTO
            puntaje += const.PUNTAJE_ACIERTO_LETRA

        else:
            letras_erroneas.append(letra)
            mensaje = const.MENSAJE_DESACIERTO
            puntaje += const.PUNTAJE_DESACIERTO_LETRA
            tuvo_errores = True #tuve errores, entonces para el turno al prox jugador

        mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas)

        gano = juego_ganado(palabra, letras_adivinadas)

        if tiene_intentos(letras_erroneas) and not gano and not tuvo_errores:
            letra = pedir_letra(letras_adivinadas + letras_erroneas)
    
    if not tiene_intentos(letras_erroneas):
        mostrar_mensaje_final(palabra, letras_adivinadas, letra)

    return [palabra, puntaje, letras_adivinadas, letras_erroneas, gano]


"""
def solicitar_nombre(nombres_jugadores):
"""
    #Solicita el ingreso de un nombre y valida que no se encuentre en la lista de nombres recibida por parámetro,
"""
    nombre_correcto = False
    nombre_jugador = ""

    while not nombre_correcto:
        repite_nombre = False
        nombre_jugador = input("Ingrese su nombre (Presione enter para salir): ")

        for nombre in nombres_jugadores:
            if nombre.lower() == nombre_jugador.lower():
                repite_nombre = True

        if not repite_nombre:
            nombre_correcto = True
        else:
            print("El nombre ingresado ya existe")

    return nombre_jugador.lower()

def solicitar_nombres_jugadores():
"""
    #Solicita el ingreso de los nombres de los jugadores. Valida que no sean más de 5 y que no se repitan.
    #Devuelve una lista con los nombres.
"""
    nombres_jugadores = []
    numero_jugador = 1

    print(f"Jugador {numero_jugador}")
    nombre = solicitar_nombre(nombres_jugadores)

    while nombre != "" and numero_jugador <= 5:
        numero_jugador += 1
        nombres_jugadores.append(nombre)

        if numero_jugador <= 5:
            print(f"Jugador {numero_jugador}")
            nombre = solicitar_nombre(nombres_jugadores)

    return nombres_jugadores
"""