#-*- coding:utf-8
'''
Created on 2020. 10. 20.

@author: user
'''
# Ex01_tuple

# 튜플(tuple):
#     ()로 묶는다.
#     변경이 불가능하다.
    
t = (1,2,3,4,5,6,7,8)
# t = 1,2,3,4,5,6,7,8
# t = (1) # 타입은 int
# t = (1,) #tuple
# t= 1, # tuple

print('t:',t)
print(type(t))
print('len(t):',len(t))
print(t[1])
print(t[-1])

for i in range(len(t)) : # 0,8,1
    print(t[i],end=' ')
print()

# t[1] = 22
# print('t:',t)

x,y,z = 1,2,3
print(x,y,z)

x,y = y,x
print(x,y)


t = (1,2,'hello')
print('t:',t)
print(t[0])
# t[0]=111

a,b,c = t
print(a,b,c)

L = list(t)
print('L:',L)

t2 = tuple(L)
print('t2:',t2)

def calc(a,b):
    return a+b,a-b,a*b

x = calc(30,3)
print(x)
    

q,w,e = calc(40,4)
print(q,w,e)

 




