def sumar_naturales(numero: int) -> int:
    if numero == 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)

print(sumar_naturales(5))
