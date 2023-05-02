import random

arreglo = random.randint(10, 30)


array_final = [random.randint(0, 10) for x in range(arreglo)]


array_final.sort()

print("Ordenado de forma ascendiente")
print(array_final)

print("Ordenado de forma aleatoria")

random.shuffle(array_final)

print(array_final)
