import re
# mobile number validation
a=str(input('Enter mobile no:'))
if len(a)==10 and a.isdigit() and re.search('^[6-9].{9}',a):
    print('Valid mobile number')
else:
    print('Invalid mobile number')

# email validation
a=str(input('Enter email:'))
if re.search('^[a-z].{2}.*@gmail.com$',a):
    print('valid email')
else:
    print('invalid')
    
# password validation
a=str(input('enter password:'))
if len(a)>=8 and re.search('[a-zA-Z].*[0-9].*',a):
    print('valid')
else:
    print('invalid')




