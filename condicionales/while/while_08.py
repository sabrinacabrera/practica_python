# Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

texto = input("Ingrese un texto: ")  
cantidad_vocales = 0
vocales = ["a", "e", "i", "o", "u"]
i = 0

while i < len(texto):
  
    if texto[i].lower() in vocales:
        cantidad_vocales += 1
    i += 1

print("La cantidad de vocales en la cadena de texto es:", cantidad_vocales)
