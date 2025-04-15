estacion = int(input("Ingrese la estación del año cuando quiere viajar:\n"
                 "1) Invierno\n"
                 "2) Verano\n"
                 "3) Otoño\n"
                 "4) Primavera\n"))
while estacion != 1 and estacion != 2 and estacion != 3 and estacion != 4:
    input("ERROR. Ingrese una opción válida:\n"
                 "1) Invierno\n"
                 "2) Verano\n"
                 "3) Otoño\n"
                 "4) Primavera\n")
localidad = int(input("Ingrese la localidad:\n"
                 "1) Bariloche\n"
                 "2) Cataratas\n"
                 "3) Mar del Plata\n"
                 "4) Córdoba):\n"))
while estacion != 1 and estacion != 2 and estacion != 3 and estacion != 4:
    input("ERROR. Ingrese una opción válida:\n"
                 "1) Bariloche\n"
                 "2) Cataratas\n"
                 "3) Mar del Plata\n"
                 "4) Córdoba):\n")
precio_final = 15000

if estacion == 1:
    match localidad:
        case 1:
            precio_final = int(precio_final * 1.20)
        case 2:
            descuento = precio_final * 0.10
            precio_final = precio_final - descuento
        case 3:
            descuento = precio_final * 0.20
            precio_final = precio_final - descuento
        case 4:
            descuento = precio_final * 0.10
            precio_final = precio_final - descuento

elif estacion == 2 :
    match localidad:
        case 1:
            descuento = precio_final * 0.20
            precio_final = precio_final - descuento
        case 2:
            precio_final = precio_final * 1.10
        case 3:
            precio_final = precio_final * 1.20
        case 4:
            precio_final = precio_final * 1.10

elif estacion == 3 or estacion == 4:
    match localidad:
        case 1:
            precio_final = precio_final * 1.10
        case 2:
            precio_final = precio_final * 1.10
        case 3:
            precio_final = precio_final * 1.10
        case 4:
            pass

print(f"El precio final es de ${precio_final}.")