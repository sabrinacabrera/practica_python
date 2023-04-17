# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es positivo" 
# si el primer número es mayor que cero, "El segundo número es positivo"
# si el segundo número es mayor que cero, o "Ambos números son negativos"
# si los dos números son negativos.

numero_uno= input("ingrese un numero entero ")
uno= int(numero_uno)

numero_dos= input("ingrese un segundo numero entero ")
dos= int(numero_dos)

if(uno > 0):
    print("El primer número es positivo")


if (dos> 0):
    print("El segundo número es positivo")

elif(uno < 0 and dos < 0):
    print("Ambos números son negativos")



