# hierarchial inheretance

class mall:
    def shops(self):
        print('shops')
        
class foodcourt(mall):
    def food(self):
        print('food')
    def drinks(self):
        print('drinks')
        
class games(mall):
    def vr_games(self):
        print('vr')
    def fun_rides(self):
        print('rides')
        
cust1=games()
cust1.vr_games()
cust1.shops()
cust2=foodcourt()
cust2.shops()
cust2.food()
