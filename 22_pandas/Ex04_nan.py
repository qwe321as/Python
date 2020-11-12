#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: user
'''
import numpy as np
from pandas import *
import pandas as pd

df = DataFrame([[3,5,1],[9,2]],
               index=['apple','banana'],
               columns=['kim','park','jung'])

print('df:\n',df)
print()

df = DataFrame([[3,np.NaN,1],[9,2]],
               index=['apple','banana'],
               columns=['kim','park','jung'])

print('df:\n',df)
print()

filename = 'mynan.csv'
table = pd.read_csv(filename,encoding='euc-kr',
                    index_col=0) 
print('table:\n',table)
print(type(table))
print(table.size)

print(table.isna())
print()

print(pd.isna(table))
print()

print(table.notnull())
print()

table2 = table.dropna()
print('table2:\n', table2)
print()

table2 = table.dropna(how='any')
print('table2(any):\n', table2)
print()

table2 = table.dropna(how='all')
print('table2(all):\n', table2)
print()

table = table.fillna({'kor':20,'eng':90})
print('table:\n',table)  



filename="mynan2.csv"
table.to_csv(filename,encoding='euc-kr')






print('\n' * 10)

