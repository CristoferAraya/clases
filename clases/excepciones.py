try:
    numero = int("2")
    print(10 / numero)
except ValueError:
    print("Error al transformar el numero")
except ZeroDivisionError:
    print("Error al dividir por 0")
except:
    print("Error desconocido")
else:
    print("Ejecucion exitosa")