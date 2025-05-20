matriz = [
    [5, 2, 3, 4],
    [5, 2, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]

def tres_en_fila(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == matriz[i + 1][j] and matriz[i][j] == matriz[i + 2][j]:
                return matriz[i][j]
    return None
            
resultado = tres_en_fila(matriz)
print(resultado)