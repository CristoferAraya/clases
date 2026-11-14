alumno = {}

def agregar():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")
    correo = input("Correo: ")
    return {
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera,
        "correo": correo,
    }

def actualizar(alumno):
    correo = input("Nuevo correo: ")
    alumno["correo"] = correo
        

def imprimir(alumno):
    for clave, valor in alumno.items():
        print(clave, "-", valor)



while True :

    print("===== ALUMNO =====")
    print("1. Crear")
    print("2. Actualizar")
    print("3. Imprimir")
    print("4. Salir")

    op = int(input("Ingrese una opcion :"))

    if op == 1:
        alumno = agregar()
    elif op == 2:
        actualizar(alumno)
    elif op == 3:
        imprimir(alumno)
    elif op == 4:
        print("Salir")
    else :
        print("Opcion invalida")