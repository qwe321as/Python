#-*- coding:utf-8
'''
Created on 2020. 10. 20.

@author: user
'''
# Ex02_for

# for 변수 in 반복할대상 :
#     반복문장

print(range(1,10,2))

for i in range(1,10,2) :
    print(i,end=' ')
print()    

for i in range(1,6) :
    print(i,end=' ')
print()

# 10~1 출력
sum = 0
for i in range(10,0,-1) :
    print(i,end=' ')
    sum += i
print()    
print('합계 :',sum)

# 이중 for문
# 1 6
# 1 7
# 1 8
# ###
# 2 6
# 2 7
# 2 8
# ###
# 3 6
# 3 7
# 3 8
# ###
# ===============

for i in range(1,4) :
    for j in range(6,9) : 
        print(i,j)
    print('###')
print('=========')


# 1~10사이의 수
even = 0
odd = 0
for i in range(1,11) :
    if i%2==0:
        even = even + i
    else :
        odd += i 
    
print('홀수합:',odd)
print('짝수합:',even)

print('----------')

for i in range(2,10):
    print('***',i,'단***')
    for j in range(1,10):
        print(i,'*',j,'=',i*j)
    print('------------')













