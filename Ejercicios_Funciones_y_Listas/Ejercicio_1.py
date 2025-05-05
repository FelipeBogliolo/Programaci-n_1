def lista_nombres() -> list:
    lista_nombres = [] 
    for i in range(1, 11):
        ingreso_nombre = input(f"Ingrese 10 nombres, este es el número {i}:\n")
        lista_nombres += [ingreso_nombre]
    return lista_nombres

lista_nombres = lista_nombres()
for i in range(len(lista_nombres)):
    print(lista_nombres[i])