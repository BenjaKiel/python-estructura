import array
import random

array_tamaño = random.randint(10, 30)

array = array.array('i', [random.randint(0, 99) for _ in range(array_tamaño)])

print(array)

buscar = int(input("Ingrese el elemento que desea buscar en el arreglo: "))

if buscar in array:
    print(f"{buscar} se encuentra en el arreglo.")
else:
    print(f"{buscar} no se encuentra en el arreglo.")
