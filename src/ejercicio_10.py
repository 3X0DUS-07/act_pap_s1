contador = 0

while True:
    palabra = input("Escribe una palabra (escribe 'fin' para terminar): ")
    if palabra.lower() == "fin":
        break
    contador += 1

print("Cantidad de palabras ingresadas:", contador)
