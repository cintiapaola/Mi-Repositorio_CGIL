#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lenovo
#
# Created:     17/09/2022
# Copyright:   (c) lenovo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #Ejercicio n°3 - Utilizando el input mas "f" para que me traiga la variable que se encuentra entre "llaves"
    Nombre = (input ("ingrese su Nombre: "))
    DNI = (input ("Ingrese su DNI: "))
    print (f"El Nombre del Usuario es {Nombre} y su DNI es {DNI}")

    #Ejercicio n°3 - ídem anterior pero sin utilizar "f"
    Nombre = (input ("ingrese su Nombre: "))
    DNI = (input ("Ingrese su DNI: "))
    print ("El Nombre del Usuario es " + Nombre + " y su DNI es " + DNI)







if __name__ == '__main__':
    main()

