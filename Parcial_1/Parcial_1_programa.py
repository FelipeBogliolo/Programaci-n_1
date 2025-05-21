from Parcial_1_funciones import * 

while True:
    ingreso = menu()

    match ingreso:
        case 1:
            mostrar_ventas(productos, ventas)
        case 2:
            ordenar_mayor_menor()
            print("Productos ordenados correctamente.")
        case 3:
            busqueda_producto()
        case 4:
            busqueda_valor_venta(ventas)
        case 5:
            print("¡Gracias por usar el programa!")
            break
            