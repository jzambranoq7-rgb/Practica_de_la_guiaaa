# ==========================================
# EJERCICIOS PROPUESTOS
# ==========================================

# ==========================================
# Ejercicio 1: Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
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
# Ejercicio 2: Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima. Imprime los tres valores con 2 decimales.
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
# Ejercicio 3: Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados respetando el orden de la primera aparición.
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
# Ejercicio de práctica (modificado): Función elementos_duplicados(lista) que retorne un conjunto (set) únicamente con los elementos que aparecen 2 o más veces.
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
# Ejercicio 4: Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas). Al final, imprime la palabra que más se repite.
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