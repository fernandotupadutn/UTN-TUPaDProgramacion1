# EJERCICIO N1 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero_usuario = int(input("Ingresa un número entero positivo: "))

if numero_usuario < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f" Factoriales de 1 hasta {numero_usuario}")
    for i in range(1, numero_usuario + 1):
        print(f"Factorial de {i} = {factorial(i)}")
# ------
# EJERCICIO N2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion_usuario = int(input("Ingresa la posición (n) de la serie de Fibonacci: "))

if posicion_usuario < 0:
    print("Ingresa un número positivo o cero.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion_usuario} ---")
    for i in range(posicion_usuario + 1):
        print(fibonacci(i), end=" ")
    print()
# --------

# EJERCICIO N3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

    
# --------

# EJERCICIO N4
def decimal_a_binario(n):
    n = int(n) 
    
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


# -------

# EJERCICIO N5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False


# --------
# EJERCICIO N6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# --------
# EJERCICIO N7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


# --------
# EJERCICIO N8
def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo_digito = numero % 10
    
    coincidencia = 0
    if ultimo_digito == digito:
        coincidencia = 1
        
    return coincidencia + contar_digito(numero // 10, digito)




