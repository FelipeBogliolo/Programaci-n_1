lista_numeros = [10, 5, 8, 7, 6, 4, 3]

def encontrar_numero(lista: list, numero: int) -> bool:
    for i in range(len(lista)):
        if lista[i] == numero:
            return True
            break
        else:
            continue
    return False

variable = encontrar_numero(lista_numeros, 8)
print(variable)

variable = encontrar_numero(lista_numeros, 11)
print(variable)