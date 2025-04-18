numero = int(input("Ingresá un número: "))
contador_primos = 0

for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
        contador_primos += 1

# Mostrar cuántos primos se encontraron
print("Cantidad de números primos encontrados:", contador_primos)
