# Dada una lista de números, imprimir la suma de todos los elementos de la lista.

numeros = [3, 8, 2, 10, 5]
indice = 0
suma = 0

while indice < len(numeros):
    suma += numeros[indice]
    indice = indice+1

print("La suma de los números en la lista es:", suma)
