def ingreso_int() -> float:
    ingreso_float = float(input("Ingrese un número entero:\n"))
    while ingreso_float < 0: 
        ingreso_float = float(input("ERROR, valor no válido. Por favor, ingrese un número entero:\n"))
    return ingreso_float

def ingreso_int() -> int:
    ingreso_int = int(input("Ingrese un número entero:\n"))
    while ingreso_int < 0: 
        ingreso_int = int(input("ERROR, valor no válido. Por favor, ingrese un número entero:\n"))
    return ingreso_int

def ingreso_cadena() -> str:
    ingreso = input("Ingrese una cadena:\n")
    while ingreso == "":
        ingreso = input("ERROR. Ingrese una cadena no vacía:\n")
    return ingreso

