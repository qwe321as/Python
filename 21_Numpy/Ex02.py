#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
# Ex02.py

import numpy as np

a = np.array([-1,3,2,-6])
b = np.array([3,6,1,2])

print(a.ndim)
print(a.shape)

print('a+b : ' ,a+b)
print('a*b : ' ,a*b)
ab = np.matmul(a,b)
print('ab:',ab)
print()


A = a.reshape([2,2])

print('A:',A)
print(A.ndim)
print(A.shape)
print(type(A))
print()

B = np.reshape(b,[1,4])
print('B:',B)
print(B.ndim)
print(B.shape)
print(type(B))
print()

B = np.transpose(B)
print('B:',B)
print(B.ndim)
print(B.shape)
print(type(B))
print()









