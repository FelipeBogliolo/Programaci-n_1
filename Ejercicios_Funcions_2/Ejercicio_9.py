def tabla_multiplicar(numero: int) -> int:
    opcional_inicio = input("¿Quiere ingresar un número donde quiere inicializar? Ingrese 'Si' o 'No'. Por defecto es 1.\n")
    opcional_final = input("¿Quiere ingresar un número quiere finalizar? Ingrese 'Si' o 'No'. Por defecto es 10.\n")
    if opcional_inicio == "Si" and opcional_final == "Si":
        ingreso_inicio = int(input("Ingrese donde quiere incializar."))
        ingreso_final = int(input("Ingrese donde quiere finalizar."))
        for i in range(ingreso_inicio, ingreso_final + 1):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    elif opcional_inicio == "Si" and opcional_final == "No":
        ingreso_inicio = int(input("Ingrese donde quiere incializar."))
        for i in range(ingreso_inicio, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    elif opcional_inicio == "No" and opcional_final == "Si":
        ingreso_final = int(input("Ingrese donde quiere finalizar."))
        for i in range(1, ingreso_final + 1):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

tabla_multiplicar(2)