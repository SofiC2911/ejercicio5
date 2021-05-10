# -*- coding: utf-8 -*-
#from ClaseManejadorAlum import ManejadorA
from ClaseAlumno import Alumno

class Menu:
    __switcher = None
    
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.salir,
                           }
        
    def getSwitcher(self):
        return self.__switcher
    
    def salir(self,al):
        print('Salir del menu')
        
    def opcion(self,op,al):
        if type(op) == int:
            func = self.__switcher.get(op, lambda: print("Opción no válida"))
            func(al)
        else:
            print('error de tipo de op')
    
    def opcion1(self,al):
        a = input('Ingrese año: ')
        di = input('Ingrese division:')
        al.mostrar(a,di)
        
        
    def opcion2(self,al):
        cant = int(input('Ingrese cantidad maxima a modificar para instancias: '))
        Alumno.setMaxIna(cant)
        print('nueva cantidad max: ',Alumno.getmaxIna())