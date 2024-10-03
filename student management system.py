l = []
while True:

    print('''
        1.Add Student
        2.View Student
        3.Update Student
        4.Delete Student
        5.Exit
        ''')
    ch = int(input('Your choice:'))
    if ch == 1:
        roll_no = int(input('Enter roll number:'))
        name = str(input('Enter name:'))
        email = str(input('Enter email:'))
        course = str(input('Enter course:'))
        l.append({'roll_no':roll_no,'name':name,'email':email,'course':course})
    elif ch==2:
        print('{:<10}{:<12}{:<20}{:<12}'.format('Roll no','Name','Email','Course'))
        for i in l:
            print('{:<10}{:<12}{:<20}{:<12}'.format(i['roll_no'],i['name'],i['email'],i['course']))
    elif ch==3:
        roll_no = int(input('Enter roll number:'))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                name = str(input('Enter name:'))
                i['name']=name
                email = str(input('Enter email:'))
                i['email']=email
                course = str(input('Enter course:'))
                i['course']=course
                f=1
        if f==0:
            print('id not available')
    elif ch==4:
        roll_no = int(input('Enter roll number:'))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                l.remove(i)
                print('student data deleted')
                f=1
        if f==0:
            print('id not available')
    else:
        print('invalid choice')   