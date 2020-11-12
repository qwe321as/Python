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

siljuk = [25,30,40,35,25,45]
members = ['태연','윤아','웬디','슬기','효리','서현']


plt.barh(members,siljuk)
# x축:회원이름
# y축:실적
# 그래프제목:회원별 업무실적
plt.xlabel('회원이름')
plt.ylabel('실적',rotation=0)
plt.title('회원별 업무실적')

filename="barGraph.png"
plt.savefig(filename)
plt.show()











