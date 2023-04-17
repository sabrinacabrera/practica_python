# Dado un número entero n, imprimir la suma de todos 
# los números pares menores o iguales a n.


n = int(input("Ingrese un número entero: "))
numero= int(n)
suma_pares = 0
i = 0

while i <= numero:
    if i % 2 == 0:
        suma_pares += i
    i += 1

print("La suma de todos los números pares menores o iguales a",
      numero, "es:", suma_pares)
 