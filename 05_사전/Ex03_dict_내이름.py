#-*- coding:utf-8
'''
Created on 2020. 10. 29.

@author: user
'''
# Ex03_dict_내이름

student = {} # {'kim':'10', 'park':'20'}
while True :
    print()
    num = int(input('메뉴번호(1:출력, 2:입력, 3:검색, 4:삭제, 5:수정, 6:종료 => '))
    
    if num == 1 :
        
        if len(student) != 0 :
            for i,j in student.items():
                print(i,'\t',j)
        else:
            print('입력한 데이터 없음')
            
    elif num == 2:
        name = input('이름:')
        jumsu = input('점수:')
        student[name]=jumsu
        
    elif num == 3:
        searchName = input('찾는 이름:')
        
        if student.get(searchName) != None :
            print(searchName,'의 점수는 ', student.get(searchName), student[searchName])
        else:
            print('찾는 이름 없음')
            
    elif num == 4:
        deleteName = input('삭제할 이름:')
        if deleteName in student :
            student.pop(deleteName)
            # del student[deleteName]
        else:
            print('찾는 이름 없음')
            
    elif num == 5:
        updateName = input('수정할 이름:')
        if updateName in student :
            jumsu = input('수정할 점수:')
            student[updateName]=jumsu
        else:
            print('찾는 이름 없음')  
            
    elif num == 6:
        print('프로그램 종료')
        import sys
        sys.exit() 
    else :
        print('번호 잘못 입력함')
        
        


# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  1
# 입력한 데이터 없음
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  2
# 정보 입력
# 이름 : kim
# 점수 : 11
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  2
# 정보 입력
# 이름 : park
# 점수 : 22
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  1
# 이름    점수
# kim      11
# park      22
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  3
# 정보 검색
# 이름 : park
# park 의 점수는  22 22
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  3
# 정보 검색
# 이름 : choi
# 찾는 이름 없음
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  4
# 정보 삭제
# 삭제할 이름 : choi
# 찾는 이름 없음
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  4
# 정보 삭제
# 삭제할 이름 : kim
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  1
# 이름    점수
# park      22
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  5
# 정보 수정
# 수정할 이름 : park
# 찾는 이름 없음
# 
# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  5
# 정보 수정
# 수정할 이름 : kim
# 점수 : 22

# 메뉴번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정 , 6:종료) =>  6
# 프로그램 종료
