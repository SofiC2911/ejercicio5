# -*- coding: utf-8 -*-
class Alumno:
    __nombre = ''
    __año = 0
    __division = ''
    __cantInasisitencia = 0
    maxInasistencia = 20
    cantClase = 30
    
    def __init__(self,nomb,a,divi,inasist):
        self.__nombre = nomb
        self.__año = a
        self.__division = divi
        self.__cantInasisitencia = inasist
    
    def __str__(self): 
        return ('Nombre: {} \n Año: {} \n Division: {} \n Cantidad de inasistencias: {}'.format(self.__nombre, self.__año, self.__division, self.__cantInasisitencia))
    
    def getNomb(self):
        return self.__nombre
    
    def getInas(self):
        return self.__cantInasisitencia
    
    @classmethod
    def getmaxIna(cls):
        return cls.maxInasistencia
    
    def getA(self):
        return self.__año
    
    def getDi(self):
        return self.__division
    
    @classmethod
    def setMaxIna(cls,cant):
        if type(cant) == int:
            cls.maxInasistencia = cant
        else:
            print('error de tipo de cant')
        