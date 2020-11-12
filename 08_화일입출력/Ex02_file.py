#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''
# 3*1=3
# 3*9=27

for i in range(1,10,1):
    data = "3 * %d = %d" % (i,3*i)
    print(data)

print('-' * 20)

# gugudan.txt
f = open('gugudan.txt','w')
for i in range(1,10,1):
    data = "3 * %d = %d\n" % (i,3*i)
    f.write(data)
f.close()

print('readline()')

f = open('gugudan.txt','r')
cnt = 0
print(f.tell())
while True:
    line = f.readline();
    
    if line == '':
        break
    cnt += 1
    print('line:',line,end='')
print('구구단 출력 끝 반복횟수 : ',cnt)    
print(f.tell())# 화일포인터 위치를 알고싶을 때
f.seek(0) # 화일포인터의 위치를 바꾸고 싶을 때
print(f.tell())

lines = f.readlines()
print('lines:',lines) # list
print(type(lines))

for line in lines : 
    print(line,end='')
f.close()

print('=====================')

f = open('gugudan.txt')
lines2 = f.read()
print(type(lines2))
print('len(lines2):',len(lines2))
print(lines2)
# a = "apple"
for i in lines2 :
    print(i)


s = 'ab cde f g hi'
print('s:',s)
s2 = s.split()
print('s2:',s2)











print('\n'*20)
