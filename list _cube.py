a=[1,2,3,4,5]
b=[]
for i in a:
    c=i**3
    b.append(c)
print(b)

a=[1,2,3,4,5]
b=map(lambda x:x**3,a)
print(list(b))

print(list(map(lambda x:x**3,a)))

def sample(x):
     return x**3
print(list(map(sample,a)))