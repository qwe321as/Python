#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''
try:
    a = int(input("숫자1:"))
    b = int(input("숫자2:"))
    
except ValueError:
    print('값이 적절하지 않습니다.')

else:
    print('a+b=',a+b)
    
print('-' * 20)


# 없으면 : 화일 발견 못함
# 있으면 : 그 화일의 내용을 읽어서 출력

try:
    f = open('a.txt','r') # ,encoding='UTF-8'
    
except FileNotFoundError:
    print('화일 발견 못함')

else :
    print(f.read())
    
finally:
    f.close()
    
print('*' * 20)


try:
    a = int(input("숫자1:"))
    b = int(input("숫자2:"))
    
    if a<0 or b<0 :
        raise ArithmeticError('음수입력함')
    else:
        print('두 수 모두 양수 입력됨')
    
except ArithmeticError as err :
    print('예외발생:' ,err)











    
