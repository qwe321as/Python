#-*- coding:utf-8
'''
Created on 2020. 10. 20.

@author: user
'''
# Ex01_if.py

su = 10
if su % 2 == 0 :
    print("짝수")
else  :
    print("홀수")
       
# else if => elif

# jumsu 입력
# >=90 A학점
# 80점대 B학점
# 70점대 C학점 
# 60점대 D학점
# 60점 미만 F학점

jumsu = int(input('점수:'))

if jumsu>=90 :
    print('A학점')
    print('*****')
elif jumsu>=80 :
    print('B학점')
elif jumsu>=70 :
    print('C학점')
elif jumsu>=60 :
    print('D학점')
else :
    print('F학점')
    
     








  
  
  
  
  
  
  
  
    