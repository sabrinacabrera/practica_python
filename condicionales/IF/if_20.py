# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "Los dos números son iguales" si los dos números son iguales, 
# "El primer número es mayor" si el primer número es mayor que el segundo, 
# o "El segundo número es mayor" si el segundo número es mayor que el primero.

numero_uno = input("Ingresa el primer número entero: ")
numero_uno_int= int(numero_uno)

numero_dos = int(input("Ingresa el segundo número entero: "))
numero_dos_int = int(numero_dos)

if numero_uno_int == numero_dos_int:
    print("Los dos números son iguales")
elif numero_uno_int > numero_dos_int:
    print("El primer número es mayor")
else:
    print("El segundo número es mayor")
