# Dado un número entero n, imprimir todos los números primos menores o iguales a n.

n = input("ingrese un numero: ")
numero = int(n)
i = 2

while i <= numero:
    es_primo = True
    j = 2

    # verificar si el número actual es primo o no
    while j <= i // 2:
        if i % j == 0:
            es_primo = False
            break
        j += 1

    # si el número es primo, imprimirlo
    if es_primo:
        print(i)

    i += 1
