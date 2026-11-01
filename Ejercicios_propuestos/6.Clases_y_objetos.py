import math

#ejercicio1
#Clase Rectangulo con base, altura, calculo de area y perimetro
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo {self.base}x{self.altura}, área={self.area()}, perímetro={self.perimetro()}"

r = Rectangulo(5, 3)
print(r)
print("Área:", r.area())


#ejercicio2
#Clase Circulo con radio, calculo de area y circunferencia usando math.pi
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo r={self.radio}, área={self.area():.2f}"

c = Circulo(5)
print(c)


#ejercicio3
#Clase Estudiante que almacena notas en una lista, calcula promedio y valida aprobacion
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 7

    def __str__(self):
        return f"{self.nombre}: {self.notas} → prom={self.promedio():.2f}"

ana = Estudiante("Ana")
for n in [8, 6, 9]:
    ana.agregar_nota(n)
print(ana)
print(f"Aprobado: {ana.aprobado()}")


#ejercicio4
#Clase Vehiculo con odometro que acumula distancia y alerta mantenimiento cada 10000 km
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0
        self._ultimo_mantenimiento = 0

    def recorrer(self, distancia):
        self.km += distancia

    def necesita_mantenimiento(self):
        return (self.km - self._ultimo_mantenimiento) >= 10000

    def hacer_mantenimiento(self):
        self._ultimo_mantenimiento = self.km
        print(f"Mantenimiento hecho a los {self.km} km")

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.km} km"

auto = Vehiculo("Toyota", "Corolla")
auto.recorrer(15000)
print(auto)
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")
auto.hacer_mantenimiento()
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")


#ejercicio5
#Clase Vuelo con capacidad maxima, lista de pasajeros, reserva y cancelacion de asientos
class Vuelo:
    def __init__(self, codigo, destino, capacidad):
        self.codigo = codigo
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)

    def reservar_asiento(self, nombre_pasajero):
        if self.asientos_disponibles() <= 0:
            print(f"Vuelo {self.codigo} lleno. No se pudo registrar a {nombre_pasajero}.")
            return False
        if nombre_pasajero in self.pasajeros:
            print(f"{nombre_pasajero} ya tiene reserva en este vuelo.")
            return False
        self.pasajeros.append(nombre_pasajero)
        print(f"Reserva confirmada para {nombre_pasajero}.")
        return True

    def cancelar_reserva(self, nombre_pasajero):
        if nombre_pasajero in self.pasajeros:
            self.pasajeros.remove(nombre_pasajero)
            print(f"Reserva cancelada para {nombre_pasajero}.")
            return True
        print(f"{nombre_pasajero} no tiene reserva activa.")
        return False

    def __str__(self):
        return f"Vuelo {self.codigo} ({self.destino}) | Ocupación: {len(self.pasajeros)}/{self.capacidad} | Libres: {self.asientos_disponibles()}"

v = Vuelo("UIO-204", "Quito - Guayaquil", 2)
v.reservar_asiento("Carlos Mendoza")
v.reservar_asiento("Lucía Vega")
v.reservar_asiento("Mario Silva")
print(v)


#EJERCICIOS MIO


#ejercicio1
#Clase TrianguloRectangulo con calculo de area, hipotenusa y perimetro
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def hipotenusa(self):
        return (self.base**2 + self.altura**2) ** 0.5

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def __str__(self):
        return f"Triángulo Rectángulo {self.base}x{self.altura} | Hipotenusa: {self.hipotenusa():.2f} | Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"

t = TrianguloRectangulo(3, 4)
print(t)


#ejercicio2
#Clase Cilindro con calculo de area de la base, volumen y area total
class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def area_base(self):
        return math.pi * (self.radio ** 2)

    def volumen(self):
        return self.area_base() * self.altura

    def area_total(self):
        return (2 * self.area_base()) + (2 * math.pi * self.radio * self.altura)

    def __str__(self):
        return f"Cilindro r={self.radio}, h={self.altura} | Volumen: {self.volumen():.2f} | Área Total: {self.area_total():.2f}"

