entrada = [10, 20, 30, 40] #lista de numeros, parametro actual
valor = 24 #parametro actual

def calcular_promedio(lista, valor): #parametros formales lista y valor
    acum = 0 #acumulador para sumar valores de la lista
    contador = 0 #contador que cuenta cada valor que contiene la lista
    for i in range(len(lista)): #recorre la lista completra
        acum += lista[i] #suma cada valor en el acumulador
        contador += 1 #suma 1 al contador por cada valor que contiene la lista
    promedio = acum / contador #calcula un promedio entre valores de ambas variables
    if promedio > valor: #compara valores y de acuerdo a eso retorna True (en caso de que el promedio es mayor)
        return True      #False en caso de que sea menor.
    else:
        return False

prueba = calcular_promedio(entrada, valor) #la variable prueba invoca la funcion y luego toma el valor del retorno
print(prueba) #printeamos el valor de la variable prueba, en este caso 'True'