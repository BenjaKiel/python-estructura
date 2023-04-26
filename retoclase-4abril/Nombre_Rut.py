Personas = []
for i in range(5):
    nombre = input("Ingrese el nombre de la persona: ")
    rut = input("Ingrese el RUT de la persona: ")
    
    Persona = {"nombre": nombre, "rut": rut}
    

    Personas.append(Persona)


print("Lista: ")
for Persona in Personas:
    print("Nombre: " + Persona["nombre"] + ", RUT: " + Persona["rut"])