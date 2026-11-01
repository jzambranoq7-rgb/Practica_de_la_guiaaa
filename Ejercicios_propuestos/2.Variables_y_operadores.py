# ==========================================
# EJERCICIOS PROPUESTOS
# ==========================================

# ==========================================
# Ejercicio 1: Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo -> 435 -> 4+3+5 = 12.
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
# Ejercicio 2: Lee una cantidad de minutos y muéstrala como <<X horas Y minutos>>. Ejemplo: 135 -> <<2 horas 15 minutos>>
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
# Ejercicio 3: Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula = peso / estatura**2. Muestra el IMC con 2 decimales
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
# Ejercicio 4: Lee un número decimal y una cantidad de decimales, y muéstralo redondeado. Ejemplo 3.14159 con 2 decimales -> 3.14.
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
# Ejercicio 5: Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si compras entre 5 y 9 te dan 5%. Calcula el total
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