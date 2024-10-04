user=[{'id':100,'name':'dhan','email':'email1','password':'pas','ph_no':1234,'book':[]}]
#print(user)
book=[{'id':100,'name':'sample','stock':10,'price':10}]
while True:
    print('''
        1.Register
        2.Login
        3.Exit
    ''')
    ch=int(input('enter your choice:'))
    if ch==1:
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
        #print(user)
    elif ch==2:
        user_name=input('enter username:')
        password=input('enter password:')
        f=0
        if user_name=='admin' and password=='admin':
            print('Admin login')
            f=1
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
                    if len(book)==0:
                        id=100
                    else:
                        id=book[-1]['id']+1
                        print('book id:',id)
                    name=input('enter book name:')
                    stock=int(input('enter number of stock:'))
                    price=int(input('enter price:'))
                    book.append({'id':id,'name':name,'stock':stock,'price':price})
                elif ch1==2:
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
                elif ch1==3:
                    id=int(input('enter id:'))
                    f1=0
                    for i in book:
                        if i['id']==id:
                            f1=1
                            book.remove(i)
                    if f1==0:
                        print('book not available')
                elif ch1==4:
                    print('{:<10}{:<12}{:<12}{:<12}'.format('id','Name','Stock','Price'))
                    for i in book:
                        print('{:<10}{:<12}{:<12}{:<12}'.format(i['id'],i['name'],i['stock'],i['price']))
                elif ch1==5:
                    print('{:<10}{:<12}{:<20}{:<12}'.format('id','Name','Email','Phone no'))
                    for i in user:
                        print('{:<10}{:<12}{:<20}{:<12}'.format(i['id'],i['name'],i['email'],i['ph_no']))
                elif ch1==6:
                    break
                    

        if user_name.isdigit():
            user_name=int(user_name)
        for i in user:
            if user_name==i['id'] and password==i['password']:
                print('User login')
                f=2
                while True:
                    print('''
                            1.View book
                            2.Lend book
                            3.Return book
                            4.Book in hand
                            5.Log out
                            ''')
                    ch2=int(input('enter choice:'))
                    if ch2==1:
                        print('{:<10}{:<12}{:<12}{:<12}'.format('id','Name','Stock','Price'))
                        for j in book:
                            print('{:<10}{:<12}{:<12}{:<12}'.format(j['id'],j['name'],j['stock'],j['price']))  
                    elif ch2==2:
                        id=int(input('enter id:'))
                        f1=0
                        for j in book:
                           if j['id']==id:
                                f1=1
                                if j['stock']>0:
                                    i['book'].append(id)
                                    j['stock']-=1
                                else:
                                    print('out of stock')
                        if f1==0:
                            print('book not available')
                        #print(user)
                    elif ch2==3:
                        id=int(input('enter id:'))
                        f1=0
                        for j in book:
                            if j['id']==id and id in i['book']:
                                f1=1
                                j['stock']+=1
                                i['book'].remove(id)
                        if f1==0:
                            print('book not available')
                    elif ch2==4:
                        if len(i['book'])==0:
                            print('no books in hand')
                        else:
                            print(i['book'])
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

