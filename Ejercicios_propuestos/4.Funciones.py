# ==========================================
# EJERCICIOS PROPUESTOS
# ==========================================

# ==========================================
# Ejercicio 1: Función area_rectángulo(base, altura) que retorne el área
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
# Ejercicio 2: Función máximo(a, b, c) que retorne el mayor de tres números.
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
# Ejercicio 3: Un año es bisiesto si es divisible entre 4 y no entre 100, o si es divisible entre 400
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
# Ejercicio 4: Función factorial(n) y luego combinatoria(n, k) = n! / (k! * (n-k)!)
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
# Ejercicio 5: Programa con funciones separadas para cada operación (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.
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
        return None
    return a / b


while True:
    print("1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
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