ingreso = int(input("Ingrese un número:\n"))
cantidad_divisores = 0

print(f"Los divisores de {ingreso} son:")
for i in range(1, ingreso + 1):
    if ingreso % i == 0:
        cantidad_divisores += 1
        print(i, end = " ")

print(f"\nLa cantidad de divisores encontrados son {cantidad_divisores}.")