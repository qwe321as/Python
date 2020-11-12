#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''

x=4
y=2
L = [1,2,3]

try:
    print(x/y)
    print(L[1])
    a = 1 + 2
    
except ZeroDivisionError as err:
    print('ZeroDivisionError:',err)

except IndexError as err :
    print('IndexError:',err)
    
except :
    print('그 밖의 에러 처리')

else :
    print('else')
    
finally:
    print('finally')
           
print('예외처리 공부하는 중..')    
    
# docs.python.org










    
    
    
    
    