#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: user
'''

import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

x1 = [1,2,3,4]
y1 = [3,7,6,4]

x2 = [1,2,3,4]
y2 = [4,6,8,5]

ymax = max(max(y1) , max(y2)) + 1  #max(7,8) + 1=>9
ymin = min(min(y1), min(y2)) - 1
print(ymax ,',', ymin) #9,2 
print()

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_location).get_name()
plt.rc('font',family=font_name)

plt.plot(x1,y1,label='first line',color='red')
plt.plot(x2,y2,label='second line')
plt.legend()
plt.yticks(np.arange(ymin,ymax+1))
plt.xlabel('xlabel')
plt.ylabel('y축')

plt.title('제목')

plt.annotate('두선이 만나는 지점',xy=(1.5,5),xytext=(2,4),
             arrowprops={'color':'green'})

filename ='brokenLine.jpg'
plt.savefig(filename)
plt.show()




















