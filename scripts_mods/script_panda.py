#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:54:45 2020
Pandas es una biblioteca con fundamento en numpy,
su dato base es el DataFrame
@author: japeto
"""
import numpy as np
import pandas as pd
# =============================================================================
# Crear una serie de manera maual
# =============================================================================
a_list = list('abcedfghijklmnopqrstuvwxyz')
a_arr = np.arange(26)
a_dict = dict(zip(a_list, a_arr))
print(a_dict)
# =============================================================================
# Crea una serie con la libreria pandas
# =============================================================================
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
print(ser)
ser_no2 = pd.Series(np.random.randint(1,10,35))
print(ser_no2)

ser_date = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2020'])
print(ser_date)

df = pd.DataFrame(np.arange(20).reshape(-1,5), 
                        columns=list('abcde'))

print(df)
#df["a"]
# =============================================================================
# Carga de archivo con extension txt
# https://scipy-lectures.org/_downloads/populations.txt
# =============================================================================
data = np.loadtxt('populations.txt')
print(data)
year, hares, lynxes, carr = data.T
print(year)

import matplotlib.pyplot as plt 
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, lynxes, carr)
plt.legend("Hare", "lynx", "Carrot", loc=(1.05, 0.5))













