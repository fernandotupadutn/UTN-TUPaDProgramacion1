#EJERCICIO-1
inicio=0
fin=100
for i in range(inicio, fin + 1):
    print(i)
#--------------------
#EJERCICIO-2
numero=int(input("Ingrese un numero entero: "))
contador = 0
if numero == 0: 
    contador = 1
else: 
    while numero > 0: 
        numero//= 10
        contador +=1
print("El numero tiene", contador, "digitos")
#----------------------------
#EJERCICIO-3
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
suma = 0 
for i in range(num_1+1,num_2):
    suma += i
    print(f"N°: {i}")
print(suma)     
#-----------------------------------
#EJERCICIO-4
num=int(input("Ingrese un numero: "))
suma = 0
while num != 0: 
    suma += num
    num = int(input("Ingrese un numero: "))
print("La suma es: ", suma)
#---------------------------------
#EJERCICIO-5
import random
contador=0
acertado=random.randint(0,9)
num=int(input("adivine el numero del 0 al 9: "))
while num !=acertado:
    num=int(input("no es el numero, ingrese otro: "))
    contador +=1
print(f"los intentos fueron {contador}")
print(f"el numero era {acertado}")
#--------------------
#EJERCICIO-6
for i in reversed(range(0,100)):
    if i%2==0:
        print(f"el nro par es: {i}")
#-------------------------
#EJERCICIO-7

num=int(input("ingrese un numero: "))
suma=0
for i in range(0,num + 1 ):
    print(i)
    suma+=i
print(suma) 
#--------------------------
#EJERCICIO-8
negativos=0
positivos=0
pares=0
impares=0
for i in range(1,10 + 1 ):
    num=int(input("ingrese numero del 1 al 100: "))
    if (num > 0):
         positivos+=1
    if(num%2==0):
        pares+=1
    if (num%2!=0):
         impares+=1
    if(num < 0):
         negativos+=1
print(f"los positivos son {positivos}\n, los pares son {pares}\n,los impares son {impares}\n, los negativos son {negativos}")
#-------------------------------------

