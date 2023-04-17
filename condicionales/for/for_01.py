# Dada una lista de números, imprimir el número más grande de la lista.

lista = [2, 5, 7, 1, 10, 4, 6]

max = lista[0]

for numero in lista:
    if numero > max:
        max = numero

print("El número más grande es:", max)
