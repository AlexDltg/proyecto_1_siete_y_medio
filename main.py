import random
# Lista con tuplas de los valores de las cartas del mazo
mazo = [(1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1), (2, 1, 2), (2, 2, 2), (2, 3, 2), (2, 4, 2), (3, 1, 3), (3, 2, 3), (3, 3, 3), (3, 4, 3), (4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4), (5, 1, 5), (5, 2, 5), (5, 3, 5), (5, 4, 5), (6, 1, 6), (6, 2, 6), (6, 3, 6), (6, 4, 6), (7, 1, 7),
        (7, 2, 7), (7, 3, 7), (7, 4, 7), (8, 1, 8), (8, 2, 8), (8, 3, 8), (8, 4, 8), (9, 1, 9), (9, 2, 9), (9, 3, 9), (9, 4, 9), (10, 1, 0.5), (10, 2, 0.5), (10, 3, 0.5), (10, 4, 0.5), (11, 1, 0.5), (11, 2, 0.5), (11, 3, 0.5), (11, 4, 0.5), (12, 1, 0.5), (12, 2, 0.5), (12, 3, 0.5), (12, 4, 0.5)]

jugadores = {}

# bucle for para añadir a los jugadores
while len(jugadores) < 8:

    nombre = input("Escribe el nombre de un jugador: ")

    # Comprobamos que el nombre sea alphanumerico y que el primer caracter sea una letra
    if nombre.isalnum() and nombre[0].isalpha():
        # print(nombre)  # DEBUG
        # le generamos una carta al jugador
        carta = random.randrange(len(mazo))
        # agregamos el jugador a la lista, con la carta generada
        jugadores[nombre] = [mazo[carta]]
        continuar = input("Continuas? (Si, No): ")
        if continuar.upper() == "NO":
            break
    else:
        print("El nombre tiene que ser alphanumerico, el primer caracter tiene que ser una letra y no puede contener "
              "espacios!!")

print(jugadores)  # DEBUG