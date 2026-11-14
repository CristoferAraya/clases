alumnos = []

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

def agregar_alumno(alumno):
    alumnos.append(alumno)

def actualizar(alumno):
    correo = input("Nuevo correo: ")
    alumno["correo"] = correo

def modificar_alumno():

    for i, alumno in enumerate(alumnos):
        print(f"{i}.- {alumno['nombre']}")
    
    if len(alumnos) == "":
          print("No hay alumno a  modificar")
    else:
         try:
            indice= int(input("Ingrese el alumno a modificar :"))

            if indice < 0 or indice > len(alumnos):
              print("Ese alumno no existe")
            else:
              actualizar(alumnos[indice])

         except:
              print("Debe escribir un texto")
        

def imprimir(alumno):
    for clave, valor in alumno.items():
        print(clave, "-", valor)

def eliminar_alumno(indice):
    for i, alumno in enumerate(alumnos):
        print(f"{i}.- {alumno['nombre']}")

    if len(alumnos) == "":
        print("No hay alumno a eliminar")
    else:
        try:
            indice= int(input("Ingrese el alumno a eliminar :"))

            if indice < 0 or indice > len(alumnos):
                print("Ese alumno no existe")
            else:
                alumnos.pop(alumnos[indice])

        except:
            print("Debe escribir un texto")

alumno ={}

while True :

    print("===== ALUMNO =====")
    print("1. Crear")
    print("2. Actualizar")
    print("3. Imprimir")
    print("4. Eliminar")
    print("5. Salir")

    op = int(input("Ingrese una opcion :"))

    if op == 1:
        alumno = agregar()
        agregar_alumno(alumno)
        print("Alumno agregado")
    elif op == 2:
        modificar_alumno()
    elif op == 3:
        imprimir(alumno)
    elif op == 4:
        eliminar_alumno(alumno)
    elif op == 5:
        print("Salir")
    else :
        print("Opcion invalida")