# ==============================================================================
# EJERCICIOS DE TALLER (GUÍA)
# ==============================================================================

# ==========================================
# Ejercicio 1: Leer el nombre del usuario y saludarlo por su nombre.
# ==========================================
# ENTRADA: Nombre (string)
# PROCESO: Interpolar el nombre en el saludo
# SALIDA:  Mensaje de bienvenida
# ==========================================

Nombre = input('Escriba su nombre: ')
print(f'Hola {Nombre}, bienvenido')

# ==========================================
# Ejercicio de práctica (modificado): Leer nombre, apellido y edad del usuario, formatear el nombre completo a mayúsculas y calcular en qué año cumplirá 100 años.
# ==========================================
# ENTRADA: nombre (string), apellido (string), edad (int)
# PROCESO: Unir nombre y apellido con .upper(), calcular año_centenario = 2026 + (100 - edad)
# SALIDA:  Mensaje de bienvenida formal y proyección de edad
# ==========================================

nombre_usr = input('Ingrese su nombre: ')
apellido_usr = input('Ingrese su apellido: ')
edad_usr = int(input('Ingrese su edad: '))

nombre_completo = f"{nombre_usr} {apellido_usr}".upper()
anio_centenario = 2026 + (100 - edad_usr)

print(f"Bienvenido estimado/a {nombre_completo}. Cumplirás 100 años en el año {anio_centenario}.")

# ==========================================
# Ejercicio 2: Leer tres notas de un estudiante y mostrar su promedio.
# ==========================================
# ENTRADA: n1, n2, n3 (float)
# PROCESO: (n1 + n2 + n3) / 3
# SALIDA:  Promedio
# ==========================================

n1 = float(input('Escriba una calificación: '))
n3 = float(input('Escriba otra calificación: '))
n2 = float(input('Escriba otra calificación: '))

Promedio = (n1 + n2 + n3) / 3

print(f'El promedio es: {Promedio}')

# ==========================================
# Ejercicio de práctica (modificado): Leer 3 calificaciones almacenándolas en una lista y determinar si el estudiante aprueba (promedio >= 7.0) o reprueba.
# ==========================================
# ENTRADA: calificaciones individuales (float)
# PROCESO: Guardar notas en una lista, calcular promedio = sum(lista) / len(lista) y evaluar condición lógica
# SALIDA:  Promedio final y estado del estudiante (Aprobado / Reprobado)
# ==========================================

notas = []
for i in range(3):
    calif = float(input(f'Ingrese la calificación {i + 1}: '))
    notas.append(calif)

promedio_final = sum(notas) / len(notas)
estado = "Aprobado" if promedio_final >= 7.0 else "Reprobado"

print(f'Notas ingresadas: {notas}')
print(f'Promedio calculado: {promedio_final:.2f} — Estado: {estado}')

# ==========================================
# Ejercicio 3: Leer la base y la altura de un rectángulo y mostrar su área y su perímetro. (Recuerda área=base x altura, perímetro = 2x (base + altura))
# ==========================================
# ENTRADA: base, altura (float)
# PROCESO: area = base * altura | perimetro = 2 * (base + altura)
# SALIDA:  Área y perímetro con 2 decimales
# ==========================================

base = float(input('Ingrese la base: '))
altura = float(input('Ingrese la altura: '))

area = base * altura
perimetro = 2 * (base + altura)

print(f'El área es: {area:.2f} y el perímetro es: {perimetro:.2f}')

# ==========================================
# Ejercicio de práctica (modificado): Leer el radio de un círculo, calcular su área y perímetro (circunferencia) y guardar los resultados en una tupla.
# ==========================================
# ENTRADA: radio (float)
# PROCESO: area_circulo = pi * radio^2 | perimetro_circulo = 2 * pi * radio, empaquetar en una tupla
# SALIDA:  Resultados de área y perímetro redondeados a 2 decimales
# ==========================================

import math

radio = float(input('Ingrese el radio del círculo: '))

area_circ = math.pi * (radio ** 2)
perimetro_circ = 2 * math.pi * radio

metricas = (area_circ, perimetro_circ)

print(f'Área del círculo: {metricas[0]:.2f}')
print(f'Perímetro del círculo: {metricas[1]:.2f}')

# ==========================================
# Ejercicio 4: Leer el precio de un producto sin IVA y mostrar el IVA y el precio final. El IVA en Ecuador es 15%
# ==========================================
# ENTRADA: precio (float)
# PROCESO: iva = precio * 0.15 | total = precio + iva
# SALIDA:  IVA y total a pagar con 2 decimales
# ==========================================

IVA = 0.15

precio = float(input("Precio sin IVA: $"))
iva = precio * IVA
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")

# ==========================================
# Ejercicio de práctica (modificado): Lee el precio total con IVA incluido (15%) y desglosa el precio base (subtotal) y el valor exacto del impuesto.
# ==========================================
# ENTRADA: total_con_iva (float)
# PROCESO: subtotal = total_con_iva / 1.15 | valor_iva = total_con_iva - subtotal
# SALIDA:  Subtotal sin impuesto y monto del IVA desglosado a 2 decimales
# ==========================================

total_con_iva = float(input("Ingrese el total pagado con IVA incluido: $"))

subtotal = total_con_iva / 1.15
valor_iva = total_con_iva - subtotal

print(f"Subtotal neto: ${subtotal:.2f}")
print(f"IVA incluido:  ${valor_iva:.2f}")

# ==========================================
# Ejercicio 5: Leer un número entero y determinar si es par o impar
# ==========================================
# ENTRADA: numero (int)
# PROCESO: Evaluar si numero % 2 == 0
# SALIDA:  Mensaje indicando si es par o impar
# ==========================================

numero = int(input('Ingrese un número: '))

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')

# ==========================================
# Ejercicio de práctica (modificado): Leer un número entero y determinar si es positivo, negativo o cero, evaluando además si es múltiplo de 5.
# ==========================================
# ENTRADA: num_eval (int)
# PROCESO: Estructura condicional if/elif/else para el signo y evaluación con operador residuo num_eval % 5 == 0
# SALIDA:  Diagnóstico completo de signo y multiplicidad
# ==========================================

num_eval = int(input("Ingrese un número entero para evaluar: "))

if num_eval > 0:
    signo = "positivo"
elif num_eval < 0:
    signo = "negativo"
else:
    signo = "cero"

es_mult_5 = (num_eval % 5 == 0) and (num_eval != 0)

print(f"El número {num_eval} es {signo}.")
if es_mult_5:
    print(f"Además, {num_eval} es múltiplo de 5.")
else:
    print(f"{num_eval} no es múltiplo de 5.")

# ==========================================
# Ejercicio 6: Leer una cantidad total de segundos y mostrarla como HH:MM:SS. Ejemplo: 3275 -> 01:02:05
# ==========================================
# ENTRADA: seconds (int)
# PROCESO: horas = seconds // 3600 | resto = seconds % 3600 | minutos = resto // 60 | segundos = resto % 60
# SALIDA:  Tiempo en formato HH:MM:SS
# ==========================================

seconds = int(input("Ingrese el tiempo en segundos: "))
horas = seconds // 3600
resto = seconds % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

# ==========================================
# Ejercicio de práctica (modificado): Pide horas, minutos y segundos por separado y calcula el total consolidado en segundos.
# ==========================================
# ENTRADA: h (int), m (int), s (int)
# PROCESO: total_seg = (h * 3600) + (m * 60) + s
# SALIDA:  Total acumulado en segundos
# ==========================================

h = int(input("Ingrese horas: "))
m = int(input("Ingrese minutos: "))
s = int(input("Ingrese segundos: "))

total_seg = (h * 3600) + (m * 60) + s

print(f"El tiempo total acumulado es: {total_seg} segundos")

