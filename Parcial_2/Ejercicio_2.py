#2. Desarrolla un sistema de gestión de inventario utilizando listas bidireccionales. Cada artículo del inventario tiene un código único, un nombre, una descripción y una cantidad disponible. 
# El sistema debe realizar las siguientes operaciones: A. Agregar un artículo al inventario, ingresando su código, nombre, descripción y cantidad inicial 
# B. Eliminar un artículo del inventario utilizando su código C. Buscar un artículo en específico por su código D. Actualizar la cantidad disponible de un artículo 
# E. Mostrar todos los artículos del inventario en orden ascendente según su código Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los resultados obtenidos anteriormente. 
# Esto implica que se deben ejecutar las funciones con datos de prueba o ejemplos específicos para demostrar su funcionamiento.


class Articulo:
    def __init__(self, codigo, nombre, descripcion, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.siguiente = None
        self.anterior = None
    
    def __str__(self):
        return self.codigo + " " + self.nombre + " " + self.descripcion + " " + str(self.cantidad)
    

class Inventario:
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def agregarArticulo(self, codigo, nombre, descripcion, cantidad):
        nuevo = Articulo(codigo, nombre, descripcion, cantidad)
        if self.estaVacio():
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
    
    def estaVacio(self):
        return self.primero == None
    
    
    def mostrarArticulos(self):
        actual = self.primero
        while actual:
            print(actual)
            actual = actual.siguiente
            if actual == self.primero:
                break
    
    def buscarArticulo(self, codigo):
        actual = self.primero
        while actual:
            if actual.codigo == codigo:
                print(actual)
                break
            actual = actual.siguiente
            if actual == self.primero:
                break
    
    def actualizarCantidad(self, codigo, cantidad):
        actual = self.primero
        while actual:
            if actual.codigo == codigo:
                actual.cantidad = cantidad
                break
            actual = actual.siguiente
            if actual == self.primero:
                break
    
    def eliminarArticulo(self, codigo):
        actual = self.primero
        while actual:
            if actual.codigo == codigo:
                if actual == self.primero:
                    self.primero = actual.siguiente
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
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



inventario = Inventario()

#A. Agregar un artículo al inventario, ingresando su código, nombre, descripción y cantidad inicial

inventario.agregarArticulo("A1", "Air Jordan 1", "Color cafe edicion limitada", 7)
inventario.agregarArticulo("A2", "Nike Dunk", "Color verde Tallas Hombre", 70) 
inventario.agregarArticulo("A3", "Air Force One Nike", "Colab nocta extra laces", 40)
inventario.agregarArticulo("A4", "Nike Retro 4", "Color militar tallas OG", 20)
inventario.agregarArticulo("A5", "Nike Retro 3", "Color lima tallas Mujer", 20)
inventario.agregarArticulo("A6", "Vans Knu Skool", "Color negro extra laces Unisex", 120)
inventario.agregarArticulo("A7", "Adi2000 Adidas", "Colores Varios tallas Unisex", 80)

#B. Eliminar un artículo del inventario utilizando su código
print("\nEliminar articulo A2 del inventario ")

inventario.eliminarArticulo("A2")

print("Producto ya eliminado")
inventario.mostrarArticulos()

#C. Buscar un artículo en específico por su código

print("\nBuscar articulo A4")
inventario.buscarArticulo("A4")

#D. Actualizar la cantidad disponible de un artículo

print("\nActualizar cantidad de producto de A6")

inventario.actualizarCantidad("A6", 40)

print("\nProducto ya actualizado")
inventario.buscarArticulo("A6")

#E. Mostrar todos los artículos del inventario en orden ascendente según su código

print("\n Mostrar Articulos en orden ascendente")

inventario.mostrarArticulos()


