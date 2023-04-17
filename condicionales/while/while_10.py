# Dada una lista de números, imprimir la cantidad de números pares en la lista.

numeros = [2, 5, 6, 7, 8, 10, 12]  
cantidad_pares = 0
i = 0

while i < len(numeros):  
    if numeros[i] % 2 == 0:
        cantidad_pares += 1
    i += 1

print("La cantidad de números pares en la lista es:", cantidad_pares)
