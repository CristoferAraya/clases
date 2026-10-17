def validar_texto(texto):
    if len(texto) < 3:
        print("El texto debe tener al menos 3 caracteres.")
        return False
    return True

def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except:
            print("Debes ingresar un numero.")

def agregar_producto(lista):
    producto = input("Producto: ")

    if validar_texto(producto) == False:
        return

    if producto in lista:
        print("Ese producto ya está en la lista.")
        return
    lista.append(producto)
    print("Producto agregado")
    
def listar(lista):
    if len(lista) == 0:
        print("La lista de compras está vacía.")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def buscar(lista):
    if len(lista) == 0:
        print("No hay productos.")
    else:
        producto = input("Producto a buscar: ")

        if validar_texto(producto) == True:
            if producto in lista:
                posicion = lista.index(producto)
                print(f"Producto encontrado: {posicion + 1}")
            else:
                print("No se encontró el producto.")

def eliminar(lista):
    if len(lista) ==0:
        print("La lista de compras está vacía.")
    else:
        listar(lista)
        numero = validar_numero("Ingrese el número del producto a eliminar: ")
        posicion = numero - 1

        if posicion >= 0 and posicion < len(lista):
            lista.pop(posicion)
            print("Producto eliminado")
        else:
            print("Ese numero no exiate")



compras = []

while True:
    print("===== LISTA DE COMPRAS =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    op=int(input("Ingrese una opción: "))

    if op == 1:
        agregar_producto(compras)
    elif op == 2:
        listar(compras)
    elif op == 3:
        buscar(compras)
    elif op == 4:
        eliminar(compras)
    elif op == 5:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida. Intente de nuevo")

