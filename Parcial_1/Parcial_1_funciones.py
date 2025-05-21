productos = ["A", "B", "C"]
ventas = [
    [50, 60, 70], #A
    [80, 55, 45], #B
    [50, 65, 75]  #C 
]

#MENU
def menu() -> int:
    """
    Muestra un menú de opciones al usuario para interactuar con el programa,
    solicita una opción válida y la retorna.
    El usuario debe ingresar un número entero entre 1 y 5. Si ingresa un valor
    fuera de ese rango, se solicitará nuevamente hasta que sea válido.

    Returns:
        int: Opción seleccionada por el usuario, entre 1 y 5.
    """
    print("\n--- MENÚ DE OPCIONES ---\n"
        "1. Mostrar productos y ventas.\n"
        "2. Ordenar productos por ventas anuales (desc).\n"
        "3. Buscar producto por nombre y mostrar sus ventas.\n"
        "4. Buscar producto por monto de venta.\n"
        "5. Salir.\n")
    ingreso = int(input("Ingrese una opción:\n"))
    while ingreso < 1 or ingreso > 5:
        print("ERROR. Ingrese un valor válido de 1 al 5.")
        ingreso = int(input("Ingrese una opción:\n"))
    return ingreso



#PUNTO 1
def mostrar_ventas(productos: list, ventas: list) -> str:
    """
    Muestra por consola una tabla de ventas organizada por producto y mes.

    Args:
        productos (list): Lista con nombres de los productos.
        ventas (list of lists): Matriz que contiene las ventas por producto y por mes.
    """
    print("Ventas trimestrales (en miles de $)")
    print("Producto | Tri 1 | Tri 2 | Tri 3 | Total")
    print("--------------------------------")
    for i in range(len(productos)):
        total = ventas_totales(ventas, i)
        fila = f"{productos[i]:^8} |"
        for venta in ventas[i]:
            fila += f" {venta:^5} |"
        fila += f" {total:^5} |"
        print(fila)

#PUNTO 2
def ventas_totales(lista_ventas: list, fila: int) -> int:
    """
    Calcula el total de ventas de un producto específico.

    Args:
        lista_ventas (list of list): Matriz de ventas.
        fila (int): Índice del producto cuyas ventas se desean sumar.

    Returns:
        int: Suma total de ventas del producto.
    """
    total_producto = 0
    for i in lista_ventas[fila]:
        total_producto += i
    return total_producto


#PUNTO 3
def ordenar_mayor_menor():
    """
    Ordena las listas 'ventas' y 'productos' en orden descendente según el total de ventas de cada producto.
    Las listas se mantienen paralelas para conservar la relación entre producto y sus ventas.
    """
    for i in range(len(ventas) - 1):
        for j in range(i + 1, len(ventas)):
            total_i = ventas_totales(ventas, i)
            total_j = ventas_totales(ventas, j)
            if total_j > total_i:
                # Intercambio de filas en la matriz de ventas
                aux_ventas = ventas[i]
                ventas[i] = ventas[j]
                ventas[j] = aux_ventas
                # Intercambio en la lista de productos
                aux_producto = productos[i]
                productos[i] = productos[j]
                productos[j] = aux_producto
 

#PUNTO 4
def busqueda_producto():
    """
    Solicita al usuario un producto (A, B o C) y muestra su total de ventas.
    Utiliza la función 'ventas_totales' para obtener los datos.
    """
    ingreso = input("Ingrese el producto que quiere buscar ('A', 'B' O 'C'):\n")
    match ingreso:
        case "A":
            total = ventas_totales(ventas, 0)
            print(f"Las ventas totales de este producto son de {total}")
        case "B":
            total = ventas_totales(ventas, 1)
            print(f"Las ventas totales de este producto son de {total}")
        case "C":
            total = ventas_totales(ventas, 2)
            print(f"Las ventas totales de este producto son de {total}")


#PUNTO 5 
def busqueda_valor_venta(matriz: list) -> str:
    """
    Busca un valor de venta específico en la matriz.
    Si se encuentra, informa en qué trimestre (mes) y de qué producto es.

    Args:
        matriz (list of list): Matriz de ventas a recorrer.
    """
    ingreso = int(input("Ingrese el valor que desea buscar:\n"))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ingreso:
                if i == 0:
                    print(f"El valor {matriz[i][j]} se encuentra en el trimestre {j + 1} y pertenece al producto 'A'")
                elif i == 1:
                    print(f"El valor {matriz[i][j]} se encuentra en el trimestre {j + 1} y pertenece al producto 'B'")
                elif i == 2:
                    print(f"El valor {matriz[i][j]} se encuentra en el trimestre {j + 1} y pertenece al producto 'C'")
