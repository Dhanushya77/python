from login_reg import *
from admin import *
from user import*

user=[{'id':100,'name':'dhan','email':'email1','password':'pas','ph_no':1234,'book':[]}]
book=[{'id':100,'name':'sample','stock':10,'price':10}]

while True:
    print('''
        1.Register
        2.Login
        3.Exit
    ''')
    ch=int(input('enter your choice:'))
    if ch==1:
        register()
    elif ch==2:
        f,users=login()
        if f==1:
            print('admin login')
            while True:
                print('''
                    1.Add book
                    2.Update book
                    3.Delete book
                    4.View book
                    5.View user
                    6.Log out
                      ''')
                ch1=int(input('Enter choice:'))
                if ch1==1:
                    add_book()
                elif ch1==2:
                    up_book()
                elif ch1==3:
                    del_book()
                elif ch1==4:
                    view_book()
                elif ch1==5:
                    view_user()
                elif ch1==6:
                    break
        elif f==2:
            print('user login')
            while True:
                    print('''
                            1.View_pro
                            2.view book
                            3.lend book
                            4.return book
                            5.Log out
                            ''')

                    ch2=int(input('enter choice:'))
                    if ch2==1:
                        view_pro(users)
                    elif ch2==2:
                        view_book()
                    elif ch2==3:
                        lend_book(users)
                    elif ch2==4:
                        return_book(users)
                    elif ch2==5:
                        break
                    else:
                        print('Invalid choice')

        if f==0:
            print('User name or Password invalid')
    elif ch==3:
        break

    else:
        print('invalid choice')