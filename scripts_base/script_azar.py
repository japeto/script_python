#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:57:50 2020
Este script permite la generación de numeros
aleatorios
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""
import random  # se importa la libreria que permite 
#=====================================
# Se debe crear un script que permita verificar
# si un numero es igual a uno que ha sido generado
# de manera aleatoria.
#=====================================
a_number= input("Ingresar un numero positivo: ") # permite ingresar un numero durante la ejecución
if a_number == random.randint(0, 100):    	# valida que el numero sea igual a uno aleatorio
    print("Le pegaste!!!") 							# En el caso donde ambos numeros son iguales imprime este mensaje
else:
    print("No le pegaste :( ")

# Nota: En Python no se utilizan corchetes ({}) para determinar los ambientes.
# El simbolo (:) es un simple que esta compuesto  por un solo simbolo,
# a diferencia de los corchetes

# Nota: No olvidar los espacios o tabulaciones para definir que instrucciones
# hacen parte o no de un ambiente. Ej . La linea numero 17 de este script, 
# posee una tabulacion para determinar que hace parte del if que inicia 
# en la linea numero 16
