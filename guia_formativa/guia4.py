modelo =[]
anio = []
precio = []


def validar_modelo(modelo):
    if len(modelo.strip()) == 0:
        return False
    else: return True


def validar_anio(anio):
    anio = int(anio )> 1900
    return False

  

def validar_precio(precio):
    if precio == "":
        print("El campo no puede estar vacio")
    else:
        precio = float("Ingrese un valor")



def mostar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")

def leer_op():
    while True:
        try:
            op = int(input("Ingrese una opcion"))
            if 1 < op <= 6:
                return op
            else:
                print("Ingrese una opcion valida")
        except:
            print("Error, ingrese un numero entero")

def agregar_vehiculo(lista_vehiculos):
    modelo = int(input("Ingresa el modelo : "))
    anio = int("Ingrese el año :")
    precio = float("Ingrese un valor")

    if validar_modelo(modelo) == False:
        print("Este campo no puede estar vacio")
        return 
    if validar_anio(anio) == False:
        print("Debes ingresar un año igual o mayor a 1900")
        return
    if validar_precio(precio) == False :
        print("Debes ingresar un valor mayor a 0")
        return
    vehiculo ={
        "modelo": modelo.strip(),
        "anio" : anio,
        "precio" : precio,
        "disponible" : False
}
    lista_vehiculos.append(vehiculo)
    print(f'Vehiculo {vehiculo[modelo]} agregado ')

def buscar_vehiculo (lista_vehiculos,modelo_buscar):
    for i in range(len(lista_vehiculos)):
        if lista_vehiculos[i] ["modelo"] == modelo_buscar:
                return i
        return -1

def actualizar_disponibilidad(lista_vehiculos):
     for vehiculo in lista_vehiculos:
        if vehiculo["anio"] >=2020:
         vehiculo["disponible"] = True

def mostrar_vehiculo(lista_vehiculos):
    actualizar_disponibilidad(lista_vehiculos)
    print("lista de vehiculos")
    if len(lista_vehiculos) == 0:
        print("No hay vehiculo registrado")
        return
    for vehiculo in lista_vehiculos:
        if vehiculo ["disponible"] == True:
            estado = "Disponible"
        else:
            estado =" No disponible"
        print(f'Modelo : {vehiculo['modelo']}')
        print(f'Año : {vehiculo['anio']}' )
        print(f'Precio : {vehiculo['precio']}')
        print(f'Estado{estado}')

def main():
    vehiculos =[]

    while True:
        mostar_menu()
        op = leer_op()
        if op == 1:
            agregar_vehiculo(vehiculos)
        elif op == 2:
            modelo_buscar = input("Ingresa el modelo a buscar :")
            posicion = buscar_vehiculo(vehiculos,modelo_buscar)
            if posicion != 1 :
                v = vehiculos[posicion]
                if v['disponible']== True:
                    estado = "Disponible"
                else:
                    estado ="No disponible"
                    print(f'Vehiculo encontrado en la posicion{posicion} :')
                    print(f'Modelo{v['modelo']} | Año : {v[anio]} | Precio : {v['precio']} | Estado :{estado}')
            else:
                print(f'El vehiculo{modelo_buscar} no se encuentra registrado')
        elif op == 3:
            modelo_eliminar = input("Ingrese el modelo del vehiculo a eliminar")
            posicion = buscar_vehiculo(vehiculos,modelo_eliminar)

            if posicion != 1:
                eliminado = vehiculos.pop(posicion)
                print(f'Vehiculo { eliminado['modelo']} eliminado correctamente')
            else:
                 print(f'El vehiculo{modelo_eliminar} no se encuentra registrado')
        elif op == 4:
            actualizar_disponibilidad(vehiculos)
            print("Disponibilidad de todos los vehiculos actualizados")

        elif op == 5:
            mostrar_vehiculo(vehiculos)
        elif op == 6:
            print("Gracias por usar el sistema")
            break


main()