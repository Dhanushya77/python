employee=[{'id':100,'name':'anu','email':'anu@','ph_no':1234,'position':'BDE'}]
print('''
    1.Login 
    2.Exit
    ''')
ch=int(input("enter choice:"))
if ch==1:
    user_name=input('enter username:')
    password=input('enter password:')
    f=0
    if user_name=='admin' and password=='admin':
            print('Admin login')
            f=1
            while True:
                print('''
                    1.Add employee
                    2.view employee
                    3.delete employee
                    4.update employee
                    5.log out
                        ''')
                ch1=int(input('enter choice'))
                if ch1==1:
                    if len(employee)==0:
                        id=100
                    else:
                        id=employee[-1]['id']+1
                        print('Employee id:',id)
                    name=input('enter name:')
                    email=input('enter email:')
                    dob=input('enter dob')
                    ph_no=int(input('enter ph no:'))
                    position=input('enter position:')
                    employee.append({'id':id,'name':name,'email':email,'ph_no':ph_no,'position':position})
