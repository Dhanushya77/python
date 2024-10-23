# hybrid inheretance

class college:
    def staff(self):
        print('staff')

class sports(college):
    def indoor(self):
        print('indoor')
    def outdoor(self):
        print('outdoor')
        
class arts(college):
    def dance(self):
        print('dance')
    def music(self):
        print('music')
        
class football(sports):
    def football_match(self):
        print('football match')

class cricket(sports):
    def cricket_match(self):
        print('cricket match')
        
std1=cricket()
std1.indoor()
std1.cricket_match()

std2=football()
std2.outdoor()
std2.football_match()
std2.staff()
