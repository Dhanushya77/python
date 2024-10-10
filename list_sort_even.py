a=[1,2,3,4,5,6,7,8]
b=[]
for i in a:
    if i%2==0:
        #print (i)
        b.append(i)
print(b)

b=filter(lambda x:x%2==0,a)
print(list(b))

def even(x):
    return x%2==0

print(list(filter(even,a)))
