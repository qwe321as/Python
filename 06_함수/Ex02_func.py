#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''

def add(a,b=99,c=100):
    return a+b+c

print(add(1))
print(add(1,2))
print(add(1,2,3))
    
def func(*args):
    for i in args:
        print(i,'/',end=' ')
    print('-----')
    
func(1,2)
func(1,2,3,4,5)
func()
    
d = {'b':2,'a':1,'c':3}    

def func2(a,b,c):
    print(a,b,c)
        
    
# func2(d)
func2(*d)    
func2(**d)    
    
x=10  # 전역변수  
def func3():
#     x=20
    global x
    y=99 # 지역변수
    x = x+3
    print('x:',x,'y:',y)

func3()
print('전역변수x:',x)
# print('y:',y)

print('======================')

def func4(x):
    return x**2

print(func4(8))

# lambda 매개변수 : 반환값

a = lambda x : x**2
print(a(8))


b = lambda x,y : x+y
print(b(10,20))    
    
    
    
    
    
    
    
    
    
    
    