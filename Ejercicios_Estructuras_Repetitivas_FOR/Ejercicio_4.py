ingreso = int(input("Ingrese el número del cual quiere ver la tabla de multiplicar:\n"))
for numero in range(0, 10):
    resultado = numero * ingreso
    print(f"{numero} * {ingreso} = {resultado}")