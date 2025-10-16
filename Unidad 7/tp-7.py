# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# precios_frutas['Naranja']=1200
# precios_frutas['Manzana']=1500
# precios_frutas['Pera']=2300
# print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas['Banana']=1330
# precios_frutas['Manzana']=1700
# precios_frutas['Melón']=2800

# print(precios_frutas)

# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# # desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# # precios
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# lista_sin_precios=precios_frutas.keys()

# print('Lista sin precios',lista_sin_precios)
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

lista_telefono={}

for _ in range(2):
 nombre=input("Ingrese el nombre de la persona: ")
 telefono=int(input("Ingrese el numero de telofo: "))
 lista_telefono[nombre]=telefono

nombre=input("Nombre a buscar")

if nombre in lista_telefono.keys():
  encontrado={nombre:lista_telefono[nombre]}
  print(encontrado)
else:
  print("No esta cargado")

  # 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra


frase=input("ingrese una frase ")
frase= frase.split() #separamos las frase

unicas=set(frase) #convertimos a set la frase para que saque las repetidas

print(frase)
print(unicas)

recuento={} #creamos un diccionario para ver que palabra esta repetida y cuantas veces

for f in frase:
    if f in recuento:
        recuento[f]+=1
    else:
        recuento[f]=1

print(recuento)
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos={}

for i in range(3):
    notas=[]
    nombre=input("ingrese el nombre")
    for nota in range(3):
     nota=int(input("ingrese la nota"))
     notas.append(nota)
    alumnos[nombre]=tuple(notas)

for alumno,nota in alumnos.items():
   promedio = sum(nota) / len(nota)
   print("Alumno: ",alumno,"nota:",nota,"promedio:",promedio)

   # 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1={1,2,3,4,5,6}
parcial2={4,5,6,7,8,9}

ambos=parcial1 & parcial2
al_menos_dos=parcial1 ^ parcial2 
aprobaron_al_menos_uno=parcial1 | parcial2

print("alumnos que aprobaron ambos parciales: ", ambos)
print("alumnos que aprobaron uno de los dos: ",al_menos_dos)
print("alumnos totales que aprobaron al menos un parciale: ",aprobaron_al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos={}

cantida = int(input("ingrese la cantidad de productos "))

for producto in range(cantida):
    producto_nombre=input("nombre del producto: ")
    stock=int(input("stock: "))
    productos[producto_nombre]=stock



buscar_producto=input("nombre a buscar: ")
for producto,stock in productos.items():
    if buscar_producto in producto:
       agregar_stock=int(input("cuanto stock va a sumar: "))
       stock+=agregar_stock
       print(producto,stock) 
    else:
        productos[producto_nombre]=0


print(productos.items())

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda={
    ("lunes","20:00"):"ir gimnacion",
    ("martes","16:00"):"trabajo"
    }

dia=input("ingrese el dia del evento")
hora=input("ingrese la hora")

claves=(dia,hora)


if claves in agenda:
    print("Actividad",agenda[claves])
else:
    print("No hay actividad ese dia")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# original={"Argentina":"Buenos Aires","Chile":"Santiago"}
# invertido={}


# for paises,capitales in original.items():
#     invertido[capitales]=paises

# print(original)
# print(invertido)