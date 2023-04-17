# Dado un número entero n, imprimir la suma de los números 
# impares menores o iguales a n.

n = input("Ingrese un número entero: ")
numero = int(n)

suma = 0

for i in range(1, numero+1, 2):
    suma += i

print("La suma de los números impares menores o iguales a", numero, "es:", suma)
