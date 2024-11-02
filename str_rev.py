a=input('enter a string value ')
# print(a[::-1])
rev=''
i=0
len=len(a)
while i<len:
    rev=a[i]+rev
    i=i+1
print(rev)

  
