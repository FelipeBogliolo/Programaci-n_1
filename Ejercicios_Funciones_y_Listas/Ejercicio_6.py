from listas_personas import *

with open("Ejercicios_Funciones_y_Listas/listas_personas.py", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    lista_nombres = nombres

def mostrar_lista(lista: list) -> str:
    for i in lista:
        print(i)

mostrar_lista(lista_nombres)