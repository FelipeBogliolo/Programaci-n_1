def maximo(ingreso_1: int, ingreso_2: int, ingreso_3: int) -> int:
    if ingreso_1 > ingreso_2 and ingreso_1 > ingreso_3:
        return f"El ingreso más grande es {ingreso_1}"
    if ingreso_2 > ingreso_1 and ingreso_2 > ingreso_3:
        return f"El ingreso más grande es {ingreso_2}"
    else:
        return f"El ingreso más grande es {ingreso_3}"
    
print(maximo(4,5,6))