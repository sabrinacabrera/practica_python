#listas
numeros_identificacion = []
nombres = []
edades = []
tipos_membresia = []


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
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        
        identificacion = int(input("Ingresa el número de identificación: "))
        numeros_identificacion.append(identificacion)
        
        nombre = input("Ingresa el nombre del miembro: ")
        nombres.append(nombre)
        
        edad = int(input("Ingresa la edad del miembro: "))
        edades.append(edad)
        
        membresia = input("Ingresa el tipo de membresía del miembro: ")
        tipos_membresia.append(membresia)
        
            
       # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        print("Información de todos los miembros:")
        for i in range(len(numeros_identificacion)):
            print(numeros_identificacion[i],nombres[i], edades[i],tipos_membresia[i])
            print("--------------------")

    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        
        identificacion = int(
        input("Ingresa el número de identificación del miembro: "))
        
        if identificacion in numeros_identificacion:
            
            membresia_nueva = input("Ingresa el nuevo tipo de membresía del miembro: ")
            indice = numeros_identificacion.index(identificacion)
            tipos_membresia[indice] = membresia_nueva
            
            print("Tipo de membresía actualizado correctamente")
            
        else:

            print("Miembro no encontrado")

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        identificacion = int(
        input("Ingresa el número de identificación del miembro: "))
        
        if identificacion in numeros_identificacion:
            
            indice = numeros_identificacion.index(identificacion)
            print("Nombre:", nombres[indice])
            print("Edad:", edades[indice])
            print("ID:", tipos_membresia[indice])
            
        else:
            print("Miembro no encontrado")

    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        
       promedio_edad = sum(edades) / len(edades)
       print("El promedio de edad de los miembros es:", promedio_edad)

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        
        indice_joven = edades.index(min(edades))
        indice_viejo = edades.index(max(edades))
        
        print("Miembro más joven:")
        print("ID:",numeros_identificacion[indice_joven])
        print("Nombre:", nombres[indice_joven])
        
        print("--------------------")
        print("Miembro más viejo:")
        print("ID:",numeros_identificacion[indice_viejo])
        print("Nombre:", nombres[indice_viejo])


    # Opcion 0: Salir
    elif opcion == "0":
        break

    else:
        print("Opción inválida")
