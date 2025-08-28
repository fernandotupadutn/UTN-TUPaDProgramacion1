#EJERCICIO-1
# edad=int(input("Ingrese su edad: "))
# mayor_edad = 18
# if edad >= mayor_edad: 
#     print("Es mayor de edad")
#-------------------------------------    
#EJERCICIO-2
# nota=int(input("Ingrese su nota: "))
# aprobado=6
# if nota >= aprobado:
#     print("Aprobado")
# else: 
#     print("Desaprobado")
#-------------------------------------  
#EJERCICIO-3
# nro_par=int(input("Ingrese un numero par: "))
# if (nro_par % 2 == 0):
#     print("Ha ingresado un numero par ")
# else: print("Por favor, ingrese un número par")
#-------------------------------------  
#EJERCICIO-4
# edad=int(input("Ingrese su edad: "))
# ninio=12
# adolecente=18
# adulto_joven=30

# if edad < ninio:
#     print("Niño/a")
# elif edad >= ninio and edad < adolecente:
#     print("Adolecente")
# elif edad >= adolecente and edad < adulto_joven:
#     print("Adulto/a joven")
# else: 
#     edad >= adulto_joven
#     print("Adulto/a")
#------------------------------------- 
#EJERCICIO-5
# password = input("Ingrese una contraseña que debe contener de 8 a 16 caracteres: ")
# characters = len(password)
# min=8
# max=14
# print(characters)
# if (characters >= min) and (characters <= max):
#     print("Ha ingresado una contraseña correcta")
# else: print("Ingrese una contraseña de entre 8 a 14 caracteres")
#------------------------------------- 
#EJERCICIO-6
# from statistics import mode,median,mean
# import random
# list=[random.randint(1,100) for i in range(50)]
# calculate_moda=mode(list)
# calculate_mediana=median(list)
# calculate_media=mean(list)
# print(calculate_moda)
# print(calculate_mediana)
# print(calculate_media)
#------------------------------------- 
# frase=input("Ingrese una frase: ")
# end =len(frase)
# nueva = ""
# if ( ("a" == frase[-1]) or ("e" == frase[-1]) or ("i" == frase[-1]) or ("o" == frase[-1]) or ("u" == frase[-1]) ):
#         nueva = frase + " ! " 
#         print(nueva)
# else:
#         print(frase)
#EJERCICIO-8
# usuario = input("Ingrese un usuario: ")
# opcion = int(input("1:- Obtener usuario en mayusculas\n 2:-Usuario en minusculas\n 3:-Si quiere el usuario con la primer letra en mayusculas\n"))
# if opcion == 1 : 
#     usuario= usuario.upper()
# elif opcion == 2: 
#     usuario = usuario.lower()
# elif opcion == 3: 
#     usuario = usuario.title()
# print(usuario)
#------------------------------------- 
#EJERCICIO-9
# terremoto_magnitud = int(input("Ingrese la magnitud del terremoto: "))
# if (terremoto_magnitud < 3) :
#     print("Muy leve imperceptible")
# elif (terremoto_magnitud >= 3 and terremoto_magnitud < 4 ):
#     print("Leve ligeramente perceptible")
# elif (terremoto_magnitud >= 4 and terremoto_magnitud < 5):
#     print("Moderado sentido por personas, pero generalmente no causa daños")
# elif (terremoto_magnitud >= 5 and terremoto_magnitud < 6 ):
#     print("Fuerte puede causar daños en estructuras débiles")    
# elif (terremoto_magnitud >= 6 and terremoto_magnitud < 7):
#     print("Muy fuerte puede causar daños significativos")
# elif (terremoto_magnitud >= 7 ):
#     print("Extremo puede causar graves daños a gran escala")
#------------------------------------- 

#EJERCICIO-10
# hemiferio = input("Hermiferio Norte o Sur? \n Ingrese S O N ")
# hemiferio = hemiferio.upper()
# mes = (input("Ingrese el mes en el que se encuentra: Por ejemplo: Diciembre"))
# dia = int(input("Ingrese el dia en el que se encuentra: "))
# mes = mes.title()

# if (mes == "Diciembre" and dia == 21) or (mes == "Marzo" and dia == 20) :
#     if(hemiferio == "N"):
#         print("Invierno")
#     elif(hemiferio == "S"):
#         print("Verano")
# elif (mes== "Marzo" and dia == 21 ) or (mes == "Junio" and dia == 20):
#    if(hemiferio == "N"):
#      print("Primavera")
#    elif(hemiferio == "S"):
#       print("Otoño")
# elif (mes == "Junio" and dia == 21 ) or (mes == "Septiembre" and dia == 20):
#     if(hemiferio == "N"):
#         print("Verano")
#     elif(hemiferio == "S"):
#         print("Invierno")
# elif (mes == "Septiembre" and dia == 21 ) or (mes == "Diciembre" and dia == 20):
#    if(hemiferio == "N"):
#         print("Otoño")
#    elif(hemiferio == "S"):
#         print("Primavera")
#------------------------------------- 
