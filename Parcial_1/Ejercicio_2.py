import random
import numpy as np

# Crear dos matrices donde la cantidad de filas y columnas serán 3 x 3. Los
# elementos de estas matrices deben ser generados de forma aleatoria (-5 a -10).
# Luego se deben multiplicar ambas matrices e imprimir la matriz resultante.
# Agregar una condición para que las dimensiones sean acordes para realizar la
# multiplicación entre ambas matrices.
# Esta matriz resultado se debe multiplicar por una matriz identidad, e imprimir la matriz final.


m1_filas = 3
m1_columnas = 3

m2_filas = 3
m2_columnas = 3


m1 = []
for i in range(m1_filas):
    fila = []
    for j in range(m1_columnas):
        fila.append(random.randint(-10, -5))
    m1.append(fila)

m2 = []
for i in range(m2_filas):
    fila = []
    for j in range(m2_columnas):
        fila.append(random.randint(-10, -5))
    m2.append(fila)


# prints

print("Matriz 1")
for x in m1:
    print(x)
print("/"*20)
print("Matriz 2")
for x in m2:
    print(x)


# funciones
def mult(m1, m2):
    mult = np.dot(m1, m2)
    return mult


matriz_mult = mult(m1, m2)

print("///////////////////////////////")
print("Matriz m1 y m2 multiplicadas")

for x in matriz_mult:
    print(x)
