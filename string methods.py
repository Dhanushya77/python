#string methods
s='hi all i am dhanushya'
print(s.capitalize())
print(s.isupper())
print(s.islower())
print(s.lower())
print(s.upper())
s='            hi all i am dhanushya              '
print(s)
print(s.strip())
s='            hi all i am dhanushya              '
print(s.lstrip())
print(s.rstrip())
s='hi all i am dhanushya'
print(s.split(' '))
print(s.startswith('f'))
print(s.endswith('a'))
print(s.count('l'))
print(s.index('h'))
#print(s.index('z')) shows error
print(s.find('l'))
print(s.find('z'))
print(s.center(40))
s='1234'
print(s.isdigit())
# r string
print('welcome\new')
print(r'welcome\new')
#f string
a='apple'
b=200
print(f'The product is {a} which costs about {b} rupees.')