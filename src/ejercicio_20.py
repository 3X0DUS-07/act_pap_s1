edad_mayor = None

while True:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad_mayor is None or edad > edad_mayor:
        edad_mayor = edad

if edad_mayor is not None:
    print("La edad mayor ingresada es:", edad_mayor)
else:
    print("No se ingresaron edades.")
