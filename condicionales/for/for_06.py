# Dada una lista de palabras, imprimir la cantidad total 
# de vocales en la lista.

lista = ["lunes", "martes", "miercoles", "jueves", "viernes"]

vocales = "aeiouAEIOU"
total_vocales = 0

for palabra in lista:
    for letra in palabra:
        if letra in vocales:
            total_vocales += 1

print("La cantidad total de vocales en la lista es:", total_vocales)
