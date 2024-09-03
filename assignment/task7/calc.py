
# Write program for a simple calculator


num1=int(input("enter first number: "))

num2=int(input("enter second number: "))

choice=int(input("1 : Addition,2 : Subraction,3 : Multiplication,4 : Division: "))

if choice==1:

    add=(num1+num2)

    print(add)

elif choice==2:

    sub=num1-num2

    print(sub)

elif choice==3:

    mul=num1*num2

    print(mul)

elif choice==4:

    div=num1/num2

    print(div)