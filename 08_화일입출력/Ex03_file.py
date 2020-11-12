#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''

fr = open('sungjuk.txt','r')
fw = open('sungjuk_write.txt','w')

line = fr.readline()
fw.write(line)
print(fw.tell())
fw.seek(fw.tell()-2)
fw.write('\t합계\n')

for line in fr.readlines() : # fr
#     print(line) # 길동    22    33    44
    fw.write(line)
    s = line.split()
    print(s)
    
    total = 0
    for i in range(1,len(s),1) :
#         print(s[i])
        total += int(s[i])
    print('total:',total)
    fw.seek(fw.tell()-2)
    fw.write('\t'+str(total)+'\n') # 11 => '11'

fr.close()
fw.close()


    
    
    
    
    