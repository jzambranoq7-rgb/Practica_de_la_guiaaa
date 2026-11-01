# ==========================================
# EJERCICIOS PROPUESTOS
# ==========================================

# ==========================================
# Ejercicio 1: Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
# ==========================================
# ENTRADA: n (int)
# PROCESO: Iterar con for de 1 a 12 multiplicando n * i
# SALIDA:  Tabla de multiplicar del 1 al 12
# ==========================================

n = int(input('Ingrese el número del cual quiere visualizar su tabla: '))

for i in range(1, 13):
    print(f'{n} * {i} = {n * i}')

# ==========================================
# Ejercicio de práctica (modificado): Generar la tabla de multiplicar de N usando un ciclo while y almacenar los resultados en un diccionario {multiplicador: producto}.
# ==========================================
# ENTRADA: n_tabla (int)
# PROCESO: Ciclo while de 1 a 12 calculando producto = n_tabla * i y guardándolo en un diccionario
# SALIDA:  Diccionario con la tabla de multiplicar completa
# ==========================================

n_tabla = int(input('Ingrese el número para generar la tabla en diccionario: '))
tabla_dict = {}
contador_tabla = 1

while contador_tabla <= 12:
    tabla_dict[contador_tabla] = n_tabla * contador_tabla
    contador_tabla += 1

print(f"Tabla de multiplicar del {n_tabla}:")
for mult, prod in tabla_dict.items():
    print(f"{n_tabla} x {mult} = {prod}")

# ==========================================
# Ejercicio 2: Lee un número y cuenta cuántos dígitos tiene (sin convertir a string)
# ==========================================
# ENTRADA: numero (int)
# PROCESO: Dividir sucesivamente n entre 10 con división entera (// 10) e incrementar contador
# SALIDA:  Cantidad de dígitos del número
# ==========================================

numero = int(input('Número: '))
n = abs(numero)
digitos = 0

if n == 0:
    digitos = 1
else:
    while n > 0:
        digitos += 1
        n = n // 10

print(f'{digitos} dígitos')

# ==========================================
# Ejercicio de práctica (modificado): Invertir un número entero matemáticamente (sin convertir a string) utilizando divisiones enteras y residuos.
# ==========================================
# ENTRADA: num_a_invertir (int)
# PROCESO: Extraer el último dígito con % 10, construir invertido = (invertido * 10) + digito y reducir num //= 10
# SALIDA:  Número original y su versión invertida
# ==========================================

num_a_invertir = int(input('Ingrese un número entero para invertir: '))
aux_inv = abs(num_a_invertir)
num_invertido = 0

while aux_inv > 0:
    dig = aux_inv % 10
    num_invertido = (num_invertido * 10) + dig
    aux_inv //= 10

if num_a_invertir < 0:
    num_invertido = -num_invertido

print(f"Número invertido: {num_invertido}")

# ==========================================
# Ejercicio 3: Lee N números y muestra la suma de los pares y la suma de los impares por separado
# ==========================================
# ENTRADA: n (int), x números enteros (int)
# PROCESO: Evaluar si x % 2 == 0 para acumular en suma_pares, caso contrario en suma_impares
# SALIDA:  Total de suma de pares y total de suma de impares
# ==========================================

n = int(input('¿Cuántos números ingresará?: '))
suma_pares = 0
suma_impares = 0

for i in range(n):
    x = int(input(f'Número {i + 1}: '))
    if x % 2 == 0:
        suma_pares += x
    else:
        suma_impares += x

print(f'La suma de los pares es: {suma_pares}')
print(f'Suma impares: {suma_impares}')

# ==========================================
# Ejercicio de práctica (modificado): Leer números indefinidamente hasta que el usuario ingrese 0, calculando el promedio de los pares y el promedio de los impares.
# ==========================================
# ENTRADA: val_ingresado (int) hasta ingresar 0 (condición de parada)
# PROCESO: Bucle while con centinela, acumular listas separadas de pares e impares y calcular sus promedios
# SALIDA:  Promedio aritmético de los números pares y de los impares
# ==========================================

lista_pares = []
lista_impares = []

while True:
    val_ingresado = int(input('Ingrese un número (0 para terminar): '))
    if val_ingresado == 0:
        break
    if val_ingresado % 2 == 0:
        lista_pares.append(val_ingresado)
    else:
        lista_impares.append(val_ingresado)

prom_p = sum(lista_pares) / len(lista_pares) if lista_pares else 0
prom_i = sum(lista_impares) / len(lista_impares) if lista_impares else 0

print(f"Pares ingresados: {lista_pares} | Promedio: {prom_p:.2f}")
print(f"Impares ingresados: {lista_impares} | Promedio: {prom_i:.2f}")

