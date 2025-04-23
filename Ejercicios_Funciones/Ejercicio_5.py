def restar_1(numero_1, numero_2) -> int:
    resta = numero_1 - numero_2
    return resta

def restar_2() -> int:
    numero_1 = int(input("Ingrese el primer número:\n"))
    numero_2 = int(input("Ingrese el primer número:\n"))
    resta = numero_1 - numero_2
    return resta

def restar_3(numero_1, numero_2):
    resta = numero_1 - numero_2
    return resta

def restar_4():
    numero_1 = int(input("Ingrese el primer número:\n"))
    numero_2 = int(input("Ingrese el primer número:\n"))
    resta = numero_1 - numero_2
    return resta

while True:
    opcion = int(input("Ingrese la función que quiere utilizar:\n"
                    "1)Restar1(int,int) -> int\n"
                    "2)Restar2() -> int\n"
                    "3)Restar3(int,int)\n"
                    "4)Restar4()\n"
                    "5)Salir\n"))
    match opcion:
        case 1:
            numero_1 = int(input("Ingrese el primer número:\n"))
            numero_2 = int(input("Ingrese el segundo número:\n"))
            print(restar_1(numero_1, numero_2))
        case 2:
            print(restar_2())
        case 3:
            numero_1 = int(input("Ingrese el primer número:\n"))
            numero_2 = int(input("Ingrese el segundo número:\n"))
            print(restar_3(numero_1, numero_2))
        case 4:
            print(restar_4())
        case 5:
            print("Gracias por usar el programa.")
            break


        