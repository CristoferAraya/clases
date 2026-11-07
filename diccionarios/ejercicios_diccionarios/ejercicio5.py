estudiantes = {"Ana": 5.5, "Luis": 6.0}

nombre = input("Nombre: ")
nota = float(input("Nota nueva: "))

if nombre in estudiantes:
    estudiantes[nombre] = nota
    print(f"La nota de {nombre} fue actuaslizada a {nota}")
else:
    print(f"El nombre{nombre} no existe")

print(estudiantes)