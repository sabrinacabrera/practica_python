# Dado un número entero n, imprimir la secuencia de números 
# de Harshad menores o iguales a n.

n = ("Ingrese un número entero: ")
numero = int(n)

for num in range(1, numero+1):
    suma_digitos = sum(int(d) for d in str(num))
    if num % suma_digitos == 0:
        print(num)
