estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro",
            "Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui",
            "Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def mayor_primer_ingreso(lista, posicion_1, posicion_2):
    # Intercambiar estudiantes
    auxiliar = lista[posicion_1]
    lista[posicion_1] = lista[posicion_2]
    lista[posicion_2] = auxiliar
    # Intercambiar apellidos
    auxiliar_apellidos = apellidos[posicion_1]
    apellidos[posicion_1] = apellidos[posicion_2]
    apellidos[posicion_2] = auxiliar_apellidos
    # Intercambiar notas
    auxiliar_nota = nota[posicion_1]
    nota[posicion_1] = nota[posicion_2]
    nota[posicion_2] = auxiliar_nota

def ordenamientos_letras(lista) -> list:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                mayor_primer_ingreso(lista, i, j)
            elif lista[i] == lista[j]:
                if apellidos[i] > apellidos[j]:
                    mayor_primer_ingreso(lista, i, j)
                elif apellidos[i] == apellidos[j]:
                    if nota[i] > nota[j]:
                        mayor_primer_ingreso(lista, i, j)
    return lista
