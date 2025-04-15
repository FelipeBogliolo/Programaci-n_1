cantidad = 0 

pares = 0
impares = 0

menor = 0
bandera_primer_menor = True

mayor_numero_par = 0
bandera_primer_mayor_par = True

suma_positivos = 0
producto_negativos = 0
bandera_primer_negativo = True

while cantidad < 5:
    ingreso = int(input("Ingrese 5 números:\n"))
    cantidad += 1
    #PARES
    if ingreso % 2 == 0:
        pares += 1
        #MAYOR PAR
        if bandera_primer_mayor_par == True or ingreso > mayor_numero_par:
            mayor_numero_par = ingreso
            bandera_primer_mayor_par = False
    #IMPARES
    else:
        impares += 1
    #NÚMERO MENOR
    if bandera_primer_menor == True or ingreso < menor:
        menor = ingreso
    #SUMA POSITIVOS
    if ingreso > 0:
        suma_positivos += ingreso
    #PRODUCTO NEGATIVOS
    else:
        if bandera_primer_negativo == True:
            producto_negativos = ingreso
            bandera_primer_negativo = False
        else:
            producto_negativos *= ingreso
    
#PRINT
print(f"La cantidad de pares ingresados fue de {pares}, y la cantidad de impares fue de {impares}")
print(f"El menor número ingresado es {menor}")
print(f"De los pares el mayor ingresado fue {mayor_numero_par}")
print(f"La suma de los positivos es igual a {suma_positivos}")
print(f"El producto de los negativos es igual a {producto_negativos}")