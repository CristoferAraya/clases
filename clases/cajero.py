op= 0
saldo = 100000.0
deposito = 0
retiro = 0

while True:
    print("===== CAJERO DUOC =====")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    while True:
        try:
            op = int(input("Ingrese una opcion :"))

            if op > 4 or op < 0:
                print("Ingrese una opcion valida")
            else:
                break
        except:
            print("Debes ingresar solo numeros")

    if op == 4:
        print(" Gracias por usar el cajero.")
        break

    if op == 1:
        print(f"su saldo es {saldo}")

    elif op == 2:
        deposito=float(input("Ingrese monto a ingresar :"))
        if deposito > 0 :
            saldo = saldo + deposito
            print("Deposito ingresado correctamente")
        else:
            ("Error de deposito")
    elif op == 3:
        retiro = float(input("Ingrese monto a retirar :"))
        if retiro > 0:
            saldo = saldo - retiro
        print("Retiro exitoso")
    else:
        print("Error al retirar dinero")