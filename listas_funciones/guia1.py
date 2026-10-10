tareas = []

while True:
    print("===== MIS TAREAS =====")
    print("1. Agregar")
    print("2. Listar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")

    try:
        op = int(input("Elija una opcion: "))
    except ValueError:
        print("Error: debes ingresar un numero.")
        continue

    if op == 1:
        tarea_eleccion = input("Ingrese nombre de la tarea: ")

        if tarea_eleccion.strip() == "":
            print("La tarea no puede estar vacia.")
        else:
            tareas.append(tarea_eleccion)
            print("Tu tarea son:", tarea_eleccion)

    elif op == 2:
        if len(tareas) == 0:
            print("No hay tareas agregadas.")
        else:
            numero = 1
            for tarea in tareas:
                print(numero, "-", tarea)
                numero += 1

    elif op == 3:
        if len(tareas) == 0:
            print("No hay tareas para modificar.")
        else:
            try:
                numero = int(input("Numero de tarea a modificar: "))
            except ValueError:
                print("Error: ingresa un numero valido.")
                continue

            if numero < 1 or numero > len(tareas):
                print("Ese numero no existe.")
            else:
                nuevo = input("Nueva tarea: ")

                if nuevo.strip() == "":
                    print("La tarea no puede estar vacia.")
                else:
                    tareas[numero - 1] = nuevo
                    print("Tarea modificada correctamente.")

    elif op == 4:
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            try:
                numero = int(input("Numero de la tarea: "))
            except ValueError:
                print("Error: ingresa un numero valido.")
                continue

            if numero < 1 or numero > len(tareas):
                print("Ese numero no existe.")
            else:
                eliminada = tareas.pop(numero - 1)
                print("Tarea eliminada:", eliminada)

    elif op == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion invalida. Por favor, elija una opcion valida.")
