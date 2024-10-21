#leet code problem1 two sum
a=[2,11,15,7]
target=9
for i in range(len(a)-1):
    if (a[i]+a[i+1]==target):
        print([i,i+1])      
