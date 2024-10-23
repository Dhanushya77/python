# example of polymorphism 
# super function is used

class bank:
    def __init__(self):
        print('''
              SBI
              BRANCH:EKM
              IFSC:SBIN00004
              LOCATION:MG ROAD''')
    def deposit(self):
        print('amount deposited')
        
class users(bank):
    def __init__(self):
        super().__init__()
        self.name=input('Enter name:')
        self.email=input('Enter email:')
    def user_dtls(self):
        print(self.name,self.email)
        
user1=users()
user1.user_dtls()