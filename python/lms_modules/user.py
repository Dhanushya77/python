user=[{'id':100,'name':'dhan','email':'email1','password':'pas','ph_no':1234,'book':[]}]
book=[{'id':100,'name':'sample','stock':10,'price':10}]


def view_pro(users):
    print (users)

def lend_book(users):
    id=int(input('enter id:'))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            if i['stock']>0:
                users['book'].append(id)
                i['stock']-=1
            else:
                print('out of stock')    
    if f1==0:
        print('book not available')
    #print(user)
def return_book(users):
    id=int(input('enter id:'))
    f1=0
    for j in book:
        if j['id']==id and users['book'] == id:
            f1=1
            j['stock']+=1
            users['book'].remove(id)
            if f1==0:
                print('book not available')