cil = Cilindro(3, 7)
print(cil)


#ejercicio3
#Clase CarritoCompras que almacena precios, calcula subtotal y aplica descuentos
class CarritoCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.precios = []

    def agregar_producto(self, precio):
        if precio > 0:
            self.precios.append(precio)

    def subtotal(self):
        return sum(self.precios)

    def total_con_descuento(self, porcentaje):
        descuento = self.subtotal() * (porcentaje / 100)
        return self.subtotal() - descuento

    def __str__(self):
        return f"Carrito de {self.cliente} | Artículos: {len(self.precios)} | Subtotal: ${self.subtotal():.2f}"

carrito = CarritoCompras("Carlos")
carrito.agregar_producto(15.50)
carrito.agregar_producto(24.00)
carrito.agregar_producto(10.50)
print(carrito)
print(f"Total con 10% de descuento: ${carrito.total_con_descuento(10):.2f}")


#ejercicio4
#Clase Impresora con control de hojas, impresion de paginas, recarga y alerta de stock
class Impresora:
    def __init__(self, modelo, hojas_iniciales=100):
        self.modelo = modelo
        self.hojas = hojas_iniciales
        self.paginas_impresas = 0

    def imprimir(self, cantidad):
        if cantidad <= 0:
            return
        if cantidad > self.hojas:
            print(f"Falta papel: se requieren {cantidad} hojas, pero solo quedan {self.hojas}.")
            return
        self.hojas -= cantidad
        self.paginas_impresas += cantidad
        print(f"Imprimiendo {cantidad} páginas...")

    def recargar_hojas(self, cantidad):
        if cantidad > 0:
            self.hojas += cantidad
            print(f"Recargadas {cantidad} hojas. Stock actual: {self.hojas}")

    def nivel_bajo(self):
        return self.hojas < 50

    def __str__(self):
        aviso = "¡Nivel bajo de papel!" if self.nivel_bajo() else "Papel suficiente"
        return f"Impresora {self.modelo} | Hojas restantes: {self.hojas} | Total impresas: {self.paginas_impresas} ({aviso})"

imp = Impresora("Epson L3250", 120)
imp.imprimir(80)
print(imp)
imp.recargar_hojas(100)
print(imp)


#ejercicio5
#Clase HabitacionHotel que gestiona check-in, capacidad de huespedes y cobro en check-out
class HabitacionHotel:
    def __init__(self, numero, precio_noche, capacidad):
        self.numero = numero
        self.precio_noche = precio_noche
        self.capacidad = capacidad
        self.huespedes = []

    def esta_ocupada(self):
        return len(self.huespedes) > 0

    def hacer_check_in(self, grupo):
        if self.esta_ocupada():
            print(f"La habitación {self.numero} ya está ocupada.")
            return False
        if len(grupo) > self.capacidad:
            print(f"El grupo supera la capacidad máxima ({self.capacidad} personas).")
            return False
        self.huespedes = grupo
        print(f"Check-in exitoso en habitación {self.numero} para: {', '.join(grupo)}")
        return True

    def hacer_check_out(self, noches):
        if not self.esta_ocupada():
            print(f"La habitación {self.numero} ya se encuentra vacía.")
            return 0.0
        total = noches * self.precio_noche
        print(f"Check-out habitación {self.numero}. Total: ${total:.2f}")
        self.huespedes.clear()
        return total

    def __str__(self):
        estado = f"Ocupada ({len(self.huespedes)} pers.)" if self.esta_ocupada() else "Disponible"
        return f"Habitación {self.numero} | Tarifa: ${self.precio_noche}/noche | Capacidad: {self.capacidad} | Estado: {estado}"

hab = HabitacionHotel(204, 65.0, 3)
print(hab)
hab.hacer_check_in(["Ana López", "Pedro Soto"])
print(hab)
hab.hacer_check_out(3)
print(hab)