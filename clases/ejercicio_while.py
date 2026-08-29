cantidad_alumnos = 5
nombrados = 1

if nombrados <= cantidad_alumnos:
    print("Nombrar alumno (if)")

while nombrados <= cantidad_alumnos:
    print(f"Nombrar alumno {nombrados}")
    nombrados = nombrados + 1

    if nombrados == 3:
        break