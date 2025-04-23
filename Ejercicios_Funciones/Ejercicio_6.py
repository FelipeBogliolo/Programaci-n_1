from Ejercicios_Funciones.Ejercicio_4 import funcion_min_max

def realizar_descuento(numero) -> int:
    descuento = (5 * numero) / 100
    valor_final = numero - descuento
    return valor_final

variable1 = funcion_min_max(10, 100)

print(realizar_descuento(variable1))
