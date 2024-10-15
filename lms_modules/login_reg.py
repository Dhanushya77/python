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