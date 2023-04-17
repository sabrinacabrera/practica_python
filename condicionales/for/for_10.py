# Dada una lista de palabras, imprimir las palabras que comienzan
#  y terminan con la misma letra.

palabras = ["Anastasia", "ryan", "lola", "oso", "Andrea"]

for palabra in palabras:
    if palabra[0].lower() == palabra[-1].lower():
        print(palabra)
