import random 
import numpy as np
matriz1=np.zeros((3,3))
matriz2=np.zeros((3,3))
for f in range(len(matriz1)):
    for c in range(len(matriz1)):
        randomizao1=random.randint(1,100)
        matriz1[f][c]=randomizao1
print(matriz1)
print("===========================")
for f2 in range(len(matriz2)):
    for c2 in range(len(matriz2)):
        randomizao2=random.randint(1,100)
        matriz2[f2][c2]=randomizao2
print(matriz2)
print("===========================")
res=matriz1*matriz2
print(res)
