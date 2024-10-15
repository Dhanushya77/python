import add
import sub
import mul
import div
import mod
from num import num
while True:
    print('''
    1.Addition
    2.Substraction
    3.Multiplication
    4.Division
    5.Modulus
    6.Exit''')
    ch=int(input('Enter your choice:'))
    if ch==1:
        a,b=num()
        add.add(a,b)
    elif ch==2:
        a,b=num()
        sub.sub(a,b)
    elif ch==3:
        a,b=num()
        mul.mul(a,b)
    elif ch==4:
        a,b=num
        div.div(a,b)
    elif ch==5:
        a,b=num()
        mod.mod(a,b)
    elif ch==6:
        break
    else:
        print('Invalid choice!')