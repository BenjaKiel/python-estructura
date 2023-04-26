from random import randint
from numpy import *

f= int(input("Ingrese cantidad de filas: "))
c= int(input("Ingrese cantidad de columnas: "))
lista = [0]*f
for x in range(len(lista)):
        lista[x]= [0]*c
for z in range(len(lista)):
        for x in range(len(lista[z])):
            lista[x][z] = randint(1,5)  
                
        print (lista[z])


f= int(input("Ingrese cantidad de filas: "))
c= int(input("Ingrese cantidad de columnas: "))
lista = [0]*f
for x in range(len(lista)):
        lista[x]= [0]*c
for z in range(len(lista)):
        for x in range(len(lista[z])):
            lista[x][z] = randint(1,5)  
                
        print (lista[z])




