#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:07:53 2020
@author: japeto
"""

import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
 
    except Error:
        print(Error)
    finally:
        con.close()
 
sql_connection()