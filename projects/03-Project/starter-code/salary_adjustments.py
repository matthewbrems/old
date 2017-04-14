#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:00:32 2017

@author: jennydoyle
"""




import pandas as pd


def compile_files():
    import glob
    import pandas as pd
    import numpy as np
    indeed_csvs = '/Users/jennydoyle/Desktop/dsi/indeed/'
    files = glob.glob(indeed_csvs + '*.csv')
    print files
    indeed_final = pd.DataFrame(columns=['job','company','location','salary','description'])
    for f in files:
        f = pd.read_csv(f, names=['job','company','location','salary','description'],low_memory=False)
        indeed_final = indeed_final.append(f)
    indeed_final.drop_duplicates(inplace=True)
    indeed = np.array(indeed_final)
    return indeed


indeed_final = compile_files()

df = pd.DataFrame(indeed_final[1:],columns=indeed_final[0])

df['salary_list'] = df.salary.str.split()[df.salary.notnull()]
df['salary_list'] = df.salary.str.split()




df['low_end']= ''
df['high_end']= ''
df['pay_period']=''
df['salary_clean']=''
df['salary_adjusted']=''


df['low_end'][df.salary_list.notnull()&df.salary.str.contains('-')]= [x[0] for x in df.salary_list[df.salary_list.notnull()&df.salary.str.contains('-')]]

df['high_end'][df.salary_list.notnull()&df.salary.str.contains('-')]= [x[2] for x in df.salary_list[df.salary_list.notnull()&df.salary.str.contains('-')]]

df['pay_period'][df.salary.notnull()&df.salary.str.contains('a year')]='1'
df['pay_period'][df.salary.notnull()&df.salary.str.contains('a month')]='12'
df['pay_period'][df.salary.notnull()&df.salary.str.contains(' hour')]='2080'


def numbers_commas_to_int(string):
    import locale # given a string of a number with commas, convert to float
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for american comma notation
    # if european comma notation needed, change 2nd parameter to 'fr_FR'
    num = int(locale.atof(string))
    return int(num)


df['salary_clean'][df.salary.notnull()]= [x[0].strip('$') for x in df.salary_list[df.salary_list.notnull()]]


import numpy as np
df.salary_clean[df.salary_clean=='']=np.NaN
df.pay_period[df.pay_period=='']=np.NaN
df.high_end[df.high_end=='']=np.NaN
df.low_end[df.low_end=='']=np.NaN



df['salary_clean'][df.salary_clean.notnull()]=[numbers_commas_to_int(x) for x in df.salary_clean[df.salary_clean.notnull()]]

df['pay_period']=df.pay_period.astype(float)


for i,j in df[['pay_period','salary_clean']][df.salary_clean.notnull() & df.pay_period.notnull()]:
    df['salary_adjusted']=i*j

df['salary_adjusted'][df.salary_clean.notnull() & df.pay_period.notnull()]=map(df.pay_period*df.salary_clean)
  
