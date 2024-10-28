
from num import num
import add
from substract
from multiply
from divide
from modulus
while True:
    print('''
          1.Add
          2.Sub
          3.Mul
          4.Div
          5.Mod
          6.exit
          ''')
    ch=int(input("choice:"))
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
        a,b=num()
        div.div(a,b)
    elif ch==5:
        a,b=num()
        mod.mod(a,b)
    elif ch==6:
        break
    else:
        print('invalid')