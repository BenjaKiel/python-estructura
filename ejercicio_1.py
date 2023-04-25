import random
import numpy as np


m1_filas = int(input("Ingrese la cantidad de filas de matriz 1: "))
m1_columnas = int(input("Ingrese la cantidad de columnas de matriz 1: "))

m2_filas = int(input("Ingrese la cantidad de filas de matriz 2: "))
m2_columnas = int(input("Ingrese la cantidad de columnasde matriz 2: "))


m1 = []
for i in range(m1_filas):
    fila = []
    for j in range(m1_columnas):
        fila.append(random.randint(0, 5))
    m1.append(fila)

m2 = []
for i in range(m2_filas):
    fila = []
    for j in range(m2_columnas):
        fila.append(random.randint(0, 5))
    m2.append(fila)

# Mostrar la matriz generada
print("Matriz 1 generada:")
for fila in m1:
    print(fila)
# Mostrar la matriz generada
print("Matriz 2 generada:")
for fila in m2:
    print(fila)


def suma(m1, m2):
    m_final_suma = np.add(m1, m2)
    return m_final_suma

def resta(m_final_suma, m3):
    m_final_resta = np.subtract(m_final_suma, m3)
    return m_final_resta

m_final_suma = suma(m1, m2)
print("\nLa matriz resultado de la suma es:")
print(m_final_suma)

m3_filas = int(input("Ingrese la cantidad de filas de matriz 3: "))
m3_columnas = int(input("Ingrese la cantidad de columnasde matriz 3: "))

m3 = []
for i in range(m3_filas):
    fila = []
    for j in range(m3_columnas):
        fila.append(random.randint(0, 5))
    m3.append(fila)

# Mostrar la matriz generada
print("Matriz 3 generada:")
for fila in m3:
    print(fila)

m_final_resta = resta(m_final_suma, m3)
print("\nLa matriz resultado de la resta es:")
print(m_final_resta)
