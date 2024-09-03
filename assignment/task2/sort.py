# program to print three number in sort order?

num1=int(input("enter the first number\n"))

num2=int(input("enter the second number\n"))

num3=int(input("enter the third number\n"))

if(num1>num2 and num1>num3):

    if(num2>num3):

        print(f"sorted order = {num1},{num2},{num3}")

    else:

       print(f"sorted order = {num1},{num3},{num2}")

elif(num2>num1 and num2>num3):

    if(num1>num3):

        print(f"sorted order = {num2},{num1},{num3}")
    else:

        print(f"sorted order = {num2},{num3},{num1}")

elif(num3>num1 and num3>num2):

    if(num1>num2):

        print(f"sorted order = {num3},{num1},{num2}")

    else:

       print(f"sorted order = {num3},{num2},{num1}")
