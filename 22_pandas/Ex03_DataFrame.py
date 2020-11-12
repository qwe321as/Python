#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: user
'''
# Ex03_DataFrame


import pandas as pd
from pandas import *
import numpy as np

frame = DataFrame(np.arange(9).reshape((3,3)), 
           index=['박보검','이영자','유재석'],
           columns=['서울','부산','광주']  )

print('frame:\n',frame)


# frame:
#         서울  부산  광주
# 박보검   0   1   2
# 이영자   3   4   5
# 유재석   6   7   8


frame = frame.reindex(index=['박보검','아이유','이영자','유재석'])
print('reindex:\n',frame)
print()

states = ['서울','부산','울산']
frame = frame.reindex(columns=states)
print('reindex:\n',frame)
print()

print('---------------1-------------------')

# myframe:
#         서울  부산  광주  대구
# one     0   1   2   3
# two     4   5   6   7
# three   8   9  10  11
# four   12  13  14  15


myframe = DataFrame(np.arange(16).reshape((4,4)), 
           index=['one','two','three','four'],
           columns=['서울','부산','광주','대구']  )

print('myframe:\n',myframe)
print()

myframe2 = myframe.drop(['two','three'],axis=0) # ,axis=0 생략 가능 
print('myframe2:\n',myframe2)
print()

myframe2 = myframe.reindex(index=['one','four'])
print('myframe2:\n',myframe2)
print()

print('---')

myframe3 = myframe.drop(['부산'],axis=1)
print('myframe3:\n',myframe3)
print()

myframe3 = myframe.reindex(columns=['서울','광주','대구'])
print('myframe3:\n',myframe3)
print()


# one three 부산 광주
myframe6 = myframe.reindex(index=['one','three'],columns=['부산','광주'])
print("myframe6:\n",myframe6)
print()



print('---------------2-------------------')

s= Series(['A','B','C','D','E','F','G',],
          index=[50,49,48,47,2,3,4])
print('s:\n',s)
print()

print(s.loc[3]) # F
print(s.iloc[3])

print(s.loc[48])
# print(s.iloc[48])
print()

print(s.loc[:3])
print()
print(s.iloc[:3])
print()

print('---')
print('myframe:\n',myframe)
print()

myframe2 = myframe.loc['two']
print('1:\n',myframe2)
print(type(myframe2))
print()


myframe2 = myframe.loc[['two']]
print('2:\n',myframe2)
print(type(myframe2))
print()


myframe2 = myframe.loc[['two','three']]
print('3:\n',myframe2)
print(type(myframe2))
print()


myframe2 = myframe.reindex(index=['two','three'])
print('4:\n',myframe2)
print(type(myframe2))
print()

print(myframe['서울']['two'])
# print(myframe['two']['서울']) # 에러
# myframe4 = myframe.reindex(index=['two'],columns=['서울'])
# print(myframe4)


print(myframe.loc['two']['서울'])
# print(myframe.loc['서울']['two']) # 에러

print(myframe.loc[['two'],['서울']])


#         서울  광주
# two     4   6
# three   8  10

myframe2 = myframe.loc[['two','three'],['서울','광주']]
print('myframe2:\n',myframe2)
print()

print(myframe['부산'])
print()

print(myframe['부산']>5)
print()

print(myframe[myframe['부산']>5])
print()


print('---------------3-------------------')

df = DataFrame([[4,9]] * 3,columns=['A','B'])
print('df:\n',df)

#     A  B
# 0  4  9
# 1  4  9
# 2  4  9

# apply : 데이터프레임에 행 또는 열을 기준으로 특정 함수를 적용시키는 기능

df1 = df.apply(np.sqrt)
print('df1:\n',df1)
print()

df2 = np.sqrt(df)
print('df2:\n',df2)
print()

print('np.sum(df):\n',np.sum(df))
print()

print('np.sum(df,axis=0):\n',np.sum(df,axis=0))
print()

print('np.sum(df,axis="index"):\n',np.sum(df,axis='index'))
print()


print('np.sum(df,axis=1):\n',np.sum(df,axis=1))
print()

print('np.sum(df,axis="columns"):\n',np.sum(df,axis='columns'))
print()

df2 = df.apply(np.sum,axis=0)
print('df2:\n',df2)
print()

df2 = df.apply(np.sum,axis='index')
print('df2:\n',df2)
print()

print('myframe:\n',myframe)
print()

myframe1 = myframe.apply(np.max,axis=1)
print(myframe1)
print()

myframe2 = myframe.apply(np.max,axis=0)
print(myframe2)
print()


# one       3
# two       7
# three    11
# four     15
# 
# 
# 서울    12
# 부산    13
# 광주    14
# 대구    15


print('myframe:\n',myframe)
print()

print('1:\n',myframe.sort_index()) # axis=0,ascending=True 
print()

print('2:\n',myframe.sort_index(axis=0))
print()

print('3:\n',myframe.sort_index(axis=1))
print()

print('4:\n',myframe.sort_index(axis='columns'))
print()

print('5:\n',myframe.sort_index(axis='columns',ascending=False))
print()

frame = DataFrame([[20,-80,40],[-70,30,40],[70,90,-10]],  
           index=['박보검','이영자','유재석'],
           columns=['국어','영어','수학']  )

print('frame:\n',frame)
print()

frame = np.abs(frame)
print('frame:\n',frame)
print()

print('6:\n',frame.sort_values(by='수학'))
print()

print('7:\n',frame.sort_values(by=['수학','영어']))
print()

print('8:\n',frame.sort_values(by=['수학','영어'], ascending=[True,False]))
print()


frame1 = frame.apply(np.sum,axis=1)
print(frame1)
print()

# 과목별 최고점수
frame2 = frame.apply(np.max)
print(frame2)





print('\n'*10)














