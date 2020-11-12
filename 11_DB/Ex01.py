#-*- coding:utf-8
'''
Created on 2020. 10. 30.

@author: user
'''
# Ex01

import cx_Oracle

con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')
cur = con.cursor()

print(type(con))
print(type(cur))

drop = 'drop table person'
cur.execute(drop)

dropseq = 'drop sequence perseq'
cur.execute(dropseq)

seq = 'create sequence perseq'
cur.execute(seq)

create = '''create table person(
            num number primary key,
            id varchar2(10),
            name varchar2(10),
            addr varchar2(10)
            )  
'''
cur.execute(create)

cur.execute('select * from person')

for row in cur:
    print('row:',row)

print('------------------')
    
insert = "insert into person values(perseq.nextval,'hong','길동','서울')"
cur.execute(insert)

insert = "insert into person values(perseq.nextval,'kim','연아','부산')"
cur.execute(insert)

con.commit()

cur.execute('select * from person')
for row in cur:
    print('row:',row)

print('------------------')

update = "update person set name='길자' where id='hong'"
cur.execute(update)
con.commit()

cur.execute('select * from person')
for row in cur:
    print('row:',row)

print('------------------')


delete = "delete from person where id='hong'"
cur.execute(delete)
con.commit()

cur.execute('select * from person')
for row in cur:
    print('row:',row)

cur.close()
con.close()













