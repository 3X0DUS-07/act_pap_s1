n = int(input("Introduce un número entero positivo: "))

if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    contador = 1
    
    while contador <= n:
        factorial *= contador
        contador += 1
    
    print(f"El factorial de {n} es: {factorial}")
