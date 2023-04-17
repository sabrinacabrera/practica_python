#Escribir un programa que le pida al usuario que ingrese su nombre, 
#y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro",
# o "Hola desconocido" si el nombre ingresado no es uno de esos tres.

nombre=input("ingrese un nombre: ")

if nombre.lower() == 'juan' or nombre.lower() == 'jaría' or nombre.lower() == 'pedro':
    print("Hola",nombre)
else:
    print("Hola desconocido")
