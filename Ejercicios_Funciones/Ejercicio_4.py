def funcion_min_max(numero_desde, numero_hasta) -> int:
    bandera = True
    while bandera:
        numero = int(input("Ingrese un valor:\n"))
        if numero_desde <= numero <= numero_hasta:
            print(f"El número que esta función recibió como parámetro fue {numero}")
            return numero
        else:
            print("ERROR. El número no cumple con los requisitos de ingreso.")

if __name__ == "__main__":
    def funcion_min_max_2():
        numero_desde = int(input("Ingrese el rango mínimo:\n"))
        numero_hasta = int(input("Ingrese el rango máximo:\n"))
        numero = int(input("Ingrese el número:\n"))
        if numero >= numero_desde and numero <= numero_hasta:
            return f"El número que esta función recibió como parámetro fue {numero} y esta dentro del rango sugerido."
        else:
            return 'ERROR. El número no cumple con los requisitos de ingreso.'

    funcion_min_max(1, 100)

    print(funcion_min_max_2())