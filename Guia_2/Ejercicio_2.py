#Se está implementando un programa para administrar una cola de atención al cliente en una farmacia. 
# Cada cliente tiene un número de ticket y un número de caja para que pueda ser atendido. Se solicita implementar un algoritmo que contenga una lista circular para manejar la cola de atención de tres cajas: Caja 1, Caja 2 y Caja 3.


class Cliente:
    def __init__(self, ticket, caja):
        self.ticket = ticket
        self.caja = caja


class Cola_Atencion:
    def __init__(self):
        self.cajas = ["Caja 1", "Caja 2", "Caja 3"] #lista de cajas
        self.clientes = [] #lista de clientes
        self.indice_actual = 0 #indice de la caja actual

    def agregar_cliente(self, ticket):
        caja_actual = self.cajas[self.indice_actual]
        cliente = Cliente(ticket, caja_actual)
        self.clientes.append(cliente)
        self.indice_actual = (self.indice_actual + 1) % len(self.cajas) #se mueve al siguiente indice

    def atender_cliente(self):
        if len(self.clientes) > 0:
            cliente = self.clientes.pop(0) #saca el primer cliente de la lista
            print(f"Atendiendo al cliente con ticket {cliente.ticket} en {cliente.caja}")
        else:
            print("No hay clientes en la cola de atención")

    def mostrar_cola(self):
        if len(self.clientes) > 0: #si hay clientes en la cola
            print("Cola de atención:")
            for cliente in self.clientes:
                print(f"Ticket: {cliente.ticket} - Caja: {cliente.caja}")
        else:
            print("No hay clientes en la cola de atención")



cola = Cola_Atencion() #se crea la cola

#se agrega un cliente con el def agregar_cliente
cola.agregar_cliente(1)
cola.agregar_cliente(2)
cola.agregar_cliente(3)

#muestra la cola para que el cliente vea su ticket
cola.mostrar_cola()

#atiende al cliente
cola.atender_cliente()
cola.atender_cliente()

cola.mostrar_cola()

    