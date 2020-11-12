#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
# Ex03_module

# from math import factorial
# n = factorial(5) # 5!
# print('n:',n) # 120

import math
n = math.factorial(5) 
print('n:',n)

# random 모듈
# import random
# r = random.random() # 0<= x < 1
# print('r:',r)

from random import *
r = random()
print('r:',r)

r2 = randint(1,10) # 1 <=x < 10
print('r2:',r2)

from datetime import *

now = datetime.now()
print('now:',now)
print(now.year)
print(now.hour)









