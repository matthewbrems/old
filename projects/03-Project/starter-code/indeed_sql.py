# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import sqlite3
from pandas.io import sql


indeed_final = compile_files()

conn = sqlite3.connect('/Users/jennydoyle/Desktop/dsi/indeed/indeed_db.sqlite')
connection.text_factory = str

c = conn.cursor()

df.to_sql('salaries',if_exists='replace')
                                   
c.execute(query,conn)
