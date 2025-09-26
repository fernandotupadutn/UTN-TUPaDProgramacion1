# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia

materias= [
    [4, 6, 8], #para mostrar el de cada estudiante, debo sumar las 3 notas 
    [5, 8, 9],   # para mostra el promedio de cada materia tengo que sumar de arriba hacia abajo
    [3, 7, 9],
    [2, 7, 3],
    [10,8,6]
]

for estudiante in range(len(materias)):
    suma = 0 
    for materia in range(len(materias[estudiante])):
        suma+=materias[estudiante][materia]
    promedio=suma/len(materias[0])
    print("promedio de cada estudiante",estudiante+1,promedio)

for materia in range(len(materias)):
    suma=0
    for estudiantes in range(len(materias[materia])):
        suma += materias[materia][estudiantes]
    promedio=suma/len(materias[1])
    print("el promedio por materia es:",promedio,"del estudiante:",materia+1)