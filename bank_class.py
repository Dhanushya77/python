## without parameter

# class bank:
#      def __init__(s):    #constructor function
#         s.id = int(input('Enter your id:'))
#         s.name = input('Enter your name:')
#         s.bal=0
#     def balance(self):
#         print(self.bal)
#     def depo(s):
#         depo_amount = int(input('Enter deposited amount:'))
#         s.bal+=depo_amount
    
# cus1=bank()
# cus1.depo()
# cus1.balance()

#with parameter
class bank:
    def __init__(s,id,name,bal):    #constructor function
        s.id = id
        s.name = name
        s.bal = bal
    def balance(self):
        print(self.bal)
    def depo(s,amnt):
        s.bal+=amnt
    
cus1=bank(1,'sd',100)
cus1.depo(100)
cus1.balance()