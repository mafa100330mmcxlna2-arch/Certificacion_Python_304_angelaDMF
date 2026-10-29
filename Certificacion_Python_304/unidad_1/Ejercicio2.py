try:
    alumnos = ["Aaron", "Michelle", "Angela", "Alma", "Jorge","Joshua"]
    calificaciones = [7, 8, 8,8, 6, 7]
    print("alumnos: " alumnos[0], "calificacion: ",calificaciones[0])
    print("alumnos: " alumnos[3], "calificacion: ",calificaciones[3])
    print("alumnos: " alumnos[5], "calificacion: ",calificaciones[5])
except SyntaxError:
    print("Error: Indice Incorrecto")
