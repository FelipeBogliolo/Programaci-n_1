def ingreso_int() -> int:
    ingreso_int = int(input("Ingrese un número entero:\n"))
    while ingreso_int < 0: 
        ingreso_int = int(input("ERROR, valor no válido. Por favor, ingrese un número entero:\n"))
    return ingreso_int
