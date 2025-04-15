ingreso = int(input("Ingrese un número:\n"))
no_divisor = False

for i in range(1, ingreso):
    if ingreso % i == 0:
        divisor = True


if divisor == False:
    print("El número NO es primo.")
else:
    print("El número es compuesto.")