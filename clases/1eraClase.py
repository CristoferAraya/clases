# Entradas
nota_1 = 6.5
nota_2 = 6.0
nota_3 = 5.5

# proceso, un promedio se calcula sumando tosas las notas
# y dividiendolas por la cantidad de notas

# suma (+)
# resta (-)
# division (/)
# multiplicacion (*)
# resto (%)
promedio = nota_1 + nota_2 + nota_3
promedio = promedio / 3

# salida
print("tu promedio es :" + str(promedio)) #concatenacion explicita
print("tu promedio es :", promedio) # concatenacion implicita
print(f"tu promedio es : {promedio}")

porcentaje_asistencia = 30
eximido_asistencia = True

if promedio >= 4.0:
    if porcentaje_asistencia > 70:
        print("Aprobado")
    elif eximido_asistencia == True:
        print("Aprobado")

    print("Aprobado")
else:
    print("Reprobado")