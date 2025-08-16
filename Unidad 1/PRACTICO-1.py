#EJERCICIO-1
print("Hello World!")
#---------------------------------------------------------------------------------
#EJERCICIO-2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre} !")
#---------------------------------------------------------------------------------
#EJERCICIO-3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#---------------------------------------------------------------------------------
#EJERCICIO-4
radio=float(input("Ingrese el radio del circulo: "))
pi=3.14159
area = pi * radio * radio
print(f"El area del circulo es: {area}")
#---------------------------------------------------------------------------------
#EJERCICIO-5
segundos= float(input("Ingrese la cantidad de segudos: "))
hora = 3600
horasCalculadas=segundos/hora
print(f"La cantidad de horas a partir de los segundos ingresados son: {horasCalculadas} horas")
#---------------------------------------------------------------------------------
#EJERCICIO-6
numero=int(input("Ingrese un numero para crear una tabla: "))
for i in range (1,11):
    print(numero,"x",i,"=", numero * i)
#---------------------------------------------------------------------------------
# EJERCICIO-7
numero1=int(input("Ingrese un numero distinto de 0: "))
numero2=int(input("Ingrese otro numero distinto de 0: "))
suma=(numero1+numero2)
resta=(numero1-numero2)
multiplicacion=(numero1*numero2)
division=(numero1/numero2)
print(f"el resultado de sumar los nros es: {suma}\n el resultado de restarlos es: {resta}" )
print(f"el resultado de multiplicarlos los nros es: {multiplicacion} \n el resultado de dividirlos es: {division}" )    
#---------------------------------------------------------------------------------
#EJERCICIO-8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso/(altura ** 2)
print(f"su masa corporal es de: {imc}")
#---------------------------------------------------------------------------------
#EJERCICIO-9
gradoscelsius=float(input("Ingrese la temperatura en grados celsius: "))
gradosFahrenheit = (9/5 * gradoscelsius + 32)
print(f"los grados {gradoscelsius} equivalentes  en fahrenheit son : {gradosFahrenheit}")
#---------------------------------------------------------------------------------
#EJERCICIO-10
numero1=float(input("Ingrese un numero: "))
numero2=float(input("Ingrese otro numero: "))
numero3=float(input("Ingrese otro numero: "))
promedio = (numero1 + numero2 + numero3 ) / 3
print(f"el promedio de los 3 numeros es: {promedio}")
#---------------------------------------------------------------------------------