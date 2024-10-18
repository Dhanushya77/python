l=[1,2.5,6,9,'bd',6,10,'ad']
sum=0
for i in l:
    try:
        sum+=i
    except:
        pass
print(sum)