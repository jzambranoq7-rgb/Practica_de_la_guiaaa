# Taller: 6 ejercicios paso a paso

# ==========================================
# Ejercicio 1: Lee un número N y mostrar los números del 1 al N
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
# Ejercicio 2: Leer N y calcular la suma de 1 + 2 + 3 + ... + N
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
# Ejercicio 3: Factorial de N: Leer N y calcular el factorial (N! = 1 x 2 x 3 ... x N). Ejemplo: 5! = 120
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
# Ejercicio 4: Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (Nota >= 70)
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
# Ejercicio 5: Leer las notas de N estudiantes y mostrar la más alta
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
# Ejercicio 6: Leer un número y determinar si es primo (solo divisible entre 1 y él mismo)
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