asientos_libres = 20
entradas_vendidas = 0
recaudacion = 0.0
PRECIO_NINO = 5000.0
PRECIO_ADULTO = 8000.0

while True:
    print("===== CINE CAMPUS =====")
    print("1. Ver estado")
    print("2. Vender entradas")
    print("3. Ver resumen")
    print("4. Salir")

    op = int(input("Ingrese una opcion :"))

    if op == 1:
        print("Asientos libres :", asientos_libres)
        print("Entradas vendidas :", entradas_vendidas)
        print("Recaudacion :", recaudacion)

    elif op == 2:
        while True:
            try:
                cantidad_entradas = int(input("Cantidad de entradas"))
                 
                if cantidad_entradas <= asientos_libres and cantidad_entradas > 0:
                    break
                else:
                    print ("Debe ingresar una cantidad igual o menor a asientos disponibles")   
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
                        print("Edad debe ser mayor a 0")
                except:
                    print("Edad debe ser un numero")

            if edad < 18:
                precio = PRECIO_NINO
                print("precio :", PRECIO_NINO)
            else:
                precio = PRECIO_ADULTO
                print("Precio :", PRECIO_ADULTO)

            recaudacion = recaudacion + precio

            asientos_libres = asientos_libres - cantidad_entradas
            entradas_vendidas = entradas_vendidas + cantidad_entradas

    
          
                    
    elif op == 3:
        if entradas_vendidas == 0:
            print("Aun no hay ventas")
        else:
            print("---Resumen del dia")
            print("Entradas vendidas :", entradas_vendidas)
            print("Recaudacion :", recaudacion)
            ticket_promedio = recaudacion / entradas_vendidas
            print("Ticket promedio :", round(ticket_promedio, 1))

            if recaudacion == 0:
                print("Sin ventas")
            elif recaudacion < 0:
                print("Dia con ventas ")

                
    elif op == 4:
        print("Caja cerrada. Hasta luego.")
    else:
        print("Opcion invalida. Intente nuevamente")