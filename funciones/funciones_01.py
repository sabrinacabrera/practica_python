# Crear una función que convierta grados Celsius a grados Fahrenheit. 
# Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

def celsius_a_fahrenheit(celsius):
    """
    Esta función convierte grados celsius a grados fahrenheit.

    :param celsius: un número que representa grados Celsius.
    :return: el equivalente en grados Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


print(celsius_a_fahrenheit(100))
