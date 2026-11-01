#ejercicio1
#Funcion para eliminar elementos duplicados de una lista conservando el orden de aparicion
def eliminar_duplicados(lista):
    vistos = set()
    resultado = []
    for elem in lista:
        if elem not in vistos:
            vistos.add(elem)
            resultado.append(elem)
    return resultado

numeros = [4, 2, 4, 3, 2, 1, 5, 3]
print(eliminar_duplicados(numeros))


#ejercicio2
#Funcion para rotar los elementos de una lista k posiciones hacia la derecha usando slicing
def rotar_derecha(lista, k):
    if not lista:
        return []
    k = k % len(lista)
    return lista[-k:] + lista[:-k]

datos = [1, 2, 3, 4, 5]
print(rotar_derecha(datos, 2))


#ejercicio3
#Funcion para fusionar dos listas ordenadas en una sola lista manteniendo el orden
def fusionar_ordenadas(l1, l2):
    i = 0
    j = 0
    resultado = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            resultado.append(l1[i])
            i += 1
        else:
            resultado.append(l2[j])
            j += 1
    resultado.extend(l1[i:])
    resultado.extend(l2[j:])
    return resultado

lista_a = [1, 3, 5, 7]
lista_b = [2, 4, 6, 8, 9]
print(fusionar_ordenadas(lista_a, lista_b))


#ejercicio4
#Funcion para aplanar una lista que contiene sublistas anidadas de un nivel
def aplanar_lista(matriz):
    resultado = []
    for fila in matriz:
        if isinstance(fila, list):
            for elemento in fila:
                resultado.append(elemento)
        else:
            resultado.append(fila)
    return resultado

anidada = [[1, 2], [3, 4, 5], [6], 7]
print(aplanar_lista(anidada))


#ejercicio5
#Funcion para encontrar los dos numeros que sumados den un valor objetivo retornando sus indices
def dos_suma(lista, objetivo):
    posiciones = {}
    for i, num in enumerate(lista):
        complemento = objetivo - num
        if complemento in posiciones:
            return [posiciones[complemento], i]
        posiciones[num] = i
    return []

valores = [2, 7, 11, 15]
print(dos_suma(valores, 9))


#ejercicios mio.


#ejercicio1
#Funcion para contar la frecuencia de cada elemento en una lista retornando un diccionario
def contar_frecuencias(lista):
    frecuencias = {}
    for elem in lista:
        frecuencias[elem] = frecuencias.get(elem, 0) + 1
    return frecuencias

items = ["manzana", "pera", "manzana", "platano", "pera", "manzana"]
print(contar_frecuencias(items))


#ejercicio2
#Funcion para invertir una lista manualmente sin usar reverse ni slicing inverso
def invertir_lista(lista):
    resultado = []
    for i in range(len(lista) - 1, -1, -1):
        resultado.append(lista[i])
    return resultado

original = [10, 20, 30, 40, 50]
print(invertir_lista(original))


#ejercicio3
#Funcion para separar numeros pares e impares en dos listas independientes
def separar_pares_impares(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

numeros_muestra = [12, 7, 9, 14, 22, 5, 18]
p, imp = separar_pares_impares(numeros_muestra)
print("Pares:", p)
print("Impares:", imp)


#ejercicio4
#Funcion para calcular la diferencia entre el valor maximo y minimo de una lista sin usar max ni min
def rango_amplitud(lista):
    if not lista:
        return 0
    mayor = lista[0]
    menor = lista[0]
    for num in lista[1:]:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    return mayor - menor

precios = [25, 12, 89, 45, 6, 70]
print("Rango:", rango_amplitud(precios))


#ejercicio5
#Funcion para agrupar elementos continuos repetidos en sublistas
def agrupar_consecutivos(lista):
    if not lista:
        return []
    grupos = []
    grupo_actual = [lista[0]]
    for elem in lista[1:]:
        if elem == grupo_actual[-1]:
            grupo_actual.append(elem)
        else:
            grupos.append(grupo_actual)
            grupo_actual = [elem]
    grupos.append(grupo_actual)
    return grupos

repetidos = [1, 1, 2, 3, 3, 3, 4, 2, 2]
print(agrupar_consecutivos(repetidos))