# ==========================================
# Ejercicio 7: Un cajero solo tiene billetes de $20, $10, $5 y $1. Dado un monto, mostrar cuántos billetes de cada uno se necesitan (usando la menor cantidad)
# ==========================================
# ENTRADA: monto (int)
# PROCESO: Descomponer el monto usando divisiones enteras (//) y residuos (%) para billetes de 20, 10, 5 y 1
# SALIDA:  Cantidad de billetes de cada denominación
# ==========================================

monto = int(input("Monto: $"))
resto = monto

b20 = resto // 20
resto = resto % 20

b10 = resto // 10
resto = resto % 10

b5 = resto // 5
resto = resto % 5

b1 = resto // 1
resto = resto % 1

print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")

# ==========================================
# Ejercicio de práctica (modificado): Descomponer un monto en denominaciones de billetes de $100, $50, $20, $10, $5 y $1 almacenando el desglose en un diccionario.
# ==========================================
# ENTRADA: monto_cajero (int)
# PROCESO: Iterar sobre una lista de denominaciones calculando cantidad // y actualizando residuo % para guardar en diccionario
# SALIDA:  Diccionario con la cantidad asignada a cada tipo de billete
# ==========================================

monto_cajero = int(input("Ingrese monto total a retirar: $"))
denominaciones = [100, 50, 20, 10, 5, 1]
desglose = {}
saldo_restante = monto_cajero

for billete in denominaciones:
    cant_b = saldo_restante // billete
    saldo_restante = saldo_restante % billete
    desglose[f"${billete}"] = cant_b

print(f"Desglose para ${monto_cajero}:")
for denom, qty in desglose.items():
    if qty > 0:
        print(f"{denom} x {qty}")

# ==========================================
# Ejercicio 8: Lee un número N y mostrar los números del 1 al N
# ==========================================
# ENTRADA: n (int)
# PROCESO: Recorrer con un bucle for desde 1 hasta n
# SALIDA:  Los números del 1 al n impresos uno por línea
# ==========================================

n = int(input('Ingrese un numero hasta el que contar: '))

for i in range(1, n + 1):
    print(i)

# ==========================================
# Ejercicio de práctica (modificado): Lee un número N y muestra la cuenta regresiva desde N hasta 1 usando un bucle while, guardando los valores en una lista.
# ==========================================
# ENTRADA: n_regresivo (int)
# PROCESO: Bucle while con decremento (contador -= 1) almacenando cada valor en una lista
# SALIDA:  Lista con la secuencia en orden descendente
# ==========================================

n_regresivo = int(input('Ingrese un número para la cuenta regresiva: '))
contador = n_regresivo
lista_conteo = []

while contador >= 1:
    lista_conteo.append(contador)
    contador -= 1

print(f"Cuenta regresiva: {lista_conteo}")

# ==========================================
# Ejercicio 9: Leer N y calcular la suma de 1 + 2 + 3 + ... + N
# ==========================================
# ENTRADA: numero (int)
# PROCESO: Acumular la suma de los valores de i desde 1 hasta numero
# SALIDA:  Resultado total de la suma
# ==========================================

numero = int(input('Número a sumar: '))
suma = 0

for i in range(1, numero + 1):
    suma = suma + i

print(f'Suma: {suma}')

# ==========================================
# Ejercicio de práctica (modificado): Leer N y calcular la suma de los primeros N números utilizando tanto la fórmula de Gauss como un ciclo while, comparando ambos resultados.
# ==========================================
# ENTRADA: n_gauss (int)
# PROCESO: suma_formula = (n * (n + 1)) // 2 | suma_while iterando con contador
# SALIDA:  Resultado obtenido por ambas vías para verificar equivalencia
# ==========================================

n_gauss = int(input('Ingrese N para calcular la suma acumulada: '))

suma_formula = (n_gauss * (n_gauss + 1)) // 2

suma_while = 0
idx = 1
while idx <= n_gauss:
    suma_while += idx
    idx += 1

print(f"Suma por bucle while: {suma_while}")
print(f"Suma por fórmula matemática: {suma_formula}")

# ==========================================
# Ejercicio 10: Factorial de N: Leer N y calcular el factorial (N! = 1 x 2 x 3 ... x N). Ejemplo: 5! = 120
# ==========================================
# ENTRADA: n (int)
# PROCESO: Multiplicar consecutivamente fact * i desde 1 hasta n
# SALIDA:  Factorial resultante (n!)
# ==========================================

