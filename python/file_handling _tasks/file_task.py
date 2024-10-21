limit=int(input('enter limit:'))
f=open('name.txt','w')
for i in range(limit):
    name=input('enter name:')
    f.write(name +'\n')
