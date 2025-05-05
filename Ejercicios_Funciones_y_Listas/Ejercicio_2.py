def lista_numeros() -> list:
    lista_numeros = [0] * 10
    for i in range(len(lista_numeros)):
        ingreso_valor = int(input("Ingrese el valor:\n"))
        ingreso_posicion = int(input("Ingrese la posición:\n"))
        while ingreso_posicion < 0 or ingreso_posicion > 9:
            ingreso_posicion = int(input("ERROR. Ingrese una posición válida (0 a 9):\n"))
        lista_numeros[ingreso_posicion] = ingreso_valor
        seguir = input("¿Quiere ingresar otro valor? Ingrese 'Si' o 'No'\n")
        if seguir != "Si":
            break
    return lista_numeros

lista  = lista_numeros()
for i in range(len(lista)):
    print(lista[i])