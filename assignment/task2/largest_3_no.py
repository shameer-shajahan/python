# print largest three number?

num1=int(input("enter the first number\n"))

num2=int(input("enter the second number\n"))

num3=int(input("enter the third number\n"))

if(num1>num2 and num1>num3):

    print(f"largest number is = {num1}")

elif(num2>num1 and num2>num3):

    print(f"largest number is = {num2}")

else:
    
    print(f"largest number is = {num3}")