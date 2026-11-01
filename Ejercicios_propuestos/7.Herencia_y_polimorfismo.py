import math

#ejercicio1
#Clase base Persona con subclases Pasajero y Empleado usando super() y polimorfismo en __str__
class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cédula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"

class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):
        self.millas += m

    def __str__(self):
        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"

class Empleado(Persona):
    def __init__(self, nombre, cedula, codigo_emp, salario):
        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"

p = Pasajero("Ana", "0912345678", "AB-123")
e = Empleado("Luis", "0987654321", "EMP-01", 1200.0)
p.sumar_millas(500)
e.aumentar_salario(10)
print(p)
print(e)


#ejercicio2
#Clase base Figura con subclases Rectangulo y Circulo que implementan polimorficamente area() y perimetro()
class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0.0

    def perimetro(self):
        return 0.0

class RectanguloFigura(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo {self.color} {self.base}x{self.altura} | Área: {self.area():.2f}"

class CirculoFigura(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo {self.color} r={self.radio} | Área: {self.area():.2f}"

figuras = [RectanguloFigura("Azul", 4, 5), CirculoFigura("Rojo", 3)]
for fig in figuras:
    print(fig)


#ejercicio3
#Clase base Vehiculo con subclases Auto y Moto que calculan peaje con tarifas distintas
class VehiculoTransporte:
    def __init__(self, placa, marca):
        self.placa = placa
        self.marca = marca

    def calcular_peaje(self):
        return 0.0

class Auto(VehiculoTransporte):
    def __init__(self, placa, marca, pasajeros):
        super().__init__(placa, marca)
        self.pasajeros = pasajeros

    def calcular_peaje(self):
        return 2.00

    def __str__(self):
        return f"Auto {self.marca} [{self.placa}] | Peaje: ${self.calcular_peaje():.2f}"

class Moto(VehiculoTransporte):
    def __init__(self, placa, marca, cilindraje):
        super().__init__(placa, marca)
        self.cilindraje = cilindraje

    def calcular_peaje(self):
        return 0.50

    def __str__(self):
        return f"Moto {self.marca} [{self.placa}] | Peaje: ${self.calcular_peaje():.2f}"

a = Auto("GBA-1234", "Chevrolet", 4)
m = Moto("MC-5678", "Yamaha", 250)
print(a)
print(m)


#ejercicio4
#Clase base Cuenta con subclases CuentaAhorros (interes) y CuentaCorriente (sobregiro)
class Cuenta:
    def __init__(self, numero, saldo=0.0):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

class CuentaAhorros(Cuenta):
    def __init__(self, numero, saldo=0.0, tasa_interes=0.02):
        super().__init__(numero, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        ganancia = self.saldo * self.tasa_interes
        self.saldo += ganancia

    def __str__(self):
        return f"Ahorros {self.numero} | Saldo: ${self.saldo:.2f}"

class CuentaCorriente(Cuenta):
    def __init__(self, numero, saldo=0.0, limite_sobregiro=200.0):
        super().__init__(numero, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if 0 < monto <= (self.saldo + self.limite_sobregiro):
            self.saldo -= monto
            return True
        return False

    def __str__(self):
        return f"Corriente {self.numero} | Saldo: ${self.saldo:.2f} (Sobregiro max: ${self.limite_sobregiro:.2f})"

ca = CuentaAhorros("AH-01", 1000.0)
ca.aplicar_interes()
cc = CuentaCorriente("CC-02", 100.0)
cc.retirar(250.0)
print(ca)
print(cc)


#ejercicio5
#Clase base Notificacion con polimorfismo en enviar() para Email y SMS
class Notificacion:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar(self):
        pass

class NotificacionEmail(Notificacion):
    def __init__(self, destinatario, mensaje, asunto):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        print(f"Enviando Email a {self.destinatario} | Asunto: {self.asunto} | Mensaje: {self.mensaje}")

class NotificacionSMS(Notificacion):
    def __init__(self, destinatario, mensaje):
        super().__init__(destinatario, mensaje)

    def enviar(self):
        print(f"Enviando SMS al número {self.destinatario} | Texto: {self.mensaje}")

notificaciones = [
    NotificacionEmail("usuario@correo.com", "Tu vuelo sale a las 10:00", "Confirmación de vuelo"),
    NotificacionSMS("0991234567", "Tu código de acceso es 8492")
]
for n in notificaciones:
    n.enviar()


#ejercicios mio.


#ejercicio1
#Clase base MiembroClub con subclases MiembroEstandar y MiembroVIP que aplica descuentos exclusivos
class MiembroClub:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro

    def obtener_cuota(self):
        return 30.00

    def __str__(self):
        return f"Socio: {self.nombre} [{self.id_miembro}]"

class MiembroEstandar(MiembroClub):
    def __init__(self, nombre, id_miembro):
        super().__init__(nombre, id_miembro)

    def __str__(self):
        return f"{super().__str__()} | Tipo: Estándar | Cuota: ${self.obtener_cuota():.2f}"

class MiembroVIP(MiembroClub):
    def __init__(self, nombre, id_miembro, casillero):
        super().__init__(nombre, id_miembro)
        self.casillero = casillero

    def obtener_cuota(self):
        return 60.00

    def __str__(self):
        return f"{super().__str__()} | Tipo: VIP (Casillero #{self.casillero}) | Cuota: ${self.obtener_cuota():.2f}"

m1 = MiembroEstandar("Diego Ramos", "SOC-101")
m2 = MiembroVIP("Elena Morales", "SOC-007", 14)
print(m1)
print(m2)


#ejercicio2
#Clase base Instrumento con subclases Guitarra y Tambor implementando polimorficamente afinar() y tocar()
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def afinar(self):
        pass

    def tocar(self):
        pass

class Guitarra(Instrumento):
    def __init__(self, nombre, cuerdas=6):
        super().__init__(nombre)
        self.cuerdas = cuerdas

    def afinar(self):
        print(f"Afinando las {self.cuerdas} cuerdas de la guitarra {self.nombre}...")

    def tocar(self):
        print(f"Tocando un acorde en la guitarra {self.nombre}: ¡Strum!")

class Tambor(Instrumento):
    def __init__(self, nombre, diametro):
        super().__init__(nombre)
        self.diametro = diametro

    def afinar(self):
        print(f"Ajustando parches del tambor {self.nombre} de {self.diametro}cm...")

    def tocar(self):
        print(f"Golpeando el tambor {self.nombre}: ¡Boom boom!")

orquesta = [Guitarra("Fender"), Tambor("Bata", 40)]
for inst in orquesta:
    inst.afinar()
    inst.tocar()


#ejercicio3
#Clase base EmpleadoEmpresa con subclases EmpleadoFijo y EmpleadoPorHoras que calculan sueldo neto
class EmpleadoEmpresa:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

    def calcular_sueldo(self):
        return 0.0

class EmpleadoFijo(EmpleadoEmpresa):
    def __init__(self, nombre, cargo, sueldo_base):
        super().__init__(nombre, cargo)
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

    def __str__(self):
        return f"{self.nombre} ({self.cargo}) | Sueldo mensual fijo: ${self.calcular_sueldo():.2f}"

class EmpleadoPorHoras(EmpleadoEmpresa):
    def __init__(self, nombre, cargo, valor_hora, horas_trabajadas):
        super().__init__(nombre, cargo)
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        return self.valor_hora * self.horas_trabajadas

    def __str__(self):
        return f"{self.nombre} ({self.cargo}) | Horas: {self.horas_trabajadas} | Sueldo: ${self.calcular_sueldo():.2f}"

ef = EmpleadoFijo("Mariana Paz", "Analista", 1500.0)
eh = EmpleadoPorHoras("Javier Cruz", "Tutor", 12.5, 80)
print(ef)
print(eh)


#ejercicio4
#Clase base DispositivoElectronico con subclases Smartphone y Laptop que gestionan consumo de bateria
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def cargar(self):
        self.bateria = 100
        print(f"{self.marca} {self.modelo} cargado al 100%.")

    def usar(self, horas):
        pass

class Smartphone(DispositivoElectronico):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def usar(self, horas):
        gasto = horas * 10
        self.bateria = max(0, self.bateria - gasto)
        print(f"Teléfono usado por {horas}h. Batería restante: {self.bateria}%")

class Laptop(DispositivoElectronico):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def usar(self, horas):
        gasto = horas * 25
        self.bateria = max(0, self.bateria - gasto)
        print(f"Laptop usada por {horas}h. Batería restante: {self.bateria}%")

telefono = Smartphone("Samsung", "S23")
compu = Laptop("Lenovo", "ThinkPad")
telefono.usar(3)
compu.usar(2)


#ejercicio5
#Clase base MetodoPago con subclases TarjetaCredito y PayPal que procesan pagos con comisiones polimorficas
class MetodoPago:
    def __init__(self, titular):
        self.titular = titular

    def procesar_pago(self, monto):
        pass

class TarjetaCredito(MetodoPago):
    def __init__(self, titular, numero_tarjeta):
        super().__init__(titular)
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, monto):
        comision = monto * 0.03
        total = monto + comision
        print(f"Pago de ${monto:.2f} con Tarjeta ...{self.numero_tarjeta[-4:]}. Comisión 3%: ${comision:.2f}. Total cobrado: ${total:.2f}")

class PayPal(MetodoPago):
    def __init__(self, titular, email):
        super().__init__(titular)
        self.email = email

    def procesar_pago(self, monto):
        comision = 0.50
        total = monto + comision
        print(f"Pago de ${monto:.2f} con PayPal ({self.email}). Tarifa fija: ${comision:.2f}. Total cobrado: ${total:.2f}")

pagos = [TarjetaCredito("Santiago Mora", "1234567890123456"), PayPal("Santiago Mora", "smora@gmail.com")]
for pago in pagos:
    pago.procesar_pago(50.00)