user=[{'id':100,'name':'dhan','email':'email1','password':'pas','ph_no':1234,'book':[]}]
book=[{'id':100,'name':'sample','stock':10,'price':10}]

def register():
    if len(user)==0:
        id=100
    else:
        id=user[-1]['id']+1
        print('your id is',id)
    name=input('enter name:')
    email=input('enter email:')
    ph_no=int(input('enter phone number:'))
    password=input('enter password:')
    user.append({'id':id,'name':name,'email':email,'password':password,'ph_no':ph_no,'book':[]})
    
def login():
    user_name=input('enter username:')
    password=input('enter password:')
    f=0
    users=''
    
    if user_name=='admin' and password=='admin':
        f=1
    if user_name.isdigit():
        user_name=int(user_name)
        for i in user:
            if user_name==i['id'] and password==i['password']:
                f=2
                users=i
    if f==0:
        print('invalid username or password')     
        
    return f,users

def add_book():
    if len(book)==0:
        id=100
    else:
        id=book[-1]['id']+1
        print('book id:',id)
    name=input('enter book name:')
    stock=int(input('enter number of stock:'))
    price=int(input('enter price:'))
    book.append({'id':id,'name':name,'stock':stock,'price':price})
    
def up_book():
    id=int(input('enter id:'))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            i['name']=input('enter new name:')
            i['stock']=stock=int(input('enter number of stock:'))
            i['price']=int(input('enter price:'))
            if f1==0:
                print('Book not available')
                
def del_book():
    id=int(input('enter id:'))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            book.remove(i)
            if f1==0:
                print('book not available')
                
def view_book():
    print('{:<10}{:<12}{:<12}{:<12}'.format('id','Name','Stock','Price'))
    for i in book:
        print('{:<10}{:<12}{:<12}{:<12}'.format(i['id'],i['name'],i['stock'],i['price']))

def view_user():
    print('{:<10}{:<12}{:<20}{:<12}'.format('id','Name','Email','Phone no'))
    for i in user:
        print('{:<10}{:<12}{:<20}{:<12}'.format(i['id'],i['name'],i['email'],i['ph_no']))

def view_pro(users):
    print (users)
    
    

                    



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
                ch1=int(input('enter choice:'))
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
                    
                    elif ch2==5:
                        break
                    else:
                        print('invalid choice')

        if f==0:
            print('User name or Password invalid')
    elif ch==3:
        break

    else:
        print('invalid choice')

