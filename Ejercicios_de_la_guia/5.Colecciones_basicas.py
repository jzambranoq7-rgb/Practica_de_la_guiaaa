# EN ESTE APARTADO NO HABIAN EJERCICIOS DE "EJEMPLO" PARA PRACTICAR, SOLO HABIAN EJEMPLOS (EJERCICIOS YA RESUELTOS)

# CADENAS
# Creación
saludo = "Hola mundo"
mensaje = 'con comillas simples también'
multi = """tres comillas
para varias líneas"""

# Acceso e índice negativo
print(saludo[0])   # 'H'
print(saludo[-1])  # 'o' (último)

# Slicing (rebanadas)
print(saludo[0:4])  # 'Hola'
print(saludo[5:])   # 'mundo'

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
print(notas[0])       # 7
print(notas[-1])      # 6.5 (último)
print(len(notas))     # 4
print(9 in notas)     # True

# Modificación
notas[0] = 10          # cambiar por índice
notas.append(8)         # añadir al final → O(1)
notas.insert(0, 5)      # insertar al inicio → O(n)
notas.remove(6.5)        # quita la primera ocurrencia de 6.5
ultima = notas.pop()      # saca y retorna el último

# Recorrido
for n in notas:
    print(n)

for i, n in enumerate(notas):
    print(f"posición {i} → {n}")

# Ordenamiento
notas.sort()              # in-place, ascendente
notas.sort(reverse=True)  # in-place, descendente
nueva = sorted(notas)   # retorna copia ordenada

# Slicing y copia
primeras = notas[:2]     # primeros 2
copia = notas[:]          # copia completa (no alias)

# Comprensión de listas
cuadrados = [n*n for n in range(6)]  # [0,1,4,9,16,25]
pares = [n for n in notas if n % 2 == 0]

########################################################################################
# TUPLAS
# Creación (los paréntesis son opcionales)
punto = (3, 4)
color = 255, 128, 0       # también es tupla
uno = (5,)                # cuidado: (5) es int, (5,) es tupla

# Acceso — igual que list
print(punto[0], punto[1])   # 3 4

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
print(c.count(2))       # 2
print(c.index(3))       # 2

########################################################################################
# SETS

# Creación
vacio = set()          # ← {} es dict, no set!
letras = {"a", "b", "c"}
unicos = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Operaciones básicas
letras.add("d")         # añade uno
letras.discard("z")     # quita si existe (no falla si no)
letras.remove("a")      # quita, KeyError si no existe
print("b" in letras)  # True — búsqueda O(1)
print(len(letras))     # cuántos elementos

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
alt = dict(nombre="Ana", edad=30)   # forma alterna

# Lectura
print(persona["nombre"])     # "Ana" — KeyError si no existe
print(persona.get("tel"))    # None — nunca falla
print(persona.get("tel", "—"))  # "—" — valor por defecto

# Modificación
persona["edad"] = 31           # cambia el valor
persona["email"] = "a@x.com"    # añade nueva clave
del persona["ciudad"]         # elimina
persona.pop("edad", None)      # elimina si existe, retorna valor

# Verificación de clave
if "nombre" in persona:
    print("tiene nombre")

# Recorrido
for clave in persona:                # solo claves
    print(clave, persona[clave])
for clave, valor in persona.items():  # claves y valores juntos
    print(f"{clave} = {valor}")
for valor in persona.values():         # solo valores
    print(valor)

# Caso típico: contar frecuencias
texto = "la casa de la abuela"
conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)  # {'la': 2, 'casa': 1, 'de': 1, 'abuela': 1}


# ==============================================================================
# EJERCICIOS DE PRÁCTICA (COLECCIONES Y ESTRUCTURAS DE DATOS)
# ==============================================================================

