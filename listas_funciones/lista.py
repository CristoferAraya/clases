listaAlumnos = ["Jesus", "Marco", "Alyson" ]


#(C) Create
listaAlumnos.append("Nicolas")
listaAlumnos.insert(1, "Pablo")

#(R) Read
# Leer Lista
print(listaAlumnos)


# Leer u elemento de la lista segun su posicion
print(listaAlumnos[0])

# Leer cada elemento de la lista 
for alumno in listaAlumnos:
    print(alumno)

#(U) Update
listaAlumnos[1] = "Miguel"
print(listaAlumnos)

#(D) Delete
# Elimina el elemento en la posicion indicada
elementoELiminado =listaAlumnos.pop(0)
print("Se a eliminado el elemento", elementoELiminado)
print(listaAlumnos)

listaAlumnos.remove("Miguel")
print(listaAlumnos)


listaAlumnos.reverse()

print(len(listaAlumnos))

for i in range (len(listaAlumnos)):
    print(f'{i}',listaAlumnos[i])