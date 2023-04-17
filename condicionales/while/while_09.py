# Dado un número entero n, imprimir todos los números impares menores o iguales a n.

n = input("ingrese un numero: ")
numero= int(n)
numero_impar = 1


while numero_impar <= numero:
    print(numero_impar)
    numero_impar += 2
