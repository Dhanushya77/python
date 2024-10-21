l=['apple','mango','orange','kiwi']
a=str(input('search for:'))
for i in l:
    if a in i:
        print(i)
#using function
b=filter(lambda i:a in i,l)
print(list(b))
# using list comprehensive
l=['apple','mango','orange','kiwi']
a=str(input('search for:'))
b=[i for i in l if a in i]
print(list(b))
