frase = "programacion es divertida"
vocales = "aeiou"
contador = 0

for caracter in frase.lower():
    if caracter in vocales:
        contador += 1

print("Número total de vocales:", contador)
