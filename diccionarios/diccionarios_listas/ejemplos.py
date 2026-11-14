def crearAlumno():
    id = int(input("Ingresa el id del alumno :"))
    nombre = input("Ingresa el nombre del alumno :")
    telefono = int(input("Ingresa el telefono del alumno :"))
    correo = input("Ingresa el correo del alumno :")


    alumno = {
        "id" : id,
        "nombre" : nombre,
        "telefono" : telefono,
        "correo" : correo
    }

    return alumno

def imprimirAlumno(alumno: dict):
    for llave,valor in alumno.items():
        print(f"{llave}: {valor}")

curso =[]

alumno = crearAlumno()
alumno2 = crearAlumno()
alumno3 = crearAlumno()

curso.append(alumno)
curso.append(alumno2)
curso.append(alumno3)

for alumno in curso:
    imprimirAlumno(alumno)