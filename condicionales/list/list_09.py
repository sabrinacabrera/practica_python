# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. 
# Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra. 
# Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró


numeros = [10, 20, 30, 40, 50]

nuevo_num= input("Ingrese un numero ")
num= int(nuevo_num)
numeros.append(num)

# print(numeros)

if num in numeros:
    posicion = numeros.index(num)
    print(f"El número {num} se encuentra en la posición {posicion} de la lista.")
else:
    print("El número no se encuentra en la lista.")


