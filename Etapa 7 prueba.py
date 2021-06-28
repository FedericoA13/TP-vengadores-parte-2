import random

palabras = {"holass":0,"perros":0,"gatoss":0}


def multijugador():
    lista_de_jugadores = []
    jugador = input("Nuevo Jugador (Max 5 jugadores)(Presionar enter para dejar de ingresar nombres): ")
    while len (lista_de_jugadores) < 5 and jugador != "":
        if jugador not in lista_de_jugadores:
            lista_de_jugadores.append(jugador)
            jugador = input("Nuevo Jugador (Max 5 jugadores)(Presionar enter para dejar de ingresar nombres): ")
        else:
            print ("El nombre ya fue ingresado")
            jugador = input("Nuevo Jugador (Max 5 jugadores)(Preseionar enter para dejar de ingresar nombres): ")
    if len (lista_de_jugadores) == 5:
        print ("Se alcanzo el numero maximo de jugadores,",jugador,"no pudo ser ingresado")
             
        
    return lista_de_jugadores
  

def orden_de_juego():
    jugadores = multijugador()
    print ("Orden de juego es: ")
    Orden = jugadores
    random.shuffle(Orden)
    
    return Orden


def posiciones_de_inicio():
    orden = orden_de_juego()
    Posicion = 0
    contador = 0
    for palabra in palabras:
        Posicion += 1
        print (Posicion,"_",orden[contador],"-",palabra)
        contador += 1


def main():
    posiciones_de_inicio()


main()
    
    
