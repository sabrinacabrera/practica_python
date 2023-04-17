# Dado un número entero n, imprimir todos los números desde n hasta 1 
# en orden descendente.

n = input("Ingrese un número entero: ")
numero = int(n)

while numero > 0:
    print(numero)
    numero = numero-1
