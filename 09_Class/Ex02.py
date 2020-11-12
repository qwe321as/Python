#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''
# Ex02
class Bank :
    rate = 0.3
    
    def __init__(self,money): # 생성자
        print('__init__',money) 
        self.money = money
        
    def save(self):
        print('save()')
        self.money = self.money + self.money * Bank.rate
    
    def show(self):
        print(self.money)
    
if __name__ =="__main__" : 
    b1 = Bank(10000)
    b2 = Bank(30000)
    
    b1.save()
    b1.show()
       
    b2.save()
    b2.show()   
   
   
   