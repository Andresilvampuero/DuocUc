import numpy as np
def sacar_dv():
    derecho=np.zeros(8)
    tabla=np.array((2,3,4,5,6,7,2,3))
    alreves=np.zeros(8)
    for f in range(len(derecho)):
        rut=int(input(f"escriba el numero {f+1} de su rut\n"))
        derecho[f]=rut
    alreves=derecho[::-1]
    res=tabla*alreves
    suma=res[0]+res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]
    suma=round(suma)
    div=suma//11
    mult=div*11
    resta=suma-mult
    dv=11-resta
    if dv==11:
        dv=0
    elif dv==10:
        dv='K'
    return dv
print("el digito verificador de su rut es :",sacar_dv())
