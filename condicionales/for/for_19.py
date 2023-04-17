# Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.

palabras = ["hola", "Mundo", "adios", "PYTHON", "Programacion"]

print("las palabras que tienen letra mayuscula son:")

for palabra in palabras:
    for letra in palabra:
        if letra.isupper():
            print( palabra)
            break
