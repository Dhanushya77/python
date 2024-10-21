#dictionary- set of key value pairs
d={'name':'Dhanushya','roll_no':20,'age':20,'mark':30}
print(d)
print(d['name'])
#updation
d['age']=22   
print(d)  
#addition of a new key value pair
d['place']='klm' 
print(d)
#check for a value
if d['age']==22:
    print('yes')
else:
    print('no')
#iteration of dictionary using loop
for i in d:
    #print(i) - prints all the keys
    #print(d[i]) - prints all the values
    print(i,':',d[i])   #prints all keys and values
