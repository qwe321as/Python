#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''
class Person:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return '<Person %s %s>' % (self.name, self.phone)
    

class Employee(Person):
    def __init__(self,name,phone,position,salary):
        Person.__init__(self, name, phone)
        self.position = position
        self.salary = salary
        
    def __str__(self):
        return '<Employee %s %s %s %s>' % \
                (self.name, self.phone,self.position,self.salary)
      
      
p1 = Person('윤아',1234)
print(p1.__str__())  
print(p1)   
      
e1 = Employee('효연',9876,'과장',300)     
print(e1) 
      
      
      
      
      
      
      
      