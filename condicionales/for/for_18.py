# Dada una lista de números, imprimir la suma de los números 
# en la lista que son mayores que el promedio de la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

promedio = sum(numeros) / len(numeros)

suma_mayores_promedio = 0

for num in numeros:
    if num > promedio:
        suma_mayores_promedio =suma_mayores_promedio + num

print("La suma de los números mayores que el promedio es:", suma_mayores_promedio)
