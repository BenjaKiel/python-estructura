#Un equipo de desarrolladores tiene la misión de programar una aplicación de reproducción de música y se necesita implementar una lista enlazada doble para administrar la lista de reproducción de un usuario en específico. Cada nodo de la lista representa una canción, y cada canción tiene un título y un artista. Se solicita implementar una lista enlazada doble para una lista de reproducción de música.


class Nodo:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0
        
    def agregar(self, titulo, artista):
        nuevo = Nodo(titulo, artista)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamano += 1
        
    def imprimir(self):
        aux = self.cabeza
        while aux != None:
            print(aux.titulo, aux.artista)
            aux = aux.siguiente
            
            
    def ordenar(self):
        for i in range(self.tamano):
            aux = self.cabeza
            for j in range(self.tamano-i-1):
                if aux.titulo > aux.siguiente.titulo:
                    aux.titulo, aux.siguiente.titulo = aux.siguiente.titulo, aux.titulo
                    aux.artista, aux.siguiente.artista = aux.siguiente.artista, aux.artista
                aux = aux.siguiente

lista = Lista()

lista.agregar("Antes de perderte", "Duki")
lista.agregar("Hablamos mañana", "Bad bunny")
lista.agregar("Here", "Alessia Cara")
lista.agregar("Trance", "metro boomin")
lista.agregar("Sico mode", "Travis Scott")
lista.agregar("My blood", "Pablo Chill-E")
lista.agregar("La cone", "Mora")
lista.agregar("Many nights", "Metro boomin")

lista.imprimir()

print()

lista.ordenar()



