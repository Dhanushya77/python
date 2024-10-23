from abc import ABC,abstractmethod
class clg:
    @abstractmethod
    def register(self):
        print('reg')
    def classroom(self):
        print('classes')
        
class students(clg):
    def register(self):
        name=input('Enter name')
        course=input('Enter course')
    def notes(self):
        print('notes')
        
class staff(clg):
    def register(self):
        name=input('Enter name')
        salary=int(input('Enter salary'))
    def exam(self):
        print('exam')
        
staff1=staff()
staff1.register()

student1=students()
student1.register()