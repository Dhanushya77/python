import sqlite3
con=sqlite3.connect("batch2.db")
try:
    con.execute("create table user(No int, Name text, Age int)")
except:
    print("Table created")
# con.execute("insert into user(No, Name, Age)values(1,'dhanushya',22),(2,'anu',20)")
# con.commit()

# no = int(input('Enter no:'))
# name = input('Enter name:')
# age = int(input('Enter age:'))
# con.execute("insert into user(No, Name, Age)values(?, ?, ?)",(no, name, age))
# con.commit()

# limit = int(input('Enter limit:'))
# for i in range(limit):
#     no = int(input('Enter no:'))
#     name = input('Enter name:')
#     age = int(input('Enter age:'))
#     con.execute("insert into user(No, Name, Age)values(?, ?, ?)",(no, name, age))
#     con.commit()

# data=con.execute("select * from user")
# print(data)
# print('{:<10}{:<20}{:<10}'.format('No','Name','Age'))
# for i in data:
#     print('{:<10}{:<20}{:<10}'.format(i[0],i[1],i[2]))

# no=int(input('Enter no:'))
# data=con.execute("select * from user where no=?",(no,))
# for i in data:
#     print(i)

# value=input('Enter value to be updated:')
# new_name=input('New name:')
# con.execute("update user set name=? where name=? ",(new_name,value,))
# con.commit()

# no=int(input("enter a no:"))
# con.execute("delete from user where no=?",(no,))
# con.commit()

