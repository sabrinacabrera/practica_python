# Dada una lista de números, imprimir todos los números 
# que son mayores que el promedio de la lista.

numeros = [1, 2, 3, 4, 5] 
promedio = sum(numeros) / len(numeros)
i = 0

while i < len(numeros):
    if numeros[i] > promedio:
        print(numeros[i])
    i += 1
