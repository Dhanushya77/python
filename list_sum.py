#total sum of elements in a given list
a=[1,2,3,4,5,6,7,8,9]
sum=0
for i in a:
    sum= sum+i
print (sum)

#find sum when strings are present
a=[1,2,3,4,5,6,7,8,9,"abc","efg"]
sum=0
for i in a:
    if type(i)==int or type(i)==float :
        sum= sum+i
print (sum)

#remove duplicate elements and print output
a=[1,2,3,2,1,4,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

