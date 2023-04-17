# escribir un programa en python con while que Dado un número entero n,
# imprimir todos los números perfectos menores o iguales a n. 
# Los números perfectos son aquellos números enteros positivos que 
# son iguales a la suma de sus divisores propios(excluyendo al propio número). 
# En otras palabras, si sumamos todos los divisores propios de un número
# (excluyendo el número en sí mismo) y el resultado es igual al número, 
# entonces ese número se considera un número perfecto.
# Por ejemplo, el primer número perfecto es 6, ya que sus divisores 
# propios son 1, 2 y 3, y 1 + 2 + 3 = 6. Otros ejemplos de números perfectos 
# son 28, 496 y 8128. Actualmente se conocen más de 50 números perfectos, y 
# se cree que existen infinitos números perfectos, aunque no se ha 
# podido demostrar matemáticamente esta afirmación.


n = input("Ingresa un número entero positivo: ")
numero= int(n)
indice = 1

while indice <= numero:
    divisores = []
    j = 1
    while j < indice:
        if indice % j == 0:
            divisores.append(j)
        j += 1
    if sum(divisores) == indice:
        print(indice)
    indice = indice + 1
