#Condicional doble.
#Determina si una persona es mayor o menor de edad.
from tkinter.tix import InputOnly


edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")