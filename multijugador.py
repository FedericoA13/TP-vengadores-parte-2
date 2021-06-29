import random


def solicitar_nombre(nombres_jugadores):
    """
    Solicita el ingreso de un nombre y valida que no se encuentre en la lista de nombres recibida por parámetro,
    """
    nombre_correcto = False
    nombre_jugador = ""

    while not nombre_correcto:
        repite_nombre = False
        nombre_jugador = input("Ingrese su nombre: ")

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
    Solicita el ingreso de los nombres de los jugadores. Valida que no sean mas de 5 y que no se repitan.
    Devuelve una lista con los nombres.
    """
    nombres_jugadores = []
    numero_jugador = 1
    print(f"Jugador {numero_jugador}")
    nombre = solicitar_nombre(nombres_jugadores)

    while nombre != "" and numero_jugador <= 5:
        numero_jugador += 1
        nombres_jugadores.append(nombre)
        print(f"Jugador {numero_jugador}")
        nombre = solicitar_nombre(nombres_jugadores)

    return nombres_jugadores


#print(solicitar_nombres_jugadores())


def asignar_turno_jugadores(nombres_jugadores, ganador):
    """
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
    Muestra cual es el turno de cada jugador
    """
    for i in range(len(nombres_jugadores)):
        #print(f"El jugador {nombres_jugadores[i]} tiene el turno {i + 1}")
        print(f"Turno {i + 1}: {nombres_jugadores[i]}")

informar_turnos_jugadores(["didy", "facu", "ale"])

def asignar_palabras_jugadores():
    """
    Asigna una palabra aleatoria a cada jugador. Todas las palabras contendrán la misma longitud.
    """
    palabra = seleccion_palabra(input(const.DESEA_LETRAS))
    return {"jugador1": ["palabra", [], []], "jugador2": ["sandia", [], []]}


def jugar_ahorcado_multijugador():
    #´TODO: esto deberia ir en el archivo de integracion
    nombres_jugadores = solicitar_nombres_jugadores()
    nombre_ultimo_ganador = ""

    nombres_jugadores = asignar_turno_jugadores(nombres_jugadores, nombre_ultimo_ganador)
    informar_turnos_jugadores(nombres_jugadores)

    dicc_jugadores = asignar_palabras_jugadores()