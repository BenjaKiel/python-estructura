from random import randint

lista = [0]*5
for x in range(len(lista)):
    lista[x] = [0]*5
for z in range(len(lista)):
    for x in range(len(lista[z])):
        lista[x][z] = randint(0, 30)
    print(lista[z])


suma_columnas = [sum(columna) for columna in zip(*lista)]

suma_mas_alta = max(suma_columnas)

suma_filas = [sum(fila) for fila in lista]

suma_mas_baja = min(suma_filas)


print("Suma de cada columna:", suma_columnas)
print("Suma más alta entre las columnas:", suma_mas_alta)
print("Suma de cada fila:", suma_filas)
print("Suma más baja entre las filas:", suma_mas_baja)
