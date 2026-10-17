def eliminar(lista, pocision):
    if lista == "":
        print("No hay datos")

    if len(lista) < 0 or pocision >= len(lista):
        print("Esa posicion no existe")
    else:
        lista.pop (pocision)
        print("Elimonado")

lista =["pan", "leche", "huevos"]
eliminar(lista, 1)

def listar(lista):
    if len(lista) == 0:
        print("La lista esta vacia")
    else:
        for indice,listar in enumerate(lista):
            print(f'{indice +1 } - {listar}')