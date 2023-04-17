# Dado un número entero n, imprimir la secuencia de números 
# perfectos menores o iguales a n.

n = input("Ingrese un número entero: ")
numero = int(n)
suma_divisores = 0

for num in range(1, numero+1):
    
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
            
    if suma_divisores == num:
        print(num)
