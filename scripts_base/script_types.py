#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:20:25 2020
Python posee un numero amplio pero limitado de tipos de datos,
al ser orientado a objetos se pueden crear nuevos, pero los basicos
son descritos en este script
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""

import numpy as np
# ===================================
# Listas
# ===================================
lista_no1 = list()			# Lista vacia
lista_no1.append(1)  	## adiciona un elemento
print(type(lista_no1))	## imprimo el tipo de dato de la variable

lista_no2 = []				# Lista vacia
print(type(lista_no2))	## imprimo el tipo de dato de la variable

# Nota: Las listas no son para hacer operaciones matematicas,
# la idea es almacenar otros tipos de datos, se espera que una lista
# todos los datos sean del mismo tipo.

# ===================================
# Tuplas
# ===================================
atuple = ()						#Creo una tupla
atuple = (3, 2, 4, 5)		#Creo una tupla
atuple = (3, 2)				#Creo una tupla, note que se reescribe la variable
print(atuple[0])				# primera posicion de la tupla
print(atuple[1])				# segunda posicion
# atuple[0]=100			# remueva el comentario,  elimine el simbolo (#)
									# al modificar generar un error
print(atuple[0])				# primera posicion de la tupla
print(type(atuple)) 		## imprimo el tipo de dato de la variable

# Nota: las tuplas son tipos de datos no-mutables, 
# no se pueden alterar una vez se crean

# ===================================
# Numericos
# ===================================
integer = int(3)					# Numero entero, 3
integer = 3						# De manera simple
print(type(integer))			## Imprime el tipo de dato

flotante = float(3)				# Flotante
flotante_np = 1.				# Flotante pero desde numpy
print(type(flotante))			## Imprime el tipo de dato
print(type(flotante_np))	## Imprime el tipo de dato

complejo_no1 = complex(3,4) 	# numero complejo
complejo_no2 = 3+4j				# numero complejo
print(type(complejo_no1)) 	## Imprime el tipo de dato
print(type(complejo_no2)) 	## Imprime el tipo de dato

vector = np.array([2., 2.]) 		# numero vectores
result = vector*vector			# Con numpy puedo hacer operaciones entre vectores
print(type(vector))				## Imprime el tipo de dato

# ===================================
# Cadenas de texto
# ===================================
string= ""								# Una cadena es una secuencia de caracterres
string = str()							# Una cadena es una secuencia de caracterres
print(type(string))					## Imprime el tipo de dato

# ===================================
# Diccionarios
# ===================================
dictionary =dict()					# Es un tipo de dato base para otros tipos de datos.
dictionary["key"] = 10			# clave "key" un string, valor 10
dictionary["lista"] = [1,2,3] 	# puedo almacenar distintos tipos de datos
print(dictionary)					## Imprime el diccionario, note que es un JSON
print(type(dictionary))			## Imprime el tipo de dato
