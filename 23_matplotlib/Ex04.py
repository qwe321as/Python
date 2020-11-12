#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: user
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_location).get_name()
plt.rc('font',family=font_name)


slices=[1,2,3,4]
hobbies = ['공부','영화감상','운동','게임']
cols = ['c','m','r','b']

plt.pie(slices, labels=hobbies,colors=cols,shadow=True,
        startangle=90,explode=(0,0.2,0,0),autopct='%.2f%%')
plt.legend(loc=0)
# 0:best
# 1:우상
# 2:좌상
plt.show()










