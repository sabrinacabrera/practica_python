# Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

palabras = ["hilo", "aguaja", "lana", "del", "rey", "trueno", "aurora"]
palabras_impares = []

for palabra in palabras:
    if len(palabra) % 2 != 0:
        palabras_impares.append(palabra)

print("Las palabras con longitud impar son:", palabras_impares)
