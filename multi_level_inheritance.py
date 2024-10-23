# multi-level inheritance

class university:
    def exams(self):
        print('university exams')
    def syllabus(self):
        print('syllabus')
class college(university):
    def notes(self):
        print('notes')
    def classes(self):
        print('classes')
class students(college):
    def uniform(self):
        print('uniform')

std1=students()
std1.classes()
std1.uniform()
std1.exams()
clg1=college()
clg1.syllabus()
clg1.notes()




