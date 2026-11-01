#ejercicio1
#Calculo de la suma de los digitos de un numero entero de 3 cifras
num = int(input("Número de 3 cifras: "))
centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10
suma = centenas + decenas + unidades
print(f"Suma: {suma}")


#ejercicio2
#Conversion de una cantidad total de minutos a horas y minutos
total = int(input("Minutos totales: "))
horas = total // 60
mins = total % 60
print(f"{horas} horas {mins} minutos")


#ejercicio3
#Calculo del indice de masa corporal (IMC) a partir del peso y la estatura
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))
imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")


#ejercicio4
#Redondeo de un numero decimal segun la cantidad de decimales indicada
num = float(input("Número: "))
dec = int(input("Decimales: "))
resultado = round(num, dec)
print(resultado)


#ejercicio5
#Calculo del total a pagar aplicando descuentos escalonados segun la cantidad comprada
PRECIO = 12
cant = int(input("Cantidad: "))
if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0
subtotal = PRECIO * cant
total = subtotal * (1 - descuento)
print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento * 100)}%")
print(f"Total: ${total:.2f}")


#ejercicios mio.


#ejercicio1
#Calculo del producto de los digitos de un numero entero de 3 cifras
num = int(input("Número de 3 cifras: "))
centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10
producto = centenas * decenas * unidades
print(f"Producto: {producto}")


#ejercicio2
#Conversion de una cantidad de dias a semanas y dias restantes
total_dias = int(input("Total de días: "))
semanas = total_dias // 7
dias_restantes = total_dias % 7
print(f"{semanas} semanas y {dias_restantes} días")


#ejercicio3
#Calculo de la densidad de un objeto a partir de su masa y volumen
masa = float(input("Masa (kg): "))
volumen = float(input("Volumen (m3): "))
densidad = masa / volumen
print(f"Densidad: {densidad:.2f} kg/m3")


#ejercicio4
#Calculo del valor absoluto de la diferencia entre dos numeros decimales redondeado a dos cifras
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
diferencia = abs(n1 - n2)
print(f"Diferencia absoluta: {round(diferencia, 2)}")


#ejercicio5
#Calculo del costo total de envio con recargo por peso adicional
TARIFA_BASE = 5.0
peso_paquete = float(input("Peso del paquete (kg): "))
if peso_paquete > 10:
    recargo = 0.20
elif peso_paquete > 5:
    recargo = 0.10
else:
    recargo = 0.0
total_envio = TARIFA_BASE * (1 + recargo)
print(f"Tarifa base: ${TARIFA_BASE:.2f}")
print(f"Recargo: {int(recargo * 100)}%")
print(f"Total envío: ${total_envio:.2f}")