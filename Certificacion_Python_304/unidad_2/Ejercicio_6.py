tablas = [
    ["Nombre","Edad","Calificacion"],
    ["Aaron",17,6.0],
    ["Michelle",16,8.0],
    ["Angela",16,8.0],
    ["Keilani",16,6.0],
    ["Santiago",16,8.0],
    ["Alma",16,8.0],
    ["Jorge",16,6.0],
    ["Danna",16,7.0],
    ["Joshua",16,7.0],
    ["Angel",16,9.0]
]
filas=len(tablas)
columnas=len(tablas[0])
buscar_nombre = input("Ingresa el nombre:")
for i in range(filas):
    for j in range(columnas):
        if j == 0 and tablas[i][j] == buscar_nombre:
            print(f"nombre encontrado en la posicion [{i}][{j}]")
