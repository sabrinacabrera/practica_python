# Dada una lista de números, imprimir la cantidad de números negativos en la lista.

numeros = [10, -5, 8, -3, -2, 0, 7, -9, 4]

i = 0
cant_negativos = 0

while i < len(numeros):
    if numeros[i] < 0:
        cant_negativos += 1
    i += 1

print("La cantidad de números negativos en la lista es:", cant_negativos)
