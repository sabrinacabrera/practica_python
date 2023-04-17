# Dada una lista de números, imprimir el número más pequeño de la lista.

lista = [2, 5, 7, 1, 10, 4, 6]

min = lista[0]

for numero in lista:
    if numero < min:
        min = numero

print("El número más chico es:", min)
