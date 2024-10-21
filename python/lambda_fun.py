#lambda function-its an anonymous function-can only give single expression
add=lambda a,b:a+b
print(add(10,2))
# lambda function can function even without any arguments
a=lambda:print("welcome")
a()

#a=[1,2,3,4,5]
#b=[]
#for i in a:
#    c=i**3
#    b.append(c)
#print(b)


# a=[1,2,3,4,5,6,7,8]
#b=map(lambda x:x**3,a)
#print(list(b))

#print(list(map(lambda x:x**3,a)))
#def sample(x):
#     return x**3
#print(list(map(sample,a)))

#even numbers sorting

#b=[]
#for i in a:
#    if i%2==0:
#        #print (i)
#        b.append(i)
#print(b)

#b=filter(lambda x:x%2==0,a)
#print(list(b))

#def even(x):
#    return x%2==0

#print(list(filter(even,a)))

#l=['apple','mango','orange','kiwi']
#a=str(input('search for:'))
#for i in l:
#    if a in i:
#        print(i)

#b=filter(lambda i:a in i,l)
#print(list(b))

# l=[1,2,3,4,5]
# a=[i**3 for i in l]
# print (a)

# a=[i for i in l if i%2==0]
# print(a)



