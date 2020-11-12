
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

x1 = [1,2,3,4]
y1 = [3,7,6,4]

x2 = [1,2,3,4]
y2 = [4,6,8,5]

plt.subplot(2,1,1)
plt.plot(x1,y1,'yo-')

plt.subplot(2,1,2)
# plt.plot(x2,y2,'r.--')
plt.plot(x2,y2,color='green',linestyle='dotted',marker='D')

plt.show()


















