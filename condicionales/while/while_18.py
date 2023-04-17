# Dado un número entero n, imprimir la suma de todos 
# los números que son múltiplos de 5 menores o iguales a n.

n = input("Ingrese su numero: ")
numero= int(n)
suma = 0
indice = 5

while indice <= numero:
    suma += indice
    indice = indice+5

print(suma)
