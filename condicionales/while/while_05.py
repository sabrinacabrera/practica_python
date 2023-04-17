# Dado un número entero n, imprimir si el número es primo o no.

numero = int(input("Ingrese un número entero: "))
numero_int = int(numero)
es_primo = True
divisor = 2

while divisor <= numero_int // 2:
    if numero_int % divisor == 0:
        es_primo = False
        break
    divisor += 1

if es_primo:
    print(numero_int, "es un número primo")
else:
    print(numero_int, "no es un número primo")
