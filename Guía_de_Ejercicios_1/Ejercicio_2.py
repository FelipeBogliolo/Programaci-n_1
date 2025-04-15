edad = int(input("Ingrese su edad:\n"))

if edad > 18:
    print("Mayor de edad.")
elif edad > 13 and edad < 17:
    print("Adolescente")
else:
    print("Niño")