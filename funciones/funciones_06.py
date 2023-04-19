# Crear una función que calcule el área de un triángulo. 
# Recibe dos parámetros (base y altura) y devuelve el área.

base= input("Ingrese la base del triangulo: ")
base_int= int(base)

altura= input("Ingrese la altura del triangulo : ")
altura_int= int(altura)


def calcular_area_triangulo(base_int, altura_int):
    """
    Esta función calcula el area de un triangulo.
    :param base_int: base del triangulo .
    :param altura_int: altura del triangulo  .
    :return:area del triangulo.
    """
    area = (altura_int * altura_int)/2
    return area


area_triangulo = calcular_area_triangulo(altura_int, altura_int)

print("El area del triaungulo es : ",area_triangulo)