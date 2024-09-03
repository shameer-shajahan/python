# 1) Write a program to check if a number is positive, negative or zero
# 2) Write a program to check if a person is eligible for voting or not
# conditions – age greater than or equal to 18 the person is eligible
#                        age less than 18 not eligible for voting
# 3) Write a program to check the given number is odd or even
# 4) Write  a program for grade classification based on percentage
# conditions
#  percentage = 90
#  grade A
# percentage in between 80-90
# grade B
# percentage in between 70-80
# grade C
# percentage less than 70
# fail
# 5) Write a program to check the given year is a leap year or not
# 6) Write a program to determine largest of three numbers
# 7) Write program for a simple calculator






# 1) Write a program to check if a number is positive, negative or zero

# num=int(input("enter the number\n"))

# if (num>0):

#     print("number is positive")

# elif num==0:

#     print("number is zero")

# else:

#     print("number is negative")











# 2) Write a program to check if a person is eligible for voting or not
# conditions – age greater than or equal to 18 the person is eligible age less than 18 not eligible for voting




# age=int(input("enter the person age\n"))

# if age>=18:

#     print("this person has eligible for votting")

# else:

#     print("this person is not eligible for votting")











# 3) Write a program to check the given number is odd or even

# num=int(input("enter the number\n"))

# if num%2==0:

#     print("given number is even")

# else:

#     print("given number is odd")












# 4) Write  a program for grade classification based on percentage

# conditions
# percentage = 90 grade A
# percentage in between 80-90 grade B
# percentage in between 70-80 grade C
# percentage less than 70 fail


# percentage=int(input("enter the percentage\n"))

# if percentage >=90:

#     print(" A Grade ")

# elif percentage >=80 and percentage<90:

#     print(" B Grade ")

# elif percentage >=70 and percentage<80:

#     print(" C Grade ")

# else:

#     print(" Fail ")







# 5) Write a program to check the given year is a leap year or not

# year=int(input("enter the year\n"))

# y=["leap year" if year%100==0 and year%400==0 or year%4==0 and year%100!=0 else "not leap year"]
# print(y)







# 6) Write a program to determine largest of three numbers

# num1=int(input("enter the first number: "))

# num2=int(input("enter the second number: "))

# num3=int(input("enter the third number: "))

# if num1>num2 and num1>num3:

#     print(f"{num1} is largest")

# elif num2>num1 and num2>num3:

#     print(f"{num2} is largest")

# else:

#     print(f"{num3} is largest")







# Write program for a simple calculator


# num1=int(input("enter first number: "))

# num2=int(input("enter second number: "))

# choice=int(input("1-Addition,2-Subraction,3-Multiplication,4-Division: "))

# if choice==1:

#     add=(num1+num2)

#     print(add)

# elif choice==2:

#     sub=num1-num2

#     print(sub)

# elif choice==3:

#     mul=num1*num2

#     print(mul)

# elif choice==4:

#     div=num1/num2

#     print(div)