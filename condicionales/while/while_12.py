# Dado un número entero n, imprimir la suma de todos 
# los números impares menores o iguales a n.

n = input("Ingrese un numero: ")
numero= int(n)


suma_impares = 0
num_actual = 1


while num_actual <= numero:
    if num_actual % 2 != 0:
        suma_impares += num_actual
    num_actual += 1

print("La suma de todos los números impares menores o iguales a",
      numero, "es:", suma_impares)
