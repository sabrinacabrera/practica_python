
# Escribir un programa que le pida al usuario que ingrese un número entero positivo,
# y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto, 
# o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.

import math

numero = int(input("Ingrese un número entero positivo: "))

raiz = math.sqrt(numero)

if raiz.is_integer():
    print("El número es un cuadrado perfecto")
else:
    print("El número no es un cuadrado perfecto")
