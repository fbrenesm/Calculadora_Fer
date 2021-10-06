def Opciones():

    print """************

Opciones del programa

Que desea realizar?

1) Calculos Aritmeticos
2) Verificacion de numeros Primos
3) Verificacion de numeros Palindromos
4) Salir """


def Operaciones():

    print """************

Que desea realizar?

1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir """

def Calculadora():
    Operaciones()
    opcion = int(input("Selecione Opcion\n"))
    while (opcion >0 and opcion <5):
        numero1 = int(input("Ingrese Numero\n"))
        numero2 = int(input("Ingrese Otro Numero\n"))
        if (opcion==1):
            print "El resultado de la Suma es:", numero1+numero2, "\n"

            Escoger()
            opcion = int(input("Selecione Opcion\n"))

        elif(opcion==2):
            print "El resultado de la Resta es:",numero1-numero2, "\n"
            Escoger()
            opcion = int(input("Selecione Opcion\n"))

        elif(opcion==3):
            print "El resultado de la Multiplicacion es:",numero1*numero2, "\n"
            Escoger()
            opcion = int(input("Selecione Opcion\n"))
            
        elif(opcion==4):
            try:
              print "El resultado de la Division es:", numero1/numero2, "\n"
              opcion = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print "No se Permite la Division Entre 0"
              Escoger()
              opcion = int(input("Selecione Opcion\n"))

def Primos():

    numeroaverificar = int(input("Ingrese Numero\n"))
    esprimo=True

    for i in range(2,numeroaverificar):
            if numeroaverificar % i == 0:
                esprimo=False
                break
    if esprimo:
        print "El numero", numeroaverificar, "es primo"  
    else:
        print "El numero", numeroaverificar, "No es primo"  
    Escoger()
    opcion = int(input("Selecione Opcion\n"))

def Palindromos():
    minumero = int(raw_input("Ingrese un numero "))
    if str(minumero)==str(minumero)[::-1]:
      print "Es un palindromo"
    else:
      print "No es un Palindromo" 
              
    Escoger()
    opcion = int(input("Selecione Opcion\n"))

def Escoger():

    Opciones()

    seleccion = int(input("Selecione una Opcion\n"))

    while (seleccion >0 and seleccion <4):

        if (seleccion==1):
            Calculadora()
        elif(seleccion==2):
            Primos()
        elif(seleccion==3):  
            Palindromos()


Escoger()              