def buscar_posicion(lista,texto):
    for indice,elemento in enumerate(lista):
      if elemento == texto:
         return indice

    return -1 

lista = ["pan", "leche", "huevos", "arroz"]

pos_huevos = buscar_posicion(lista, "huevos")
print(pos_huevos)

pos_cafe = buscar_posicion(lista, "cafe")
print(pos_cafe)