precio=int(input("Digite precio"))
def calcular_iva(precio):
    calculo=precio*0.19
    return calculo

print("el iva es de ", round(calcular_iva(precio)))
desc=int(input("Cuanto % quieres de descuento"))
def descuento(precio,desc):
    descu=precio*desc/100
    calculo=precio-descu
    return calculo
print("el valor con descuento es de ", descuento(precio,desc))

