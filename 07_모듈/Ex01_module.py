#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
# Ex01_module.py

def sum(a,b) :
    return a+b

def safe_sum(a,b):
    if type(a) != type(b) :
        print('타입이 달라서 덧셈 불가능') 
    else :
        return a+b    
    
if __name__ =="__main__" :    
    print(sum(2,3))
    print(safe_sum(10,20))    
    print(safe_sum('apple','banana'))    
    print(safe_sum('apple',20))

    







