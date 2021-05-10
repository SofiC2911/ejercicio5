# -*- coding: utf-8 -*-
import csv
from ClaseAlumno import Alumno

class ManejadorA:
    __listaAlum = []

    def __init__(self): #inicializa la lista
        self.__listaAlum = []
        
    def __str__(self): #mustra por pantalla a la lista
        s = ""
        for ObjAlum in self.__listaAlum:
            s += str(ObjAlum) + '\n'
        return s
    
    def AgregarAl(self):  #carga la lista con el archivo
        archivo = open('Alumnos.csv')
        reader = csv.reader(archivo,delimiter=';')
        
        bandera = True
        for i in reader:
            if bandera:
                bandera = not bandera
            else:
                nombre = i[0]
                a = i[1]
                division = i[2]
                cantI = int(i[3])
                unAlum = Alumno(nombre,a,division,cantI)
                self.__listaAlum.append(unAlum)
        archivo.close()
        
    def mostrar(self,a,di):
        print('\n %15s %23s' % ('ALUMNO','PORCENTAJE'))
        for ObjAlum in self.__listaAlum:
            if((ObjAlum.getA()) == a) and (ObjAlum.getDi() == di.upper()):
                porce = (ObjAlum.getInas() * 100)/ObjAlum.getmaxIna()
                
                if porce > 100:
                    print(' {}      {}%'.format(ObjAlum.getNomb(),porce))
    
    