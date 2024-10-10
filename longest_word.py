#longest word
l=['apple','mango','orange','kiwi']
a=""
for i in l:
    if len(i) > len(a):
        a=i
print(a)
    
#using list comprehensive    
b=[i for i in l if len(i) > len(a)]
print(a)