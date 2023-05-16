
import numpy as np
import random


def crear_matriz_random():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 5))
        m.append(fila)
    return m


def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_suma = []
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            elemento_suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(elemento_suma)
        matriz_suma.append(fila_suma)
    return matriz_suma


def fun_escalar(m1, m2):
    m_final_mult = np.dot(m1, m2)
    return m_final_mult


def mult_matriz(m1, m2):
    m_final_mult = np.dot(m1, m2)
    return m_final_mult


matriz_1 = crear_matriz_random()

matriz_2 = crear_matriz_random()

matriz_suma = sumar_matrices(matriz_1, matriz_2)

escalar = int(input("Ingrese el escalar: "))

matriz_escalar = fun_escalar(matriz_suma, escalar)

print("/"*15)
print("Matriz 1")
print("/"*15)
for x in matriz_1:
    print(x)

print("/"*15)
print("Matriz 2")
print("/"*15)
for x in matriz_2:
    print(x)


print("/"*15)
print("Matriz Suma")
print("/"*15)
for x in matriz_suma:
    print(x)


print("Matriz por escalar: ", escalar)
for x in matriz_escalar:
    print(x)

matriz_3 = crear_matriz_random()
print("Matriz 3")
for x in matriz_3:
    print(x)

matriz_final = mult_matriz(matriz_3, matriz_escalar)
print("Matriz Final")
for x in matriz_final:
    print(x)
