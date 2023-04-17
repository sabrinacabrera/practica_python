# Escribir un programa que le pida al usuario que ingrese un número entero positivo
# , y luego imprima "El número ingresado es positivo" si el número es mayor que cero,
#  o "El número ingresado es cero o negativo" si el número es menor o igual a cero.

numero_texto= input("Ingrese un numero: ")
numero_int=int(numero_texto)


if numero_int>0:
    print("El número ingresado es positivo")
else:
    print("El número ingresado es cero o negativo")
