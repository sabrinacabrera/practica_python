# Dada una lista de números, imprimir todos los números 
# que son mayores que el número anterior en la lista.


lista_numeros = [3, 5, 2, 8, 1, 9, 4] 
indice = 1

while indice < len(lista_numeros):
    if lista_numeros[indice] > lista_numeros[indice-1]:
        print(lista_numeros[indice],end= " ")
    indice = indice + 1
