#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:41:07 2020

@author: japeto
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# Creo las variables
# =============================================================================
mes_num=[1,2,3,4,5]
chevrolet = [50,40,70,32,89]
bmw = [34,23,12,10,18]
benz = [45,30,20,16,10]
honda = [30,43,56,98,45]
hyundai = [30,18,20,56,10]
plt.figure()
plt.plot(mes_num, chevrolet, label="chevrolet", 
         linewidth=5, color = "#FF883233")
plt.plot(mes_num, bmw, label="BMW",
         linewidth=5)
plt.plot(mes_num, benz, label="M.Benz",
         linewidth=5)
plt.plot(mes_num, honda, label="Honda",
         linewidth=5)
plt.plot(mes_num, hyundai, label="Hiunday",
         linewidth=5)

plt.title("Cantidad vehiculos vs. Mes")
plt.ylabel("Cantidad vehiculos")
plt.xlabel("Numero de Mes")
plt.legend()











