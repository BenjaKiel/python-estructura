import random


n_filas = int(input("Ingrese la cantidad de filas: "))
n_columnas = int(input("Ingrese la cantidad de columnas: "))

escalar = int(input("Ingrese el escalar: "))


matriz = []
for i in range(n_filas):
    fila = []
    for j in range(n_columnas):
        fila.append(random.randint(0, 10))
    matriz.append(fila)

# Mostrar la matriz generada
print("Matriz generada:")
for fila in matriz:
    print(fila)

print("////////////////////////////////////////////////")
print("Matriz generada se multiplicara por:", (escalar))
print("////////////////////////////////////////////////")

for i in range(n_filas):
    for j in range(n_columnas):
        matriz[i][j] *= escalar


print("Matriz resultante:")
for fila in matriz:
    print(fila)
