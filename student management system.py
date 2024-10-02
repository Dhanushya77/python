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
        email = str(input('Enter email'))
        course = str(input('Enter course'))
        l.append({'roll_no':roll_no,'name':name,'email':email,'course':course})
    elif ch==2:
        print('{:<10}{:<12}{:<20}{:<12}'.format('Roll no','Name','Email','Course'))
        for i in l:
            print('{:<10}{:<12}{:<20}{:<12}'.format(i['roll_no'],i['name'],i['email'],i['course']))


    else:
        print('invalid choice')   