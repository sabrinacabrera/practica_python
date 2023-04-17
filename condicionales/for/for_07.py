# Dado un número entero n, imprimir la secuencia de números
#  impares menores o iguales a n.

n = input("Ingrese un número entero: ")
numero = int(n)

for i in range(1, numero+1, 2):
    print(i, end=" ")
