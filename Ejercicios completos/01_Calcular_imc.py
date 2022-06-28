peso = float(input("Ingresa tu peso: (kg)"))
estatura = float(input("Ingresa tu estatura (m)"))

imc = peso / estatura ** 2
if imc > 0 and imc <18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <24.99:
    print("Normal")
elif imc >= 15 and imc <29.99:
    print("Sobre peso")
elif imc >= 30:
    print("Obesidad")
else:
    print("Datos no validos")