temperatura=[
    [8,10],
    [10,14],
    [12,16],
    [5,9],
    [10,13],
    [16,22],
    [18,30]
]
promedio_min=[]
promedio_max=[]
oscilacion=[]
for fila in range(len(temperatura)):
    promedio_min.append(temperatura[fila][0])
    promedio_max.append(temperatura[fila][1])
    oscilacion_dia= temperatura[fila][1] - temperatura[fila][0]
    oscilacion.append(oscilacion_dia)
max_oscilacion=max(oscilacion)
dia=oscilacion.index(max_oscilacion) + 1
# oscilacion= temp_max-temp_min
promedio_minimo = sum(promedio_min) / len(promedio_min)
promedio_maximo = sum(promedio_max) / len(promedio_max)
print(f"el promedio de las temperaturas bajas fue de: {promedio_minimo:.2f}")
print(f"el promedio de las temperaturas maximas fue de: {promedio_maximo:.2f}")
print(f"el dia que se registro mayor amplitud termica fue: {dia}")
