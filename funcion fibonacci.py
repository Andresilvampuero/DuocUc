num=int(input("Cuántos números de fibonacci desea mostrar?"))
def fibonacci(num):
    list=[]
    primero=0
    segundo=1
    cont=0
    while cont<num:
        list.append(primero)
        x=primero+segundo
        primero=segundo
        segundo=x
        cont=cont+1
    return list
print("Los",num,"números de fibonacci son :\n",(fibonacci(num)))