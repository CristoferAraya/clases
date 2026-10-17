def agregar(lista,texto):
    if texto == "":
        print("El texto no puede estar vacio")
    else:
        lista.append(texto)
        print("Texto agregado")

def listar(lista):
    if len(lista) == 0:
        print("La lista esta vacia")
    else:
        for indice,listar in enumerate(lista):
            print(f'{indice +1 } - {listar}')

lista = []
agregar(lista,"")
agregar(lista,"estudiar")

listar(lista)