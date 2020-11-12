#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''
class Tiger:
    def jump(self):
        print('호랑이 jump')
    
    def cry(self):
        print('호랑이 어흥~')
    
class Lion:
    def bite(self):
        print('사자 bite')
    def cry(self):
        print('사자 으르렁~')
        
class Liger(Lion,Tiger):
    def play(self):
        print('라이거와 놀기')
        
l = Lion()
l.cry()        
        
l2 = Liger()
l2.play()        
l2.jump()
l2.bite() 
l2.cry()     
        
        
        
            