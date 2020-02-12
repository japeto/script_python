#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:52:39 2020
En Python se pueden definir funciones que pueden 
ser utilizadas en otros scripts.
- Un modulo en Python contiene definiciones de funcione
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""
a_variable = 12
result = 23
#==========================================
# Esta funcion permite calcular el promedio de una lista
# de datos numericos
# tiene un valor por defecto.
#==========================================
def arimetic_mean(numbers=[0,0,0]):    # Note que es necesario el simbolo (:)
    """
    @param numbers a list of real numbers
    @return mean
    """
    result = sum(numbers) / len(numbers) 	# Se crea una variable denominada result, 
																# no es igual que la variable de la linea numero 11 de este script
    return result    ## Esta variable es la que se asigno en la linea numero 22, a pesar de tener el mismo nombre.

arimetic_mean()							# Llamado a la funcion sin parametros
arimetic_mean([1,3,4,2,5,6,12])	# Lamado a la funcion con parametros

# Nota: el valor por defecto me evita errores, en el llamado de la linea 26 de este script
# sum([0,0,0]) = 0, mientras que len([0,0,0]) = 3. El resultado sera 0/3.

# Nota: 

