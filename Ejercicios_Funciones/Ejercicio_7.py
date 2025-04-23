from Ejercicio_4 import funcion_min_max


numero1 = funcion_min_max(10, 100)
numero2 = funcion_min_max(10, 100)
operacion = input("Ingrese 'S' para suma y 'R' para resta:\n")

while operacion != "S" and operacion != "R":
    print("ERROR. Ingrese una respuesta válida.") 
    operacion = input("Ingrese 'S' para suma y 'R' para resta:\n")

if operacion == "S":
    cuenta = numero1 + numero2
elif operacion == "R":
    cuenta = numero1 - numero2


print(f"El resultado es {cuenta}.")

