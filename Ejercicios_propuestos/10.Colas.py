#ejercicio1
#Clase Cola con operaciones basicas usando lista interna (enqueue, dequeue, front, is_empty, size)
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def frente(self):
        if self.esta_vacia():
            return None
        return self.items[0]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return f"Frente -> {self.items} <- Final"

c = Cola()
c.encolar("Cliente 1")
c.encolar("Cliente 2")
c.encolar("Cliente 3")
print(c)
print("Atendido:", c.desencolar())
print(c)


#ejercicio2
#Simulador de cola de impresion de documentos
class ColaImpresion:
    def __init__(self):
        self.documentos = []

    def agregar_documento(self, nombre_doc):
        self.documentos.append(nombre_doc)
        print(f"Documento '{nombre_doc}' agregado a la cola de impresion.")

    def imprimir_siguiente(self):
        if not self.documentos:
            print("No hay documentos pendientes de impresion.")
            return None
        doc = self.documentos.pop(0)
        print(f"Imprimiendo: {doc}")
        return doc

    def pendientes(self):
        return len(self.documentos)

ci = ColaImpresion()
ci.agregar_documento("tesis.pdf")
ci.agregar_documento("informe.docx")
ci.imprimir_siguiente()
print("Pendientes:", ci.pendientes())


#ejercicio3
#Problema de conteo circular de la papa caliente usando una cola
def papa_caliente(lista_nombres, num_pases):
    cola = list(lista_nombres)
    while len(cola) > 1:
        for _ in range(num_pases):
            cola.append(cola.pop(0))
        eliminado = cola.pop(0)
        print(f"{eliminado} quedo fuera del juego.")
    return cola[0]

jugadores = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
ganador = papa_caliente(jugadores, 3)
print("Ganador:", ganador)


#ejercicio4
#Invertir el contenido de una cola utilizando una pila como estructura auxiliar
def invertir_cola(cola_original):
    pila_auxiliar = []
    while len(cola_original) > 0:
        pila_auxiliar.append(cola_original.pop(0))
    while len(pila_auxiliar) > 0:
        cola_original.append(pila_auxiliar.pop())
    return cola_original

cola_datos = [10, 20, 30, 40, 50]
print("Cola original:", cola_datos)
print("Cola invertida:", invertir_cola(cola_datos))


#ejercicio5
#Cola con prioridad simple donde cada elemento incluye su nivel de prioridad
class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def encolar(self, elemento, prioridad):
        self.cola.append((elemento, prioridad))
        self.cola.sort(key=lambda x: x[1], reverse=True)

    def desencolar(self):
        if not self.cola:
            return None
        return self.cola.pop(0)[0]

    def __str__(self):
        return str(self.cola)

cp = ColaPrioridad()
cp.encolar("Consulta general", 1)
cp.encolar("Emergencia medica", 5)
cp.encolar("Urgencia menor", 3)
print(cp)
print("Atendido de inmediato:", cp.desencolar())
print(cp)


#ejercicios mio.


#ejercicio1
#Simulador de atencion por turnos de un banco
class BancoTurnos:
    def __init__(self):
        self.cola = []
        self.conteo = 0

    def tomar_turno(self, nombre):
        self.conteo += 1
        turno = f"T-{self.conteo:03d}"
        self.cola.append((turno, nombre))
        print(f"{nombre} tomo el turno {turno}")

    def atender_cliente(self):
        if not self.cola:
            print("No hay clientes en espera.")
            return None
        turno, nombre = self.cola.pop(0)
        print(f"Llamando a {nombre} con {turno}")
        return turno, nombre

banco = BancoTurnos()
banco.tomar_turno("Maria")
banco.tomar_turno("Juan")
banco.atender_cliente