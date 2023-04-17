# Dada una lista de palabras, imprimir todas las palabras 
# que tengan una longitud mayor a 5 caracteres.

palabras = ["Accio", "Alohomora", "Expelliarmus", "Crucio", "Lumos",
            "Nox", "Imperius"]  # reemplace esto con su lista de palabras

# inicializar la variable de índice en cero
i = 0

# imprimir todas las palabras con una longitud mayor a 5 caracteres
while i < len(palabras):
    if len(palabras[i]) > 5:
        print(palabras[i])
    i += 1
