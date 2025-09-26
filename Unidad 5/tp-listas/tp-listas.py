
# 1) 
# notas_alumnos = [6,4,7,8,9]
# largo_array = len(notas_alumnos)
# promedio_notas = 0
# suma = 0
# nota_alta = notas_alumnos[0]
# nota_baja = notas_alumnos[0]

# print(f"Nota de los alumnos {notas_alumnos}")

# for i in range (largo_array):
#     if notas_alumnos[i] < nota_baja:
#           nota_baja = notas_alumnos[i]
#     if notas_alumnos[i] > nota_alta:
#            nota_alta = notas_alumnos[i]
#     suma= suma + notas_alumnos[i]  
# promedio_notas = suma / largo_array
# print (f"La nota mas baja es: ({nota_baja})")
# print (f"La nota mas alta es: ({nota_alta})")
# print (f"El promedio de las notas es: ({promedio_notas})")

# 2) 
# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# productos_lista = []
# for i in range (3):
#     producto = input("ingrese un producto que quiera a la lista: ")
#     productos_lista.append(producto)
# productos_lista.sort()
# print(productos_lista)
# producto_eliminar = input("quiere eliminar un producto de la lista? : ")
# productos_lista.remove(producto_eliminar)
# productos_lista.sort()
# print(productos_lista) 

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.



# import random
# numeros_azar = []
# numeros_pares= []
# numeros_impares= []
# largo_impar=0
# largo_par=0
# numeros_random =  random.sample(range(1, 10), 5)



# for i in numeros_random:
#     if (i%2==0):
#          numeros_pares.append(i)
#     if (i%2!=0):
#         numeros_impares.append(i)


# # print(numeros_random)
# largo_impar= len(numeros_impares)
# largo_par=len(numeros_pares)
# print(f"La cantidad de numeros pares es:{largo_par}")
# print(f"Nros pares {numeros_pares }")
# print(f"La cantidad de numeros impares es:{largo_impar}")
# print(f"Nros impares {numeros_impares }")

# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
# datos= [1,3,5,3,7,1,9,5,3]
# datos = [1,3,5,3,7,1,9,5,3]
# lista_nueva=[]

# for i in datos:
#     print(i)
#     if i not in lista_nueva:
#         lista_nueva.append(i)
# print(lista_nueva)


# 5) 
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada


# alumnos=['fernando','rosalia','kati','lucia','guada','romina','rosana','tor']
# opcion=""
# opcion=input("desea eliminar a un alumno? : E o Agregar a un alumno: A ").upper()
# if opcion == 'E':
#     nombre_a_eliminar=input("ingrese el nombre del alumno que desea eliminar: ").upper()
#     if nombre_a_eliminar in alumnos:
#         alumnos.remove(nombre_a_eliminar)
#     else: 
#         print("El nombre del alumno no esta en la lista")
# elif opcion == 'A':
#     nombre_a_agregar=input("Ingrese el nombre del alumno que desea agregar: ").title()
#     alumnos.append(nombre_a_agregar)
    

# for i in alumnos:
#     print( i, end=" ")



# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

# numeros  = [1,2,3,4,5,6,7]
# ultimo = numeros[-1]
# ultimo = [ultimo]
# lista_nueva =   ultimo + numeros[:-1] 
# for i in lista_nueva:
#     print(i, end=" ")


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 
# temperatura=[
#     [5,7] ,
#     [9,12],
#     [12,14],
#     [14,17],
#     [17,21],
#     [21,25],
#     [25,35],
# ]
# temperaturas_min=[]
# temperaturas_max=[]

# promedio_temp_maximo=0
# promedio_temp_minimo=0


# for temp_min in temperatura:
#     temperaturas_min.append(temp_min[0])

# for temp_max in temperatura:
#     temperaturas_max.append(temp_max[1])


# promedio_temp_minimo= sum(temperaturas_min) / len(temperaturas_min) 
# promedio_temp_maximo= sum(temperaturas_max) / len(temperaturas_max) 




# amplitud_dias=[]
# for amplitud in temperatura:
#     amplitud_dias.append(amplitud[1] - amplitud[0])
#     print(amplitud)
# dia_maximo_amplitud= amplitud_dias.index(max(amplitud_dias))+1



# print("Promedio temperaturas minimas: ",promedio_temp_minimo)
# print("Promedio temperaturas maximas: ",promedio_temp_maximo)
# print("El dia con mayor amplitud termica fue el dia: ",dia_maximo_amplitud)

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

# tateti=[]

# for i in range(3):
#     fila = []
#     for k in range(3):
#         fila.append(" - ")
#     tateti.append(fila)



# for fila in tateti:
#     for celda in fila:
#         print(celda,end=" ")
#     print()

# jugada = 0
# jugador1='x'
# jugadas=0

# while jugadas < 9:
#     print("turno jugardor", jugador1)

#     fila=int(input("ingrese la fila de 0-2: "))
#     columna = int(input("ingrese la columna de 0-2: "))
   
#     if tateti[fila][columna]==' - ':
#         tateti[fila][columna]=jugador1

#     for fila in tateti:
#         for celda in fila:
#            print(celda,end=" ")
#         print()

#     jugadas +=1

#     if jugador1 == 'x':
#        jugador1 =  'o'
#     else:
#         jugador1='x'

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.


# ventas_semanales=[
#     [1,5,7,8,9,2,7],
#     [1,3,6,7,1,2,10],
#     [1,5,2,3,9,4,28],
#     [1,10,2,5,9,12,7],
# ]

# ventas_productos = []
# mas_vendido_semana=[]
# dia_mayor_venta=0

# for filas in range(len(ventas_semanales)):
#     ventas_totales=0 # para que la suma no se pisen cuando termina cada iteracion 
#     mas_vendido=0
#     for columna in range(len(ventas_semanales[filas])):
#         ventas_totales+=ventas_semanales[filas][columna]
#     ventas_productos.append(ventas_totales)
  
# for i in  range(len(ventas_productos)):
#     print("Producto: ",i + 1,"cantidad de venta: ",ventas_productos[i])


# for dia in range(len(ventas_semanales[0])):
#     venta_total_dia=0
#     for producto in range(len(ventas_semanales)):
#         venta_total_dia+=ventas_semanales[producto][dia]
#     if venta_total_dia > dia_mayor_venta:
#         dia_mayor_venta=dia+1
#     print("Dia: ", dia+1, " ventas de : ",venta_total_dia)
# print("Mayor día con ventas fue: ", dia_mayor_venta)
