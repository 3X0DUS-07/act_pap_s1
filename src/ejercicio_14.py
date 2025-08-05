import random

numero_secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (del 1 al 10): "))
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número!")
        adivinado = True
    else:
        print("Intenta de nuevo.")
