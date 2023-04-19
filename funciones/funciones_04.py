# Crear una función que calcule el promedio de edad de un grupo 
# de personas. Recibe una lista de edades y devuelve el promedio.

edades=[10,10,10,10,10]

def promedio_edad(edades):
    """
    Esta función determina el promedio de edades de un grupo de personas.
    :param edades : lista de edades a calcular
    :return: promedio calculado.
    """
    promedio= sum(edades)/len(edades)
    return promedio

promedio = promedio_edad(edades)

print("El promedio de edad es: ",promedio)