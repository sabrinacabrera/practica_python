
# Escribir un programa que le pida al usuario que ingrese
# un número entero positivo, y luego imprima "El número es primo" 
# si el número es primo, o "El número no es primo" si el número no es primo.

numero = input("Ingresa un número entero positivo: ")
numero_int = int(numero)

if numero_int > 1:
    for indice in range(2, numero_int):
        if (numero_int % indice) == 0:
            print("El número no es primo")
            break
    else:
        print("El número es primo")

