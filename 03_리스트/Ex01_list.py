#-*- coding:utf-8
'''
Created on 2020. 10. 20.

@author: user
'''
# Ex01_list
from audioop import reverse

# 리스트 :
# []로 묶는다.
# 변경이 가능하다.

L = [1,2,3]
print('L:', L)
print(L[0])
print(L[1])
print(L[-1])
# print(L[3])
print('len(L):',len(L))

for i in range(3): # range(0,3,1), range(0,3)
    print(i,end=' ')
print()

for i in range(len(L)): # range(0,3,1)
    print(L[i],end=' ')    
print()

print(L[1:3]) # 1~2번방
print(L[1:]) #1~끝
print(L[:2])

L[1] = 22
print('L:',L)


L2=['apple','banana',100,200]
print('L2:',L2)

L2[1:1] = [9]
print('L2:',L2)

L2[2:4] = [1,2,3,4,5]
print('L2:',L2)

del(L2[1])
print('L2:',L2)

print(type(L2))

L2.append(11)
print('L2:',L2)

L2.insert(2,22)
print('L2:',L2)

print(L2.index(3))
L2.remove(3)
print('L2:',L2)

L2.insert(3,'orange')
print('L2:',L2)


# L2.sort()

L3 = ['banana','orange','apple','grape']
L3.sort(reverse=True)
print('L3:',L3)

L4=['123','34','56','2345']
L4.sort()
print('L4:',L4)

L4.sort(key=int)
print('L4:',L4)






print('\n\n\n\n\n\n\n\n')









