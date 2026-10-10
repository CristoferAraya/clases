tareas = []
while True:
    print("===== MIS TAREAS =====")
    print("1. Agregar")
    print("2. Listar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")

    
    op = int(input("Elija una opcion :"))

    if op ==1:
        tarea_eleccion= input("Ingrese nombre de la tarea : ")
        
        if tarea_eleccion == "":
            print("La tarea no puede estar vacía.")
        else:
            tareas.append(tarea_eleccion)
            print(f'Tus tareas son :', tarea_eleccion)
    elif op == 2:
        if len(tarea_eleccion) == 0:
            print("No hay tareas agregadas")
        else:
            numero = 1
            for tarea_eleccion in tareas:
                print(numero, "-", tarea_eleccion)
                numero = numero +1
    elif op == 3:
        if len (tarea_eleccion) == 0:
            print("No hay tareas para modificar")
        else:
            numero = int(input("Numero de tarea a modificar : "))
            if numero <1 or numero >len(tarea_eleccion):
                print("Ese numero no existe")
            else:
                nuevo = input("Nueva tarea :")
                tareas[numero - 1] = nuevo
    elif op == 4:
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            numero = int(input("Número de la tarea: "))
        if numero <1 or numero >len(tareas):
            print("Ese numero no existe")
        else:
            tareas.pop(numero - 1)

    elif op == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")   

