# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número es múltiplo de 4 y de 6" 
# si el número es múltiplo de 4 y de 6, 
# o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.


numero = input("Ingresa un número entero: ")
numero_int= int(numero)

if numero_int % 4 == 0 and numero_int % 6 == 0:
    print("El número es múltiplo de 4 y de 6")
else:
    print("El número no es múltiplo de 4 y de 6")
