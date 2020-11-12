#-*- coding:utf-8
'''
Created on 2020. 10. 22.

@author: user
'''
# Ex02.py

import numpy as np
import pandas as pd

arr = np.array([[1,2,3],[4,5,6]])
print('arr:\n',arr)
print('차원:',arr.ndim)
print(arr.shape)
print(arr[1][2])
print()

# DataFrame :
#     2차원 형태의 표(행/열) 구조를 가지는 자료구조
#        열 1개가 하나의 Series 구조이다.
    
df = pd.DataFrame([[1,2,3],[4,5,6]])
print('df:\n',df)
print(type(df))
print(df.ndim)
print(df.shape)
print(df[2][1]) # df[칼럼명][index]
print()

my_dict = {'a':['1','3'], 'b':['4','7'], 'c':['2','5'] } # 키:값
df2 = pd.DataFrame(my_dict)
print('df2:\n',df2)
print()

my_dict = {'도시':['서울','부산','대구','부산','서울'],
           'year' : [2000,2001,2002,2002,2001],
           'pop' : [1.5, 1.7, 1.2, 1.8, 2.3]    
           }

df3 = pd.DataFrame(my_dict)
print('df3:\n',df3)
print()
print(df3['pop'][2])
print(df3['도시'])
print()

print(df3.year)
print()
print(df3[['도시','year']])
print()

df3['income'] = 12.34
print('df3:\n',df3)
print()

df3['income'] = [11,12,13,14,15]
print('df3:\n',df3)
print()

myseries = pd.Series([1.1, 2.2, 3.3,4.4,5.5], 
    index=['one','two','three','four','five'])

print('myseries:\n', myseries)


myindex = ['one','two','three','four','five']
df3 = pd.DataFrame(my_dict,index=myindex)
print('df3:\n',df3)
print()

df3['pop'] = myseries
print('df3:\n',df3)
print()













print("\n\n\n\n\n\n\n")

