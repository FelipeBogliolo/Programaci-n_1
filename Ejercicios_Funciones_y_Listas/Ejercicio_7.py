from Funciones import *

def menu()-> int:
    while True:
        opcion = int(input("\nIngrese la opción que desea:\n"
                        "1)Importar Lista\n"
                        "2)Listar los datos de los usuarios de México\n"
                        "3)Listar los nombre, mail y teléfono de los usuarios de Brasil\n"
                        "4)Listar los datos del/los usuario/s más joven/es\n"
                        "5)Obtener un promedio de edad de los usuarios\n"
                        "6)De los usuarios de Brasil, listar los datos del usuario de mayor edad\n"
                        "7)Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n"
                        "8)Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n"))
        match opcion:
            case 1:
                opcion_1()
            case 2:
                opcion_2()
            case 3:
                opcion_3()
            case 4:
                opcion_4()
            case 5:
                opcion_5()
            case 6:
                opcion_6()
            case 7:
                opcion_7()
            case 8:
                opcion_8()

        seguir = input("\n¿Desea ingresar otra opción?\n")
        if seguir == "No":
            False
menu()
