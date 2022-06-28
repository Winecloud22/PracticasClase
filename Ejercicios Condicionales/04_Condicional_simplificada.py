#Condicional anidada simplificada.
edad = int(input("Ingresa tu edad:"))

if edad >= 0 and edad <= 12:
    print("Etapa niñez")
elif edad >= 13 and edad <= 18:
    print("Etapa adelescencia")
elif edad >= 19 and edad <= 59:
    print("Etapa Adulto")
elif edad >= 60 and edad <= 115:
    print("Etapa Adulto mayor")
else:
    print("Edad no válida")