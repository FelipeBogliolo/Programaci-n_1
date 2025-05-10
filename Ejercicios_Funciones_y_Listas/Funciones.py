from listas_personas import *

def opcion_1(): #IMPORTAR LISTAS
    with open("Ejercicios_Funciones_y_Listas/listas_personas.py", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido
        
def opcion_2(): #MOSTRAR DATOS USUARIOS MEXICO
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(f"\nNombre: {nombres[i]}; "
                f"Teléfono: {telefonos[i]}; "
                f"Mail: {mails[i]}; "
                f"Dirección: {address[i]}; "
                f"Código postal: {postalZip[i]}; "
                f"Región: {region[i]}; "
                f"País: {country[i]}; "
                f"Edad: {edades[i]}")
            
def opcion_3(): #MOSTRAR NOMBRE MAIL Y TELEFONO DE USUARIOS DE BRASIL
    for i in range(len(country)):
        if country[i] == "Brazil":
            print(f"\nNombre: {nombres[i]}; "
                f"Teléfono: {telefonos[i]}; "
                f"Mail: {mails[i]}")
            
def opcion_4(): #MOSTRAR USUARIO MAS JOVEN
    edad_mas_joven = 0
    posicion = []
    bandera_primer_ingreso = True
    for i in range(len(edades)):
        if bandera_primer_ingreso == True or edades[i] < edad_mas_joven:
            edad_mas_joven = edades[i]
            posicion = [i]
            bandera_primer_ingreso = False
        elif edades[i] == edad_mas_joven:
            posicion += [i]
    for i in posicion:
        print(f"\nNombre: {nombres[i]}; "
            f"Teléfono: {telefonos[i]}; "
            f"Mail: {mails[i]}; "
            f"Dirección: {address[i]}; "
            f"Código postal: {postalZip[i]}; "
            f"Región: {region[i]}; "
            f"País: {country[i]}; "
            f"Edad: {edades[i]}")

def opcion_5() -> int: #PROMEDIO EDAD USUARIOS
    acumulador = 0
    contador = 0
    for i in range(len(edades)):
        acumulador += edades[i]
        contador += 1
    promedio = acumulador / contador
    print(f"El promedio de edad de todos los usuarios es de {promedio}")

def opcion_6(): #MOSTRAR USUARIO MAS JOVEN DE BRASIL
    edad_mas_grande = 0
    posicion = []
    bandera_primer_ingreso = True
    for i in range(len(country)):
        if country[i] == "Brazil":
            if bandera_primer_ingreso == True or edades[i] < edad_mas_grande:
                edad_mas_grande = edades[i]
                posicion = [i]
                bandera_primer_ingreso = False
            elif edades[i] == edad_mas_grande:
                posicion += [i]
    for i in posicion:
        print(f"\nNombre: {nombres[i]}; "
            f"Teléfono: {telefonos[i]}; "
            f"Mail: {mails[i]}; "
            f"Dirección: {address[i]}; "
            f"Código postal: {postalZip[i]}; "
            f"Región: {region[i]}; "
            f"País: {country[i]}; "
            f"Edad: {edades[i]}")

def opcion_7():
    posicion = []
    for i in range(len(country)):
        if country[i] == "Brazil" or country[i] == "Mexico" and postalZip[i] > 8000:
            posicion += [i]
    for i in posicion:
        print(f"\nNombre: {nombres[i]}; "
            f"Teléfono: {telefonos[i]}; "
            f"Mail: {mails[i]}; "
            f"Dirección: {address[i]}; "
            f"Código postal: {postalZip[i]}; "
            f"Región: {region[i]}; "
            f"País: {country[i]}; "
            f"Edad: {edades[i]}")

def opcion_8():
    posicion = []
    for i in range(len(country)):
        if country[i] == "Italy" and edades[i] > 40:
            posicion += [i]
    for i in posicion:
        print(f"\nNombre: {nombres[i]}; "
            f"Teléfono: {telefonos[i]}; "
            f"Mail: {mails[i]}; "
            f"Dirección: {address[i]}; "
            f"Código postal: {postalZip[i]}; "
            f"Región: {region[i]}; "
            f"País: {country[i]}; "
            f"Edad: {edades[i]}")