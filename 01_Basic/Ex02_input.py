#-*- coding:utf-8
'''
Created on 2020. 10. 20.

@author: user
'''
print('입력 1: ',end='')
su1 = input()
print('su1=' , su1)

su2 = int(input('입력2:')) # float() float('12.3') 
print('su2=',su2)

sum = int(su1) + su2 # '11'+'22'=>1122
# 11 더하기 22는 33입니다.
print(su1 , "더하기" , su2 ,'는',sum,"입니다.")
print('{} 더하기 {}는 {}입니다.'.format(su1,su2,sum)  )
# "apple".toUpper()
print('{a} 더하기 {c}는 {b}입니다.'.format(a=su1,b=su2,c=sum)  )














