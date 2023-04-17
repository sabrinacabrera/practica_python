# Crea una lista vacía y pide al usuario que ingrese una palabra. 
# Luego, muestra la primera letra de la palabra. 
# Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

list_letras = []

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra[0] == 'z':
        break
    list_letras.append(palabra[0])
    print(palabra[0])

print("El usuario ingresó una palabra que comienza con 'z'. Fin del programa.")
