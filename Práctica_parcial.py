tablero = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

def verificar_coordenada(tablero: list, x: int, y: int) -> bool:
    if tablero[x][y] == 1:
        return True
    else:
        return False

while True:
    ingreso_x = int(input("Ingresa la coordenada X (0 a 4):\n"))
    while ingreso_x < 0 or ingreso_x > 4:
        ingreso_x = int(input("ERROR. Ingresa una coordenada X válida (0 a 4):\n"))

    ingreso_y = int(input("Ingresa la coordenada Y (0 a 4):\n"))
    while ingreso_y < 0 or ingreso_y > 4:
        ingreso_y = int(input("ERROR. Ingresa una coordenada Y válida (0 a 4):\n"))

    aciertos = 0
    info = verificar_coordenada(tablero, ingreso_x - 1, ingreso_y - 1)
    if info == True:
        print("Hundido")
        aciertos += 1
    else:
        print("Fallo")
    
    seguir = input("¿Queres seguir disparando?")
    if seguir != "Si":
        print(f"Ha hundido en total {aciertos} barco/s.")
        break
