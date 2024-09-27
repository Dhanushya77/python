#using assignment operator
l=[1,2,3,4]
l1=l
print(id(l1))
print(id(l))
print(l1,l)
l1.pop()
print(l1,l)

#copy method
l=[1,2,3,4,5,6]
l1=l.copy()
print(id(l1))
print(id(l))
print(l1,l)
l1.pop()
print(l1,l)

#sort,reverse,index and count methods
l=[3,7,4,9,6,7]
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(7))
print(l.count(7))