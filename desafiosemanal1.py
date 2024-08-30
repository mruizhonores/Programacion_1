import random

def MostrarMatriz(MatrizCalif, n, m):
    # materias
    print(" "*14, end="")
    for j in range(1, m+ 1):
        print(" "*4, "Materia", j, end="")
    print()

    # estudiantes
    i = 0
    for fila in (MatrizCalif):
        print("Estudiante: ", (i + 1), end="")
        for calificacion in fila:
            print(" "*10, calificacion, end=" ")
        print()
        i = i + 1

def PromedioCalif(MatrizCalif):
    i = 0
    for fila in MatrizCalif:
        suma = 0
        j = 0
        while j < len(fila):
            suma += fila[j]
            j = j + 1
        promedio = suma / len(fila)
        print("El promedio de calificaciones del Estudiante: ", (i + 1), " es: ", (promedio))
        i += 1

def calcular_promedio_materias(MatrizCalif):
    num_materias = len(MatrizCalif[0])
    for j in range(num_materias):
        suma = 0
        for fila in MatrizCalif:
            suma = suma + fila[j]
        promedio = suma / len(MatrizCalif)
        print("El promedio de calificaciones en la Materia", (j + 1), " es: ", (promedio))


# número de estudiantes y materias
n = int(input("Ingrese el nro de estudiantes: "))
m = int(input("Ingrese el nro de materias: "))

MatrizCalif = []

# llenar la matriz con calificaciones aleatorias 
for x in range(n):
    calificaciones_estudiante = []
    for y in range(m):
        calificacion = random.randint(1, 10)
        calificaciones_estudiante.append(calificacion)
    MatrizCalif.append(calificaciones_estudiante)

# Mostrar la matriz con encabezados
MostrarMatriz(MatrizCalif, n, m)
print()
print("Promedio calificaiones para cada estudiante")
# Imprimir los promedios de calificaciones por estudiante
print()
PromedioCalif(MatrizCalif)
print()
print("Promedio calificaciones para cada materia")
print()
# Calcular y mostrar los promedios de calificaciones por materia
calcular_promedio_materias(MatrizCalif)