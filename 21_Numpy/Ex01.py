#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
# Ex01.py
import numpy as np

a=100
print('a:',a)
print(type(a))
print()

arr1 = [1,2,3,4]
print('arr1:',arr1)
print(type(arr1))
print(len(arr1))
print(arr1[2])
# print('arr1.ndim:',arr1.ndim)
# print('arr1.shape:',arr1.shape)
print()

arr2 = [[1,2,3,4],[5,6,7,8]]
print('arr2:',arr2)
print(type(arr2))
print(len(arr2))
print(arr2[0][2])
print()

# np.array() : 
# ()안에 숫자,리스트,튜플을 인자로 넣어서 배열로 바꾸는 함수

b = np.array(200)
print('b:',b)
print(type(b))
print('b.ndim:',b.ndim) # 차원 
print('b.shape:',b.shape)
print()


c = np.array([1,2,3])
print('c:',c)
print(type(c))
print('c.ndim:',c.ndim) # 차원 
print('c.shape:',c.shape)
print()


d = np.array([[1,2,3,4],[5,6,7,8]])
print('d:',d)
print(type(d))
print('d.ndim:',d.ndim) # 차원 
print('d.shape:',d.shape)
print(d[1][3])
ds = d.shape
print('ds:',ds)
print(ds[0])
print(ds[1])
for i in range(ds[0]) : #0,1
    for j in range(d.shape[1]) : #0,1,2,3
        print(d[i][j],end='\t')
    print()
print()









print('\n\n\n\n\n\n\n')

