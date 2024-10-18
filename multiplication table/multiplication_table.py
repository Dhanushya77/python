num=int(input('enter a number:'))
f=open('mul_table.txt','w')
for i in range(11):
    print(num,'*',i ,'=',num*i)
    f.write(str(num)+'*'+str(i)+'='+str(num*i)+'\n')
