#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear un archivo de texto
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""

def save_file(path="", lines=[]):
	"""
	Allow create with lines in the path
	params
	---------
	path - path to file
	lines - array with file contents
	return
	--------
	true  if ok
	"""
	myfile = open(path, "w+") #crear archivo
	for line in lines:   # ciclo para contar lineas en el archivo
		myfile.write(line) # linea en el archivo
	myfile.close() # cierro el archivo
	return True

if __name__ == "__main__":
	save_file("test.txt", ["this is a inside line"])