# ==========================================
# Ejercicio de práctica (Cadenas): Invertir cada palabra de una oración manteniendo el orden de las palabras intacto.
# ==========================================
# ENTRADA: oracion (string)
# PROCESO: Dividir la frase con .split(), invertir cada palabra con [::-1] usando una comprensión de listas y unir con .join()
# SALIDA:  Oración con cada palabra invertida individualmente
# ==========================================

oracion = "Estructuras de datos en Python"
palabras_invertidas = " ".join([p[::-1] for p in oracion.split()])
print(f"Original:  {oracion}")
print(f"Modificada: {palabras_invertidas}")


# ==========================================
# Ejercicio de práctica (Listas): Filtrar una lista de números para obtener únicamente los números mayores al promedio general usando list comprehension.
# ==========================================
# ENTRADA: valores (lista de floats/ints)
# PROCESO: Calcular promedio = sum(valores) / len(valores) y filtrar con [x for x in valores if x > promedio]
# SALIDA:  Promedio calculado y lista de elementos que superan dicho promedio
# ==========================================

valores = [15, 8, 20, 12, 5, 30, 25]
prom_val = sum(valores) / len(valores)
mayores_al_promedio = [x for x in valores if x > prom_val]

print(f"Promedio general: {prom_val:.2f}")
print(f"Valores mayores al promedio: {mayores_al_promedio}")


# ==========================================
# Ejercicio de práctica (Tuplas): Función que recibe una lista de tuplas (producto, cantidad, precio_unitario) y calcula el valor total del inventario.
# ==========================================
# ENTRADA: inventario (lista de tuplas)
# PROCESO: Desempaquetar cada tupla en un bucle for acumulando total += cantidad * precio
# SALIDA:  Valor monetario total del inventario
# ==========================================

inventario = [
    ("Teclado", 10, 25.0),
    ("Mouse", 15, 12.5),
    ("Monitor", 5, 180.0)
]

total_inventario = 0
for prod, cant, precio_u in inventario:
    sub = cant * precio_u
    print(f"{prod}: {cant} unidades x ${precio_u:.2f} = ${sub:.2f}")
    total_inventario += sub

print(f"Total valorizado en bodega: ${total_inventario:.2f}")


# ==========================================
# Ejercicio de práctica (Sets): Encontrar elementos comunes y exclusivos entre los estudiantes inscritos en dos materias diferentes.
# ==========================================
# ENTRADA: curso_a (set de strings), curso_b (set de strings)
# PROCESO: Aplicar intersección (&) para alumnos en ambos cursos y diferencia simétrica (^) para alumnos en solo uno de ellos
# SALIDA:  Conjunto de estudiantes compartidos y exclusivos
# ==========================================

curso_a = {"Carlos", "Maria", "Juan", "Elena"}
curso_b = {"Elena", "Pedro", "Carlos", "Sofia"}

en_ambos = curso_a & curso_b
solo_en_uno = curso_a ^ curso_b

print(f"Estudiantes en ambos cursos: {en_ambos}")
print(f"Estudiantes en un solo curso: {solo_en_uno}")


# ==========================================
# Ejercicio de práctica (Diccionarios): Dado un diccionario con las notas de varios estudiantes, encontrar al estudiante con el promedio más alto.
# ==========================================
# ENTRADA: registro_estudiantes (diccionario con nombres como claves y listas de notas como valores)
# PROCESO: Calcular el promedio de cada lista con sum() / len() y determinar el valor máximo con max()
# SALIDA:  Nombre del mejor estudiante junto con su promedio
# ==========================================

registro_estudiantes = {
    "Mateo": [8.0, 9.0, 7.5],
    "Valeria": [9.5, 10.0, 9.0],
    "Andres": [7.0, 6.5, 8.0]
}

promedios = {nombre: sum(califs) / len(califs) for nombre, califs in registro_estudiantes.items()}
mejor_alumno = max(promedios, key=promedios.get)

print(f"Promedios registrados: {promedios}")
print(f"Mejor estudiante: {mejor_alumno} con promedio de {promedios[mejor_alumno]:.2f}")