n = int(input("Ingrese un número: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f'{n}! = {fact}')

# ==========================================
# Ejercicio de práctica (modificado): Calcular el factorial de un número N mediante un ciclo while con validación para valores negativos y caso base 0! = 1.
# ==========================================
# ENTRADA: num_fact (int)
# PROCESO: Validar num_fact >= 0, acumular producto en variable resultado decrementando el valor inicial con while
# SALIDA:  El valor del factorial o mensaje de error si el número es negativo
# ==========================================

num_fact = int(input("Ingrese un número para calcular su factorial con while: "))

if num_fact < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado_fact = 1
    temp = num_fact
    while temp > 1:
        resultado_fact *= temp
        temp -= 1
    print(f"Resultado de {num_fact}! = {resultado_fact}")

# ==========================================
# Ejercicio 11: Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (Nota >= 70)
# ==========================================
# ENTRADA: n (int), notas de cada estudiante (float)
# PROCESO: Leer cada nota y contar si cumple la condición (nota >= 70)
# SALIDA:  Cantidad de estudiantes aprobados sobre el total n
# ==========================================

n = int(input('¿Cuántos estudiantes son?: '))
aprobados = 0

for i in range(n):
    nota = float(input(f'Nota {i + 1}: '))
    if nota >= 70:
        aprobados += 1

print(f'Aprobados: {aprobados} de {n}')

# ==========================================
# Ejercicio de práctica (modificado): Leer las notas de N estudiantes, clasificarlas en dos listas separadas (aprobados y reprobados) y mostrar el porcentaje de aprobación.
# ==========================================
# ENTRADA: total_est (int), calificaciones individuales (float)
# PROCESO: Separar notas en listas 'lista_aprobados' y 'lista_reprobados', calcular tasa_aprobacion = (len(aprobados) / total) * 100
# SALIDA:  Sublistas de calificaciones y porcentaje general de aprobación
# ==========================================

total_est = int(input('Cantidad de estudiantes a evaluar: '))
lista_aprobados = []
lista_reprobados = []

for k in range(total_est):
    calif = float(input(f'Calificación del alumno {k + 1}: '))
    if calif >= 70:
        lista_aprobados.append(calif)
    else:
        lista_reprobados.append(calif)

porcentaje = (len(lista_aprobados) / total_est) * 100 if total_est > 0 else 0

print(f"Notas aprobadas: {lista_aprobados}")
print(f"Notas reprobadas: {lista_reprobados}")
print(f"Porcentaje de aprobación: {porcentaje:.1f}%")

# ==========================================
# Ejercicio 12: Leer las notas de N estudiantes y mostrar la más alta
# ==========================================
# ENTRADA: n (int), notas individuales (float)
# PROCESO: Comparar cada nota ingresada para almacenar y actualizar la mayor
# SALIDA:  La nota más alta ingresada
# ==========================================

n = int(input('Cuántas notas ingresará?: '))
maximanota = float('-inf')

for i in range(n):
    nota = float(input(f'Nota {i + 1}: '))
    if nota > maximanota:
        maximanota = nota

print(f'Nota más alta: {maximanota}')

# ==========================================
# Ejercicio de práctica (modificado): Leer N notas, guardarlas en una lista y determinar tanto la nota más alta como la más baja sin usar max() ni min().
# ==========================================
# ENTRADA: cantidad_notas (int), calificaciones (float)
# PROCESO: Almacenar en lista e inicializar 'mayor' y 'menor' con el primer elemento para comparar iterativamente con for
# SALIDA:  La calificación más alta y la más baja del grupo
# ==========================================

cantidad_notas = int(input('¿Cuántas calificaciones registrará?: '))
registro_notas = []

for pos in range(cantidad_notas):
    val = float(input(f'Nota {pos + 1}: '))
    registro_notas.append(val)

if registro_notas:
    mayor_nota = registro_notas[0]
    menor_nota = registro_notas[0]
    for elemento in registro_notas:
        if elemento > mayor_nota:
            mayor_nota = elemento
        if elemento < menor_nota:
            menor_nota = elemento
    print(f"Nota más alta registrada: {mayor_nota}")
    print(f"Nota más baja registrada: {menor_nota}")

# ==========================================
# Ejercicio 13: Leer un número y determinar si es primo (solo divisible entre 1 y él mismo)
# ==========================================
# ENTRADA: n (int)
# PROCESO: Verificar si n < 2 o si tiene divisores entre 2 y raíz cuadrada de n
# SALIDA:  Mensaje indicando si el número es primo o no
# ==========================================

n = int(input('Ingrese un número: '))
es_primo = True

if n < 2:
    es_primo = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(f'El número {n} es primo')
else:
    print(f'El número {n} no es primo')

# ==========================================
# Ejercicio de práctica (modificado): Leer un número límite N y generar una lista con todos los números primos comprendidos entre 1 y N usando un bucle while.
# ==========================================
# ENTRADA: limite_primos (int)
# PROCESO: Iterar desde 2 hasta limite_primos con while, evaluando primalidad y agregando los primos encontrados a una lista
# SALIDA:  Lista con la secuencia de números primos encontrados
# ==========================================

limite_primos = int(input('Generar primos hasta el número: '))
primos_encontrados = []
actual = 2

while actual <= limite_primos:
    divisible = False
    divisor = 2
    while divisor * divisor <= actual:
        if actual % divisor == 0:
            divisible = True
            break
        divisor += 1
    if not divisible:
        primos_encontrados.append(actual)
    actual += 1

print(f"Primos hasta {limite_primos}: {primos_encontrados}")


# ==========================================
# Ejercicio 14: Escribir una función calcular_iva(precio) que reciba un precio y retorne el IVA (15%). Usarla desde el programa principal
# ==========================================
# ENTRADA: precio (float)
# PROCESO: Multiplicar precio * 0.15 dentro de la función calcular_iva()
# SALIDA:  El valor del IVA formateado con 2 decimales
# ==========================================

def calcular_iva(precio):
    return precio * 0.15


# Programa principal
precio = float(input('ingrese le pcio: $'))
iva = calcular_iva(precio)
print(f'El IVA de ${precio:.2f}: ${iva:.2f}')


# ==========================================
# Ejercicio de práctica (modificado): Función calcular_descuento_y_total(precio, porcentaje_desc) que retorne el valor descontado y el total final a pagar en una tupla.
# ==========================================
# ENTRADA: monto_base (float), tasa_descuento (float)
# PROCESO: descuento = precio * (porcentaje / 100), total = precio - descuento, empaquetar y retornar tupla (descuento, total)
# SALIDA:  Detalle del descuento aplicado y precio neto final
# ==========================================

def calcular_descuento_y_total(precio, porcentaje_desc):
    descuento = precio * (porcentaje_desc / 100)
    total_pagar = precio - descuento
    return descuento, total_pagar


monto_base = float(input('Monto de compra: $'))
tasa = float(input('Porcentaje de descuento (%): '))

ahorro, valor_final = calcular_descuento_y_total(monto_base, tasa)

print(f"Descuento aplicado: ${ahorro:.2f}")
print(f"Total a pagar:      ${valor_final:.2f}")


# ==========================================
# Ejercicio 15: Escribir una función que reciba un número y retorne True si es primo, False si no.
# ==========================================
# ENTRADA: num (int)
# PROCESO: Evaluar divisibilidad hasta la raíz cuadrada en es_primo() y probar con un rango del 2 al 30
# SALIDA:  Mensaje de validación del número y lista de números primos entre 2 y 30
# ==========================================

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Número: "))
if es_primo(num):
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")

print("Primos entre 2 y 30:")
for k in range(2, 31):
    if es_primo(k):
        print(k, end=" ")
print()


# ==========================================
# Ejercicio de práctica (modificado): Función primeros_n_primos(n) que genere y retorne una lista con los primeros N números primos usando la función auxiliar es_primo().
# ==========================================
# ENTRADA: cantidad_primos (int)
# PROCESO: Bucle while que evalúa números correlativos con es_primo() hasta acumular la cantidad requerida
# SALIDA:  Lista con los primeros N números primos
# ==========================================

def primeros_n_primos(n):
    lista_primos = []
    candidato = 2
    while len(lista_primos) < n:
        if es_primo(candidato):
            lista_primos.append(candidato)
        candidato += 1
    return lista_primos


cantidad_primos = int(input("¿Cuántos números primos desea generar?: "))
resultado_primos = primeros_n_primos(cantidad_primos)
print(f"Los primeros {cantidad_primos} primos son: {resultado_primos}")


# ==========================================
# Ejercicio 16: Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
# ==========================================
# ENTRADA: num (int)
# PROCESO: Extraer el último dígito con residuo (% 10) y reducir con división entera (// 10) de forma iterativa
# SALIDA:  Suma de los dígitos del número ingresado y pruebas con lista de ejemplos
# ==========================================

def suma_digitos(n):
    n = abs(n)
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma


num = int(input('Escribe un número: '))
print(f'Suma: {suma_digitos(num)}')

for x in [123, 4783, 999]:
    print(f'{x} -> {suma_digitos(x)}')


# ==========================================
# Ejercicio de práctica (modificado): Función contar_pares_impares_digitos(n) que retorne un diccionario con el conteo de dígitos pares e impares de un número entero.
# ==========================================
# ENTRADA: valor_analizar (int)
# PROCESO: Extraer cada dígito con % 10 y // 10, evaluar si digito % 2 == 0 e incrementar el conteo en un diccionario {"pares": x, "impares": y}
# SALIDA:  Diccionario con la distribución de dígitos pares e impares
# ==========================================

def contar_pares_impares_digitos(n):
    n = abs(n)
    conteo = {"pares": 0, "impares": 0}
    if n == 0:
        conteo["pares"] = 1
        return conteo
    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            conteo["pares"] += 1
        else:
            conteo["impares"] += 1
        n = n // 10
    return conteo


valor_analizar = int(input("Ingrese un número para clasificar sus dígitos: "))
res_conteo = contar_pares_impares_digitos(valor_analizar)
print(f"Distribución de dígitos en {valor_analizar}: {res_conteo}")


# ==========================================
# Ejercicio 17: Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
# ==========================================
# ENTRADA: opcion (string), nombre (string)
# PROCESO: Bucle while para controlar el menú modularizado invocando funciones independientes según la opción elegida
# SALIDA:  Saludo personalizado, despedida, mensaje de salida o alerta de opción inválida
# ==========================================

def saludar():
    nombre = input("Nombre: ")
    print(f"Hola, {nombre}")


def despedir():
    nombre = input("Nombre: ")
    print(f"Chao, {nombre}")


def mostrar_menu():
    print("--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")


# Programa principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        print("Adiós")
        break
    else:
        print("Opción inválida")


# ==========================================
# Ejercicio de práctica (modificado): Menú interactivo modularizado para convertir unidades de longitud (metros a kilómetros, metros a centímetros y viceversa) con funciones dedicadas.
# ==========================================
# ENTRADA: seleccion (string), valor_metros (float)
# PROCESO: Invocar funciones especializadas (m_a_km, m_a_cm, km_a_m) según la opción del menú interactivo en un bucle while
# SALIDA:  Resultado de la conversión métrica seleccionada
# ==========================================

def m_a_km(m):
    return m / 1000


def m_a_cm(m):
    return m * 100


def km_a_m(km):
    return km * 1000


def menu_conversor():
    print("\n--- CONVERSOR DE UNIDADES ---")
    print("1. Metros a Kilómetros")
    print("2. Metros a Centímetros")
    print("3. Kilómetros a Metros")
    print("4. Salir")


while True:
    menu_conversor()
    seleccion = input("Seleccione una opción: ")
    if seleccion == "1":
        val = float(input("Ingrese metros: "))
        print(f"{val} m = {m_a_km(val):.4f} km")
    elif seleccion == "2":
        val = float(input("Ingrese metros: "))
        print(f"{val} m = {m_a_cm(val):.2f} cm")
    elif seleccion == "3":
        val = float(input("Ingrese kilómetros: "))
        print(f"{val} km = {km_a_m(val):.2f} m")
    elif seleccion == "4":
        print("Saliendo del conversor...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

# ==============================================================================
# EN ESTE APARTADO NO HABIAN EJERCICIOS DE "EJEMPLO" PARA PRACTICAR, SOLO HABIAN EJEMPLOS (EJERCICIOS YA RESUELTOS)
# ==============================================================================

# CADENAS
# Creación
saludo = "Hola mundo"
mensaje = 'con comillas simples también'
multi = """tres comillas
para varias líneas"""

# Acceso e índice negativo
print(saludo[0])  # 'H'
print(saludo[-1])  # 'o' (último)

# Slicing (rebanadas)
print(saludo[0:4])  # 'Hola'
print(saludo[5:])  # 'mundo'

# Longitud y recorrido
print(len(saludo))  # 10
for ch in saludo:
    print(ch)

# Inmutabilidad
# saludo[0] = "h"  ← ERROR: TypeError
saludo = "h" + saludo[1:]  # ← se crea una NUEVA cadena

########################################################################################
# LISTA
# Creación
vacia = []
notas = [7, 8.5, 9, 6.5]
mezcla = [1, "dos", True, [3, 4]]  # admite cualquier tipo

# Acceso, longitud, verificación
print(notas[0])  # 7
print(notas[-1])  # 6.5 (último)
print(len(notas))  # 4
print(9 in notas)  # True

# Modificación
notas[0] = 10  # cambiar por índice
notas.append(8)  # añadir al final → O(1)
notas.insert(0, 5)  # insertar al inicio → O(n)
notas.remove(6.5)  # quita la primera ocurrencia de 6.5
ultima = notas.pop()  # saca y retorna el último

# Recorrido
for n in notas:
    print(n)

for i, n in enumerate(notas):
    print(f"posición {i} → {n}")

# Ordenamiento
notas.sort()  # in-place, ascendente
notas.sort(reverse=True)  # in-place, descendente
nueva = sorted(notas)  # retorna copia ordenada

# Slicing y copia
primeras = notas[:2]  # primeros 2
copia = notas[:]  # copia completa (no alias)

# Comprensión de listas
cuadrados = [n * n for n in range(6)]  # [0,1,4,9,16,25]
pares = [n for n in notas if n % 2 == 0]

########################################################################################
# TUPLAS
# Creación (los paréntesis son opcionales)
punto = (3, 4)
color = 255, 128, 0  # también es tupla
uno = (5,)  # cuidado: (5) es int, (5,) es tupla

# Acceso — igual que list
print(punto[0], punto[1])  # 3 4

# Inmutabilidad
# punto[0] = 10  ← ERROR: TypeError

# Desempaquetado — súper pythónico
x, y = punto
r, g, b = color


# Retornar varios valores es una tupla implícita
def min_max(lst):
    return min(lst), max(lst)


lo, hi = min_max([3, 1, 4, 1, 5])

# Métodos limitados: count() e index()
c = (1, 2, 3, 2, 1)
print(c.count(2))  # 2
print(c.index(3))  # 2

########################################################################################
# SETS

# Creación
vacio = set()  # ← {} es dict, no set!
letras = {"a", "b", "c"}
unicos = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Operaciones básicas
letras.add("d")  # añade uno
letras.discard("z")  # quita si existe (no falla si no)
letras.remove("a")  # quita, KeyError si no existe
print("b" in letras)  # True — búsqueda O(1)
print(len(letras))  # cuántos elementos

# Recorrido (sin orden garantizado)
for x in letras:
    print(x)

# Operaciones de conjunto (como en matemáticas)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # unión         → {1,2,3,4,5,6}
print(a & b)  # intersección  → {3,4}
print(a - b)  # diferencia    → {1,2}
print(a ^ b)  # diferencia sim → {1,2,5,6}

# Caso típico: eliminar duplicados de una lista
palabras = ["sí", "no", "sí", "tal vez", "no"]
sin_repetir = list(set(palabras))  # orden no garantizado

########################################################################################
# DICCIONARIO

# Creación
vacio = {}
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Guayaquil"}
alt = dict(nombre="Ana", edad=30)  # forma alterna

# Lectura
print(persona["nombre"])  # "Ana" — KeyError si no existe
print(persona.get("tel"))  # None — nunca falla
print(persona.get("tel", "—"))  # "—" — valor por defecto

# Modificación
persona["edad"] = 31  # cambia el valor
persona["email"] = "a@x.com"  # añade nueva clave
del persona["ciudad"]  # elimina
persona.pop("edad", None)  # elimina si existe, retorna valor

# Verificación de clave
if "nombre" in persona:
    print("tiene nombre")

# Recorrido
for clave in persona:  # solo claves
    print(clave, persona[clave])
for clave, valor in persona.items():  # claves y valores juntos
    print(f"{clave} = {valor}")
for valor in persona.values():  # solo valores
    print(valor)

# Caso típico: contar frecuencias
texto = "la casa de la abuela"
conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)  # {'la': 2, 'casa': 1, 'de': 1, 'abuela': 1}

# ==============================================================================
# EJERCICIOS PROPUESTOS
# ==============================================================================

# ==========================================
# Ejercicio 1: Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C x 9/5 + 32
# ==========================================
# ENTRADA: Temperatura (float)
# PROCESO: F = (Temperatura * 9 / 5) + 32
# SALIDA:  Temperatura convertida a grados Fahrenheit
# ==========================================

Temperatura = float(input('Ingrese la temperatura en grados celsius para convertirla a grados Fahrenheit:'))

F = (Temperatura * 9 / 5 + 32)

print(f'La temperatura en grados Fahrenheit es: {F}')

# ==========================================
# Ejercicio de práctica (modificado): Pide una temperatura en Fahrenheit y conviértela a Celsius y Kelvin, guardando los resultados en un diccionario.
# ==========================================
# ENTRADA: temp_f (float)
# PROCESO: celsius = (temp_f - 32) * 5 / 9 | kelvin = celsius + 273.15, almacenar en diccionario
# SALIDA:  Temperaturas convertidas a Celsius y Kelvin con 2 decimales
# ==========================================

temp_f = float(input('Ingrese la temperatura en grados Fahrenheit: '))

celsius = (temp_f - 32) * 5 / 9
kelvin = celsius + 273.15

escalas = {
    "Celsius": round(celsius, 2),
    "Kelvin": round(kelvin, 2)
}

print(f"Conversiones: {escalas['Celsius']} °C | {escalas['Kelvin']} K")

# ==========================================
# Ejercicio 2: Pide un total de segundos y muéstralos como HH:MM:SS- Ej: 3275 segundos -> 01:02:05.
# ==========================================
# ENTRADA: seconds (int)
# PROCESO: horas = seconds // 3600 | resto = seconds % 3600 | minutos = resto // 60 | segundos = resto % 60
# SALIDA:  Tiempo formateado en HH:MM:SS
# ==========================================

seconds = int(input("Ingrese el tiempo en segundos: "))
horas = seconds // 3600
resto = seconds % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

# ==========================================
# Ejercicio de práctica (modificado): Leer días, horas y minutos por separado y calcular el total consolidado en segundos.
# ==========================================
# ENTRADA: d (int), h (int), m (int)
# PROCESO: total_segundos = (d * 86400) + (h * 3600) + (m * 60)
# SALIDA:  Equivalente total en segundos
# ==========================================

d = int(input("Días: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))

total_segundos = (d * 86400) + (h * 3600) + (m * 60)
print(f"Total en segundos: {total_segundos} s")

# ==========================================
# Ejercicio 3: Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
# ==========================================
# ENTRADA: a (int), b (int)
# PROCESO: Intercambiar valores mediante asignación múltiple: a, b = b, a
# SALIDA:  Valores invertidos de las variables a y b
# ==========================================

a = int(input("a: "))
b = int(input("b: "))

a, b = b, a

print(f"a = {a}, b = {b}")

# ==========================================
# Ejercicio de práctica (modificado): Lee tres variables (x, y, z) y realiza una rotación circular de valores (x pasa a y, y a z, z a x) usando asignación múltiple.
# ==========================================
# ENTRADA: x (int), y (int), z (int)
# PROCESO: Intercambio múltiple simultáneo x, y, z = z, x, y
# SALIDA:  Valores rotados de las tres variables
# ==========================================

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(f"Valores iniciales: x={x}, y={y}, z={z}")

x, y, z = z, x, y

print(f"Valores tras rotación circular: x={x}, y={y}, z={z}")

# ==========================================
# Ejercicio 4: Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
# ==========================================
# ENTRADA: precio (float)
# PROCESO: iva = precio * 0.15 | total = precio + iva
# SALIDA:  Monto del IVA y precio final formateados con 2 decimales
# ==========================================

IVA = 0.15

precio = float(input("Precio sin IVA: $"))
iva = precio * IVA
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")

# ==========================================
# Ejercicio de práctica (modificado): Lee el precio de un producto, aplica un porcentaje de descuento ingresado por el usuario y luego calcula el IVA (15%) sobre el subtotal con descuento.
# ==========================================
# ENTRADA: precio_art (float), pct_desc (float)
# PROCESO: subtotal_desc = precio_art * (1 - pct_desc/100), iva_final = subtotal_desc * 0.15, total_pagar = subtotal_desc + iva_final
# SALIDA:  Subtotal con descuento, IVA y total final a pagar
# ==========================================

precio_art = float(input("Precio regular: $"))
pct_desc = float(input("Porcentaje de descuento (%): "))

subtotal_desc = precio_art * (1 - (pct_desc / 100))
iva_final = subtotal_desc * 0.15
total_pagar = subtotal_desc + iva_final

print(f"Subtotal con descuento: ${subtotal_desc:.2f}")
print(f"IVA (15%):               ${iva_final:.2f}")
print(f"Total neto a pagar:      ${total_pagar:.2f}")

# ==========================================
# Ejercicio 5: Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo -> 4+3+5 = 12.
# ==========================================
# ENTRADA: numero (int)
# PROCESO: Extraer centenas (// 100), decenas ((// 10) % 10) y unidades (% 10) para sumarlos
# SALIDA:  Suma total de los dígitos
# ==========================================

numero = int(input("Ingrese un número de más de dos cifras para sumar: "))

centenas = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10

suma = centenas + decenas + unidades
print(f'La suma es: {suma}')

# ==========================================
# Ejercicio de práctica (modificado): Lee un número entero de cualquier cantidad de cifras y calcula la suma de sus dígitos usando un bucle while y el operador residuo.
# ==========================================
# ENTRADA: num_entero (int)
# PROCESO: Extraer el último dígito con % 10 y reducir con // 10 de forma iterativa acumulando en suma_total
# SALIDA:  Suma total de los dígitos del número
# ==========================================

num_entero = int(input("Ingrese un número entero cualquiera: "))
aux = abs(num_entero)
suma_total = 0

while aux > 0:
    suma_total += aux % 10
    aux = aux // 10

print(f"La suma de los dígitos de {num_entero} es: {suma_total}")

# ==========================================
# Ejercicio 6: Lee una cantidad de minutos y muéstrala como <<X horas Y minutos>>. Ejemplo: 135 -> <<2 horas 15 minutos>>
# ==========================================
# ENTRADA: total (int)
# PROCESO: horas = total // 60 | minutos = total % 60
# SALIDA:  Tiempo formateado en horas y minutos
# ==========================================

total = int(input('Minutos totales: '))

horas = total // 60
minutos = total % 60

print(f'{horas} horas y {minutos} minutos')

# ==========================================
# Ejercicio de práctica (modificado): Lee una cantidad de horas y minutos por separado y conviértela al total equivalente en minutos y en segundos guardándolo en un diccionario.
# ==========================================
# ENTRADA: h_ingresadas (int), m_ingresados (int)
# PROCESO: min_totales = (h * 60) + m | seg_totales = min_totales * 60, almacenar en diccionario
# SALIDA:  Diccionario con el tiempo expresado en minutos y segundos
# ==========================================

h_ingresadas = int(input("Horas: "))
m_ingresados = int(input("Minutos: "))

min_totales = (h_ingresadas * 60) + m_ingresados
seg_totales = min_totales * 60

conversion_tiempo = {
    "total_minutos": min_totales,
    "total_segundos": seg_totales
}

print(f"Equivalencia calculada: {conversion_tiempo}")

# ==========================================
# Ejercicio 7: Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula = peso / estatura**2. Muestra el IMC con 2 decimales
# ==========================================
# ENTRADA: peso (float), estatura (float)
# PROCESO: imc = peso / (estatura ** 2)
# SALIDA:  IMC calculado y formateado a 2 decimales
# ==========================================

peso = float(input('Ingrese su peso en kilogramos(kg): '))
estatura = float(input('Ingrese su estatura en metros (m): '))

imc = peso / (estatura ** 2)
print(f'IMC: {imc:.2f}')

# ==========================================
# Ejercicio de práctica (modificado): Calcula el IMC y clasifica el estado nutricional según la OMS (Bajo peso, Normal, Sobrepeso, Obesidad) usando condicionales if/elif/else.
# ==========================================
# ENTRADA: p (float), e (float)
# PROCESO: imc_calc = p / (e ** 2), evaluar rangos (< 18.5, < 25, < 30, >= 30)
# SALIDA:  Valor del IMC y categoría diagnóstica correspondiente
# ==========================================

p = float(input('Peso en kg: '))
e = float(input('Estatura en metros: '))

imc_calc = p / (e ** 2)

if imc_calc < 18.5:
    categoria = "Bajo peso"
elif imc_calc < 25.0:
    categoria = "Peso normal"
elif imc_calc < 30.0:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"IMC: {imc_calc:.2f} — Categoría: {categoria}")

# ==========================================
# Ejercicio 8: Lee un número decimal y una cantidad de decimales, y muéstralo redondeado. Ejemplo 3.14159 con 2 decimales -> 3.14.
# ==========================================
# ENTRADA: numero (float), decimales (int)
# PROCESO: resultado = round(numero, decimales)
# SALIDA:  Número redondeado a la cantidad de decimales indicada
# ==========================================

numero = float(input('Ingrese el número: '))
decimales = int(input('Ingrese los decimales: '))

resultado = round(numero, decimales)
print(resultado)

# ==========================================
# Ejercicio de práctica (modificado): Lee una lista de números flotantes y redondea todos sus elementos a 2 decimales utilizando una comprensión de listas.
# ==========================================
# ENTRADA: lista_flotantes (lista de floats)
# PROCESO: Generar una nueva lista aplicando round(x, 2) a cada elemento de la colección original
# SALIDA:  Lista con todos los valores redondeados homogéneamente
# ==========================================

lista_flotantes = [3.141592, 2.718281, 1.414213, 0.577215]
lista_redondeada = [round(val, 2) for val in lista_flotantes]

print(f"Valores originales:  {lista_flotantes}")
print(f"Valores redondeados: {lista_redondeada}")

# ==========================================
# Ejercicio 9: Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si compras entre 5 y 9 te dan 5%. Calcula el total
# ==========================================
# ENTRADA: cantidad (int)
# PROCESO: Determinar tasa de descuento según la cantidad (15%, 5% o 0%), subtotal = PRECIO * cantidad, total = subtotal * (1 - descuento)
# SALIDA:  Precio unitario, porcentaje de descuento aplicado y total a pagar
# ==========================================

PRECIO = 12
cantidad = int(input("Ingrese la cantidad de productos: "))

if cantidad >= 10:
    descuento = 0.15
elif cantidad >= 5:
    descuento = 0.05
else:
    descuento = 0

subtotal = PRECIO * cantidad
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento * 100)}%")
print(f"Total: ${total:.2f}")


# ==========================================
# Ejercicio de práctica (modificado): Función calcular_compra_dinamica(precio_unitario, cantidad) que calcule subtotal, descuento escalonado e IVA (15%) sobre el total con descuento.
# ==========================================
# ENTRADA: pu (float), cant (int)
# PROCESO: sub = pu * cant, aplicar tasa según cant, base_imponible = sub * (1 - desc), iva = base * 0.15, total = base + iva
# SALIDA:  Desglose financiero completo (subtotal, descuento, base neta, IVA y total a pagar)
# ==========================================

def calcular_compra_dinamica(precio_unitario, cant):
    if cant >= 20:
        tasa_desc = 0.20
    elif cant >= 10:
        tasa_desc = 0.10
    else:
        tasa_desc = 0.0

    sub = precio_unitario * cant
    monto_desc = sub * tasa_desc
    base = sub - monto_desc
    iva_calc = base * 0.15
    total_final = base + iva_calc

    return {
        "subtotal": sub,
        "descuento": monto_desc,
        "base_imponible": base,
        "iva": iva_calc,
        "total": total_final
    }


pu = float(input("Precio unitario del artículo: $"))
cant = int(input("Cantidad a adquirir: "))

factura = calcular_compra_dinamica(pu, cant)

print(f"Subtotal:       ${factura['subtotal']:.2f}")
print(f"Descuento:     -${factura['descuento']:.2f}")
print(f"Base neta:      ${factura['base_imponible']:.2f}")
print(f"IVA (15%):      ${factura['iva']:.2f}")
print(f"Total a pagar:  ${factura['total']:.2f}")

# ==========================================
# Ejercicio 10: Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
# ==========================================
# ENTRADA: n (int)
# PROCESO: Iterar con for de 1 a 12 multiplicando n * i
# SALIDA:  Tabla de multiplicar del 1 al 12
# ==========================================

n = int(input('Ingrese el número dle cual quiere visualizar su tabla: '))

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
# Ejercicio 11: Lee un número y cuenta cuántos dígitos tiene (sin convertir a string)
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
# Ejercicio 12: Lee N números y muestra la suma de los pares y la suma de los impares por separado
# ==========================================
# ENTRADA: n (int), x números enteros (int)
# PROCESO: Evaluar si x % 2 == 0 para acumular en suma_pares, caso contrario en suma_impares
# SALIDA:  Total de suma de pares y total de suma de impares
# ==========================================

n = int(input('Cuántos npumeros ingresará?: '))
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
# Ejercicio 13: Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
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
# Ejercicio 14: Genera un número secreto entre 1 y 100. El usuario intenta adivinar. En cada intento le dices si es <<mayor>> o <<menor>>. Cuenta cuántos intentos usó
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
# Ejercicio 15: Muestra los primeros N números de Fibonacci. La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... Cada número es la suma de los dos anteriores.
# ==========================================
# ENTRADA: n (int)
# PROCESO: Generar los primeros n términos actualizando a, b = b, a + b
# SALIDA:  Serie de Fibonacci impresa en una sola línea
# ==========================================

n = int(input('¿Cuántos?'))

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


# ==========================================
# Ejercicio 16: Función area_rectángulo(base, altura) que retorne el área
# ==========================================
# ENTRADA: base (float/int), altura (float/int)
# PROCESO: Multiplicar base * altura dentro de la función area_rectangulo()
# SALIDA:  Área calculada del rectángulo
# ==========================================

def area_rectangulo(base, altura):
    return base * altura


print(area_rectangulo(5, 3))
print(area_rectangulo(1.5, 2))


# ==========================================
# Ejercicio de práctica (modificado): Función area_triangulo(base, altura) y perimetro_triangulo_rectangulo(base, altura) calculando la hipotenusa mediante el teorema de Pitágoras.
# ==========================================
# ENTRADA: b (float), h (float)
# PROCESO: area = (b * h) / 2 | hipotenusa = (b**2 + h**2)**0.5 | perimetro = b + h + hipotenusa
# SALIDA:  Área y perímetro calculados del triángulo rectángulo
# ==========================================

def area_triangulo(b, h):
    return (b * h) / 2


def perimetro_triangulo_rectangulo(b, h):
    hipotenusa = (b ** 2 + h ** 2) ** 0.5
    return b + h + hipotenusa


b_in = float(input("Base del triángulo: "))
h_in = float(input("Altura del triángulo: "))

print(f"Área: {area_triangulo(b_in, h_in):.2f}")
print(f"Perímetro: {perimetro_triangulo_rectangulo(b_in, h_in):.2f}")


# ==========================================
# Ejercicio 17: Función máximo(a, b, c) que retorne el mayor de tres números.
# ==========================================
# ENTRADA: a, b, c (números reales o enteros)
# PROCESO: Determinar el valor máximo usando la función nativa max() y por comparación condicional manual
# SALIDA:  El mayor de los tres números evaluados
# ==========================================

def maximo(a, b, c):
    return max(a, b, c)


def maximo_manual(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


print(maximo(5, 9, 3))
print(maximo_manual(5, 9, 3))


# ==========================================
# Ejercicio de práctica (modificado): Función minimo_de_lista(numeros) que encuentre y retorne el valor mínimo de una lista de longitud variable mediante un ciclo for manual.
# ==========================================
# ENTRADA: lista_nums (lista de enteros/flotantes)
# PROCESO: Recorrer la lista comparando cada elemento contra una variable acumuladora del menor valor
# SALIDA:  Elemento menor encontrado en la lista
# ==========================================

def minimo_manual(lista):
    if not lista:
        return None
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return menor


muestra_valores = [14, 52, 9, 33, 7, 81, 12]
print(f"Lista de prueba: {muestra_valores}")
print(f"Valor mínimo obtenido manualmente: {minimo_manual(muestra_valores)}")


# ==========================================
# Ejercicio 18: Un año es bisiesto si es divisible entre 4 y no entre 100, o si es divisible entre 400
# ==========================================
# ENTRADA: anio (int)
# PROCESO: Evaluar condiciones de residuos: divisible para 400 (True), divisible para 100 (False), divisible para 4 (True)
# SALIDA:  Valor booleano (True/False) indicando si el año es bisiesto
# ==========================================

def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    if anio % 4 == 0:
        return True
    return False


for y in [2024, 2023, 2000, 1900]:
    print(f"{y}: {es_bisiesto(y)}")


# ==========================================
# Ejercicio de práctica (modificado): Función dias_del_mes(mes, anio) que retorne 28, 29, 30 o 31 días según el mes ingresado, integrando la función es_bisiesto() para febrero.
# ==========================================
# ENTRADA: mes (int), anio (int)
# PROCESO: Validar mes en diccionarios/listas de días fijos y consultar es_bisiesto(anio) si el mes es 2
# SALIDA:  Cantidad exacta de días que tiene el mes en ese año
# ==========================================

def dias_del_mes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    return None


m_input = int(input("Mes (1-12): "))
a_input = int(input("Año: "))
print(f"El mes {m_input} del año {a_input} tiene {dias_del_mes(m_input, a_input)} días.")


# ==========================================
# Ejercicio 19: Función factorial(n) y luego combinatoria(n, k) = n! / (k! * (n-k)!)
# ==========================================
# ENTRADA: n (int), k (int)
# PROCESO: Calcular n! mediante acumulador multiplicativo y aplicar la fórmula de combinaciones factoriales
# SALIDA:  Factorial de n y número de combinaciones posibles C(n, k)
# ==========================================

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def combinatoria(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


print(factorial(5))
print(combinatoria(5, 2))


# ==========================================
# Ejercicio de práctica (modificado): Función permutaciones(n, k) = n! / (n - k)! utilizando la función factorial() ya implementada.
# ==========================================
# ENTRADA: n (int), k (int)
# PROCESO: Evaluar formula P(n, k) = factorial(n) // factorial(n - k) validando que n >= k >= 0
# SALIDA:  Total de permutaciones posibles
# ==========================================

def permutaciones(n, k):
    if n < k or k < 0:
        return 0
    return factorial(n) // factorial(n - k)


n_val = int(input("Total de elementos (n): "))
k_val = int(input("Elementos por grupo (k): "))
print(f"P({n_val}, {k_val}) = {permutaciones(n_val, k_val)}")


# ==========================================
# Ejercicio 20: Programa con funciones separadas para cada operación (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.
# ==========================================
# ENTRADA: op (string), a (float), b (float)
# PROCESO: Bucle de menú interactivo que invoca funciones aritméticas modulares y valida división por cero retornando None
# SALIDA:  Resultado de la operación elegida o mensajes de validación
# ==========================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None  # None = "no válido"
    return a / b


while True:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")
    if op == "5":
        break
    a = float(input("a: "))
    b = float(input("b: "))
    if op == "1":
        r = sumar(a, b)
    elif op == "2":
        r = restar(a, b)
    elif op == "3":
        r = multiplicar(a, b)
    elif op == "4":
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
            continue
    else:
        print("Opción inválida")
        continue
    print(f"Resultado: {r}")


# ==========================================
# Ejercicio de práctica (modificado): Calculadora científica básica modularizada que incluya potencia(base, exponente) y modulo(dividendo, divisor), integrada en menú.
# ==========================================
# ENTRADA: opcion_calc (string), base (float), exp (float)
# PROCESO: Funciones dedicadas potencia(a, b) con operador ** y modulo_op(a, b) con % integradas en un bucle interactivo
# SALIDA:  Resultado numérico calculado o validación de error en divisor cero
# ==========================================

def potencia(base, exponente):
    return base ** exponente


def modulo_op(a, b):
    if b == 0:
        return None
    return a % b


while True:
    print("\n--- CALCULADORA AVANZADA ---")
    print("1. Potencia (a^b)")
    print("2. Módulo / Residuo (a % b)")
    print("3. Salir")
    opcion_calc = input("Elija opción: ")

    if opcion_calc == "3":
        print("Cerrando calculadora avanzada.")
        break
    if opcion_calc in ["1", "2"]:
        val_a = float(input("Valor a: "))
        val_b = float(input("Valor b: "))
        if opcion_calc == "1":
            print(f"Resultado: {potencia(val_a, val_b)}")
        elif opcion_calc == "2":
            res_mod = modulo_op(val_a, val_b)
            if res_mod is None:
                print("Error: No se puede calcular módulo con divisor cero.")
            else:
                print(f"Residuo: {res_mod}")
    else:
        print("Opción no válida.")

# ==========================================
# Ejercicio 21: Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
# ==========================================
# ENTRADA: frase (string)
# PROCESO: Convertir a minúsculas (.lower()) e iterar carácter por carácter verificando pertenencia al conjunto de vocales
# SALIDA:  Total de vocales encontradas en la frase
# ==========================================

frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0

for ch in frase:
    if ch in vocales:
        total += 1

print(f"{total} vocales")

# ==========================================
# Ejercicio de práctica (modificado): Pide una cadena de texto y cuenta la frecuencia individual de cada vocal (a, e, i, o, u) retornando los resultados en un diccionario.
# ==========================================
# ENTRADA: texto_usr (string)
# PROCESO: Recorrer la cadena en minúsculas y acumular el conteo específico de cada vocal en un diccionario {'a': x, 'e': y, ...}
# SALIDA:  Diccionario con el total por cada una de las 5 vocales
# ==========================================

texto_usr = input("Ingrese un texto para analizar sus vocales: ").lower()
conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in texto_usr:
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

print(f"Frecuencia por vocal: {conteo_vocales}")

# ==========================================
# Ejercicio 22: Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima. Imprime los tres valores con 2 decimales.
# ==========================================
# ENTRADA: notas (lista de floats/ints)
# PROCESO: Calcular promedio (sum / len), máximo (max) y mínimo (min) de la colección
# SALIDA:  Promedio, nota máxima y nota mínima formateados a 2 decimales
# ==========================================

notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")

# ==========================================
# Ejercicio de práctica (modificado): Dada una lista de calificaciones, calcular la desviación estándar muestral respecto a su promedio.
# ==========================================
# ENTRADA: notas_estudio (lista de floats)
# PROCESO: media = sum / len, acumular suma_diferencias_cuadradas = sum((x - media)**2), varianza = suma / (len - 1), desviacion = varianza ** 0.5
# SALIDA:  Promedio y desviación estándar con 2 decimales
# ==========================================

notas_estudio = [7.0, 8.5, 6.0, 9.0, 10.0, 5.5]
media_notas = sum(notas_estudio) / len(notas_estudio)

suma_cuadrados = sum((nota - media_notas) ** 2 for nota in notas_estudio)
varianza = suma_cuadrados / (len(notas_estudio) - 1)
desviacion = varianza ** 0.5

print(f"Calificaciones: {notas_estudio}")
print(f"Media: {media_notas:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")

# ==========================================
# Ejercicio 23: Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados respetando el orden de la primera aparición.
# ==========================================
# ENTRADA: datos (lista de strings)
# PROCESO: Recorrer la lista original agregando elementos nuevos a una lista resultado y registrándolos en un set auxiliar
# SALIDA:  Nueva lista con elementos únicos preservando el orden original
# ==========================================

datos = ["a", "b", "a", "c", "b", "d"]
vistos = set()
resultado = []

for x in datos:
    if x not in vistos:
        vistos.add(x)
        resultado.append(x)

print(resultado)  # ['a', 'b', 'c', 'd']


# ==========================================
# Ejercicio de práctica (modificado): Función encontrar_duplicados(lista) que retorne un conjunto (set) únicamente con los elementos que aparecen 2 o más veces.
# ==========================================
# ENTRADA: secuencia (lista de elementos variados)
# PROCESO: Registrar elementos en un set de vistos y, al encontrar una coincidencia repetida, agregarla al set de duplicados
# SALIDA:  Conjunto con los elementos repetidos
# ==========================================

def encontrar_duplicados(lista):
    visitados = set()
    repetidos = set()
    for item in lista:
        if item in visitados:
            repetidos.add(item)
        else:
            visitados.add(item)
    return repetidos


muestra_datos = ["x", "y", "z", "x", "w", "y", "x"]
print(f"Lista original: {muestra_datos}")
print(f"Elementos duplicados: {encontrar_duplicados(muestra_datos)}")

# ==========================================
# Ejercicio 24: Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas). Al final, imprime la palabra que más se repite.
# ==========================================
# ENTRADA: texto (string)
# PROCESO: Normalizar a minúsculas, separar por palabras (.split()), acumular conteos en un diccionario y hallar la clave con valor máximo
# SALIDA:  Diccionario de frecuencias y la palabra con mayor número de apariciones
# ==========================================

texto = "El perro y el gato y el perro"
conteo = {}

for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")

# ==========================================
# Ejercicio de práctica (modificado): Dado un párrafo, generar un diccionario con la longitud de cada palabra única (filtrando signos de puntuación) y hallar la palabra más larga.
# ==========================================
# ENTRADA: parrafo (string)
# PROCESO: Eliminar puntuación básica (.replace), separar palabras (.split()), armar diccionario {palabra: len(palabra)} con palabras únicas y obtener el máximo por longitud
# SALIDA:  Diccionario de longitudes y la palabra de mayor extensión
# ==========================================

parrafo = "Python es un lenguaje de programacion sumamente versatil y potente"
limpio = parrafo.lower().replace(",", "").replace(".", "")

longitudes = {pal: len(pal) for pal in set(limpio.split())}
palabra_mas_larga = max(longitudes, key=longitudes.get)

print(f"Longitudes de palabras únicas: {longitudes}")
print(f"Palabra más larga: '{palabra_mas_larga}' con {longitudes[palabra_mas_larga]} caracteres")

# ==========================================
# Ejercicio 25: Verificar si una palabra o frase es un palíndromo (se lee igual al derecho y al revés)
# ==========================================
# ENTRADA: texto (string)
# PROCESO: Limpiar espacios, convertir a minúsculas y comparar la cadena con su versión invertida ([::-1])
# SALIDA:  Mensaje indicando si el texto es palíndromo o no
# ==========================================

cadena = input("Ingrese una palabra o frase: ").lower().replace(" ", "")

if cadena == cadena[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


# ==========================================
# Ejercicio de práctica (modificado): Función es_anagrama(palabra1, palabra2) que determine si dos cadenas son anagramas comparando sus frecuencias en diccionarios.
# ==========================================
# ENTRADA: cad1 (string), cad2 (string)
# PROCESO: Normalizar caracteres y comparar los diccionarios de frecuencias de letras de ambas cadenas
# SALIDA:  Valor booleano y mensaje indicando si las palabras forman un anagrama
# ==========================================

def es_anagrama(p1, p2):
    c1 = p1.lower().replace(" ", "")
    c2 = p2.lower().replace(" ", "")
    if len(c1) != len(c2):
        return False
    dict1 = {}
    dict2 = {}
    for ch in c1:
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in c2:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2


p1_in = input("Primera palabra: ")
p2_in = input("Segunda palabra: ")
print(f"¿Son anagramas?: {es_anagrama(p1_in, p2_in)}")

# ==========================================
# Ejercicio 26: Invertir los elementos de una lista sin utilizar métodos predefinidos como .reverse() o [::-1]
# ==========================================
# ENTRADA: lista_original (lista de enteros)
# PROCESO: Usar un bucle for en decremento para construir manualmente una nueva lista invertida
# SALIDA:  Lista con el orden de elementos totalmente invertido
# ==========================================

numeros = [10, 20, 30, 40, 50]
invertida = []

for i in range(len(numeros) - 1, -1, -1):
    invertida.append(numeros[i])

print(f"Original:  {numeros}")
print(f"Invertida: {invertida}")

# ==========================================
# Ejercicio de práctica (modificado): Invertir una lista in-place (modificando la original) mediante dos punteros (inicio y fin) dentro de un ciclo while.
# ==========================================
# ENTRADA: elementos (lista de enteros)
# PROCESO: Intercambiar elementos extremos elementos[izq], elementos[der] = elementos[der], elementos[izq] incrementando izq y decrementando der
# SALIDA:  Lista invertida directamente en su misma posición de memoria
# ==========================================

arr = [1, 2, 3, 4, 5, 6, 7]
print(f"Lista inicial: {arr}")

izq = 0
der = len(arr) - 1

while izq < der:
    arr[izq], arr[der] = arr[der], arr[izq]
    izq += 1
    der -= 1

print(f"Lista invertida in-place: {arr}")


# ==========================================
# Ejercicio 27: Función que recibe una lista de números y retorna una tupla con (pares, impares) separados en sublistas
# ==========================================
# ENTRADA: lista_datos (lista de enteros)
# PROCESO: Iterar y clasificar elementos mediante x % 2 == 0 en dos listas independientes y retornarlas como tupla
# SALIDA:  Tupla que contiene la lista de pares y la lista de impares
# ==========================================

def clasificar_numeros(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


muestra = [12, 7, 5, 18, 22, 9, 3, 14]
res_pares, res_impares = clasificar_numeros(muestra)

print(f"Lista completa: {muestra}")
print(f"Pares:   {res_pares}")
print(f"Impares: {res_impares}")


# ==========================================
# Ejercicio de práctica (modificado): Función clasificar_por_signo(lista) que retorne un diccionario con tres sublistas: {"positivos": [...], "negativos": [...], "ceros": [...]}.
# ==========================================
# ENTRADA: numeros_muestra (lista de enteros)
# PROCESO: Recorrer la colección clasificando según > 0, < 0 o == 0 en listas internas del diccionario
# SALIDA:  Estructura de diccionario con números segmentados por signo
# ==========================================

def clasificar_por_signo(lista):
    resultado_signos = {"positivos": [], "negativos": [], "ceros": []}
    for val in lista:
        if val > 0:
            resultado_signos["positivos"].append(val)
        elif val < 0:
            resultado_signos["negativos"].append(val)
        else:
            resultado_signos["ceros"].append(val)
    return resultado_signos


datos_prueba = [-5, 12, 0, -3, 8, 0, -1, 15]
print(f"Datos evaluados: {datos_prueba}")
print(f"Clasificación resultante: {clasificar_por_signo(datos_prueba)}")

# ==========================================
# Ejercicio 28: Generar una matriz identidad de tamaño N x N representada mediante listas anidadas
# ==========================================
# ENTRADA: dimension (int)
# PROCESO: Construir filas con bucles anidados asignando 1 si fila == columna y 0 en caso contrario
# SALIDA:  Matriz identidad impresa fila por fila en consola
# ==========================================

dimension = int(input("Tamaño de la matriz identidad (N): "))
matriz = []

for i in range(dimension):
    fila = []
    for j in range(dimension):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

print(f"--- Matriz Identidad {dimension}x{dimension} ---")
for fila in matriz:
    print(fila)

# ==========================================
# Ejercicio de práctica (modificado): Generar una matriz de tamaño N x M con números correlativos y calcular la suma de los elementos de su diagonal principal.
# ==========================================
# ENTRADA: n_filas (int), n_cols (int)
# PROCESO: Llenar matriz con contador secuencial, acumular suma_diag sumando matriz[k][k] donde k < min(filas, columnas)
# SALIDA:  Matriz generada y valor total de la diagonal principal
# ==========================================

n_filas = int(input("Filas de la matriz: "))
n_cols = int(input("Columnas de la matriz: "))

matriz_correlativa = []
contador_matriz = 1

for r in range(n_filas):
    fila_actual = []
    for c in range(n_cols):
        fila_actual.append(contador_matriz)
        contador_matriz += 1
    matriz_correlativa.append(fila_actual)

print("--- Matriz Generada ---")
for f in matriz_correlativa:
    print(f)

suma_diagonal = 0
limite_diag = min(n_filas, n_cols)
for k in range(limite_diag):
    suma_diagonal += matriz_correlativa[k][k]

print(f"Suma de la diagonal principal: {suma_diagonal}")