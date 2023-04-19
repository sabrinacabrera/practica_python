# Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación,
# nombre, edad y tipo de membresía(por ejemplo, mensual o anual). 
# La información se encuentra almacenada en una lista de listas, donde cada sublista 
# representa a un miembro y contiene los siguientes elementos: número de identificación, 
# nombre, edad y tipo de membresía.

# Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

# Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación,
# nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a la lista de diccionarios.


# Mostrar toda la información de todos los miembros(número de identificación, nombre, 
# edad y tipo de membresía).

# Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario 
# que ingrese el número de identificación del miembro y el nuevo tipo de membresía. 
# El programa debe buscar el miembro en la lista de diccionario y actualizar el tipo de membresía correspondiente.

# Buscar información de un miembro: el programa debe pedir al usuario que ingrese 
# el número de identificación del miembro. El programa debe buscar el miembro en 
# la lista de diccionarios y mostrar su nombre, edad y tipo de membresía.

# Calcular el promedio de edad de los miembros: el programa debe recorrer la 
# lista de diccionarios y calcular el promedio de edad de los miembros.

# Buscar el miembro más joven y el más viejo: el programa debe buscar la edad 
# máxima y mínima en la lista de diccionarios y mostrar el nombre y número de identificación correspondientes.

# El programa debe permitir al usuario realizar estas operaciones tantas veces 
# como desee, hasta que decida salir del programa. El programa debe mostrar un menú 
# de opciones para que el usuario pueda elegir la operación que desea realizar.


miembros = []

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("Ingrese la opción deseada: ")

    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        id = input("Ingrese ID: ")
        nombre = input("Ingrese  nombre: ")
        edad = int(input("Ingrese  edad: "))
        tipo_membresia = input(
            "Ingrese tipo de membresía (mensual o anual): ")

        nuevo_miembro = {"id": id, "nombre": nombre,"edad": edad, "tipo_membresia": tipo_membresia}
        miembros.append(nuevo_miembro)

    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        print("\n---Información de todos los miembros---")
        for miembro in miembros:
            print(f" {miembro['id']},  {miembro['nombre']}, {miembro['edad']}, {miembro['tipo_membresia']},end= " " ")

    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id = input("Ingrese el ID del miembro: ")
        
        tipo_membresia = input(
            "Ingrese el nuevo tipo de membresía (mensual o anual): ")
        for miembro in miembros:
            if miembro['id'] == id:
                miembro['tipo_membresia'] = tipo_membresia
                print("Tipo de membresía actualizado con éxito.")
                break
        else:
            print("ERROR.Miembro no encontrado.")
            
   # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id = input("Ingrese el número de identificación del miembro: ")
        for miembro in miembros:
            if miembro['id'] == id:
                print(
                    f"Nombre: {miembro['nombre']}, Edad: {miembro['edad']}, Tipo de membresía: {miembro['tipo_membresia']}")
                break
        else:
            print("Miembro no encontrado.")

    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        
        total_edades = 0
        for miembro in miembros:
            total_edades += miembro['edad']
        promedio_edad = total_edades / len(miembros)
        print(f"El promedio de edad de los miembros es: {promedio_edad}")

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        miembro_mas_joven = miembros[0]
        miembro_mas_viejo = miembros[0]
        for miembro in miembros:
            if miembro['edad'] < miembro_mas_joven['edad']:
                miembro_mas_joven = miembro
            if miembro['edad'] > miembro_mas_viejo['edad']:
                miembro_mas_viejo = miembro
        print(f"El miembro más joven es: {miembro_mas_joven['nombre']} (ID: {miembro_mas_joven['id']}) con {miembro_mas_joven['edad']} años.")
        print(f"El miembro más viejo es: {miembro_mas_viejo['nombre']}(ID: {miembro_mas_viejo['id']}) con {miembro_mas_viejo['edad']} años ")

    # Opcion 0: Salir
    elif opcion == "0":
        break

    else:
        print("Opción inválida. Intente de nuevo.")
