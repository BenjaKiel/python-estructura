#Se requiere gestionar una jerarquía de empleados en una empresa. 
# Cada empleado tiene un cargo específico y puede tener uno o varios subordinados. 
# Utilizando un árbol, elabore el programa con las siguientes funcionalidades: A. Agregar empleado: Permite ingresar un nuevo empleado a la jerarquía. El empleado se agrega como subordinado de un empleado existente, especificando su cargo. 
# B. Eliminar empleado: Eliminar un empleado de la jerarquía, junto con todos sus subordinados. Al eliminar un empleado, todos sus subordinados pasan a ser subordinados del empleado superior. 
# C. Mostrar la jerarquía: Muestra en consola la estructura jerárquica completa de la empresa, mostrando los empleados y sus respectivos subordinados en forma de árbol. D. Buscar empleado: Permite buscar un empleado en la jerarquía por su nombre y muestra su cargo y subordinados directos, si los tiene. 
# E. Obtener jefe directo: Dado un empleado, muestra en pantalla el nombre y cargo de su jefe directo.

class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Cargo: {self.cargo}"
    
    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)
        
    def eliminar_subordinado(self, subordinado):
        self.subordinados.remove(subordinado)
        
    def mostrar_subordinados(self):
        if len(self.subordinados) > 0:
            print("Subordinados:")
            for subordinado in self.subordinados:
                print(subordinado)
        else:
            print("No tiene subordinados")
            
    def obtener_jefe_directo(self):
        print(f"Jefe directo: {self.nombre} - {self.cargo}")
        
class Empresa:
    def __init__(self):
        self.empleados = []
        
    def agregar_empleado(self, empleado, jefe):
        self.empleados.append(empleado)
        jefe.agregar_subordinado(empleado)
        
    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)
        for subordinado in empleado.subordinados:
            self.agregar_empleado(subordinado, empleado)
            
    def mostrar_jerarquia(self):
        if len(self.empleados) > 0:
            print("Jerarquía:")
            for empleado in self.empleados:
                print(empleado)
                empleado.mostrar_subordinados()
        else:
            print("No hay empleados")
            
    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                print(empleado)
                empleado.mostrar_subordinados()
                return
        print("No se encontró el empleado")
        
    def obtener_jefe_directo(self, empleado):
        empleado.obtener_jefe_directo()
        
        
def main():
    empresa = Empresa()
    
    #A. Agregar empleado:
    jefe = Empleado("Benjamín", "Gerente")
    empresa.agregar_empleado(jefe, jefe)
    empleado1 = Empleado("Pepe", "Jefe de Ventas")
    empresa.agregar_empleado(empleado1, jefe)
    empleado2 = Empleado("Josefa", "Jefe de Marketing")
    empresa.agregar_empleado(empleado2, jefe)
    empleado3 = Empleado("Lesly", "Vendedor")
    empresa.agregar_empleado(empleado3, empleado1)
    empleado4 = Empleado("Matias", "Vendedor")
    empresa.agregar_empleado(empleado4, empleado1)
    empleado5 = Empleado("Carlos", "Diseñador")
    empresa.agregar_empleado(empleado5, empleado2)
    
    #B. Eliminar empleado:
    empresa.eliminar_empleado(empleado1)
    
    #C. Mostrar la jerarquía:
    empresa.mostrar_jerarquia()
    
    #D. Buscar empleado:
    print("Busca el empleado Matias")
    empresa.buscar_empleado("Matias")
    
    #E. Obtener jefe directo de matias (empleado4):
    empresa.obtener_jefe_directo(empleado4)

    

    
main()

 