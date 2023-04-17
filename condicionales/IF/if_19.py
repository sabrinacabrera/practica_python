# Escribir un programa que le pida al usuario que ingrese su edad,
# y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18,
# "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
# o "Eres menor de edad" si la edad es menor que 13.

numero = input("Ingresa tu edad: ")
edad=int(numero)

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13 and edad <= 17:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
