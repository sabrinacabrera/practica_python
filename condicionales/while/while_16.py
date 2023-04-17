# Dada una lista de números, imprimir todos los números que son múltiplos de 3.

numeros = [5, 3, 9, 12, 8, 15, 7, 21, 30]
indice = 0

while indice < len(numeros):
    if numeros[indice] % 3 == 0:
        print(numeros[indice], end=" ")
    indice = indice + 1
