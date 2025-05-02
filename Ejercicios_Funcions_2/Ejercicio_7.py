def es_primo(ingreso):
    if ingreso < 2:
        return False
    for i in range(2, ingreso): 
        if ingreso % i == 0:
            return False
    else:
        return True