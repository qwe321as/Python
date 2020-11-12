#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: user
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager
from pandas.core.frame import DataFrame

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_location).get_name()
plt.rc('font',family=font_name)


df = DataFrame({'국어':[40,70,20], '영어':[50,50,20], '수학':[50,20,20]},
               index=['강감찬','홍길동','이순신'])

print('df:\n',df)
print()

# df:
#      국어  영어  수학
# 강감찬  40  50  50
# 홍길동  70  50  20
# 이순신  20  20  20

# df = df.transpose()
df = df.T
print('df.transpose():\n',df)
print()

# df.plot(kind='bar')
df.plot.bar()
# df.plot.bar(stacked=True)
plt.xlabel('과목')
plt.xticks(rotation=0)

plt.ylabel('점수',rotation=0)
plt.title('우리반 성적표')
plt.show()










