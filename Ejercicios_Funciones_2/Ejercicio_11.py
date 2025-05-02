def ingreso_int() -> float:
    ingreso_float = float(input("Ingrese un número entero:\n"))
    while ingreso_float < 0: 
        ingreso_float = float(input("ERROR, valor no válido. Por favor, ingrese un número entero:\n"))
    return ingreso_float