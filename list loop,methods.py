#list and methods
l=[1,2,3,4,5]
for i in l:
    print(i)
print (4 in l)
l[0]=10
print(l)
l.append(100)
l.append([6,7])
print(l)
print(200 in l)
print(l[3])
l.extend([10,11])
print(l)
l.insert(6,10)
print(l)
l.clear()
print(l)
l=[1,2,3,4,5]
l.pop()
print(l)
l.pop(2)
print(l)
l.remove(1)
print(l)
del l[0]
print(l)