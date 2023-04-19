# Crear una función que calcule el descuento aplicado a un producto. 
# Recibe dos parámetros (precio original y precio con descuento) 
# y devuelve el porcentaje de descuento aplicado.

edades = [20, 30, 40, 50]

def promedio_edad(edades):
    """
    Esta función calcula el promedio de edad .
    :param edades: una lista de números de las edades de las personas.
    :return: el promedio.
    """
    suma_edades = sum(edades)
    cantidad_personas = len(edades)
    promedio = suma_edades / cantidad_personas
    return promedio


print("El promedio de las edades es : ",promedio_edad(edades))
