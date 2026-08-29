cantidad_notas = int(input("Ingresa la cantidad de notas :"))
suma_notas = 0

for i in range(cantidad_notas):

   nota = float(input(f"Ingresa la nota {i + 1} a registrar :"))
   suma_notas = suma_notas + nota

print(f"Tu promedio es {suma_notas / cantidad_notas}")