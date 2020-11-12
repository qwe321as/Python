#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: user
'''
# Ex08_BeautifulSoup

from bs4 import BeautifulSoup
import os,shutil
from urllib.request import urlopen


myfolder = 'c:\\imsi2\\'

weekday_dict = {'mon':'월요일','tue':'화요일', 'wed':'수요일', \
                'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

print(weekday_dict.items())
# dict_items([('mon', '월요일'), ('tue', '화요일'), ('wed', '수요일'), ('thu', '목요일'), ('fri', '금요일'), ('sat', '토요일'), ('sun', '일요일')])
print()

print(weekday_dict.values())
# dict_values(['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'])

try:
    for mydir in weekday_dict.values():
        mypath = myfolder+mydir 
        print('mypath:',mypath)
        if os._exists(mypath) :
            shutil.rmtree(mypath)
        
        os.mkdir(mypath)

except FileExistsError :
    pass

#################################################

def saveFile(image_url,weekday,mytitle):
    image_file = urlopen(image_url)
    
    myfile = open('c:\\imsi2\\'+weekday_dict[weekday]+'\\'+mytitle+'.jpg','wb')
    
    myfile.write(image_file.read())
    
      
#################################################

    
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'

soup = BeautifulSoup(urlopen(myurl),'html.parser')

mytarget = soup.find_all('div',{'class':'thumb'})
print('mytarget:\n',mytarget)
print()
print(len(mytarget)) # 360
print()

for one in mytarget:
#      <div class="thumb">
# <a href="/webtoon/list.nhn?titleId=726842&amp;weekday=thu" onclick="nclk_v2(event,'thm*T.img','','26')">
# <img alt="무모협지" height="90" onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif'" src="https://shared-comic.pstatic.net/thumb/webtoon/726842/thumbnail/thumbnail_IMAG10_9a600596-d77d-4ee3-92bf-e0f06f5221cc.jpg" title="무모협지" width="83"/><span class="mask"></span>
# </a>
# </div>
    atag = one.find('a')
    myhref = atag.attrs['href']
    print('myhref:',myhref)
#     /webtoon/list.nhn?titleId=733766&weekday=mon

    myhref = myhref.replace('/webtoon/list.nhn?','')
#     titleId=733766&weekday=mon
    
    result = myhref.split('&')
#     titleId=733766
#     weekday=mon
    print('result:',result)
#     ['titleId=744313', 'weekday=sun']
    print()
    
    myweekday = result[1].split('=')[1]
    print('myweekday:',myweekday)
    print()
    
#  -----------------------------------
# one정보:
#      <div class="thumb">
# <a href="/webtoon/list.nhn?titleId=726842&amp;weekday=thu" onclick="nclk_v2(event,'thm*T.img','','26')">
# <img alt="무모협지" height="90" onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif'" src="https://shared-comic.pstatic.net/thumb/webtoon/726842/thumbnail/thumbnail_IMAG10_9a600596-d77d-4ee3-92bf-e0f06f5221cc.jpg" title="무모협지" width="83"/><span class="mask"></span>
# </a>
# </div>
    imgtag = one.find('img')
    mytitle = imgtag.attrs['title']
    print('mytitle:',mytitle)
#   신이 담긴 아이

    mytitle = mytitle.replace('?','').replace(':','')
    print()
    
    mysrc = imgtag.attrs['src']
    print('mysrc:',mysrc)
#   https://shared-comic.pstatic.net/thumb/webtoon/743721/thumbnail/thumbnail_IMAG10_1a440839-f0da-4260-a107-8840f6fa4fc9.jpg
    print()
    
    saveFile(mysrc,myweekday,mytitle) 
    
    










