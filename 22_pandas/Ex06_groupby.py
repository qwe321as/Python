#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: user
'''
# Ex06_groupby

import numpy as np
import pandas as pd
from pandas import *

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량','4종교통량','5종교통량','6종교통량','총교통량','Noname']

# 20170201|00|101 |0|1|379|7|7|43|4|1|441|
# 20170201|00|101 |0|2|1000|70|124|78|43|55|1370|
# 20170201|23|101 |1|1|391|22|10|34|8|24|489|

filename = 'capital_area.csv'

myframe = pd.read_table(filename,sep='|',names=mycolumn)
print('myframe:\n',myframe)
print(type(myframe))
print()


# '영업소코드','총교통량','1종교통량'
a = myframe.reindex(columns=['영업소코드','총교통량','1종교통량'])
print('a:\n',a)
print()

b = myframe[['영업소코드','총교통량','1종교통량']]
print('b:\n',b)
print()

mygrouping = myframe.groupby('영업소코드')
print('mygrouping:\n',mygrouping)
print()


result = mygrouping.sum()
print('result(mygrouping.sum()):\n', result)
print()

mygrouping = myframe.groupby('영업소코드')['총교통량']
print('mygrouping:\n',mygrouping)
print()

result = mygrouping.sum()
print('result2:\n', result)
print()


# 집계일자별로 5종교통량합계
grouping = myframe.groupby('집계일자')['5종교통량']
result3 = grouping.sum()
print('result3(mygrouping.sum()):\n',result3)


# 영업소코드==190
result_code = myframe[myframe['영업소코드'] == 190]
print('result_code:\n',result_code)
print()

#           집계일자  집계시  영업소코드  입출구구분코드  ...  5종교통량  6종교통량  총교통량  Noname
# 4      20170201    0    190        0  ...      4      2   149     NaN
# 5      20170201    0    190        0  ...     26     22   463     NaN
# 6      20170201    0    190        1  ...     10      9   200     NaN
# 7      20170201    0    190        1  ...     24     19   567     NaN
# 28     20170201    1    190        0  ...      0      1   115     NaN
# ...         ...  ...    ...      ...  ...    ...    ...   ...     ...
# 15911  20170228   22    190        1  ...     19     71  2006     NaN
# 15924  20170228   23    190        0  ...      4      4   302     NaN
# 15925  20170228   23    190        0  ...     22     47   935     NaN
# 15926  20170228   23    190        1  ...      5     30   362     NaN
# 15927  20170228   23    190        1  ...     21     39  1224     NaN
# 
# [2688 rows x 13 columns]

# 영업소코드==190 & 입출구구분코드==1

# print(myframe['영업소코드']==190)
# print()
# print(myframe['입출구구분코드']==1)

# result5 = myframe[myframe['영업소코드']==190][myframe['입출구구분코드']==1]
# print('result5:\n',result5)

result_code2 = myframe[(myframe['영업소코드'] == 190) & (myframe['입출구구분코드'] == 1)]
print('result_code2:\n',result_code2)
print()
# result_code2:
#             집계일자  집계시  영업소코드  입출구구분코드  ...  5종교통량  6종교통량  총교통량  Noname
# 6      20170201    0    190        1  ...     10      9   200     NaN
# 7      20170201    0    190        1  ...     24     19   567     NaN
# 30     20170201    1    190        1  ...     16     10   171     NaN
# 31     20170201    1    190        1  ...     30     12   430     NaN
# 54     20170201    2    190        1  ...     16      5   100     NaN
# ...         ...  ...    ...      ...  ...    ...    ...   ...     ...
# 15895  20170228   21    190        1  ...     33     82  2714     NaN
# 15910  20170228   22    190        1  ...      7     38   527     NaN
# 15911  20170228   22    190        1  ...     19     71  2006     NaN
# 15926  20170228   23    190        1  ...      5     30   362     NaN
# 15927  20170228   23    190        1  ...     21     39  1224     NaN
# 
# [1344 rows x 13 columns]



print('집계일자별로 총교통량의 합계가 800000이 넘는 레코드:\n')
# 집계일자
# 20170217    811152
# 20170218    800260
# 20170224    831592
# 20170225    828957
# Name: 총교통량, dtype: int64
  
grouping = myframe.groupby('집계일자')['총교통량']
sortSum = grouping.sum()
result6 = sortSum[sortSum>800000]
print(result6)

print('-------------오늘의 과제-------------------')

# df:
#     class  kor  eng
# 0    2반     33   44
# 1    1반     13   24
# 2    3반     34   84
# 3    2반     63   14
# 4    3반     88   77
# 5    1반     88   77

col = ['class','kor','eng']
df = DataFrame([ ['2반',33,44],['1반',13,24], ['3반',34,84],
                ['2반',63,14],['3반',88,77],['1반',88,77] ],
                columns=col)

print('df:\n',df)
print()


# 각 반별로 kor평균(mean)
#  class
# 1반    50.5
# 2반    48.0
# 3반    61.0
# Name: kor, dtype: float64


gb_kor = df.groupby('class')['kor'].mean()
print('gb_kor:\n',gb_kor)
print()

gb_eng = df.groupby('class')['eng'].mean()
print('gb_eng:\n',gb_eng)
print()

# 
# 각 반별로 eng평균(mean)
#  class
# 1반    50.5
# 2반    29.0
# 3반    80.5
# Name: eng, dtype: float64
# 

gb_class = df.groupby('class').mean()
print('gb_class:\n',gb_class)
print()

#          kor   eng
# class            
# 1반             50.5  50.5
# 2반             48.0  29.0
# 3반             61.0  80.5


gb_class = df.groupby('class')['kor','eng'].mean()
print('gb_class:\n',gb_class)
print()
















print('\n'*10)






