# Dada una cadena de texto, imprimir la cadena al revés.

cadena = input("ingrese cadena de texto")  # reemplace esto con su cadena de texto
longitud = len(cadena)
indice = longitud - 1

while indice >= 0:
    print(cadena[indice], end=" ")
    indice = indice - 1
