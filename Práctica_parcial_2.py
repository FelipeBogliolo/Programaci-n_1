mapa = [
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0] ]

def verificar_coordenada(mapa: list, x: int, y: int) -> int:
    if mapa[x][y] == 1:
        return 0
    else:
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == 1:
                        locacion_x = i
                        locacion_y = j
                        break
        distancia_manhattan =  abs(x - locacion_x) + abs(y - locacion_y)
        return distancia_manhattan

while True:
    ingreso_x = int(input("Ingresa la coordenada X (0 a 4):\n"))
    while ingreso_x < 0 or ingreso_x > 4:
        ingreso_x = int(input("ERROR. Ingresa una coordenada X válida (0 a 4):\n"))

    ingreso_y = int(input("Ingresa la coordenada Y (0 a 4):\n"))
    while ingreso_y < 0 or ingreso_y > 4:
        ingreso_y = int(input("ERROR. Ingresa una coordenada Y válida (0 a 4):\n"))

    valor = verificar_coordenada(mapa, ingreso_x - 1, ingreso_y - 1)
    if valor == 0:
        print("¡Encontraste el tesoro!")
        break
    else:
        print(f"Fallaste, el tesoro esta a {valor} casillero/s de distancia.")
    
    seguir = input("¿Desea continuar?\n"
                "1) Si\n" \
                "2) No\n")
    if seguir == "No":
        print("Juego finalizado")
        break
    
