#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
# Ex03

import numpy as np

a = range(5) # range(0,5), range(0,5,1)
print('a:', a)

for i in a:
    print(i, end=' ')
print()
    
b = np.arange(5) # 0,5,1
print('b:', b)
print(type(b))
print()

for i in b:
    print(i, end=' ')
print()

b = np.arange(5,10) # 5,10,1
print('b:', b)


b = np.arange(5,10,2) 
print('b:', b)

c = np.arange(6).reshape([2,3])
print('c:', c)
print('c.ndim:',c.ndim)
print('c.shape:', c.shape)






