def agregarTarea(lista):
    tarea = input("Nombre Tarea: ")

    if tarea == "":
        print("La tarea no puede estar vacia")
    else:
        lista.append(tarea)
        print("Tarea agregada")

def listar(lista):
     
    if len(lista) == 0:
          print("No hay tareas")
    else:
         #for indice range(len(lista))
            #print(f'{indice}- {lista{indice}})
         for indice,tarea in enumerate(lista):
              print(f'{indice +1 } - {tarea}')

def modificar(lista):
    if len(lista) == 0:
          print("No hay tarea para modificar")
    else:
         try:
            indice_tarea = input("Ingrese el numero de la tarea a modificar :")

            
            if indice_tarea < 1 or indice_tarea > len(lista):
              print("Ese numero no existe")
            else:
              nueva_tarea = input("Ingrese el nuevo texto de la tarea :")
              lista[nueva_tarea - 1] = nueva_tarea

         except:
              print("Debe escribir un numero")

def eliminar(lista):
    if len(lista) == 0:
               print("No hay tarea para modificar")
    else:
        try:
            indice_tarea = input("Ingrese el numero de la tarea a eliminar:")
     
                 
            if indice_tarea < 1 or indice_tarea > len(lista):
                   print("Ese numero no existe")
            else:
                lista.pop(indice_tarea - 1)
                print("Tarea eliminada")
     
        except:
            print("Debe escribir un numero")



listaTareas = []

while True:
    print("===== MIS TAREAS =====")
    print("1. Agregar")
    print("2. Listar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")



    op = int(input("Ingrese una opcion :"))

    if op == 1:
            agregarTarea(listaTareas)
    elif op == 2:
         listar(listaTareas)
    elif op == 3:
            modificar(listaTareas)

    elif op == 4:
           eliminar(listaTareas)
    elif op == 5:
            print("Salir")
            break
    else:
            print("Opcion invalida")