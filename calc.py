opt = int(input("enter the option you want to perform : 1.addition 2.multiplication"))
if opt==1:
    s=0
    n=int(input("enter how many times you want to sum up :"))
    print("enter",n,"numbers : ")
    for i in range(0,n):
        a=int(input("enter the number"))
        s=s+a
    print("the result is : ",s)

elif opt==2:
    m=1
    n1=int(input("how many times you want to multiply : "))
    print("enter",n1,"numbers :")
    for i in range(0,n1):
        
        b=int(input("enter the number :"))
        m=m*b
    print("the result is :",m)
elif opt==3:
    n2=int(input("how many times you want to substract :"))
    print("enter", n2 ,"numbers: ")
    a=int(input("enter the 1st number"))
    b=int(input("enter the 2nd number"))
    #c=(a-b)
    d=(n2-2)
    print("you have to enter ", d, "numbers more")
    for i in range(0,d):
        c=(a-b)
        e=int(input("enter the number : "))
        f=c-e
        print("the result is :", f)