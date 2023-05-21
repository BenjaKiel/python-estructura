import numpy as np

matriz = np.random.randint(1, 10, (3, 3))

for x in matriz:
    print (x)

determinante = np.linalg.det(matriz)

print("La determinante de la matriz es:", determinante)
