employees = [{'id':100,'name':'Dhan','age': 28,'position':'Developer','salary':60000.0,'password':'pas'}]

while True:
    print('''
        1. Login
        2. Exit
    ''')
    ch=int(input('Enter your choice:'))

    if ch==1: 
        username=input('Enter employee ID or admin:')
        password=input('Enter password:')
        f=0       
        if username=='admin' and password=='admin':
            print('Admin login successful')
            f=1
            while True:
                print('''
                    1.Add Employee
                    2.Update Employee
                    3.Delete Employee
                    4.View Employees
                    5.Log out
                ''')
                ch1=int(input('Enter choice: '))
                
                if ch1==1:  
                    if len(employees)==0:
                        emp_id=100
                    else:
                        emp_id=employees[-1]['id'] + 1
                    print('Employee ID:',emp_id)
                    name=input('Enter employee name: ')
                    age=int(input('Enter employee age: '))
                    position=input('Enter employee position: ')
                    salary=float(input('Enter employee salary: '))
                    password=input('Set employee password: ')
                    employees.append({'id':emp_id,'name':name,'age':age,'position':position,'salary':salary,'password':password})
                    print("Employee added successfully.")
                
                elif ch1==2: 
                    emp_id=int(input('Enter employee ID to update: '))
                    f1=0
                    for emp in employees:
                        if emp['id']==emp_id:
                            f1=1
                            emp['name']=input('Enter new name: ')
                            emp['age']=int(input('Enter new age: '))
                            emp['position']=input('Enter new position: ')
                            emp['salary']=float(input('Enter new salary: '))
                            print("Employee updated successfully.")
                            break
                    if f1==0:
                        print('Employee not found.')
                
                elif ch1==3:  
                    emp_id=int(input('Enter employee ID:'))
                    f1=0
                    for emp in employees:
                        if emp['id']==emp_id:
                            f1=1
                            employees.remove(emp)
                            print("Employee deleted successfully.")
                            break
                    if f1==0:
                        print('Employee not found.')
                
                elif ch1==4: 
                    print('{:<10}{:<15}{:<10}{:<15}{:<10}'.format('ID', 'Name', 'Age', 'Position', 'Salary'))
                    for emp in employees:
                        print('{:<10}{:<15}{:<10}{:<15}{:<10}'.format(emp['id'], emp['name'], emp['age'], emp['position'], emp['salary']))
                
                elif ch1==5:  
                    break
                else:
                    print("Invalid choice.")
       
        elif username.isdigit():
            emp_id=int(username)
            for emp in employees:
                if emp['id']==emp_id and emp['password']==password:
                    print('Employee login successful')
                    f=1
                    while True:
                        print('''
                            1.View My Details
                            2.Update My Details
                            3.Log out
                        ''')
                        ch2=int(input('Enter choice:'))
                        
                        if ch2==1: 
                            print('{:<10}{:<15}{:<10}{:<15}{:<10}'.format('ID', 'Name', 'Age', 'Position', 'Salary'))
                            print('{:<10}{:<15}{:<10}{:<15}{:<10}'.format(emp['id'], emp['name'], emp['age'], emp['position'], emp['salary']))
                        
                        elif ch2==2: 
                            emp['age']=int(input('Enter new age: '))
                            emp['position']=input('Enter new position: ')
                            emp['salary']=input('Enter new salary:')
                            print("Details updated successfully.")
                        
                        elif ch2==3: 
                            break
                        else:
                            print("Invalid choice.")
                    break
            if f==0:
                print("Invalid employee ID or password!")

        else:
            print("Invalid username or password!")

    elif ch==2: 
        break
    else:
        print("Invalid choice.")