# ==========================================
# Ejercicio 4: Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
# ==========================================
# ENTRADA: edad (int)
# PROCESO: Bucle while infinito que valida 0 <= edad <= 120 para romper el ciclo (break)
# SALIDA:  Mensaje de error si es inválida o confirmación de la edad válida ingresada
# ==========================================

while True:
    edad = int(input('Edad (0-120): '))
    if 0 <= edad <= 120:
        break
    print('Edad inválida, intenta de nuevo')

print(f'Edad válida: {edad}')

# ==========================================
# Ejercicio de práctica (modificado): Validar el ingreso de una nota académica entre 0.0 y 10.0 con un máximo de 3 intentos permitidos.
# ==========================================
# ENTRADA: calificacion (float)
# PROCESO: Bucle while controlando un contador de intentos restantes; romper si la nota está en rango
# SALIDA:  Confirmación de la nota ingresada o aviso de intentos agotados
# ==========================================

intentos_restantes = 3
nota_valida = None

while intentos_restantes > 0:
    calificacion = float(input(f"Ingrese nota (0.0 a 10.0) [Intentos restantes: {intentos_restantes}]: "))
    if 0.0 <= calificacion <= 10.0:
        nota_valida = calificacion
        break
    print("Nota fuera de rango.")
    intentos_restantes -= 1

if nota_valida is not None:
    print(f"Calificación registrada exitosamente: {nota_valida:.2f}")
else:
    print("Ha superado el límite de intentos permitidos.")

# ==========================================
# Ejercicio 5: Genera un número secreto entre 1 y 100. El usuario intenta adivinar. En cada intento le dices si es <<mayor>> o <<menor>>. Cuenta cuántos intentos usó
# ==========================================
# ENTRADA: intento (int)
# PROCESO: Comparar intento con secreto generado aleatoriamente (1 a 100) y contar repeticiones
# SALIDA:  Pistas ("Es mayor" / "Es menor") y mensaje final con total de intentos
# ==========================================

import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input('Adivina (1-100): '))
    intentos += 1
    if intento == secreto:
        print(f'¡Correcto, y tan solo en {intentos} intentos!')
        break
    elif intento < secreto:
        print('Es mayor')
    else:
        print('Es menor')

# ==========================================
# Ejercicio de práctica (modificado): Juego de adivinar número con límite de 7 intentos, registrando cada intento fallido en una lista de historial.
# ==========================================
# ENTRADA: intento_usr (int)
# PROCESO: Comparar con número aleatorio, guardar valor en lista 'historial_intentos' y verificar si se agota el tope de 7 oportunidades
# SALIDA:  Pistas de dirección, historial de jugadas y resultado (victoria o derrota)
# ==========================================

numero_objetivo = random.randint(1, 100)
max_intentos = 7
historial_intentos = []
ganado = False

for turno in range(1, max_intentos + 1):
    intento_usr = int(input(f"Intento {turno}/{max_intentos} - Adivina (1-100): "))
    historial_intentos.append(intento_usr)

    if intento_usr == numero_objetivo:
        print(f"¡Felicidades! Adivinaste el número {numero_objetivo} en {turno} intentos.")
        ganado = True
        break
    elif intento_usr < numero_objetivo:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if not ganado:
    print(f"Se acabaron los intentos. El número era: {numero_objetivo}")

print(f"Historial de intentos realizados: {historial_intentos}")

# ==========================================
# Ejercicio 6: Muestra los primeros N números de Fibonacci. La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... Cada número es la suma de los dos anteriores.
# ==========================================
# ENTRADA: n (int)
# PROCESO: Generar los primeros n términos actualizando a, b = b, a + b
# SALIDA:  Serie de Fibonacci impresa en una sola línea
# ==========================================

n = int(input('¿Cuántos?: '))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# ==========================================
# Ejercicio de práctica (modificado): Función generar_fibonacci(limite) que retorne una lista con los términos de Fibonacci menores o iguales a un valor tope dado.
# ==========================================
# ENTRADA: tope (int)
# PROCESO: Bucle while acumulando términos en una lista mientras el valor actual sea menor o igual al límite especificado
# SALIDA:  Lista con la secuencia de Fibonacci hasta el tope
# ==========================================

def generar_fibonacci(limite):
    serie = []
    x, y = 0, 1
    while x <= limite:
        serie.append(x)
        x, y = y, x + y
    return serie


tope = int(input("Mostrar términos de Fibonacci menores o iguales a: "))
resultado_fibo = generar_fibonacci(tope)
print(f"Términos generados: {resultado_fibo}")
print(f"Cantidad total de elementos: {len(resultado_fibo)}")