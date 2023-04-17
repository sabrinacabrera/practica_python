# Escribir un programa que le pida al usuario que ingrese una letra, 
# y luego imprima "Es una vocal" si la letra es una vocal(a, e, i, o, u), 
# o "Es una consonante" si la letra es una consonante.

letra=input("Ingrese una letra:")

if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    print("es una vocal")
else:
    print("es una consonante")