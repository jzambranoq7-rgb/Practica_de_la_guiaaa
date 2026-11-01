# Taller 4 ejercicios paso a paso

# ==========================================
# Ejercicio 1: Escribir una función calcular_iva(precio) que reciba un precio y retorne el IVA (15%). Usarla desde el programa principal
# ==========================================
# ENTRADA: precio (float)
# PROCESO: Multiplicar precio * 0.15 dentro de la función calcular_iva()
# SALIDA:  El valor del IVA formateado con 2 decimales
# ==========================================

def calcular_iva(precio):
    return precio * 0.15

# Programa principal
precio = float(input('Ingrese el precio: $'))
iva = calcular_iva(precio)
print(f'El IVA de ${precio:.2f} es: ${iva:.2f}')

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
# Ejercicio 2: Escribir una función que reciba un número y retorne True si es primo, False si no.
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
# Ejercicio 3: Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
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
# Ejercicio 4: Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
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
    print("--- CONVERSOR DE UNIDADES ---")
    print("1. Metros a Kilómetros")
    print("2. Metros a Centímetros")
    print("3. Kilómetros a Metros")
    print("4. Salir")

while True:
    menu_conversor()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        val = float(input("Ingrese metros: "))
        print(f"{val} m = {m_a_km(val):.4f} km")
    elif opcion == "2":
        val = float(input("Ingrese metros: "))
        print(f"{val} m = {m_a_cm(val):.2f} cm")
    elif opcion == "3":
        val = float(input("Ingrese kilómetros: "))
        print(f"{val} km = {km_a_m(val):.2f} m")
    elif opcion == "4":
        print("Saliendo del conversor...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")