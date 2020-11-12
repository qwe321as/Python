#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: user
'''
# Ex05_merge

import numpy as np
import pandas as pd
from pandas import *

df1 = DataFrame([[1001,'윤아'],[1002,'수영'],[1003,'서현'],[1004,'효연'],[1005,'써니']],
               columns=['고객번호','이름'])
print('df1:\n',df1)
print()

#    고객번호  이름
# 0  1001  윤아
# 1  1002  수영
# 2  1003  서현
# 3  1004  효연
# 4  1005  써니

df2 = DataFrame( {'고객번호':[1001,1007,1003,1004,1002,1001],
                  '금액':[10000,20000,15000,5000,100000,30000]
                  }   
                )
print('df2:\n',df2) 
print()


print('pd.merge(df1,df2):\n',pd.merge(df1,df2))
print()

print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='inner'))
print()


print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='outer'))
print()


print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='left'))
print()


print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='right'))
print()


print('-----------------------------------')
df1 = DataFrame({'고객명':['춘향','춘향','몽룡'],
                 '날짜':['2018-01-01','2018-01-02','2018-01-03'],
                 '데이터':[100,200,300]})

df2 = DataFrame({'고객명':['춘향','몽룡','향단'],
                 '데이터':['여자','남자','여자'],
                 '주소':['경기','서울','부산']})

print('df1:\n',df1)
print()

print('df2:\n',df2)
print()

# df1:
#    고객명          날짜      데이터
# 0  춘향  2018-01-01  100
# 1  춘향  2018-01-02  200
# 2  몽룡  2018-01-03  300
# 
# 
# df2:
#    고객명 데이터  주소
# 0  춘향  여자  경기
# 1  몽룡  남자  서울
# 2  향단  여자  부산

# merge1 = pd.merge(df1,df2,how='inner')
merge1 = pd.merge(df1,df2,on='고객명',suffixes=['1','2'],how='inner')
print('merge1:\n',merge1)
print()












print('\n'*10)

