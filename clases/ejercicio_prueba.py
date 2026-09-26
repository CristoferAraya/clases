capacidad_total = 40
asientos_libres = 40
entradas_vendidas = 0
recaudacion = 0.0
con_descuento = 0
precio_base = 12000.0

while True:
    print("===== BOLETERÍA DUOC FEST =====")
    print("1. Consultar estado")
    print("2. Vender entradas")
    print("3. Resumen del día")
    print("4. Salir")

    op = int(input("Elija una opcion :"))

    if op == 1:
        print("Asientos libres :" ,asientos_libres)
        print("Entradas vendidas :", entradas_vendidas)
        print("Recaudacion :", recaudacion)
    elif op == 2:

        while True:
            try:
                cantidad_entradas = int(input("Cantidad de entradas :"))

                if cantidad_entradas <= asientos_libres and cantidad_entradas > 0:
                        break
                else:
                    print("Debes ingresar una cantidad menor o igual a asientos libres ")
            except:
                print("Debe ser un numero mayor a 0")

        for i in range(1, cantidad_entradas + 1):
            while True:
                try:
                    edad = int(input("Ingrese la edad :"))
                    if edad > 0:
                        print("Edad valida")
                        break
                    else:
                        print("Edad debe ser mayor que 0")
                except:
                    print("Edad debe ser un numero")   

            precio = precio_base

            if edad < 12:
                precio = precio * 0.5
                con_descuento +=1
            elif edad >= 12 and edad <= 17:
                con_descuento +=1
                precio = precio *0.7
            elif edad > 17 and  edad < 60:
                precio = precio_base
            else:
                precio = precio * 0.6
                con_descuento +=1

            print("El precio de tu entrada es :", precio)
            recaudacion += precio

        asientos_libres = asientos_libres - cantidad_entradas
        entradas_vendidas = entradas_vendidas + cantidad_entradas
            
    elif op == 3:
        if entradas_vendidas == 0:
            print("Aun no hay ventas")
        else:
            print("--- RESUMEN DEL DÍA ---")
            print("Entradas vendidas :", entradas_vendidas)
            print("Con descuento :", con_descuento)
            ticket_promedio = recaudacion / entradas_vendidas
            print("Ticket promedio: ", round(ticket_promedio, 1))

            if recaudacion == 0:
                print("Sin movimiento")
            elif recaudacion > 0 and recaudacion <= 100000:
                print("Jornada baja")
            elif recaudacion > 0 and recaudacion <= 200000:
                print("Jornada normal")
            elif recaudacion > 300000:
                print("Jornada alts")


    elif op == 4:
        print("Caja cerrada, hasta luego")
    else:
        print("Opcion invalida, Intente nuevamente")
        