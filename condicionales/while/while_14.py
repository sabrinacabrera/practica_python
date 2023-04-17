# Dada una cadena de texto, imprimir la cantidad de veces 
# que aparece una letra específica en la cadena.

cadena = input("ingrese su texto: ")
letra = input("ingrese una letra: ")

# inicializar la variable de índice en cero y la cantidad de veces que aparece la letra en cero
i = 0
cant_letra = 0

# contar todas las ocurrencias de la letra en la cadena
while i < len(cadena.lower()):
    if cadena[i] == letra.lower():
        cant_letra += 1
    i += 1

# imprimir la cantidad de veces que aparece la letra en la cadena
print("La letra", letra, "aparece", cant_letra, "veces en la cadena de texto.")
