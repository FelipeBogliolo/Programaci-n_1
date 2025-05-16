nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia",
        "Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenamientos_letras(lista) -> list:
    for i in range(len(lista) - 1):
        for j in range (i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
                auxiliar_edad = edades[i]
                edades[i] = edades[j]
                edades[j] = auxiliar_edad
    return lista

lista_ordenada = ordenamientos_letras(nombres)
print(lista_ordenada)
for i in edades:
    print(i)