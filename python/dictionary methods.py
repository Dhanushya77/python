#dictionary methods
d={'name':'Dhanushya','roll_no':20,'age':20,'mark':30}
#to delete an item
d.pop('name')
print(d)
#to delete last item
d.popitem()
print(d)
#to print all keys, values, and items
print(d.keys())
print(d.values())
print(d.items())
#to add a new key with default value
d.setdefault('mark')
print(d)
#to display value of a key
print(d.get('age'))
#fromkeys
l=[1,2,3,4]
d1=d.fromkeys(l)
print(d1)
#to clear all key value pairs
d.clear()
print(d)
#to update values or add new key value pair
d.update({'name':'anu'})
print(d)