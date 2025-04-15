ingreso = int(input("Ingrese la cantidad de niveles de la pirámide: "))

for i in range(1, ingreso + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()