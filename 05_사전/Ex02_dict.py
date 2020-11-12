#-*- coding:utf-8
'''
Created on 2020. 10. 29.

@author: user
'''
d = {}  # 철수:50, 영희:70, 용승:100 이름=''이면 break
total = 0
while True : 
    name = input('이름:')
    if name == '':
        break
    jumsu = int(input('점수:'))
    total += jumsu
    d[name]=jumsu
    
print('d:',d)
print('total:',total)

# print(d['bb'])
print(d.get('bb')) # None


searchName = input('찾는 이름 입력:')
# aa의 점수는 33입니다.
# bb는 없는 이름입니다.

if d.get(searchName) == None :
    print(searchName,"은 없는 이름입니다.")
else:
    print(searchName,"의 점수는 ",d.get(searchName))
    print(searchName,"의 점수는 ",d[searchName])


# d.pop('bb')
del d['bb']
print('d:',d)








