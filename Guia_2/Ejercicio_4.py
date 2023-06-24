#Un supermercado necesita un programa para el manejo de un almacén de productos en una de sus sucursales. Los productos se reciben en una pila y se despachan en una cola para su entrega a los clientes. Se solicita implementar un algoritmo que incluya tanto el uso de pila y cola. Debe realizarse las siguientes operaciones: A. Agregar producto: Permite ingresar un nuevo producto al almacén. El producto se agrega a la pila de productos recibidos.
# B. Despachar producto: Remueve el producto más antiguo de la cola y lo entrega al cliente. Si la cola está vacía, muestra un mensaje indicando que no hay productos disponibles para despachar. C. Verificar si la pila de productos recibidos está vacía: Devuelve un mensaje que indica si la pila de productos recibidos está vacía. D. Verificar si la cola de productos para despachar está vacía: Devuelve un mensaje que indica si la cola de productos para despachar está vacía. 
# E. Imprimir lista de productos recibidos: Muestra en consola los productos almacenados en la pila de productos recibidos. 
# F. Imprimir lista de productos para despachar: Muestra en consola los productos almacenados en la cola de productos para despachar. G. Mostrar cantidad total de productos en el almacén: Muestra en consola la cantidad total de productos que hay en el almacén, sumando la cantidad de productos recibidos en la pila y la cantidad de productos para despachar en la cola.


class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        
    def __str__(self):
        return f"Producto: {self.nombre} - Cantidad: {self.cantidad}"
    
class Almacen:
    def __init__(self):
        self.productos_recibidos = []
        self.productos_despachar = []
        
    def agregar_producto(self, producto):
        self.productos_recibidos.append(producto)
        
    def despachar_producto(self):
        if len(self.productos_despachar) > 0:
            producto = self.productos_despachar.pop(0)
            print(f"Despachando producto: {producto}")
        else:
            print("No hay productos para despachar")
            
    def verificar_pila_vacia(self):
        if len(self.productos_recibidos) > 0:
            print("La pila de productos recibidos no está vacía")
        else:
            print("La pila de productos recibidos está vacía")
            
    def verificar_cola_vacia(self):
        if len(self.productos_despachar) > 0:
            print("La cola de productos para despachar no está vacía")
        else:
            print("La cola de productos para despachar está vacía")
            
    def imprimir_productos_recibidos(self):
        if len(self.productos_recibidos) > 0:
            print("Productos recibidos:")
            for producto in self.productos_recibidos:
                print(producto)
        else:
            print("No hay productos recibidos")
            
    def imprimir_productos_despachar(self):
        if len(self.productos_despachar) > 0:
            print("Productos para despachar:")
            for producto in self.productos_despachar:
                print(producto)
        else:
            print("No hay productos para despachar")
            
    def cantidad_total_productos(self):
        cantidad_total = len(self.productos_recibidos) + len(self.productos_despachar)
        print(f"Cantidad total de productos: {cantidad_total}")
        
        
almacen = Almacen()

# A. Agregar producto:

producto1 = Producto("Arroz", 60)
producto2 = Producto("Fideos", 23)
producto3 = Producto("Azúcar", 30)
producto4 = Producto("Sal", 80)
producto5 = Producto("Aceite", 90)

almacen.agregar_producto(producto1)
almacen.agregar_producto(producto2)
almacen.agregar_producto(producto3)
almacen.agregar_producto(producto4)
almacen.agregar_producto(producto5)



# B. Despachar producto:



almacen.despachar_producto()
 
# C. Verificar si la pila de productos recibidos está vacía: 

almacen.verificar_pila_vacia()

# D. Verificar si la cola de productos para despachar está vacía: 

almacen.verificar_cola_vacia()

# E. Imprimir lista de productos recibidos: 

almacen.imprimir_productos_recibidos()

# F. Imprimir lista de productos para despachar: Muestra en consola los productos almacenados en la cola de productos para despachar.

almacen.imprimir_productos_despachar()

# G. Mostrar cantidad total de productos en el almacén: M

almacen.cantidad_total_productos()

