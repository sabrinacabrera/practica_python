# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo,
#"El segundo número es mayor" si el segundo número es mayor que el primero,
#o "Los dos números son iguales" si los dos números son iguales.

numero_texto_uno = input("Ingrese un numero entero: ")
numero_int_uno = int(numero_texto_uno)

numero_texto_dos = input("Ingrese un numero entero: ")
numero_int_dos = int(numero_texto_dos)

# Comparamos los números e imprimimos el resultado
if numero_int_uno > numero_int_dos:
    print("El primer número es mayor")
elif numero_int_dos > numero_int_uno:
    print("El segundo número es mayor")
else:
    print("Los dos números son iguales")
