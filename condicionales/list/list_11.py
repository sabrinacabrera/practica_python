# Crea una lista de palabras y pide al usuario que ingrese una palabra. 
# Luego, muestra todas las palabras de la lista que tienen 
# la misma longitud que la palabra ingresada.

lista_palabras = ["Hermione", "harry", "kiwi", "watermelon","Ron","jon","Daenerys","Luna"]

palabra_ingresada = input("Ingrese una palabra")

longitud_palabra_ingresada = len(palabra_ingresada)

palabras_con_la_misma_longitud = [palabra for palabra in lista_palabras if len(palabra) == longitud_palabra_ingresada]

print("Palabras con la misma longitud que", palabra_ingresada + ":")
for palabra in palabras_con_la_misma_longitud:
    print(palabra)
