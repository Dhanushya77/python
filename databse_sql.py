import sqlite3
con=sqlite3.connect("batch2.db")
try:
    con.execute("create table user(No int, Name text, Age int)")
except:
    print("Table created")
# con.execute("insert into user(No, Name, Age)values(9,'dhanushya',20),(10,'anu',28)")
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

# data=con.execute("select * from user where name like 'a%'")    #starts with a
# for i in data:
#     print(i)

# data=con.execute("select * from user where name like '__a%'")    #second letter a   # percentage multi-character
# for i in data:
#     print(i)
    
# data=con.execute("select * from user where name like '___'")    #second letter a    #underscore-single character
# for i in data:
#     print(i)
    
# data = con.execute("select * from user order by name")  #ascending order
# for i in data:
#     print(i)
    
# data = con.execute("select * from user order by name desc")  #descending order
# for i in data:
#     print(i)


try:
    con.execute("create table address(No int, place text, pincode int)")
except:
    print("Table created")

# limit = int(input('Enter limit:'))
# for i in range(limit):
#     no = int(input('Enter no:'))
#     place = input('Enter place:')
#     pin = int(input('Enter pin:'))
#     con.execute("insert into address(No, place, pincode)values(?, ?, ?)",(no, place, pin))
#     con.commit()

# data=con.execute ("select user.No, user.Name, user.Age, address.place, address.pincode from user join address on user.No=address.No")
# for i in data:
#     print(i)

# data=con.execute ("select user.No, user.Name, user.Age, address.place, address.pincode from user left join address on user.No=address.No")
# for i in data:
#     print(i)
   
   
# 
# #instead of right join we do left join swapping the tables because right join is not supported in this version only supported in versions 3.10  and above   
# data=con.execute ("select user.No, user.Name, user.Age, address.place, address.pincode from address left join user on user.No=address.No")
# for i in data:
#     print(i) 


# #group by 
# data = con.execute("select name, age from user group by name")
# for i in data:
#     print(i)

# data = con.execute("select name, min(age) from user group by name")
# for i in data:
#     print(i)

# data = con.execute("select name, max(age) from user group by name")
# for i in data:
#     print(i)

# data = con.execute("select name, sum(age) from user group by name")
# for i in data:
#     print(i)

# data = con.execute("select name, avg(age) from user group by name")
# for i in data:
#     print(i)

# data = con.execute("select name, count(age) from user group by name")
# for i in data:
#     print(i)

