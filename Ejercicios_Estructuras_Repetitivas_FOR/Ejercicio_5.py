suma = 0
promedio = 0

for numero in range(10, 0, -1):
    ingreso = int(input(f"Ingrese 10 números, le faltan {numero}\n"))
    suma += ingreso

promedio = ingreso / 10
print(f"La suma de todos los números es igual a {suma} y su promedio es igual a {numero}.")