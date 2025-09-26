
oscilacion=[]
for fila in range(len(temperatura)):
    promedio_min.append(temperatura[fila][0])
    promedio_max.append(temperatura[fila][1])
    oscilacion_dia= temperatura[fila][1] - temperatura[fila][0]
    oscilacion.append(oscilacion_dia)
max_oscilacion=max(oscilacion)
dia=oscilacion.index(max_oscilacion) + 1
# oscilacion= temp_max-temp_min