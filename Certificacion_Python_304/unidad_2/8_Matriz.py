#Creando una matriz
numeros=[ 
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Obteniendo el numero de filas
filas=len(numeros)#filas=3
#Obteniendo el numero de columnas
columnas=len(numeros[0])
#Ciclo externo para los indices de las filas
for i in range(filas):
    #CICLO INTERNO PARA LOS INDICES DE LAS COLUMNAS
    for j in range(columnas):
        print(f"[{i}][{j}] = {numeros[i][j]}")
