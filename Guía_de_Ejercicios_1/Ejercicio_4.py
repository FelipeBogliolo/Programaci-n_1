edad = int(input("Ingresa tu edad:\n"))
estado_civil = input("Ingrese su estado civil ('Soltero' o 'Casado'):\n")

if edad < 18 and estado_civil == "Casado":
    print("Es muy pequeño para NO ser soltero.")