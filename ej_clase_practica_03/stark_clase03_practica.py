# Analizar detenidamente el set de datos
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# Calcular e informar cual es el superhéroe más y menos pesado.
# Ordenar el código implementando una función para cada uno de los valores informados.
# Construir un menú que permita elegir qué dato obtener

from data_stark import lista_personajes

# Descomentar para probar que todo va bien
#print(lista_personajes)

while True:
    print("Seleccione la opción deseada:")
    print("1. Análisis detallado del set de datos")
    print("2. Nombre de cada superhéroe")
    print("3. Nombre de cada superhéroe y su altura")
    print("4. Superhéroe más alto")
    print("5. Superhéroe más bajo")
    print("6. Altura promedio de los superhéroes")
    print("7. Identidad del superhéroe más alto")
    print("8. Identidad del superhéroe más bajo")
    print("9. Superhéroe más y menos pesado")
    print("0. Salir del programa")
    opcion = input("Ingrese la opción deseada: ")
