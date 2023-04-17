# Dada una lista de números, imprimir la cantidad de números negativos en la lista.

numeros = [2, -5, 10, -8, 0, -3, 7, -1, -4]

contador_negativos = 0

for numero in numeros:
    if numero < 0:
        contador_negativos += 1

print("La cantidad de números negativos en la lista es:", contador_negativos)
