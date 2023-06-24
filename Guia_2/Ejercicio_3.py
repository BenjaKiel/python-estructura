import math


#creo mi clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista_Enlazada:
    def __init__(self):
        self.primero = None

    def agregar_dato(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def calcular_media(self):
        if self.primero is None:
            return None
        suma = 0
        contador = 0
        actual = self.primero
        while actual:
            suma += actual.dato
            contador += 1
            actual = actual.siguiente
        return suma / contador

    def calcular_desviacion_estandar(self):
        if self.primero is None:
            return None
        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        actual = self.primero
        while actual:
            suma_cuadrados += (actual.dato - media) ** 2
            contador += 1
            actual = actual.siguiente
        varianza = suma_cuadrados / contador
        desviacion_estandar = math.sqrt(varianza)
        return desviacion_estandar

    def imprimir_lista(self):
        if self.primero is None:
            print("La lista está vacía.")
        else:
            actual = self.primero
            while actual:
                print(actual.dato)
                actual = actual.siguiente

    def verificar_lista_vacia(self):
        return self.primero is None


lista = Lista_Enlazada()

# El cliente debe ingresar los datos
lista.agregar_dato(3)
lista.agregar_dato(14)
lista.agregar_dato(15)
lista.agregar_dato(30)


lista.imprimir_lista()

# Calcula la media
media = lista.calcular_media()
print("Media:", media)

# Calcula la desviación estándar
desviacion_estandar = lista.calcular_desviacion_estandar()
print("Desviación estándar:", desviacion_estandar)

# Verifica si es que la lista se encuentra vacia
esta_vacia = lista.verificar_lista_vacia()
print("¿La lista está vacía?", esta_vacia)
