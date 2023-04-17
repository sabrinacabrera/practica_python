# Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.

texto = input("Ingrese una cadena de texto: ")
longitud = len(texto)
indice = 0

while indice < longitud:
    print(texto[indice])
    indice = indice + 1
