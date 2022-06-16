import numpy as np
lista=np.zeros((4,4), dtype= str)
for f in range(4):
    for c in range(4):
        x=str(input("Escriba un letra"))
        lista[f][c]=x
print(lista)
vocal=0
for f in range(4):
    for c in range(4):
        if lista[f][c]=='a' or lista[f][c]=='e' or lista[f][c]=='i' or lista[f][c]=='o' or lista[f][c]=='u':
            vocal=vocal+1
print("hay",vocal,"vocales")
