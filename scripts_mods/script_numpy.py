#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:20:25 2020

@author: japeto
"""
import statistics as stc  			## importo la libreria base
import numpy as np 				## importo la libreria  numpy

# =============================================================================
# usar funciones de otro archivo
# =============================================================================
from modulo import  arimetic_mean ## importo la funcion desde un modulo creado por mi
arimetic_mean([1,2,3,4,5])

# =============================================================================
# =============================================================================
# crear vectores y matrices
# =============================================================================
print(np.zeros(12))
print(np.ones((3, 3)))
print(np.ones((3, 3), int))
# =============================================================================
# modificacion de dimensiones y saltos
# =============================================================================
print(np.arange(0,10,2))
A = np.arange(2,28,5)

# =============================================================================
# Operaciones entre vectores
# =============================================================================
lst = [val for val in range(2,6)]
var_no1 = np.asarray(lst)
print(var_no1)
var_no2 = np.asarray(np.arange(0,8,2))
print(var_no2)
print(var_no1 + var_no2)

# =============================================================================
# Gereacion de aleatorios
# =============================================================================
print("Random array {}".format(np.random.rand(5) ) )
m_random = np.random.rand(5, 5)
print(f"Matrix aleatoria {m_random}")

rd_normal = np.random.normal(5, 0.5, 10)
print("Normal D" ,rd_normal)

print("\nDiagonal" ,np.eye(12))

# =============================================================================
# Operaciones algebraicas
# =============================================================================
vec_no1 = np.array([1, 2])
vec_no2 = np.array([4, 5])
print("producto punto")
print(np.dot(vec_no1, vec_no2))

print("producto entre matrices")
mat_no1 = [[1,2],[3,4]]
mat_no2 = [[5,6],[7,8]]
multi_vec = np.matmul(mat_no1, mat_no2 )
print(multi_vec)

















