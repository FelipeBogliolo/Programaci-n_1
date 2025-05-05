def lista_numeros() -> list:
    lista_numeros = [0] * 10
    for i in range(len(lista_numeros)):
        ingreso_valor = int(input("Ingrese el valor:\n"))
        while ingreso_valor < 1 or ingreso_valor > 100:
            ingreso_valor = int(input("ERROR. Ingrese un valor válido (entre 1 y 100):\n"))
        lista_numeros[i] = ingreso_valor
        seguir = input("¿Quiere ingresar otro valor? Ingrese 'Si' o 'No'\n")
        if seguir != "Si":
            break
    return lista_numeros

lista  = lista_numeros()
for i in range(len(lista)):
    print(lista[i])