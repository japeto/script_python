#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: japeto <jefferson.amado.pena@correounivalle.edu.co>
"""

import pandas as pd
import numpy as np
 
data = {'Name':['James','Paul','Richards','Marico','Samantha','Ravi','Raghu','Richards','George','Ema','Samantha','Catherine'],
       'State':['Alaska','California','Texas','North Carolina','California','Texas','Alaska','Texas','North Carolina','Alaska','California','Texas']}
 
df1=pd.DataFrame(data, columns=['Name','State'])
 
print(df1)
df1.State.value_counts()
