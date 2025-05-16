estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro",
            "Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui",
            "Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def mayor_primer_ingreso(lista, posicion_1, posicion_2):
    auxiliar = lista[posicion_1]
    lista[posicion_1] = lista[posicion_2]
    lista[posicion_2] = auxiliar
    auxiliar_apellidos = apellidos[posicion_1]
    apellidos[posicion_1] = apellidos[posicion_2]
    apellidos[posicion_2] = auxiliar_apellidos
    auxiliar_nota = nota[posicion_1]
    nota[posicion_1] = nota[posicion_2]
    nota[posicion_2] = auxiliar_nota

def ordenamientos_letras(lista) -> list:
    for i in range(len(lista) - 1):
        for j in range (i + 1, len(lista)):
            if lista[i] > lista[j]:
                mayor_primer_ingreso(lista, i, j)

            elif lista[i] == lista[j]:
                if apellidos[i] > apellidos[j]:
                    auxiliar = lista[i]
                    lista[i] = lista[j]
                    lista[j] = auxiliar
                    auxiliar_apellidos = apellidos[i]
                    apellidos[i] = apellidos[j]
                    apellidos[j] = auxiliar_apellidos
                elif apellidos[i] == apellidos[j]:
                    if nota[i] > nota[j]:
                        auxiliar = lista[i]
                        lista[i] = lista[j]
                        lista[j] = auxiliar
                        auxiliar_nota = nota[i]
                        nota[i] = nota[j]
                        nota[j] = auxiliar_nota
                    else:
                        auxiliar = lista[j]
                        lista[j] = lista[i]
                        lista[i] = auxiliar
                        auxiliar_nota = nota[j]
                        nota[j] = nota[i]
                        nota[i] = auxiliar_nota
                else:
                    auxiliar = lista[j]
                    lista[j] = lista[i]
                    lista[i] = auxiliar
                    auxiliar_apellidos = apellidos[j]
                    apellidos[j] = apellidos[i]
                    apellidos[i] = auxiliar_apellidos
    return lista
