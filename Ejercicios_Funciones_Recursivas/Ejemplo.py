def factorial(numero: int) -> int:
    if numero == 1:
        return numero
    else:
        return numero * factorial(numero - 1)
    
print(factorial(4))