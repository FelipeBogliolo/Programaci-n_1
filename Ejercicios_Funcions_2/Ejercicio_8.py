def primos_encontrados(numero: int):
    contador_primos = 0
    for i in range(2, numero + 1):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            contador_primos += 1

    return f"La cantida de números primos encontrados fué de {contador_primos}"

print(primos_encontrados(100))