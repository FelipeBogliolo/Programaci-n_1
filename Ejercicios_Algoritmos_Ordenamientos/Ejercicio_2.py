Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales",
        "Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
        "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenamientos_letras(lista) -> list:
    for i in range(len(lista) - 1):
        for j in range (i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
            elif lista[i] == lista[j]:
                if Puntos[i] > Puntos[j]:
                    auxiliar = lista[i]
                    lista[i] = lista[j]
                    lista[j] = auxiliar
                    auxiliar_puntos = Puntos[i]
                    Puntos[i] = Puntos[j]
                    Puntos[j] = auxiliar_puntos
                else:
                    auxiliar = lista[j]
                    lista[j] = lista[i]
                    lista[i] = auxiliar
                    auxiliar_puntos = Puntos[j]
                    Puntos[j] = Puntos[i]
                    Puntos[i] = auxiliar_puntos
    return lista

lista_ordenada = ordenamientos_letras(Nombres)
print(lista_ordenada)
for i in Puntos:
    print(i)