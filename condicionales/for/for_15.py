# Dada una lista de números, imprimir la cantidad de números impares en la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cantidad_impares = 0

for numero in numeros:
    if numero % 2 != 0:
        cantidad_impares = cantidad_impares+ 1

print("La cantidad de números impares en la lista es:", cantidad_impares)
