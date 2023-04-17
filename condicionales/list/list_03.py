# Crea una lista vacía y pide al usuario que ingrese números enteros 
# hasta que ingrese un número negativo. Luego, muestra la suma de todos 
# los números ingresados.



lista_numeros= []
suma=0
numero = int(input("ingrese un numero entero (o negativo para terminar el programa): "))

while numero > 0:
    lista_numeros.append(numero)
    suma = suma+numero
    numero = int(input("ingrese un numero entero (o negativo para terminar el programa): "))

    


print("la suma de los numeros ingresados es ",suma)

