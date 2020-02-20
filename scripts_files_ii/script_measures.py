#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""
import os
import pandas as pd
import numpy as np
from numpy import genfromtxt

data = {'Name':['James','Paul','Richards','Marciana','Samantha','Ravi','Raghu','Richards','George','Ema','Samantha','Catherine'],
       'State':['Alaska','California','Texas','North Carolina','California','Texas','Alaska','Texas','North Carolina','Alaska','California','Texas']}
 
dataframe=pd.DataFrame(data, columns=['Name', 'State', "Age"])

print( "Conjunto de datos\n")
print( dataframe )
print( "Cuantas personas hay por estado \n")
print( dataframe.State.value_counts() )

os.chdir("/Users/macbookpro/Documents/Academia/ejercicios/script_python/scripts_files_ii")
ages = genfromtxt("age_users.csv", delimiter=";", dtype=int)
ages = ages.T

dataframe['Age'] = ages[1][1:13]
sp=pd.cut(x=dataframe['Age'], bins=[20, 29, 39, 49, 59, 69, 79])
sp.unique()
