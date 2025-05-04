def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + suma_digitos(numero // 10)
    
suma_digitos(4567)