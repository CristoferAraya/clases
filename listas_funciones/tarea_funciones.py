def agregarTarea(lista):
    tarea = input("Nombre Tarea: ")

    if tarea == "":
        print("La tarea no puede estar vacia")
    else:
        lista.append(tarea)
        print("Tarea agregada")

def mostarMenu():
    print("===== MIS TAREAS =====")
    print("1. Agregar")
    print("2. Listar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")



listaTareas = []

while True:
    mostarMenu()

    op = int(input("Ingrese una opcion :"))

    if op == 1:
       agregarTarea(listaTareas)
    elif op == 2:
        if len(listaTareas) == 0:
            print("No hay tareas agregadas")
        else:
            numero = 1
            for tarea in listaTareas:
                print(numero, "-", tarea)
                numero = numero +1
    elif op == 3:
        while True:
            try:
                if len(listaTareas) == 0:
                    print("No hay tareas para modificar")
                    break
                else:
                    numero = int(input("Numero de tarea a modificar : "))
                    if numero <1 or numero >len(listaTareas):
                        print("Ese numero no existe")
                        break
                    else:
                        nuevo = input("Nueva tarea :")
                        listaTareas[numero - 1] = nuevo
            except:
                print("Ingrese una opcion valida")

    elif op == 4:
        print()
    elif op == 5:
        print("Salir")
        break
    else:
        print("Opcion invalida")