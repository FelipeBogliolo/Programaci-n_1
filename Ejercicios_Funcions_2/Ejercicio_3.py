def par_impar(numero: int) -> int:
    es_par = False
    if numero % 2 == 0:
        es_par = True
        return f"El número {numero} es par."
    else:
        return f"El número {numero} es impar."
    
print(par_impar(10))