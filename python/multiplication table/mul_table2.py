limit=int(input('enter a limit:'))
f=open('mul_table1.txt','w')
for i in range(1,11):
    for j in range(1,limit+1):
        print(i,'*',j,'=',i*j,)
        f.write(str(i)+'*'+str(j)+'='+str(i*j)+'\t'+'\t')
    f.write('\n')