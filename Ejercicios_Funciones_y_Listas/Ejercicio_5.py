nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
        "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def busqueda_menor_edad(lista_edades: list) -> list:
    menor_edad = 0
    indice = []
    bandera_primer_ingreso = True
    for i in range(len(lista_edades)):
        if bandera_primer_ingreso == True or lista_edades[i] <= menor_edad:
            menor_edad = lista_edades[i]
            indice += [i]
            bandera_primer_ingreso = False
    return indice

indice = busqueda_menor_edad(edades)
for i in indice:
    print(f"{nombres[i]} - {edades[i]} años")