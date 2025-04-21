estadistica_1 = 0

#estadistica_2
edad_estadistica_2 = 0
bandera_primer_ingreso_edad = True
nombre_estadistica_2= ""
categoria_estadistica_2 = ""

#estadistica_3
categoria_experto = 0
cantidad_ingresos = 0

#estadistica_4
categoria_avanzado = 0
edades_cat_avanzado = 0

#estadistica_5
saque_plano = 0
saque_liftado = 0
saque_cortado = 0

while True:
    ingreso_nombre = input("Ingrese el nombre del jugador:\n")
    ingreso_edad = int(input("Ingrese la edad del jugador:\n"))

    while ingreso_edad < 18:
        ingreso_edad = int(input("ERROR. Ingrese una edad válida:\n"))

    ingreso_cantidad_puntos = int(input("Ingrese cantidad de puntos que anotó el jugador:\n"))

    while ingreso_cantidad_puntos < 0 or ingreso_cantidad_puntos % 2 != 0 or ingreso_cantidad_puntos > 60:
        ingreso_cantidad_puntos = int(input("ERROR. Ingrese una cantidad de puntos válida:\n"))

    ingreso_partidos_ganados = int(input("Ingrese la cantidad de partidos ganados:\n"))

    while ingreso_partidos_ganados < 0 or ingreso_partidos_ganados % 2 != 0 or ingreso_partidos_ganados > 35:
        ingreso_partidos_ganados = int(input("ERROR. Ingrese una cantidad de partidos válidos:\n"))

    tipo_saque = input("Ingrese el tipo de saque del jugador (Plano, Liftado, Cortado):\n")
    categoria = input("Ingrese la categoría del jugador (Elite, Experto, Avanzado):\n")

    #estadistica_3
    if categoria == "Experto":
        categoria_experto += 1
    elif categoria == "Avanzado":
        categoria_avanzado += 1
        edades_cat_avanzado += ingreso_edad

    if categoria == "Elite":
        if tipo_saque == "Plano":
            saque_plano += 1
        elif tipo_saque == "Liftado":
            saque_liftado += 1
        else:
            saque_cortado += 1

    cantidad_ingresos += 1 #estadistica_3

    #estadistica 1
    if categoria == "Elite" and tipo_saque == "Plano" and (19 <= ingreso_edad <= 25):
        estadistica_1 += 1

    #estadistica_2 (ahora busca menor edad con más de 50 puntos)
    if ingreso_cantidad_puntos > 50 and (bandera_primer_ingreso_edad or ingreso_edad < edad_estadistica_2):
        nombre_estadistica_2 = ingreso_nombre
        categoria_estadistica_2 = categoria
        edad_estadistica_2 = ingreso_edad
        bandera_primer_ingreso_edad = False

    continuar = input("¿Desea ingresar otro jugador? (Si/No):\n")
    if continuar.lower() != "si":
        break

#estadistica_1
print("La cantidad de jugadores de categoría Elite, con tipo de saque 'Plano',"
      f" cuya edad está entre 19 y 25 es de {estadistica_1}")

#estadistica_2
if bandera_primer_ingreso_edad == False:
    print(f"El nombre del jugador de menor edad con más de 50 puntos es {nombre_estadistica_2}"
          f" y la categoría de dicho jugador es {categoria_estadistica_2}")
else:
    print("No se registraron jugadores con más de 50 puntos.")

#estadistica_3
if cantidad_ingresos > 0:
    porcentaje = (categoria_experto / cantidad_ingresos) * 100
    print(f"El porcentaje de jugadores de categoría Experto es de {porcentaje}%")
else:
    print("No se ingresaron jugadores.")

#estadistica_4
if categoria_avanzado > 0:
    promedio = edades_cat_avanzado / categoria_avanzado
    print(f"El promedio de edad de los jugadores cuya categoría es Avanzado es de {promedio} años.")
else:
    print("No se ingresaron jugadores de categoría Avanzado.")

#estadistica_5
if saque_plano > saque_liftado and saque_plano > saque_cortado:
    print("El saque más usado en la categoría Elite es el 'Plano'")
elif saque_cortado > saque_plano and saque_cortado > saque_liftado:
    print("El saque más usado en la categoría Elite es el 'Cortado'")
elif saque_liftado > 0 or saque_plano > 0 or saque_cortado > 0:
    print("El saque más usado en la categoría Elite es el 'Liftado'")
else:
    print("No se registraron saques en la categoría Elite.")
