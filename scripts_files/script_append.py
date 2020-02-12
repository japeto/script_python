#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para agregar contenido un archivo de texto
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""


def append_totxt(path="file_saved.txt"):
	with open(path, "a+") as afile:
		afile.write("Esta es un linea que agrego antes del final")
		afile.write("Esta es un linea que agrego al final ")
		afile.close()

if __name__ == "__main__":
	append_totxt()
