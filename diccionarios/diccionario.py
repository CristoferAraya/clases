alumno = {
    "id": "1",
    "nombre": "Jesus",
    "edad": 35,
    "titulado": True 
}

# Read (leer)
nombre = alumno["nombre"]
edad = alumno["edad"]

print("El nombre del alumno es :", nombre)
print("El largo del nombre es :", len(nombre))
print("La edad es :", edad)
print("La edad mas un año es :", edad +1)
print(alumno)

# Update (modificar)
edadSumada = alumno ["edad"] + 1
print(edadSumada)
print(alumno)

alumno["edad"] = alumno["edad"] + 1
alumno["titulado"] = False
print(alumno)

# Eliminar
del alumno["id"]
print(alumno)

# Agregar
alumno["telefono"] = "+56912345678"
print(alumno)

# Listar
print("")
print("El alumno es :")
for clave, valor in alumno.items():
    print(clave,":", valor)

# Validar existencia
if "nota" in alumno:
    print("La nota del alumno es : ", alumno["nota"])
else:
    print("El alumno no tiene nota registrada")

"""lista = ["arroz", "fideos", "azucar"]

compra1 = {
    "producto" : "arroz",
    "precio" : 1500,
    "cantidad" : 2
}

compra2 = {
    "producto" : "fideos",
    "precio" : 1000,
    "cantidad" : 3
}"""