#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:25:47 2020
Otro tipo de dato son las listas, este script
permite hacer uso de este tipo de dato
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""
# No es necesario importar ninguna libreria, las listas
# son tipos de la base del lenguaje.

numeros = []  			# Forma basica de crear una lista vacia
numeros = list()   		# Otra forma de crea una lista vacia. Note que la variable se reescribe.

print("="*60)							#  Mensajes de fina coqueteria
print("Este algoritmo permite hallar el maximo y el minimo, ")
print("de 10 numeros que ingrese.")
print("="*60)

for position in range(0, 10):  
	## El bloque de control for, note los (:) y el espacio al incio de esta linea
    print ("Ingrese un numero positivo %d " % position)  # impresion del mensaje para captura de datos
    numeros.append( int(input("")) )			# adiciono datos a  una lista vacia
    
print(numeros)									# Se imprime la lista
print("el mayor es: ", max(numeros))	# Imprime cual es el mayor de la lista
print("el menor es: ", min(numeros))	# Imprime cual es el menor de la lista

# Nota: las funciones como list, max, min, input estan en la base del lenguaje.
# Nota: input retorna una cadena de texto, con int se asegura que sea un entero.

# Nota: las listas de Python indexan desde 0, a diferencia de los vectores de R


