# Crear una función que calcule el área de un círculo. 
# Recibe un parámetro (radio) y devuelve el área del círculo.

import math


def area_circulo(radio):
    """
    calcula el área de un círculo dado su radio.

    :param radio: un número que representa el radio del círculo.
    :return: el área del círculo.
    """
    area = math.pi * (radio ** 2)
    return area


print("Area del circulo: ",area_circulo(10))
