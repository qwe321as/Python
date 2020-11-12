#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
# Ex01_file

f = open('file.txt','w')
f.write('apple\nbanana')
f.close()


f2 = open('file.txt','r')
str = f2.read()
print('str:',str)
f2.close()

import os
print(os.getcwd())
print(os.listdir('.'))


def filetype(fpath):
    print(fpath,':',end='')
    if os.path.isfile(fpath):
        print("File")
    if os.path.isdir(fpath):
        print("Directory")
        
flist = os.listdir('.')
for fname in flist :
    filetype(fname)
  
    












