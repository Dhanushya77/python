# employee management system
import sqlite3
con=sqlite3.connect("employee_details.db")
try:
    con.execute("create table ems(Name text, Age int, Phn_no int, Email text, Position text, Salary int)")
except:
    print("Table created")
while True:
    print('''
          1.Add employee
          2.View employee
          3.Update employee
          4.Delete employee
          5.Exit
    ''')
    ch=int(input('Enter choice:'))
    if ch == 1:
        name = input('Enter employee name:')
        age = int(input('Enter age:'))
        phn_no = int(input('Enter phn_no:'))
        email = input('Enter email:')
        position = input('Enter position:')
        salary=int(input('Enter salary:'))
        con.execute("insert into ems(Name, Age, Phn_no, Email, Position, Salary) values(?,?,?,?,?,?)",(name, age, phn_no, email, position, salary))
        con.commit()
        print("Employee added succesfully")
    elif ch == 2:
        name=input("Enter name:")
        data=con.execute("select * from ems where Name=?",(name,))
        print('{:<20}{:<10}{:<15}{:<20}{:<20}{:<15}'.format('Name','Age','Phn_no','Email','Position','Salary'))
        for i in data:
            print('{:<20}{:<10}{:<15}{:<20}{:<20}{:<15}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif ch == 3:
        while True:
            print('''
                1.Name
                2.Age
                3.Phn_no
                4.Email
                5.Position
                6.Salary
                7.exit
                ''')
            ch1 = int(input('Enter field you need to update:'))
            
            if ch == 1:
                name=input('Enter name:')
                new_name=input('New name:')
                con.execute("update ems set Name=? where Name=? ",(new_name,name,))
                con.commit()
            
            elif ch == 2:
                age = int(input('Enter age:'))
                new_age = int(input('Enter age:'))
                con.execute("update ems set Age=? where Age=? ",(new_age,age,))
                con.commit()
            
            elif ch == 3:
                phn_no = int(input('Enter phn_no:'))
                new_no = int(input('Enter phn_no:'))
                con.execute("update ems set Phn_no=? where Phn_no=? ",(new_phn_no,phn_no,))
                con.commit()
            
            elif ch == 4:
                email = input('Enter email:')
                new_email = input('Enter email:')
                con.execute("update ems set Email=? where Email=? ",(new_email,email,))
                con.commit()
            
            elif ch == 5:
                position = input('Enter position:')
                new_position = input('Enter position:')
                con.execute("update ems set Position=? where Position=? ",(new_position,position,))
                con.commit()
            
            elif ch == 6:
                salary=int(input('Enter salary:'))
                new_salary=int(input('Enter salary:'))
                con.execute("update ems set Salary=? where Salary=? ",(new_salary,salary,))
                con.commit()
            elif ch == 7:
                break
            else:
                print('Invalid choice')
    
    elif ch == 4:
        name=input("enter name:")
        con.execute("delete from user where name=?",(name,))
        con.commit()
    elif ch == 5:
        break
    else:
        print("Invalid choice")