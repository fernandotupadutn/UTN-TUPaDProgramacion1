EJERCICIO-1
def holamundo():
  return print("Hola mundo")
holamundo()

EJERCICIO-2
def saludar_usuario(nombre):
    return print(f"Hola, {nombre}, como estas?")


nombre=input("Ingrese su nombre: ")

saludar_usuario(nombre)


EJERCICIO-3
def informacion_personal(nombre,apellido,edad,recidencia):
    return print(f"Hola me llamo {nombre}, mi apellido es {apellido}, tengo {edad} años y vivo en {recidencia}")


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
recidencia=input("Ingrese su recidencia: ")


informacion_personal(nombre,apellido,edad,recidencia)

EJERCICIO-4
def calcular_area_circulo(radio):
    area_calculada=3.1416*radio*radio
    return area_calculada

radio_ingresado=int(input("Ingrese el radio "))

print(calcular_area_circulo(radio_ingresado))

EJERCICIO-5
def segundos_a_horas(segundos):
    segundos_calculados=segundos/3600
    return segundos_calculados

ingresar_segundos=int(input("ingrese los segundos "))

print(segundos_a_horas(ingresar_segundos),"Hs")


EJERCICIO-6
def tabla_multiplicar(n):
    for i in range (11):
      resultado=print (n , " x ", i , " = ", i*n)
    return resultado

tabla=int(input("ingrese el nro de la tabla de multiplicar que quiera hacer "))
tabla_multiplicar(tabla)

EJERCICIO-7
def operaciones_basicas(a,b):
    
    multiplicacion=a*b
    division=a/b
    suma=a+b
    resta=a-b

    resultados=f"La suma de los numeros es {a} y {b} es {suma} \n La resta de {a} y {b} es {resta} \n La multiplicacion de {a} y {b} es {multiplicacion} \n"
    f"La division de {a} y {b} es {division}"  

    return resultados

n1=int(input("ingrese un numero "))
n2=int(input("ingrese otro numero "))

print (operaciones_basicas(n1,n2))


EJERCICIO-8
def calcular_imc(peso,altura):
    altura_metros=altura/100
    imc= peso / ( altura_metros ** 2 )
    return imc


altura=float(input("Ingrese su altura "))
peso=float(input("Ingrese su peso "))

print(calcular_imc(peso , altura))

EJERCICIO-9
def celsius_a_fahrenheit(temp):
    
    temperatura=(temp*9)/5+32

    
    return temperatura

temperatura_ingresada=float(input("ingrese la temperatura en celsius "))

print(celsius_a_fahrenheit(temperatura_ingresada))

EJERCICIO-10
def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    return promedio

nota1=float(input("ingrese la 1er nota "))
nota2=float(input("ingrese la 2da nota "))
nota3=float(input("ingrese la 3era nota "))

print(calcular_promedio(nota1,nota2,nota3))


# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    return promedio

nota1=float(input("ingrese la 1er nota "))
nota2=float(input("ingrese la 2da nota "))
nota3=float(input("ingrese la 3era nota "))

print(calcular_promedio(nota1,nota2,nota3))