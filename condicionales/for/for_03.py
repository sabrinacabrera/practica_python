# Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.

n = input("Ingrese un número entero: ")
numero = int(n)

for i in range(2, numero +1 , 2):
    print(i, end=" ")
