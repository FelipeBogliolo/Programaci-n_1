def funcion_ejemplo(numero_desde, numero, numero_hasta) -> int:
    if numero >= numero_desde and numero <= numero_hasta:
        print(f"El número que esta función recibio como parametro fué {numero}")
    else:
        print('ERROR. El número no cumple con los requisitos de ingreso')

def funcion_ejemplo2():
    numero_desde = int(input("Ingrese el rango mínimo:\n"))


    numero_hasta = int(input("Ingrese el rango máximo:\n"))


    numero = int(input("Ingrese el número:\n"))


    if numero >= numero_desde and numero <= numero_hasta:
        return f"El número que esta función recibió como parámetro fue {numero} y esta dentro del rango sugerido."

    else:
        return 'ERROR. El número no cumple con los requisitos de ingreso.'

funcion_ejemplo(1, 80, 100)

print(funcion_ejemplo2())