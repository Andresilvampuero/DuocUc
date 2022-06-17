print("======== LEAGUE OF LEGENDS ========")
while True:
    print("[ 1 ] Numero Primo")
    print("[ 2 ] Factorial")
    print("[ 3 ] Palíndrome")
    print("[ 4 ] Salir del Programa")
    print("===================================")
    try:
        selec=int(input("Seleccione una opción\n"))
        if selec>0 and selec<5:
            if selec==1:
                while True:
                    print("\nSeleccionó la opción 'Numero Primo'\n")
                    try:
                        np=int(input("Escriba un número para saber si es primo [ 1 - 15 ]\n"))
                        if np>0 and np<16:
                            def numero_primo(np):
                                for n in range(2,np):
                                    if np % n == 0 :
                                        return'no'
                                return 'si'
                            x=numero_primo(np)
                            if x=='si':
                                print(np," sí es un número primO")
                            if x=='no':
                                print(np," no es un número primo")
                            break
                        else:
                            print("Indique un número dentro de los parámetros")
                    except ValueError:
                        print("ERROR, escriba un numero válido")
            if selec==2:
                while True:
                    print("\nSeleccionó la opción 'Factorial'\n")
                    try:
                        fact=int(input("Escriba un número para saber su factorial [ 3 - 10 ]\n"))
                        def factorial(fact):
                            cont = 1
                            while(fact > 1): 
                                cont =cont* fact 
                                fact=fact-1
                            return cont
                        print("La factorial de ", fact," es ", factorial(fact))
                        break
                    except ValueError:
                        print("ERROR, escriba un numero válido")
            if selec==3:
                while True:
                    print("Seleccionó la opción 'Palíndrome'")  
                    try:
                        pal=str(input("Escriba una palabra para saber si se escribe igual al revés ( palíndrome )\n"))      
                        def palindrome(pal):
                            alreves=''.join(reversed(pal))
                            if pal==alreves:
                                return 'si'
                            if pal!=alreves:
                                return 'no'
                        if palindrome(pal)=='si':
                            print("La palabra",pal,"sí es una palabra palíndrome")
                        elif palindrome(pal)=='no':
                            print("La palabra ",pal," no es una palabra palíndrome")
                        break
                    except ValueError:
                        print("ERROR, escriba un numero válido")
            if selec==4:
                print("Seleccionó salir del programa")
                print("====== ADIOS ======")
                break
        else:
            print("Opción inválida. Inténtelo nuevamente")
    except ValueError:
        print("Ingresó un caracter. Inténtelo nuevamente.")