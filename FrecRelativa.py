#Importa el modulo de aleatorios
from random import randint

# Cantidad de elementos del conjunto X
X = 4

#Elemento con el que se calculará la frecuencia relativa
x = 0

#Cantidad de experimentos
n = 10000000

#Código de error
error = 0

#Variable de conteo de coincidencias random con x
contX = 0

#Verificación de error
if   X <= 0           : error = 1 #Error de cantidad de elementos del conjunto
elif x <  0 or x >= X : error = 2 #Error si el elemento no pertenece al conjunto
elif n <= 0           : error = 3
else:
    for i in range(n):
        if randint(0,X-1) == x: contX += 1

#Imprime el error
if error != 0: print("Error: ",error)

#frecuencia relativa
print("Fercuencia relativa de ",x,": ",contX/n)
