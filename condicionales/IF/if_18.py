
# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es par y es múltiplo de 3" si el número es par 
# y es múltiplo de 3, o "El número no cumple ninguna de las dos condiciones"
# si el número no cumple ninguna de las dos condiciones.

numero = input("Ingresa un número entero: ")
numero_int= int(numero)

if numero_int % 2 == 0 and numero_int % 3 == 0:
    print("El número es par y es múltiplo de 3")
else:
    print("El número no cumple ninguna de las dos condiciones")
