d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("Enter a number:"))
value=''
while a!=0:
    b=a%10
    demo=d[b]
    value=demo+value
    a//=10
print(value)

    

