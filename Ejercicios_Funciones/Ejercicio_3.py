def par_impar():
    ingreso = int(input("Ingrese el número que quiere corroborar:\n"))
    if ingreso % 2 == 0:
        return True
    else:
        return False
    
print(par_impar())