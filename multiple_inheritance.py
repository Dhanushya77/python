class school:
    def classroom(self):
        print('school classroom')
    def exam(self):
        print('school exam')
class tution:
    def notes(self):
        print('tution notes')
class student(school,tution):
    def uniform(self):
        print('uniform,')

std1 = student()
std1.uniform()