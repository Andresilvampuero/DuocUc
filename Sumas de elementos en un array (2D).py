import numpy as np
import random
rango=np.arange(20)
lista=np.reshape(rango,(4,5))
for c in range(5):
    for f in range(4):
        randomiz=random.randint(0,100)
        lista[f][c]=randomiz
print(lista)
print("====== SUMA FILAS ======")
sumafilas=lista.sum(1)
print(sumafilas[0])
print(sumafilas[1])
print(sumafilas[2])
print(sumafilas[3])
print("respectivamente...")
print("")
print("====== SUMA COLUMNAS ======")
sumacolumnas=lista.sum(0)
print(sumacolumnas[0],sumacolumnas[1],sumacolumnas[2],sumacolumnas[3])
print("")
print("====== SUMA DE LA DIAGONAL ======")
dia_lista=np.diag(lista)
print("La diagonal es",dia_lista[0],dia_lista[1],dia_lista[2],dia_lista[3])
x=dia_lista.sum()
print("Da como resultado ",x)
print("")
print("====== CUANTOS IMPARES HAY EN LA LISTA ======")
impar=0
for c in range(5):
    for f in range(4):
        if lista[f][c]%2==1:
            impar=impar+1
print("Hay",impar,"impares")




