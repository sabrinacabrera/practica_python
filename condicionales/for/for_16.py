# Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

palabras = ["hola", "adios", "python", "programacion", "computadora"]
letra_especifica = "o"

for palabra in palabras:
    if letra_especifica in palabra:
        print(palabra)
