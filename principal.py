# -*- coding: utf-8 -*-
from ClaseManejadorAlum import ManejadorA
from ClaseMenu import Menu

if __name__=='__main__':
    
    alum = ManejadorA() #lista camion
    alum.AgregarAl()
    print(alum)
    
    menu = Menu()
    
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print(" 1 - Ver lista de alumnos que superan la inasistencia permitida")
        print(" 2 - Modificar cantidad maxima de inasistencias")
        print(" 3 - Salir")
        op = int(input(' Ingrese una opcion: '))
        menu.opcion(op,alum)
        if op == 3:
            salir = True