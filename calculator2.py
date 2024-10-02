while True:
    print('''
    1:Addition
    2:Substraction
    3:Multiplication
    4:Division
    5.Modulus
    6.Exit''')
        
    choice=int(input("select your choice:"))

    if choice==1:
        first_num= int(input("enter a number:"))
        second_num= int(input("enter a number:"))
        sum= first_num+second_num
        print("sum is",sum)
    elif choice==2:
        first_num= int(input("enter a number:"))
        second_num= int(input("enter a number:"))
        diff= first_num-second_num
        print("difference is",diff)
    elif choice==3:
        first_num= int(input("enter a number:"))
        second_num= int(input("enter a number:"))
        product= first_num*second_num
        print("product is",product)
    elif choice==4:
        first_num= int(input("enter a number:"))
        second_num= int(input("enter a number:"))
        result= first_num/second_num
        print("result is",result)
    elif choice==5:
        first_num= int(input("enter a number:"))
        second_num= int(input("enter a number:"))
        modulus= first_num%second_num
        print("modulus is",modulus)
    elif choice==6:
        break
    
    else:
        print("wrong choice")
 
    


