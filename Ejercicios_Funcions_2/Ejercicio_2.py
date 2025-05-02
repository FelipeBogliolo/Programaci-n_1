def area_circulo (radio: int) -> int:
    area = 3.14 * (radio * radio)
    return f"El área del circulo ingresado es {area}"

print(area_circulo(15))