#-*- coding:utf-8
'''
Created on 2020. 10. 20.

@author: user
'''
# Ex01_dict
# new HashMap<키,값>();

# 사전:
#     {}를 사용한다.
#     {키:값}
#     키로 값을 검색할 때 사용


d = {'one':'hana', 'two':'dul' ,'three':'set'}
print('d:',d)
print(type(d))

print(d['two']) # dul, d[키]
# print(d['ten']) # 에러 
# print(d['dul']) # 에러 

print('one' in d) # True
print('hana' in d) # False

d['three'] = 'sam'
print('d:',d)

d['four'] = 'net'
print('d:',d)

print(d.keys())
print(d.values())
print(d.items())

for i in d :  # d.keys()
    print(i)
print()

for i in d.items():
    print(i)
print()
    
for i in d.items():
    print(i[0], ':',i[1])
print()        
        
for i,j in d.items():
    print(i,j)
print()
          
        
d = dict()   
print('d:',d)     
        
d = dict(one=1, two=2)   
print('d:',d)         
        
d = dict([['one',1],['two',2]])   
print('d:',d)         
        
 
 
 
 
 
 
 
 
 