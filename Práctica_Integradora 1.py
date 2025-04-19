cantidad_encuestas = 0

encuesta_1 = 0

encuesta_2 = 0

maxima_edad = 0
nombre_maxima_edad = 0
tecnologia_maxima_edad = ""

while cantidad_encuestas < 10:
    ingreso_nombre = input("Ingrese su nombre:\n")
    ingreso_edad = int(input("Ingrese su edad:\n"))
    ingreso_genero = input("Ingrese su género (Femenino, Masculino, Otro):\n")
    ingreso_tecnologia = input("Ingrese su tecnología (IA, RV/RA, IOT):\n")
    cantidad_encuestas += 1
    if ingreso_genero == "Masculino" and (ingreso_tecnologia == "IOT" or ingreso_tecnologia == "IA") and 25 <= ingreso_edad <= 50:
        encuesta_1 += 1
    if ingreso_genero == "Masculino" and (ingreso_edad > 33 and ingreso_edad < 40) and ingreso_tecnologia != "IA":
        encuesta_2 += 1
    if maxima_edad > 0:
        maxima_edad = ingreso_edad
        nombre_maxima_edad = ingreso_nombre
        tecnologia_maxima_edad = ingreso_tecnologia
    
#encuesta 2
porcentaje = (encuesta_2 * 100) / 10

#1
print("La cantidad de empleados e género masculino que votaron por IOT o IA, "
    f"cuya edad esté entre 25 y 50 años inclusive es de {encuesta_1}")
#2
print("El porcentaje de empleados que no votaron por IA, siempre y cuando su"
    f"género no sea Femenino o su edad se encuentre entre los 33 y 40 es de {porcentaje}")
#3
print(f"El empleado masculino mas longevo se llama {nombre_maxima_edad} y,"
    f" voto {tecnologia_maxima_edad}")
