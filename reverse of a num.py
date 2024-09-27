#reverse of a number and checking whether it is palindrome/not
a=int(input("Enter a number:"))
c=a
rev_num=0
while a!=0:
    b=a%10
    rev_num=rev_num*10+b
    a//=10
print("reverse is", str(rev_num))
if rev_num==c:
    print("palindrome")
else:
    print("Not palindrome")