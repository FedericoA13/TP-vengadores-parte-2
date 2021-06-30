import diccionario
import ahorcado
import constantes as const
import random
 

def seleccion_palabra(desea_letras,cant_letras): #Cambie esta valiable para que acepte si desea letras o no y cuantas
    """
    Autor: Federico Aldrighetti.

    Esta función pregunta al usuario si quiere jugar con una cantidad determinada de letras. Si dice que sí,
    le pide que especifique la cantidad y le da la palabra con esa longitud validada. En caso contrario, le
    proporciona una palabra con una longitud al azar.
    """

    dicc = diccionario.devolver_diccionario()

    if desea_letras.lower() == 'si' or desea_letras.lower() == "no" :
        while not cant_letras.isnumeric() or diccionario.elegir_palabra(dicc, int(cant_letras)) == None:
            if not cant_letras.isnumeric():
                cant_letras = input('Ingrese cantidad de letras correcta: ')
            elif diccionario.elegir_palabra(dicc, int(cant_letras)) == None:
                cant_letras = input(
                    f'No hay palabras con esa longitud. Elige una longitud entre {const.LONGITUD_MINIMA_PALABRA} y {const.LONGITUD_MAXIMA_PALABRA}: ')

        palabra_adivinar = diccionario.elegir_palabra(dicc, int(cant_letras))
        
    else:
        palabra_adivinar = seleccion_palabra(input(const.INTRODUZCA_COMANDO_DE_NUEVO))

    return palabra_adivinar


def jugar_una_partida():
    """
    Autor: Facundo Sanso.

    La función inicializa la partida
    """
    nombres_jugadores = ahorcado.solicitar_nombres_jugadores() #Crea la lista con los nombres
    ahorcado.informar_turnos_jugadores(nombres_jugadores)
    saber_si_quiere_letras = input(const.DESEA_LETRAS) #Pregunta si quiere letras
    if saber_si_quiere_letras == "si":
        cant_letras = input('Cuantas letras? ')
    elif saber_si_quiere_letras == "no":
        lista = list(range(5,16)) #En el caso de "no" se crea una lista con las longuitudes que tenemos
        cant_letras = str(random.choice(lista)) #Se elige un numero al azar de esa lista que sera la cantidad de letras
    else:
        cant_letras = 0 #Ignorar
    palabras_asignadas = {} #Diccionario con nombres de los jugadores y su palabra asignada
    for jugador in jugadores:
        palabra_a_adivinar = seleccion_palabra(saber_si_quiere_letras,cant_letras)#Por cada jugador elige una palabra
        palabras_asignadas[jugador] = palabra_a_adivinar #Las sube al diccionario
    print (palabras_asignadas)#Para ver la lista
    
        
    return ahorcado.jugar_ahorcado(palabra_a_adivinar) 


def jugar_multiples_partidas():
    """
    Autor: Facundo Sanso.

    Esta función aparece al finalizar una partida. Le da una opción al usuario de seguir jugando. En caso de
    decir que no, devuelve el puntaje final y un mensaje de despedida.
    En caso de que la respuesta sea positiva, el programa inicializará una partida nueva.
    """
    puntaje = jugar_una_partida()

    seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    while seguir_jugando.lower() == "si":
        puntaje += jugar_una_partida()
        seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    print(f"\nPuntaje total = {puntaje}")
    print(const.MENSAJE_DESPEDIDA)


jugar_multiples_partidas()
