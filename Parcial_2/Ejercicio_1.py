#Desarrolla una aplicación para gestionar una lista circular bidireccional de contactos telefónicos. Cada contacto tiene un nombre, un número de teléfono y una dirección de correo electrónico. 
# Se debe implementar una lista circular bidireccional para almacenar los contactos. 
# La lista debe tener las siguientes funcionalidades. Debe contener las siguientes funciones: 
# A. Clases respectivas del problema B. Método para agregar un contacto a la lista C. Método para mostrar la lista de contactos D. Método para buscar un contacto por su nombre 
# E. Método eliminar un contacto de la lista F. Método para verificar si la lista de contacto está vacía 
# Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de prueba o ejemplos específicos para demostrar su funcionamiento.


#A. Clases respectivas del problema

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.siguiente = None
        self.anterior = None
    
    def __str__(self):
        return self.nombre + " " + self.telefono + " " + self.correo
    
class Agenda:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def estaVacia(self):
        return self.primero == None
    
    def agregarContacto(self, nombre, telefono, correo):
        nuevo = Contacto(nombre, telefono, correo)
        if self.estaVacia():
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.ultimo = nuevo
            self.primero.anterior = self.ultimo
    
    def mostrarContactos(self):
        actual = self.primero
        while actual:
            print(actual)
            actual = actual.siguiente
            if actual == self.primero:
                break
    
    def buscarContacto(self, nombre):
        actual = self.primero
        while actual:
            if actual.nombre == nombre:
                print(actual)
                break
            actual = actual.siguiente
            if actual == self.primero:
                break
    
    def eliminarContacto(self, nombre):
        actual = self.primero
        while actual:
            if actual.nombre == nombre:
                if actual == self.primero:
                    self.primero = actual.siguiente
                    self.primero.anterior = self.ultimo
                    self.ultimo.siguiente = self.primero
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                break
            actual = actual.siguiente
            if actual == self.primero:
                break   
            
agenda = Agenda()


#B. Método para agregar un contacto a la lista

agenda.agregarContacto("Juan", "923456789", "Juanito.pro@gmail.com")
agenda.agregarContacto("Pedro", "987654321", "Pedrito.GG@gmail.com")    
agenda.agregarContacto("Rosalia", "956789123", "Rosalia.rau@gmail.com")
agenda.agregarContacto("Maria", "989123456", "Maria.alejandra@gmail.com")
agenda.agregarContacto("Benjamin", "921654987", "Benjamin.kiel@gmail.com")

print("Lista de contactos")

#C. Método para mostrar la lista de contactos

agenda.mostrarContactos()

#D. Método para buscar un contacto por su nombre

print("\nBuscar contacto")

agenda.buscarContacto("Benjamin")

#E. Método eliminar un contacto de la lista

print("\nEliminar contacto")

agenda.eliminarContacto("Benjamin")

print("\nLista de contactos actualizada")

agenda.mostrarContactos()

#F. Método para verificar si la lista de contacto está vacía

print("\nVerificar si la lista esta vacia")

if agenda.estaVacia():
    print("La lista esta vacia")
    
else:
    print("La lista no esta vacia")
    

