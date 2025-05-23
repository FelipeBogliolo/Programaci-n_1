entrada = [10, 20, 30, 40]
valor = 24



def calcular_promedio(lista, valor):
    acum = 0
    contador = 0
    for i in range(len(lista)):
        acum += lista[i]
        contador += 1
    promedio = acum / contador
    if promedio > valor:
        return True
    else:
        return False

prueba = calcular_promedio(entrada, valor)
print(prueba)