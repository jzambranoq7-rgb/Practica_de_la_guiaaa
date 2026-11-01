# Taller: primeros ejercicios paso a paso

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