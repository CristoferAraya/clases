suma_notas = 0
promedio = 0
cantidad_notas = 0

while True:
    print("===== MENÚ NOTAS =====")
    print("1. Ingresar notas")
    print("2. Mostrar promedio")
    print("3. Salir")

    op = int(input("Ingrese una opcion :"))

    if op == 1:

        cantidad_notas = int(input("Ingresa la cantidad de notas :"))

        for i in range(cantidad_notas):
            nota = float(input(f"Ingresa la nota {i + 1} a registrar :"))
            suma_notas = suma_notas + nota
        
        print("Notas agregadas correctamente")
    if op == 2:
         if suma_notas == 0:
             print("Aun no hay notas ingresadas")
         else:
            promedio = suma_notas / cantidad_notas
            print(f"El promedio es {promedio:.1f}")
    elif op == 3:
        print("Salir")
        break