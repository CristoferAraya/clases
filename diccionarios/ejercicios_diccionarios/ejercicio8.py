agenda = {"Ana": "111", "Luis": "222"}
nombre = input("Nombre a eliminar: ")

if nombre in agenda:
    del agenda[nombre]
    print(f"{nombre} fue eliminado de la agenda")
else:
    print(f"{nombre} no se encuentra en el diccionario")

print(agenda)