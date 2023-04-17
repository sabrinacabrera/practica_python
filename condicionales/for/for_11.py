# Dado un número entero n, imprimir la secuencia de números
# primos menores o iguales a n.

n = input("Ingrese un número entero: ")
numero= int(n)
es_primo = True

for num in range(2, numero+1):
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    # si el número es primo, se imprime
    if es_primo:
        print(num,end= " ")
