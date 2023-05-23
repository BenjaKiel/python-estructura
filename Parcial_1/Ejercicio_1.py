import random
import numpy as np

# Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios (5
# al 10, enteros positivos). Se pueden utilizar librerías para resolver el algoritmo.

m1_filas = 3
m1_columnas = 3

m1 = []
for i in range(m1_filas):
    fila = []
    for j in range(m1_columnas):
        fila.append(random.randint(5, 10))
    m1.append(fila)


# Mostrar la matriz generada
print("Matriz 1 generada:")
for x in m1:
    print(x)


determinante = np.linalg.det(m1)

print("La determinante de la matriz es:", determinante)
