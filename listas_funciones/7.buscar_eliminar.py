lista = ["rojo", "verde", "azul", "amarillo"]
def buscar_posicion(lista,texto):
    for indice,elemento in enumerate(lista):
      if elemento == texto:
         return indice

    return -1 

def eliminar(lista, pocision):
    if lista == "":
        print("No hay datos")

    if len(lista) < 0 or pocision >= len(lista):
        print("Esa posicion no existe")
    else:
        lista.pop (pocision)
        print("Elimonado")

def listar(lista):
    if len(lista) == 0:
        print("La lista esta vacia")
    else:
        for indice,listar in enumerate(lista):
            print(f'{indice +1 } - {listar}')

pos_azul = buscar_posicion(lista,"azul")
print(pos_azul)

if pos_azul != 0:
   eliminar(lista,pos_azul)
listar(lista)