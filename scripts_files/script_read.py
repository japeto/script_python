#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para leer un archivo de texto
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""

def read_afile(path=""):
	with open (path) as filetxt:
		for line in filetxt:
			print(line)

if __name__ == "__main__":
	read_afile("file_saved.txt")
