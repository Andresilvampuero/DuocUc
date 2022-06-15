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
print("el valor con descuento aplicado es de ", (descuento(precio,desc)))
peso=float(input("Indique su peso"))
estatura=float(input("Indique su estatura"))
def calcular_imc(peso,estatura):
    x=peso/estatura**2
    return x
print("Su indice imc es", (calcular_imc(peso,estatura)))
hola=calcular_imc(peso,estatura)
if hola>0 and hola<100:
    if hola<18.5:
        print("Según su índice usted tiene bajo peso")
    elif hola>=18.5 and hola<=24.9:
        print("Según su índice usted tiene un peso adecuado")
    elif hola>=25 and hola<=29.9:
        print("Según su índice usted tiene sobrepeso")
    elif hola>=30 and hola<=34.9:
        print("Según su índice usted sufre de obesidad grado 1")
    elif hola>=35 and hola<=39.9:
        print("Según su índice usted sufre de obesidad grado 2")
    elif hola>=40:
        print("Según su índice usted sufre de obesidad grado 3")
else:
    print("ERROR, indique parámetros válidos")