import mysql.connector
con = mysql.connector.connect(host='localhost',user='dhanushya', password='dhanushya@',database='batch2')
con.autocommit=True
cur = con.cursor()
# cur.execute("create database batch2")
# cur.execute("create table user(no int, name text, age text)")
# cur.execute("insert into user(no,name,age)values(1,'anu',22)")

# #input data from user
# no = int(input('Enter no:'))
# name = input('Enter name:')
# age = int(input('Enter age:'))
# cur.execute("insert into user(no,name,age)values(%s,%s,%s)",(no,name,age))

# #read data
# cur.execute("select * from user")
# data = cur.fetchall()
# for i in data:
#     print(i)

# #update
# value=input('Enter value to be updated:')
# new_name=input('new name:')
# cur.execute("update user set name=%s where name=%s ",(new_name,value,))

# #delete
# no=int(input("enter a no:"))
# cur.execute("delete from user where no=%s",(no,))

# #starts with a
# cur.execute("select * from user where name like 'a%'")
# data = cur.fetchall()
# for i in data:
#     print(i)

# #second letter a
# cur.execute("select * from user where name like '_a%'")
# data = cur.fetchall()
# for i in data:
#     print(i)

# #last letter u
# cur.execute("select * from user where name like '%u'")
# data = cur.fetchall()
# for i in data:
#     print(i)

# #ascending order
# cur.execute("select * from user order by name")
# data = cur.fetchall()
# for i in data:
#     print(i)

# #descending order
# cur.execute("select * from user order by name desc")
# data = cur.fetchall()
# for i in data:
#     print(i)

# group by min max avg sum count
# cur.execute("select name, age from user group by name")
# data = cur.fetchall()
# for i in data:
#     print(i)
    
    
# cur.execute("select name, min(age) from user group by name")
# data = cur.fetchall()
# for i in data:
#     print(i)
