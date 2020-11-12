#-*- coding:utf-8
'''
Created on 2020. 10. 29.

@author: user
'''
L=[ ['a','b'],[1,2,3] ]
print('L:',L)
print(L[0][0] )
print(L[1][2])

print('len(L):',len(L)) # 행의 갯수
print(len(L[0])) #0행의 열의 갯수
print(len(L[1])) #1행의 열의 갯수

# a b 
# 1 2 3 

for L2 in L :
    print(L2)

print()


for L2 in L :
    for L3 in L2:
        print(L3,end=' ')
    print()

print()

print('-----')

for i in range(len(L)): # range(2)==range(0,2,1)
    for j in range(0,len(L[i])):
        print(L[i][j],end=' ')
    print()
# 00 01
# 10 11 12   
 
print('******')  
    
L = [1,['a',['x','y','z'],'b','c'],7]

print(L[0])
print(L[1])
print(L[1][1])
print(L[1][1][2])
    
# 1~10수

L2 = [i*i for i in range(1,11,1)]    
print('L2:',L2)   
    
L3 = [32,5,12,89,34]
print('합계:',sum(L3))    
print('최대:',max(L3))    
print('최소:',min(L3))    
    

    
    
        
        
print('\n'*10)        
        
        
        
        
        
        
        
        
        
        




