# Crear una función que determine si un número es primo o no.
# Recibe un parámetro(número) y devuelve True si es primo
# y False si no lo es.

numero = input("Ingrese un numero: ")
numero_ingresado = int(numero)


def es_primo(numero_ingresado):
    """
    Esta función determina si un numero es primo o no .
    :param numero: numero a verificar.
    :return: TTRUE si el numero es primo, FALSE sino.
    """
    if numero_ingresado < 2:
        return False
    for i in range(2, int(numero_ingresado ** 0.5)+1):
        if numero_ingresado % i == 0:
            return False
    return True


print(es_primo(numero_ingresado))
