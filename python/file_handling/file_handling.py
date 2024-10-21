# #file creation
# f=open('demo.txt','x')
# f.write('welcome all\n')
# f.write('hi i am dhanushya')

# #write
# f=open('demo.txt','w')
# f.write('write mode\n')
# f.write(str(1234))
# f.write(str([1,2,3,4]))

# #append
# f=open('demo.txt','a')
# f.write('\nwrite mode\n')
# f.write(str(1234))
# f.write(str([1,2,3,4]))

#read
# f=open('demo.txt','r')
# print(f.read())
# f.seek(0)
# a=f.read()
# print(a)
# f.seek(0)
# a=f.read(10)
# print(a)
# a=f.read(10)
# f.seek(0)
# a=f.readline()
# print(a)
# f.seek(0)
# a=f.readline(3)
# print(a)
# f.seek(0)
# a=f.readlines()
# print(a)

# f=open('demo.txt','r')
# a=f.readlines()
# print(len(str(a)))
# print(a)

# f=open('demo.txt','r')
# a=f.readlines()
# print(a)
# f.seek(0)
# total=0
# upper=0
# word=0
# longest_word=''
# for i in range(len(a)):
#     b=f.readline().strip()
#     c=b.split(' ')
#     for j in c:
#         if j!='':
#             word+=1
#             if len(c)>len(longest_word):
#                 longest_word=j
#     for j in b:
#         if j!=" ":
#             total+=1
#             if j.isupper():
#                 upper+=1
# print('Total count:',total)
# print('Upper case count:',upper)
# print('Lower case count:',total-upper)
# print('Total words:',word)
# print('Longest word:',longest_word)

# import os
# os.remove('demo.txt')

# import os
# if os.path.exists('demo.txt'):
#     os.remove('demo.txt')
# else:
#     print('file does not exist')

# import os
# os.mkdir('demo')#create folder
# os.rmdir('demo')#delete folder