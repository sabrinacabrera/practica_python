# Dado un número entero n, imprimir la secuencia de números 
# triangulares menores o iguales a n.

n = input("Ingrese un número entero: ")
numero = int(n)
triangular = 0

print("los numeros triangulares menores o iguales a n son ")
for i in range(1, numero+1):
    triangular = i * (i + 1) // 2
    if triangular > numero:
        break
    print(triangular)
