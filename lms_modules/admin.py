user=[{'id':100,'name':'dhan','email':'email1','password':'pas','ph_no':1234,'book':[]}]
book=[{'id':100,'name':'sample','stock':10,'price':10}]
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
    for j in user:
        print('{:<10}{:<12}{:<20}{:<12}'.format(j['id'],j['name'],j['email'],j['ph_no']))
