#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''

class Person :
    
    lastname = '김'
    
    def setname(self,name): 
        print('self:',self)
        self.fullname = self.lastname + name
        return self.fullname
    
p1 = Person()
p2 = Person()
print(p1.lastname)        
print(p2.lastname) 
print(Person.lastname)       
        
f1 = p1.setname('수현')
f2 = p2.setname('지선')
print('f1:',f1)
print('f2:',f2)
      
        
        
        
        
        
        
        
        
        
        