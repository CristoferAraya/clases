def listar(lista):
    if len(lista) == 0:
        print("La lista esta vacia")
    else:
        for indice,listar in enumerate(lista):
            print(f'{indice +1 } - {listar}')

lista = ["pan", "leche", "huevos"]
listar([])
listar(lista)