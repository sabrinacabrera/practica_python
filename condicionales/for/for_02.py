# Dada una lista de palabras, imprimir la palabra más larga de la lista.

lista = ["Harry", "Ron", "thanos", "Dumbledore", "Thonks"]

palabra_max = lista[0]

for palabra in lista:
    if len(palabra) > len(palabra_max):
        palabra_max = palabra

print("La palabra más larga es:", palabra_max)
