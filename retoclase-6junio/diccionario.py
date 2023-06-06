
A = {}

for i in range(3):
    nombre = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese el nombre de la asignatura: ")
    nota1 = float(input("Ingrese la nota del laboratorio 1: "))
    nota2 = float(input("Ingrese la nota del laboratorio 2: "))
    A[nombre] = [asignatura, nota1, nota2]
    
for i in A:
    print(i, A[i])
    
for i in A:
    promedio = A[i][1]*0.3 + A[i][2]*0.7
    A[i].append(promedio)
        
for i in A:
    print(i, A[i][3], sep=": ")
    
