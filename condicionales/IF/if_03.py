# Escribir un programa que le pida al usuario que ingrese un número entero,
#  y luego imprima "El número ingresado es par" si el número es divisible por 2,
#  o "El número ingresado es impar" si el número no es divisible por 2.

numero_texto = input("Ingrese un numero entero: ")
numero_int = int(numero_texto)

if numero_int %2==0:
    print("El número ingresado es par")
else:
   print("El número ingresado es impar")
