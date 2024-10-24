import re 
a='hello world hello HI 123'
print(re.sub('hello','HELLO',a))    #substitute 'hello' to 'HELLO'
print(re.sub('hello','HELLO',a,1))  #substitute only first occurance of 'hello' to 'HELLO'
print(re.findall('hello',a))        #find all occurance of 'hello'
print(re.search('hello',a))         #search for 'hello'
print(re.search('all',a))           #search for 'all'
print(re.search('[a-z]',a))         #search for any value betwn a-z
print(re.search('[A-Z]',a))         #search for any value betwn A-Z
print(re.search('[A-z]',a))         #search for a-z or A-Z
print(re.search('h.',a))            #'a' and the next character
print(re.search('h.*',a))           #0/more occurance
print(re.search('H.+',a))           #1/more occurance
print(re.search('h.?',a))           #0/1 occurance
print(re.search('[a-z][A-Z]',a))
print(re.search('[a-z].*[A-Z].*[0-9].*',a))
print(re.search('[a-m].*[A-Z].*',a))
b='sadf'
print(re.search('[a-m0-9A-Z].*',b))








