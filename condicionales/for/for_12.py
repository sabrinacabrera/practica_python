# Dada una lista de números, imprimir la cantidad de números pares en la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cantidad_pares = 0

for num in numeros:
    if num % 2 == 0:
        cantidad_pares = cantidad_pares + 1

print("La cantidad de números pares en la lista es:", cantidad_pares)
